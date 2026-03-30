"""
测试模块：任务管理
对应用例编号：TASK_MGMT-*
数据来源：data/task_data.yaml
"""
import time
import copy
import pytest
from utils.reporter import CaseResult


class TestTaskManagement:
    """任务管理相关测试（通过 updateFrontProjects 接口提交）"""

    # ------------------------------------------------------------------ #
    #  任务进度边界值
    # ------------------------------------------------------------------ #
    @pytest.mark.parametrize("progress,expect_pass", [
        (0,     True),
        (50,    True),
        (100,   True),
        (16.11, True),   # 真实数据中出现的小数进度
        (101,   False),
        (-1,    False),
    ])
    def test_task_progress_boundary(self, task_api, base_project_payload,
                                    reporter, progress, expect_pass):
        """TASK_MGMT-PROG-*：任务进度边界值（0/50/100/101/-1）"""
        payload = copy.deepcopy(base_project_payload)
        task_id = "1773715019830"
        for t in payload["tasks"]:
            if t["id"] == task_id:
                t["progress"] = progress
                break

        start = time.time()
        resp = task_api.update_project(payload)
        elapsed = (time.time() - start) * 1000

        try:
            if expect_pass:
                task_api.assert_success(resp)
                status = "PASS"
                err = ""
            else:
                task_api.assert_business_fail(resp)
                status = "PASS"
                err = ""
        except AssertionError as e:
            status = "FAIL"
            err = str(e)
            if not expect_pass:
                err = f"[疑似Bug] 非法进度值 {progress} 未被拦截: {e}"

        reporter.add(CaseResult(
            case_id=f"TASK_MGMT-PROG-{progress}",
            title=f"任务进度={progress}（{'合法' if expect_pass else '非法'}）",
            module="任务管理/进度",
            status=status,
            elapsed_ms=elapsed,
            error_msg=err,
        ))
        if status == "FAIL" and not expect_pass:
            pytest.xfail(err)
        elif status == "FAIL":
            pytest.fail(err)

    # ------------------------------------------------------------------ #
    #  任务时间：结束时间早于开始时间
    # ------------------------------------------------------------------ #
    def test_task_end_before_start(self, task_api, task_data,
                                    base_project_payload, reporter):
        """TASK_MGMT-TIME-001：任务结束时间早于开始时间应被拒绝"""
        payload = copy.deepcopy(base_project_payload)
        task_id = "1773715019830"
        for t in payload["tasks"]:
            if t["id"] == task_id:
                t["startDate"] = "2026-05-10"
                t["endDate"] = "2026-01-01"
                break

        start = time.time()
        resp = task_api.update_project(payload)
        elapsed = (time.time() - start) * 1000

        try:
            task_api.assert_business_fail(resp)
            status = "PASS"
            err = ""
        except AssertionError as e:
            status = "FAIL"
            err = f"[已知Bug] 任务结束时间<开始时间未被拦截: {e}"
        finally:
            restore = copy.deepcopy(base_project_payload)
            task_api.update_project(restore)

        reporter.add(CaseResult(
            case_id="TASK_MGMT-TIME-001",
            title="任务结束时间早于开始时间应被拒绝",
            module="任务管理/时间",
            status=status,
            elapsed_ms=elapsed,
            error_msg=err,
        ))
        if status == "FAIL":
            pytest.xfail(err)

    # ------------------------------------------------------------------ #
    #  任务时间：开始时间等于结束时间（单天任务）
    # ------------------------------------------------------------------ #
    def test_task_same_start_end(self, task_api, base_project_payload, reporter):
        """TASK_MGMT-TIME-002：单天任务（开始=结束）应允许保存"""
        payload = copy.deepcopy(base_project_payload)
        task_id = "1773715019830"
        for t in payload["tasks"]:
            if t["id"] == task_id:
                t["startDate"] = "2026-03-16"
                t["endDate"] = "2026-03-16"
                t["duration"] = 1
                break

        start = time.time()
        resp = task_api.update_project(payload)
        elapsed = (time.time() - start) * 1000

        try:
            task_api.assert_success(resp)
            status = "PASS"
            err = ""
        except AssertionError as e:
            status = "FAIL"
            err = str(e)
        finally:
            restore = copy.deepcopy(base_project_payload)
            task_api.update_project(restore)

        reporter.add(CaseResult(
            case_id="TASK_MGMT-TIME-002",
            title="单天任务（开始=结束日期）",
            module="任务管理/时间",
            status=status,
            elapsed_ms=elapsed,
            error_msg=err,
        ))
        assert status == "PASS", err

    # ------------------------------------------------------------------ #
    #  前置任务：设置前置任务后验证
    # ------------------------------------------------------------------ #
    def test_predecessor_task(self, task_api, base_project_payload, reporter):
        """TASK_MGMT-PRE-001：设置有效前置任务"""
        payload = copy.deepcopy(base_project_payload)
        # 任务"接触"(1773715016347) 作为 "发布"(1773715019830) 的前置任务
        for t in payload["tasks"]:
            if t["id"] == "1773715019830":
                t["predecessorTaskId"] = "1773715016347"
                break

        start = time.time()
        resp = task_api.update_project(payload)
        elapsed = (time.time() - start) * 1000

        try:
            task_api.assert_success(resp)
            status = "PASS"
            err = ""
        except AssertionError as e:
            status = "FAIL"
            err = str(e)
        finally:
            restore = copy.deepcopy(base_project_payload)
            task_api.update_project(restore)

        reporter.add(CaseResult(
            case_id="TASK_MGMT-PRE-001",
            title="设置有效前置任务",
            module="任务管理/前置任务",
            status=status,
            elapsed_ms=elapsed,
            error_msg=err,
        ))
        assert status == "PASS", err

    # ------------------------------------------------------------------ #
    #  子任务：设置 parentTaskId
    # ------------------------------------------------------------------ #
    def test_subtask_parent_relationship(self, task_api, base_project_payload, reporter):
        """TASK_MGMT-SUB-001：设置父子任务关系"""
        payload = copy.deepcopy(base_project_payload)
        parent_id = "1773715016347"
        child_id = "1773715019830"
        for t in payload["tasks"]:
            if t["id"] == child_id:
                t["parentTaskId"] = parent_id
                break

        start = time.time()
        resp = task_api.update_project(payload)
        elapsed = (time.time() - start) * 1000

        try:
            task_api.assert_success(resp)
            status = "PASS"
            err = ""
        except AssertionError as e:
            status = "FAIL"
            err = str(e)
        finally:
            restore = copy.deepcopy(base_project_payload)
            task_api.update_project(restore)

        reporter.add(CaseResult(
            case_id="TASK_MGMT-SUB-001",
            title="设置父子任务关系",
            module="任务管理/子任务",
            status=status,
            elapsed_ms=elapsed,
            error_msg=err,
        ))
        assert status == "PASS", err

    # ------------------------------------------------------------------ #
    #  批量任务性能：不同任务数量下的响应时间
    # ------------------------------------------------------------------ #
    @pytest.mark.parametrize("task_count", [1, 5, 10, 22])
    def test_batch_tasks_performance(self, task_api, base_project_payload,
                                      existing_project_id, reporter, task_count):
        """TASK_MGMT-PERF-*：不同任务数量下的响应时间"""
        payload = copy.deepcopy(base_project_payload)
        payload["tasks"] = task_api.build_tasks_batch(
            count=task_count,
            project_id=existing_project_id,
        )

        start = time.time()
        resp = task_api.update_project(payload)
        elapsed = (time.time() - start) * 1000

        try:
            task_api.assert_success(resp)
            status = "PASS"
            err = ""
        except AssertionError as e:
            status = "FAIL"
            err = str(e)
        finally:
            restore = copy.deepcopy(base_project_payload)
            task_api.update_project(restore)

        reporter.add(CaseResult(
            case_id=f"TASK_MGMT-PERF-{task_count}",
            title=f"提交{task_count}个任务的响应时间: {elapsed:.0f}ms",
            module="任务管理/性能",
            status=status,
            elapsed_ms=elapsed,
            error_msg=err,
        ))
        assert status == "PASS", err

    # ------------------------------------------------------------------ #
    #  空任务列表
    # ------------------------------------------------------------------ #
    def test_empty_tasks_list(self, task_api, base_project_payload, reporter):
        """TASK_MGMT-ERR-001：提交空任务列表"""
        payload = copy.deepcopy(base_project_payload)
        payload["tasks"] = []

        start = time.time()
        resp = task_api.update_project(payload)
        elapsed = (time.time() - start) * 1000

        try:
            task_api.assert_not_crash(resp)
            status = "PASS"
            err = ""
        except AssertionError as e:
            status = "FAIL"
            err = str(e)
        finally:
            restore = copy.deepcopy(base_project_payload)
            task_api.update_project(restore)

        reporter.add(CaseResult(
            case_id="TASK_MGMT-ERR-001",
            title="提交空任务列表不崩溃",
            module="任务管理/异常",
            status=status,
            elapsed_ms=elapsed,
            error_msg=err,
        ))
        assert status == "PASS", err

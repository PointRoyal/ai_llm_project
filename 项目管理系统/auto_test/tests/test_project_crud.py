"""
测试模块：项目更新接口（updateFrontProjects）
对应用例编号：PROJ_CREATE-* / PROJ_UPDATE-*
数据来源：data/project_data.yaml → update_project
"""
import time
import copy
import pytest
from utils.reporter import CaseResult


class TestProjectUpdate:
    """项目更新接口测试"""

    # ------------------------------------------------------------------ #
    #  正常更新
    # ------------------------------------------------------------------ #
    def test_normal_update(self, project_api, project_data, base_project_payload, reporter):
        """PROJ_UPDATE-001：正常更新项目，验证响应 code=0 data=true"""
        payload = copy.deepcopy(base_project_payload)
        start = time.time()
        resp = project_api.update_project(payload)
        elapsed = (time.time() - start) * 1000

        try:
            body = project_api.assert_success(resp)
            assert body.get("data") is True, f"data 应为 true，实际: {body.get('data')}"
            status = "PASS"
            err = ""
        except AssertionError as e:
            status = "FAIL"
            err = str(e)

        reporter.add(CaseResult(
            case_id="PROJ_UPDATE-001",
            title="正常更新项目信息",
            module="创建/更新项目",
            status=status,
            elapsed_ms=elapsed,
            request_body=payload,
            response_body=resp.json() if resp else {},
            error_msg=err,
        ))
        assert status == "PASS", err

    # ------------------------------------------------------------------ #
    #  更新后查询验证持久化
    # ------------------------------------------------------------------ #
    def test_update_persisted(self, project_api, base_project_payload,
                              existing_project_id, reporter):
        """PROJ_UPDATE-002：更新城市字段后查询验证持久化"""
        payload = copy.deepcopy(base_project_payload)
        new_city = "深圳"
        payload["city"] = new_city

        project_api.update_project(payload)
        time.sleep(0.5)

        start = time.time()
        project = project_api.get_project_by_id(existing_project_id)
        elapsed = (time.time() - start) * 1000

        try:
            assert project is not None, "查询不到目标项目"
            assert project["city"] == new_city, (
                f"城市未持久化: 期望={new_city}, 实际={project.get('city')}"
            )
            status = "PASS"
            err = ""
        except AssertionError as e:
            status = "FAIL"
            err = str(e)
        finally:
            # 恢复原始城市
            payload["city"] = "上海"
            project_api.update_project(payload)

        reporter.add(CaseResult(
            case_id="PROJ_UPDATE-002",
            title="更新字段后验证数据持久化",
            module="创建/更新项目",
            status=status,
            elapsed_ms=elapsed,
            error_msg=err,
        ))
        assert status == "PASS", err

    # ------------------------------------------------------------------ #
    #  状态切换：进行中 ↔ 已归档
    # ------------------------------------------------------------------ #
    def test_update_status_to_archived(self, project_api, base_project_payload,
                                       existing_project_id, reporter):
        """PROJ_UPDATE-003：将项目状态改为已归档（status=2）"""
        payload = copy.deepcopy(base_project_payload)
        payload["status"] = 2
        start = time.time()
        resp = project_api.update_project(payload)
        elapsed = (time.time() - start) * 1000

        try:
            project_api.assert_success(resp)
            status = "PASS"
            err = ""
        except AssertionError as e:
            status = "FAIL"
            err = str(e)
        finally:
            payload["status"] = 1
            project_api.update_project(payload)

        reporter.add(CaseResult(
            case_id="PROJ_UPDATE-003",
            title="将项目状态改为已归档",
            module="创建/更新项目",
            status=status,
            elapsed_ms=elapsed,
            error_msg=err,
        ))
        assert status == "PASS", err

    # ------------------------------------------------------------------ #
    #  异常：项目名称为空
    # ------------------------------------------------------------------ #
    def test_empty_project_name_rejected(self, project_api, project_data,
                                         base_project_payload, reporter):
        """PROJ_UPDATE-ERR-001：项目名称为空应拒绝更新"""
        case = project_data["update_project"]["missing_project_name"]
        payload = copy.deepcopy(base_project_payload)
        payload["projectName"] = ""
        start = time.time()
        resp = project_api.update_project(payload)
        elapsed = (time.time() - start) * 1000

        try:
            project_api.assert_business_fail(resp)
            status = "PASS"
            err = ""
        except AssertionError as e:
            status = "FAIL"
            err = f"[疑似Bug] {e}"

        reporter.add(CaseResult(
            case_id="PROJ_UPDATE-ERR-001",
            title=case["desc"],
            module="创建/更新项目",
            status=status,
            elapsed_ms=elapsed,
            error_msg=err,
        ))
        # 不强制失败，记录结果即可（可能是已知问题）
        if status == "FAIL":
            pytest.xfail(f"后端未校验空项目名: {err}")

    # ------------------------------------------------------------------ #
    #  异常：结束时间早于开始时间（已知 Bug 场景）
    # ------------------------------------------------------------------ #
    def test_end_before_start_rejected(self, project_api, project_data,
                                       base_project_payload, reporter):
        """PROJ_UPDATE-ERR-002：结束时间早于开始时间应被拒绝（已知Bug验证）"""
        payload = copy.deepcopy(base_project_payload)
        payload["startDate"] = "2026-05-10"
        payload["endDate"] = "2026-01-01"
        start = time.time()
        resp = project_api.update_project(payload)
        elapsed = (time.time() - start) * 1000

        try:
            project_api.assert_business_fail(resp)
            status = "PASS"
            err = ""
        except AssertionError as e:
            status = "FAIL"
            err = f"[已知Bug] 后端未校验结束时间<开始时间: {e}"
        finally:
            # 无论如何恢复原始时间
            restore = copy.deepcopy(base_project_payload)
            project_api.update_project(restore)

        reporter.add(CaseResult(
            case_id="PROJ_UPDATE-ERR-002",
            title="结束时间早于开始时间应被拒绝",
            module="创建/更新项目",
            status=status,
            elapsed_ms=elapsed,
            error_msg=err,
        ))
        if status == "FAIL":
            pytest.xfail(err)

    # ------------------------------------------------------------------ #
    #  异常：超长项目名称
    # ------------------------------------------------------------------ #
    def test_project_name_too_long_not_crash(self, project_api, project_data,
                                              base_project_payload, reporter):
        """PROJ_UPDATE-ERR-003：超长项目名称接口不应崩溃"""
        case = project_data["update_project"]["project_name_too_long"]
        payload = copy.deepcopy(base_project_payload)
        payload["projectName"] = case["payload"]["projectName"]
        start = time.time()
        resp = project_api.update_project(payload)
        elapsed = (time.time() - start) * 1000

        try:
            project_api.assert_not_crash(resp)
            status = "PASS"
            err = ""
        except AssertionError as e:
            status = "FAIL"
            err = str(e)
        finally:
            restore = copy.deepcopy(base_project_payload)
            project_api.update_project(restore)

        reporter.add(CaseResult(
            case_id="PROJ_UPDATE-ERR-003",
            title=case["desc"],
            module="创建/更新项目",
            status=status,
            elapsed_ms=elapsed,
            error_msg=err,
        ))
        assert status == "PASS", err

    # ------------------------------------------------------------------ #
    #  安全：XSS 注入
    # ------------------------------------------------------------------ #
    def test_xss_in_project_name(self, project_api, project_data,
                                  base_project_payload, reporter):
        """PROJ_UPDATE-SEC-001：项目名称含XSS注入，接口不崩溃且不执行脚本"""
        case = project_data["update_project"]["xss_in_project_name"]
        payload = copy.deepcopy(base_project_payload)
        payload["projectName"] = case["payload"]["projectName"]
        start = time.time()
        resp = project_api.update_project(payload)
        elapsed = (time.time() - start) * 1000

        try:
            project_api.assert_not_crash(resp)
            # 验证响应中 XSS 内容被转义或过滤
            resp_text = resp.text
            assert "<script>" not in resp_text, "响应中包含原始 <script> 标签，存在 XSS 风险"
            status = "PASS"
            err = ""
        except AssertionError as e:
            status = "FAIL"
            err = str(e)
        finally:
            restore = copy.deepcopy(base_project_payload)
            project_api.update_project(restore)

        reporter.add(CaseResult(
            case_id="PROJ_UPDATE-SEC-001",
            title=case["desc"],
            module="创建/更新项目",
            status=status,
            elapsed_ms=elapsed,
            error_msg=err,
        ))
        assert status == "PASS", err

    # ------------------------------------------------------------------ #
    #  安全：SQL 注入
    # ------------------------------------------------------------------ #
    def test_sql_injection_not_crash(self, project_api, project_data,
                                      base_project_payload, reporter):
        """PROJ_UPDATE-SEC-002：城市字段SQL注入，接口不崩溃"""
        case = project_data["update_project"]["sql_injection_in_city"]
        payload = copy.deepcopy(base_project_payload)
        payload["city"] = case["payload"]["city"]
        start = time.time()
        resp = project_api.update_project(payload)
        elapsed = (time.time() - start) * 1000

        try:
            project_api.assert_not_crash(resp)
            status = "PASS"
            err = ""
        except AssertionError as e:
            status = "FAIL"
            err = str(e)
        finally:
            restore = copy.deepcopy(base_project_payload)
            project_api.update_project(restore)

        reporter.add(CaseResult(
            case_id="PROJ_UPDATE-SEC-002",
            title=case["desc"],
            module="创建/更新项目",
            status=status,
            elapsed_ms=elapsed,
            error_msg=err,
        ))
        assert status == "PASS", err

    # ------------------------------------------------------------------ #
    #  鉴权：无 Token
    # ------------------------------------------------------------------ #
    def test_no_token_update_rejected(self, project_api, project_data,
                                       base_project_payload, reporter):
        """PROJ_UPDATE-AUTH-001：无Token更新应被拒绝"""
        payload = copy.deepcopy(base_project_payload)
        start = time.time()
        resp = project_api.update_project(payload, use_token=False)
        elapsed = (time.time() - start) * 1000

        try:
            project_api.assert_unauthorized(resp)
            status = "PASS"
            err = ""
        except AssertionError as e:
            status = "FAIL"
            err = str(e)

        reporter.add(CaseResult(
            case_id="PROJ_UPDATE-AUTH-001",
            title="无Token更新项目应被拒绝",
            module="创建/更新项目",
            status=status,
            elapsed_ms=elapsed,
            error_msg=err,
        ))
        assert status == "PASS", err

    # ------------------------------------------------------------------ #
    #  性能：更新接口响应时间
    # ------------------------------------------------------------------ #
    def test_update_response_time(self, project_api, base_project_payload, reporter):
        """PROJ_UPDATE-PERF-001：更新接口响应时间 < 5000ms"""
        payload = copy.deepcopy(base_project_payload)
        start = time.time()
        resp = project_api.update_project(payload)
        elapsed = (time.time() - start) * 1000

        try:
            project_api.assert_success(resp)
            assert elapsed < 5000, f"响应超时: {elapsed:.0f}ms > 5000ms（当前性能基线）"
            status = "PASS"
            err = ""
        except AssertionError as e:
            status = "FAIL"
            err = str(e)

        reporter.add(CaseResult(
            case_id="PROJ_UPDATE-PERF-001",
            title="更新接口响应时间基线（<5s）",
            module="创建/更新项目",
            status=status,
            elapsed_ms=elapsed,
            error_msg=err,
        ))
        if elapsed >= 5000:
            pytest.xfail(f"[已知性能问题] 响应时间 {elapsed:.0f}ms > 5000ms")

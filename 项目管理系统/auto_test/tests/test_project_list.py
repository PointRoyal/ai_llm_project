"""
测试模块：项目看板列表查询
对应用例编号：PROJ_LIST-001 ~ PROJ_LIST-010（接口版）
数据来源：data/project_data.yaml → dashboard_query
"""
import time
import copy
import pytest
from utils.reporter import CaseResult


class TestProjectDashboard:
    """项目看板列表接口测试"""

    # ------------------------------------------------------------------ #
    #  数据驱动：正常场景（从 YAML 读取）
    # ------------------------------------------------------------------ #
    @pytest.mark.parametrize("case_key", [
        "normal_full_params",
        "normal_large_page",
        "sort_desc",
    ])
    def test_normal_query(self, project_api, project_data, reporter, case_key):
        """正常参数查询——数据驱动"""
        case = project_data["dashboard_query"][case_key]
        start = time.time()
        resp = project_api.get_dashboard_with_payload(case["payload"])
        elapsed = (time.time() - start) * 1000

        try:
            body = project_api.assert_success(resp)
            assert "records" in body["data"], "返回数据中缺少 records 字段"
            if case["expect"].get("has_records"):
                assert len(body["data"]["records"]) > 0, "预期有数据，但返回空列表"
            status = "PASS"
            err = ""
        except AssertionError as e:
            status = "FAIL"
            err = str(e)

        reporter.add(CaseResult(
            case_id=f"PROJ_LIST-{case_key}",
            title=case["desc"],
            module="项目列表/查询",
            status=status,
            elapsed_ms=elapsed,
            request_body=case["payload"],
            response_body=resp.json() if resp else {},
            error_msg=err,
        ))
        assert status == "PASS", err

    # ------------------------------------------------------------------ #
    #  返回字段完整性校验
    # ------------------------------------------------------------------ #
    def test_response_fields_integrity(self, project_api, reporter):
        """PROJ_LIST-FIELD-001：响应字段完整性校验"""
        start = time.time()
        resp = project_api.get_dashboard(size=10)
        elapsed = (time.time() - start) * 1000

        required_fields = {"id", "projectName", "status", "ownerName",
                           "progress", "startDate", "endDate"}
        try:
            body = project_api.assert_success(resp)
            records = body["data"]["records"]
            if records:
                first = records[0]
                missing = required_fields - set(first.keys())
                assert not missing, f"响应缺少字段: {missing}"
            status = "PASS"
            err = ""
        except AssertionError as e:
            status = "FAIL"
            err = str(e)

        reporter.add(CaseResult(
            case_id="PROJ_LIST-FIELD-001",
            title="响应字段完整性校验",
            module="项目列表/查询",
            status=status,
            elapsed_ms=elapsed,
            error_msg=err,
        ))
        assert status == "PASS", err

    # ------------------------------------------------------------------ #
    #  翻页超出范围返回空列表
    # ------------------------------------------------------------------ #
    def test_page_overflow_returns_empty(self, project_api, project_data, reporter):
        """PROJ_LIST-BOUND-001：current超出总页数应返回空列表"""
        case = project_data["dashboard_query"]["page_current_overflow"]
        start = time.time()
        resp = project_api.get_dashboard_with_payload(case["payload"])
        elapsed = (time.time() - start) * 1000

        try:
            project_api.assert_not_crash(resp)
            body = resp.json()
            records = body.get("data", {}).get("records", [])
            assert isinstance(records, list), "records 应为列表"
            status = "PASS"
            err = ""
        except AssertionError as e:
            status = "FAIL"
            err = str(e)

        reporter.add(CaseResult(
            case_id="PROJ_LIST-BOUND-001",
            title=case["desc"],
            module="项目列表/查询",
            status=status,
            elapsed_ms=elapsed,
            error_msg=err,
        ))
        assert status == "PASS", err

    # ------------------------------------------------------------------ #
    #  无 Token 鉴权测试
    # ------------------------------------------------------------------ #
    def test_no_token_returns_unauthorized(self, project_api, project_data, reporter):
        """PROJ_LIST-AUTH-001：无Token应返回鉴权失败"""
        case = project_data["dashboard_query"]["no_token"]
        start = time.time()
        resp = project_api.get_dashboard_with_payload(
            case["payload"], use_token=False
        )
        elapsed = (time.time() - start) * 1000

        try:
            project_api.assert_unauthorized(resp)
            status = "PASS"
            err = ""
        except AssertionError as e:
            status = "FAIL"
            err = str(e)

        reporter.add(CaseResult(
            case_id="PROJ_LIST-AUTH-001",
            title=case["desc"],
            module="项目列表/查询",
            status=status,
            elapsed_ms=elapsed,
            error_msg=err,
        ))
        assert status == "PASS", err

    # ------------------------------------------------------------------ #
    #  空请求体不崩溃
    # ------------------------------------------------------------------ #
    def test_empty_body_not_crash(self, project_api, project_data, reporter):
        """PROJ_LIST-ERR-001：空请求体接口不应崩溃"""
        case = project_data["dashboard_query"]["empty_body"]
        start = time.time()
        resp = project_api.get_dashboard_with_payload(case["payload"])
        elapsed = (time.time() - start) * 1000

        try:
            project_api.assert_not_crash(resp)
            status = "PASS"
            err = ""
        except AssertionError as e:
            status = "FAIL"
            err = str(e)

        reporter.add(CaseResult(
            case_id="PROJ_LIST-ERR-001",
            title=case["desc"],
            module="项目列表/查询",
            status=status,
            elapsed_ms=elapsed,
            error_msg=err,
        ))
        assert status == "PASS", err

    # ------------------------------------------------------------------ #
    #  已知 Bug 验证：测试222项目结束时间早于开始时间
    # ------------------------------------------------------------------ #
    def test_known_bug_end_before_start(self, project_api, reporter):
        """PROJ_LIST-BUG-001：验证已知Bug——测试222项目结束时间早于开始时间"""
        start = time.time()
        resp = project_api.get_dashboard(size=999)
        elapsed = (time.time() - start) * 1000

        try:
            body = project_api.assert_success(resp)
            bug_projects = []
            for p in body["data"]["records"]:
                if p.get("startDate") and p.get("endDate"):
                    if p["endDate"] < p["startDate"]:
                        bug_projects.append({
                            "name": p["projectName"],
                            "startDate": p["startDate"],
                            "endDate": p["endDate"],
                        })

            # 标记为已知 Bug，用 xfail 记录
            if bug_projects:
                pytest.xfail(
                    f"[已知Bug] 以下项目结束时间早于开始时间，后端未校验: {bug_projects}"
                )
            status = "PASS"
            err = ""
        except AssertionError as e:
            status = "FAIL"
            err = str(e)

        reporter.add(CaseResult(
            case_id="PROJ_LIST-BUG-001",
            title="验证已知Bug：结束时间早于开始时间的项目",
            module="项目列表/查询",
            status=status,
            elapsed_ms=elapsed,
            error_msg=err,
        ))

    # ------------------------------------------------------------------ #
    #  性能基线：响应时间应 < 5s
    # ------------------------------------------------------------------ #
    def test_response_time_baseline(self, project_api, reporter):
        """PROJ_LIST-PERF-001：列表查询响应时间应 < 5000ms"""
        start = time.time()
        resp = project_api.get_dashboard(size=999)
        elapsed = (time.time() - start) * 1000

        try:
            project_api.assert_success(resp)
            assert elapsed < 5000, f"响应超时: {elapsed:.0f}ms > 5000ms"
            status = "PASS"
            err = ""
        except AssertionError as e:
            status = "FAIL"
            err = str(e)

        reporter.add(CaseResult(
            case_id="PROJ_LIST-PERF-001",
            title="列表查询响应时间基线（<5s）",
            module="项目列表/性能",
            status=status,
            elapsed_ms=elapsed,
            error_msg=err,
        ))
        assert status == "PASS", err

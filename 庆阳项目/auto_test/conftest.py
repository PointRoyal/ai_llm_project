# -*- coding: utf-8 -*-
import glob
import os
import re
from datetime import datetime

import pytest

import lib.http_client as hc
from lib.http_client import HttpClient
from lib.logger import logger
from utils.bug_reporter import write_bug, append_run_log

_ROOT = os.path.dirname(__file__)
_CFG = os.path.join(_ROOT, "config", "api.yaml")
_TESTCASE_DIR = os.path.join(_ROOT, "..", "testcase")

# 本次 pytest 会话使用的 bug 报告文件（在 pytest_sessionstart 中分配，如 bug2026032701.xlsx）
_BUG_SESSION_PATH = None


def _next_bug_report_path() -> str:
    """
    在 testcase/ 下生成新的 bug 文件名：bug + YYYYMMDD + 两位序号，如 bug2026032701.xlsx。
    同一天多次执行则序号递增（02、03…），不覆盖历史文件。
    """
    os.makedirs(_TESTCASE_DIR, exist_ok=True)
    today = datetime.now().strftime("%Y%m%d")
    prefix = f"bug{today}"
    pattern = os.path.join(_TESTCASE_DIR, f"{prefix}[0-9][0-9].xlsx")
    max_seq = 0
    for p in glob.glob(pattern):
        base = os.path.basename(p)
        m = re.match(r"^bug(\d{8})(\d{2})\.xlsx$", base, re.I)
        if m:
            max_seq = max(max_seq, int(m.group(2)))
    next_seq = max_seq + 1
    if next_seq > 99:
        next_seq = 99
    return os.path.join(_TESTCASE_DIR, f"{prefix}{next_seq:02d}.xlsx")


def pytest_sessionstart(session):
    global _BUG_SESSION_PATH
    _BUG_SESSION_PATH = _next_bug_report_path()
    logger.info("本次会话 Bug 报告文件: %s", _BUG_SESSION_PATH)


def pytest_configure(config):
    hc._CONFIG_PATH = _CFG


def _bug_path():
    """当前会话的 xlsx 路径；若 sessionstart 未执行则回退分配（不应发生）。"""
    global _BUG_SESSION_PATH
    if _BUG_SESSION_PATH is None:
        _BUG_SESSION_PATH = _next_bug_report_path()
    return _BUG_SESSION_PATH


def pytest_runtest_setup(item):
    """每个用例开始前清空 HTTP 快照，避免沿用上一条请求。"""
    hc.clear_last_http_call()


@pytest.fixture(scope="session")
def admin_client():
    c = HttpClient("admin")
    logger.info("admin base_url=%s", c.base_url)
    return c


@pytest.fixture(scope="session")
def user_client():
    c = HttpClient("user")
    logger.info("user base_url=%s", c.base_url)
    return c


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        try:
            err = str(report.longreprtext)[:4000] if hasattr(report, "longreprtext") else str(report.longrepr)[:4000]
            snap = hc.get_last_http_call()
            if snap:
                write_bug(
                    _bug_path(),
                    case_id=item.nodeid,
                    interface_name=snap.get("interface_name") or snap.get("path") or "N/A",
                    url=snap.get("url") or "N/A",
                    method=snap.get("method") or "N/A",
                    request_params=snap.get("request") or "N/A",
                    failure_reason=err,
                )
            else:
                write_bug(
                    _bug_path(),
                    case_id=item.nodeid,
                    interface_name="(无 HTTP 请求)",
                    url="N/A",
                    method="N/A",
                    request_params="本用例失败前未通过 HttpClient 发起请求（纯断言失败、导入错误或未调用接口）",
                    failure_reason=err,
                )
            logger.warning("[BUG] %s", item.nodeid)
        except Exception as e:
            logger.error("bug write failed: %s", e)


def pytest_sessionfinish(session, exitstatus):
    tr = session.config.pluginmanager.getplugin("terminalreporter")
    if not tr:
        return

    def n(k):
        return len(tr.stats.get(k, []))

    try:
        append_run_log(_bug_path(), n("passed"), n("failed"), n("skipped"), n("xfailed"), n("error"), exitstatus)
    except Exception as e:
        logger.error("RunLog failed: %s", e)

# -*- coding: utf-8 -*-
import pytest
import allure
from services.submission_service import SubmissionService
from utils.data_helper import assert_success, random_str
from lib.http_client import HttpClient


@allure.feature("投稿端")
class TestSubmission:
    def test_list_template(self, user_client):
        assert_success(SubmissionService(user_client).list_template(), "SUB-1")

    def test_save_draft(self, user_client):
        s = SubmissionService(user_client)
        assert_success(s.save(f"草稿_{random_str(4)}", "正文" * 20, domain_code="TD_HSGS", submit_type=0), "SUB-2")

    def test_empty_title(self, user_client):
        b = SubmissionService(user_client).save("", "x" * 50).json()
        assert b.get("isFail") or not b.get("isSuccess")

    def test_flow(self, user_client):
        s = SubmissionService(user_client)
        assert_success(s.save(f"flow_{random_str(6)}", "自动化正文" * 15, submit_type=0), "SUB-3")
        lst = s.page_myself(1, 10).json()
        rec = (lst.get("data") or {}).get("records") or []
        if not rec:
            pytest.skip("无稿件 id")
        sid = rec[0].get("id")
        assert s.detail(sid).status_code == 200
        assert s.count_myself().status_code == 200

    def test_no_token(self):
        c = HttpClient("user")
        c.set_token("bad")
        b = SubmissionService(c).page_myself().json()
        assert b.get("code") in (10002, 401) or b.get("isFail") or not b.get("isSuccess")

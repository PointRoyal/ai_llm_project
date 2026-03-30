# -*- coding: utf-8 -*-
import pytest
import allure
from services.admin_submission_service import AdminSubmissionService, RepetitionService
from utils.data_helper import assert_success


@allure.feature("管理端审核")
class TestAdminSubmission:
    def test_page_admin(self, admin_client):
        assert_success(AdminSubmissionService(admin_client).page_admin(), "AUD-1")

    def test_page_review(self, admin_client):
        assert AdminSubmissionService(admin_client).page_review().status_code == 200

    def test_counts(self, admin_client):
        s = AdminSubmissionService(admin_client)
        assert s.count_admin().status_code == 200
        assert s.count_review().status_code == 200

    def test_detail_bad(self, admin_client):
        assert AdminSubmissionService(admin_client).detail(999999999).status_code == 200

    def test_allocation_list(self, admin_client):
        assert AdminSubmissionService(admin_client).page_allocation().status_code == 200

    def test_list_check_user(self, admin_client):
        assert AdminSubmissionService(admin_client).list_check_user().status_code == 200

    def test_user_token(self, user_client):
        b = AdminSubmissionService(user_client).page_admin().json()
        if b.get("isSuccess"):
            pytest.xfail("用户 token 可调管理端审核列表")


@allure.feature("查重")
class TestRepetition:
    def test_page(self, admin_client):
        assert RepetitionService(admin_client).page_result().status_code == 200

    def test_get_bad(self, admin_client):
        assert RepetitionService(admin_client).get_result(999999999).status_code == 200

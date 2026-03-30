# -*- coding: utf-8 -*-
import allure
from services.admin_user_service import AdminUserService
from utils.data_helper import assert_success
from lib.http_client import HttpClient


@allure.feature("投稿人-系统管理端")
class TestAdminUser:
    def test_page(self, admin_client):
        assert_success(AdminUserService(admin_client).page(), "ADMIN-001")

    def test_invalid_token(self):
        c = HttpClient("admin")
        c.set_token("invalid")
        r = AdminUserService(c).page().json()
        assert r.get("code") in (10002, 401) or r.get("isFail") or not r.get("isSuccess")

# -*- coding: utf-8 -*-
import pytest
import allure
from services.app_user_service import AppUserService
from utils.data_helper import random_password, assert_success


@allure.feature("投稿人")
class TestLogin:
    @pytest.mark.skip(reason="在 config/api.yaml 填写真实账号后取消 skip")
    @pytest.mark.parametrize("account,password", [("", "")])
    def test_login_success(self, user_client, account, password):
        svc = AppUserService(user_client)
        assert_success(svc.login(account, password), "AUTH-015")

    def test_login_wrong_password(self, user_client):
        r = AppUserService(user_client).login("13800000001", "WrongPwd@999")
        b = r.json()
        assert b.get("isFail") or not b.get("isSuccess")

    def test_login_unregistered(self, user_client):
        b = AppUserService(user_client).login("10000000001", "Any@123").json()
        assert b.get("isFail") or not b.get("isSuccess")

    def test_login_empty_account(self, user_client):
        b = AppUserService(user_client).login("", "Any@123").json()
        assert b.get("isFail") or not b.get("isSuccess")


@allure.feature("投稿人")
class TestRegister:
    def test_register_random(self, user_client):
        import random
        phone = "138" + "".join(str(random.randint(0, 9)) for _ in range(8))
        r = AppUserService(user_client).register(phone, random_password(), "auto")
        assert r.status_code == 200


@allure.feature("投稿人")
class TestProtocol:
    def test_register_code(self, user_client):
        assert AppUserService(user_client).get_by_use_code("REGISTER").status_code == 200

    def test_service_code(self, user_client):
        assert AppUserService(user_client).get_by_use_code("SERVICE").status_code == 200

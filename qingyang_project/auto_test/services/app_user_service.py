# -*- coding: utf-8 -*-
import allure
from lib.http_client import HttpClient


class AppUserService:
    BASE = "/api/app/appUser"

    def __init__(self, client=None):
        self.client = client or HttpClient("user")

    @allure.step("login")
    def login(self, account, password, grant_type="password"):
        return self.client.post(
            f"{self.BASE}/login",
            json={
                "account": account,
                "password": password,
                "grantType": grant_type,
                "code": "",
                "key": "",
                "name": "",
                "zzdCode": "",
                "zzdId": "",
                "rememberMe": False,
            },
        )

    @allure.step("register")
    def register(self, account, password, name, station=""):
        return self.client.post(f"{self.BASE}/registerAppUser", json={"account": account, "password": password, "name": name, "station": station})

    @allure.step("getByUseCode")
    def get_by_use_code(self, code):
        return self.client.get(f"{self.BASE}/getByUseCode", params={"code": code})

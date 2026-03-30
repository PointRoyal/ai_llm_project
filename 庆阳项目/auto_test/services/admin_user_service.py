# -*- coding: utf-8 -*-
import allure
from lib.http_client import HttpClient
from utils.data_helper import page_params


class AdminUserService:
    BASE = "/api/system/appUser"

    def __init__(self, client=None):
        self.client = client or HttpClient("admin")

    @allure.step("page")
    def page(self, current=1, size=10, account="", name="", station=""):
        return self.client.post(f"{self.BASE}/page", json=page_params(current, size, {"account": account, "name": name, "station": station}))

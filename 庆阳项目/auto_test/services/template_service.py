# -*- coding: utf-8 -*-
import allure
from lib.http_client import HttpClient
from utils.data_helper import page_params


class TemplateService:
    BASE = "/api/template"

    def __init__(self, client=None):
        self.client = client or HttpClient("admin")

    @allure.step("saveTemplate")
    def save(self, name, title, domain, title_desc="", content_elements="", icon_url="", status=1):
        return self.client.post(
            f"{self.BASE}/saveTemplate",
            json={"name": name, "title": title, "titleDesc": title_desc, "contentElements": content_elements, "domain": domain, "iconUrl": icon_url, "status": status},
        )

    @allure.step("pageTemplate")
    def page(self, current=1, size=10, name="", status=None):
        return self.client.post(f"{self.BASE}/pageTemplate", json=page_params(current, size, {"name": name, "status": status}))

    @allure.step("detailTemplate")
    def detail(self, template_id):
        return self.client.get(f"{self.BASE}/detailTemplate", params={"id": template_id})

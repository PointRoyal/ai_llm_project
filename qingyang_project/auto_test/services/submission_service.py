# -*- coding: utf-8 -*-
import allure
from lib.http_client import HttpClient
from utils.data_helper import page_params


class SubmissionService:
    BASE = "/api/app/submission"

    def __init__(self, client=None):
        self.client = client or HttpClient("user")

    @allure.step("listTemplate")
    def list_template(self):
        return self.client.get(f"{self.BASE}/listTemplate")

    @allure.step("saveSubmission")
    def save(self, title, content_elements, domain_code="TD_HSGS", submit_type=0, anonymous=0, attachments=None):
        return self.client.post(
            f"{self.BASE}/saveSubmission",
            json={
                "title": title,
                "contentElements": content_elements,
                "domainCode": domain_code,
                "templateId": None,
                "anonymous": anonymous,
                "submitType": submit_type,
                "remark": "",
                "citationText": "",
                "attachments": attachments or [],
            },
        )

    @allure.step("pageMyselfSubmission")
    def page_myself(self, current=1, size=10, title="", submit_type=None):
        m = {"title": title}
        if submit_type is not None:
            m["submitType"] = submit_type
        return self.client.post(f"{self.BASE}/pageMyselfSubmission", json=page_params(current, size, m))

    @allure.step("countMyselfSubmission")
    def count_myself(self):
        return self.client.post(f"{self.BASE}/countMyselfSubmission", json={})

    @allure.step("detailSubmission")
    def detail(self, sid):
        return self.client.get(f"{self.BASE}/detailSubmission/{sid}")

    @allure.step("deleteSubmission")
    def delete(self, sid):
        return self.client.post(f"{self.BASE}/deleteSubmission", json={"id": sid})

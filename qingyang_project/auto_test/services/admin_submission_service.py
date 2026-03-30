# -*- coding: utf-8 -*-
import allure
from lib.http_client import HttpClient
from utils.data_helper import page_params


class AdminSubmissionService:
    BASE = "/api/submission"

    def __init__(self, client=None):
        self.client = client or HttpClient("admin")

    @allure.step("pageAdminSubmission")
    def page_admin(self, current=1, size=10, keyword=""):
        return self.client.post(f"{self.BASE}/pageAdminSubmission", json=page_params(current, size, {"keyword": keyword}))

    @allure.step("pageReviewSubmission")
    def page_review(self, current=1, size=10):
        return self.client.post(f"{self.BASE}/pageReviewSubmission", json=page_params(current, size, {}))

    @allure.step("countAdminSubmission")
    def count_admin(self):
        return self.client.get(f"{self.BASE}/countAdminSubmission")

    @allure.step("countReviewSubmission")
    def count_review(self):
        return self.client.get(f"{self.BASE}/countReviewSubmission")

    @allure.step("detailSubmission")
    def detail(self, sid):
        return self.client.get(f"{self.BASE}/detailSubmission/{sid}")

    @allure.step("pageAllocationSubmission")
    def page_allocation(self, current=1, size=10):
        return self.client.post(f"{self.BASE}/pageAllocationSubmission", json=page_params(current, size, {}))

    @allure.step("listCheckUser")
    def list_check_user(self):
        return self.client.post(f"{self.BASE}/listCheckUser", json={})


class RepetitionService:
    BASE = "/api/submissionRepetition"

    def __init__(self, client=None):
        self.client = client or HttpClient("admin")

    @allure.step("pageSubmissionRepetition")
    def page_result(self, current=1, size=10):
        return self.client.post(f"{self.BASE}/pageSubmissionRepetition", json=page_params(current, size, {}))

    @allure.step("getSubmissionRepetition")
    def get_result(self, submission_id):
        return self.client.post(f"{self.BASE}/getSubmissionRepetition", json={"submissionId": submission_id})

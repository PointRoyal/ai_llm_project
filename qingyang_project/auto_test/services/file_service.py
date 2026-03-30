# -*- coding: utf-8 -*-
import os
import allure
from lib.http_client import HttpClient


class FileService:
    BASE = "/api/pub"

    def __init__(self, client=None):
        self.client = client or HttpClient("admin")

    @allure.step("uploadFile")
    def upload_file(self, file_path):
        with open(file_path, "rb") as f:
            return self.client.post(f"{self.BASE}/uploadFile", files={"file": (os.path.basename(file_path), f)}, json=None)

    @allure.step("uploadImage")
    def upload_image(self, file_path):
        with open(file_path, "rb") as f:
            return self.client.post(f"{self.BASE}/uploadImage", files={"file": (os.path.basename(file_path), f)}, json=None)


class LargeFileService:
    BASE = "/api/pub/uploadFile"

    def __init__(self, client=None):
        self.client = client or HttpClient("admin")

    @allure.step("checkFileMd5")
    def check_file_md5(self, md5, filename, chunks):
        return self.client.post(f"{self.BASE}/checkFileMd5", params={"md5": md5, "filename": filename, "chunks": chunks}, json=None)

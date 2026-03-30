# -*- coding: utf-8 -*-
import os
import tempfile
import allure
from services.file_service import FileService, LargeFileService


@allure.feature("文件")
class TestFile:
    def test_upload_txt(self, admin_client):
        t = tempfile.NamedTemporaryFile(suffix=".txt", delete=False)
        t.write(b"hello")
        t.close()
        try:
            assert FileService(admin_client).upload_file(t.name).status_code == 200
        finally:
            os.unlink(t.name)

    def test_check_md5(self, admin_client):
        assert LargeFileService(admin_client).check_file_md5("d41d8cd98f00b204e9800998ecf8427e", "x.txt", 1).status_code == 200

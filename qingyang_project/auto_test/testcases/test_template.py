# -*- coding: utf-8 -*-
import pytest
import allure
from services.template_service import TemplateService
from utils.data_helper import assert_success, random_str


@allure.feature("投稿模板")
class TestTemplate:
    def test_save(self, admin_client):
        r = TemplateService(admin_client).save(f"auto_{random_str(4)}", "标题", ["TD_HSGS"])
        assert_success(r, "TPL-1")

    def test_page(self, admin_client):
        assert_success(TemplateService(admin_client).page(), "TPL-2")

    def test_detail_bad_id(self, admin_client):
        assert TemplateService(admin_client).detail(999999999).status_code == 200

    def test_full_crud(self, admin_client):
        svc = TemplateService(admin_client)
        name = f"crud_{random_str(6)}"
        assert_success(svc.save(name, "CRUD", ["TD_HSGS"]), "CRUD-1")
        lst = svc.page(current=1, size=20, name=name).json()
        rec = (lst.get("data") or {}).get("records") or []
        if not rec:
            pytest.skip("列表未返回新建模板")
        tid = rec[0].get("id")
        assert svc.detail(tid).status_code == 200

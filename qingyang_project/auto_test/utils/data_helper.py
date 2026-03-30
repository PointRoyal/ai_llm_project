# -*- coding: utf-8 -*-
import random
import string


def page_params(current=1, size=10, model=None):
    return {
        "current": current,
        "size": size,
        "sort": "",
        "order": "descending",
        "model": model or {},
        "map": {},
        "timeRange": None,
    }


def assert_success(resp, case_id=""):
    assert resp.status_code == 200, f"[{case_id}] HTTP {resp.status_code}"
    body = resp.json()
    ok = body.get("isSuccess") or body.get("success") or (body.get("code") == 0)
    assert ok, f"[{case_id}] {body.get('msg') or body}"
    return body


def random_str(n=6):
    return "".join(random.choices(string.ascii_lowercase, k=n))


def random_password(n=10):
    parts = (
        random.choices(string.ascii_uppercase, k=2)
        + random.choices(string.ascii_lowercase, k=3)
        + random.choices(string.digits, k=3)
        + random.choices("@#$", k=2)
    )
    random.shuffle(parts)
    return "".join(parts)

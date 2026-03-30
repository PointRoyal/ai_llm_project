# -*- coding: utf-8 -*-
import json
import os
import time
from typing import Any, Dict, Optional

import requests
import yaml

from .logger import logger

_CONFIG_PATH = None

# 最近一次 HTTP 调用（供失败时写入 bug.xlsx）；每个用例开始由 conftest 清空
_last_http_call: Optional[Dict[str, Any]] = None
_MAX_SNAPSHOT = 8000


def clear_last_http_call() -> None:
    global _last_http_call
    _last_http_call = None


def get_last_http_call() -> Optional[Dict[str, Any]]:
    return _last_http_call


def _truncate(s: str, n: int = _MAX_SNAPSHOT) -> str:
    if s is None:
        return ""
    s = str(s)
    return s if len(s) <= n else s[: n - 20] + "\n...(已截断)..."


def _summarize_request_kwargs(kwargs: dict) -> str:
    parts = []
    if kwargs.get("params"):
        try:
            parts.append("query: " + _truncate(json.dumps(kwargs["params"], ensure_ascii=False)))
        except Exception:
            parts.append("query: " + _truncate(str(kwargs["params"])))
    if kwargs.get("json") is not None:
        try:
            parts.append("json: " + _truncate(json.dumps(kwargs["json"], ensure_ascii=False)))
        except Exception:
            parts.append("json: " + _truncate(str(kwargs["json"])))
    if kwargs.get("data") is not None:
        d = kwargs["data"]
        if isinstance(d, (dict, list)):
            try:
                parts.append("data: " + _truncate(json.dumps(d, ensure_ascii=False)))
            except Exception:
                parts.append("data: " + _truncate(str(d)))
        else:
            parts.append("data: " + _truncate(str(d)))
    if kwargs.get("files"):
        fl = kwargs["files"]
        names = []
        if isinstance(fl, dict):
            for k, v in fl.items():
                if isinstance(v, tuple) and len(v) >= 1:
                    names.append(f"{k}={v[0]}")
                else:
                    names.append(f"{k}=<file>")
        else:
            names.append(str(fl))
        parts.append("multipart files: " + "; ".join(names))
    return "\n".join(parts) if parts else "(无 body/query)"


def _summarize_response(resp: requests.Response) -> str:
    line = f"HTTP {resp.status_code}"
    try:
        j = resp.json()
        body = json.dumps(j, ensure_ascii=False)
    except Exception:
        body = resp.text or ""
    return _truncate(line + "\n" + body)


def _default_cfg():
    p = _CONFIG_PATH or os.path.join(os.path.dirname(__file__), "..", "config", "api.yaml")
    with open(p, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


class HttpClient:
    def __init__(self, role: str = "admin"):
        cfg = _default_cfg()
        rc = cfg.get(role, cfg["admin"])
        self.base_url = rc["base_url"].rstrip("/")
        self.token = rc["token"]
        self.timeout = cfg.get("timeout", 30)
        self.session = requests.Session()
        self.session.headers.update(cfg.get("common_headers", {}))
        self.session.headers["Authorization"] = f"Bearer {self.token}"
        self.session.verify = False

    def set_token(self, token: str) -> None:
        self.token = token
        self.session.headers["Authorization"] = f"Bearer {token}"

    def _req(self, method: str, path: str, **kwargs):
        global _last_http_call
        url = self.base_url + path
        t0 = time.time()
        try:
            r = self.session.request(method, url, timeout=self.timeout, **kwargs)
            dt = time.time() - t0
            body = kwargs.get("json") or kwargs.get("data") or ""
            try:
                rb = r.json()
            except Exception:
                rb = r.text[:300]
            logger.debug(
                "[%s] %s → %s (%.3fs)\n  REQ: %s\n  RSP: %s",
                method, url, r.status_code, dt,
                json.dumps(body, ensure_ascii=False)[:400] if body else "-",
                json.dumps(rb, ensure_ascii=False)[:500] if isinstance(rb, dict) else str(rb)[:500],
            )
            # interface_name：与网关文档一致的 API 路径（不含 host），用于 bug 表「接口名称」列
            _last_http_call = {
                "method": method,
                "url": url,
                "path": path,
                "interface_name": path,
                "request": _summarize_request_kwargs(kwargs),
                "response": _summarize_response(r),
                "elapsed_sec": round(dt, 3),
            }
            return r
        except Exception as e:
            _last_http_call = {
                "method": method,
                "url": url,
                "path": path,
                "interface_name": path,
                "request": _summarize_request_kwargs(kwargs),
                "response": _truncate(f"请求异常（无响应体）: {type(e).__name__}: {e}"),
                "elapsed_sec": None,
            }
            logger.error("%s %s failed: %s", method, url, e)
            raise

    def get(self, path: str, params=None, **kw):
        return self._req("GET", path, params=params, **kw)

    def post(self, path: str, json=None, data=None, files=None, **kw):
        return self._req("POST", path, json=json, data=data, files=files, **kw)

    def delete(self, path: str, params=None, **kw):
        return self._req("DELETE", path, params=params, **kw)

"""
BaseAPI —— 所有 API 对象的基类
职责：
  1. 持有 Session，统一注入鉴权头
  2. 封装 GET / POST 请求，统一异常处理与日志
  3. 提供通用断言方法
"""
import time
import requests
from utils.logger import get_logger

logger = get_logger(__name__)


class BaseAPI:
    def __init__(self, env_cfg: dict):
        """
        :param env_cfg: config.yaml 中对应环境的配置字典
        """
        self.base_url = env_cfg["host"] + env_cfg["gateway"]
        self.timeout = env_cfg.get("timeout", 30)
        self.session = requests.Session()

        # 统一注入鉴权头
        bearer = env_cfg.get("bearer_token", "")
        admin_token = env_cfg.get("admin_token", "")
        self.session.headers.update({
            "Authorization": f"Bearer {bearer}",
            "Admin-Token": admin_token,
            "Content-Type": "application/json",
            "Accept": "application/json, text/plain, */*",
            "User-Agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/145.0.0.0 Safari/537.36"
            ),
        })

        # 注入 Cookie
        cookies = env_cfg.get("cookies", {})
        for k, v in cookies.items():
            self.session.cookies.set(k, v)

    def _post(self, path: str, payload: dict, use_token: bool = True,
              retry: int = 3, retry_interval: float = 2.0) -> requests.Response:
        """
        封装 POST 请求，内置限流重试
        :param path:           接口路径（相对于 gateway）
        :param payload:        请求体 dict
        :param use_token:      False 时移除鉴权头，用于测试未授权场景
        :param retry:          限流时重试次数（code=-4 系统繁忙自动重试）
        :param retry_interval: 限流重试间隔（秒）
        """
        url = self.base_url + path
        headers = {}
        if not use_token:
            headers["Authorization"] = ""
            headers["Admin-Token"] = ""

        for attempt in range(retry + 1):
            start = time.time()
            try:
                resp = self.session.post(
                    url,
                    json=payload,
                    headers=headers,
                    timeout=self.timeout,
                    verify=False,
                )
                elapsed = round((time.time() - start) * 1000, 2)
                logger.info(
                    f"POST {url} | status={resp.status_code} | elapsed={elapsed}ms"
                    + (f" | attempt={attempt + 1}" if attempt > 0 else "")
                )
                logger.debug(f"Response body : {resp.text[:500]}")

                # code=-4 为限流，自动重试
                try:
                    body = resp.json()
                    if body.get("code") == -4 and attempt < retry:
                        logger.warning(
                            f"服务端限流(code=-4)，{retry_interval}s 后重试 "
                            f"[{attempt + 1}/{retry}]"
                        )
                        time.sleep(retry_interval)
                        continue
                except Exception:
                    pass

                return resp
            except requests.exceptions.Timeout:
                logger.error(f"POST {url} 超时（>{self.timeout}s）")
                raise
            except requests.exceptions.ConnectionError as e:
                logger.error(f"POST {url} 连接失败: {e}")
                raise

        return resp  # 超出重试次数，返回最后一次响应

    def _get(self, path: str, params: dict = None, use_token: bool = True) -> requests.Response:
        """封装 GET 请求"""
        url = self.base_url + path
        headers = {}
        if not use_token:
            headers["Authorization"] = ""
            headers["Admin-Token"] = ""

        start = time.time()
        try:
            resp = self.session.get(
                url,
                params=params,
                headers=headers,
                timeout=self.timeout,
                verify=False,
            )
            elapsed = round((time.time() - start) * 1000, 2)
            logger.info(f"GET {url} | status={resp.status_code} | elapsed={elapsed}ms")
            return resp
        except requests.exceptions.Timeout:
            logger.error(f"GET {url} 超时（>{self.timeout}s）")
            raise

    # ------------------------------------------------------------------ #
    #  通用断言方法
    # ------------------------------------------------------------------ #
    @staticmethod
    def assert_success(resp: requests.Response, expected_code: int = 0) -> dict:
        """断言请求成功，返回解析后的 JSON"""
        assert resp.status_code == 200, (
            f"HTTP状态码异常: 期望200, 实际{resp.status_code}"
        )
        body = resp.json()
        assert body.get("code") == expected_code, (
            f"业务code异常: 期望{expected_code}, 实际{body.get('code')} | msg={body.get('msg')}"
        )
        assert body.get("success") is True, (
            f"success字段应为true, 实际={body.get('success')}"
        )
        return body

    @staticmethod
    def assert_unauthorized(resp: requests.Response):
        """断言未授权场景"""
        assert resp.status_code in (401, 403) or resp.json().get("code") != 0, (
            f"预期鉴权失败，但实际返回: status={resp.status_code}, body={resp.text[:200]}"
        )

    @staticmethod
    def assert_not_crash(resp: requests.Response):
        """断言接口不崩溃（状态码不为 5xx）"""
        assert resp.status_code < 500, (
            f"接口发生服务端错误: status={resp.status_code}, body={resp.text[:200]}"
        )

    @staticmethod
    def assert_business_fail(resp: requests.Response):
        """断言业务层返回失败（code != 0 或 success=false）"""
        body = resp.json()
        is_fail = (body.get("code") != 0) or (body.get("success") is False)
        assert is_fail, (
            f"预期业务失败，但实际返回成功: body={body}"
        )
        return body

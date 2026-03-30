"""
ProjectAPI —— 项目模块 API 对象（类比 PO 模式中的 Page Object）
封装所有与"项目"相关的接口调用，测试层只调用此类的方法，不关心 URL 细节
"""
from typing import Optional
from api.base_api import BaseAPI
from utils.logger import get_logger

logger = get_logger(__name__)


class ProjectAPI(BaseAPI):

    # ------------------------------------------------------------------ #
    #  接口路径常量
    # ------------------------------------------------------------------ #
    PATH_DASHBOARD = "/frontProjects/frontProjectsDashboard"
    PATH_UPDATE    = "/frontProjects/updateFrontProjects"
    PATH_CREATE    = "/frontProjects/addFrontProjects"    # 【需确认实际路径】
    PATH_DELETE    = "/frontProjects/deleteFrontProjects" # 【需确认实际路径】

    # ------------------------------------------------------------------ #
    #  查询看板列表
    # ------------------------------------------------------------------ #
    def get_dashboard(self, current: int = 1, size: int = 999,
                      order: str = "asc", sort: str = "createTime",
                      use_token: bool = True) -> dict:
        """
        查询项目看板列表
        :return: 完整响应 JSON
        """
        payload = {
            "params": {"current": current, "map": {}},
            "model": {"order": order, "size": size, "sort": sort},
        }
        resp = self._post(self.PATH_DASHBOARD, payload, use_token=use_token)
        return resp

    def get_dashboard_with_payload(self, payload: dict, use_token: bool = True):
        """使用自定义 payload 查询（用于数据驱动）"""
        return self._post(self.PATH_DASHBOARD, payload, use_token=use_token)

    def get_project_by_id(self, project_id: str) -> Optional[dict]:
        """从列表中查找指定 ID 的项目，找不到返回 None"""
        resp = self.get_dashboard(size=999)
        body = resp.json()
        for p in body.get("data", {}).get("records", []):
            if p.get("id") == project_id:
                return p
        return None

    # ------------------------------------------------------------------ #
    #  更新项目
    # ------------------------------------------------------------------ #
    def update_project(self, payload: dict, use_token: bool = True):
        """
        更新项目信息
        :param payload: 完整项目数据（含 tasks 列表）
        :param use_token: False 时测试未授权场景
        :return: Response 对象
        """
        logger.info(f"更新项目: id={payload.get('id')}, name={payload.get('projectName')}")
        return self._post(self.PATH_UPDATE, payload, use_token=use_token)

    def update_project_field(self, project_id: str, field: str, value) -> object:
        """
        便捷方法：只修改单个字段
        先查出当前项目数据，再修改指定字段后提交
        """
        project = self.get_project_by_id(project_id)
        if project is None:
            raise ValueError(f"项目不存在: {project_id}")
        project[field] = value
        # 补充 tasks（若项目数据中无 tasks 字段需单独获取）
        if "tasks" not in project:
            project["tasks"] = []
        return self.update_project(project)

    # ------------------------------------------------------------------ #
    #  创建项目（路径待确认）
    # ------------------------------------------------------------------ #
    def create_project(self, payload: dict, use_token: bool = True):
        """创建新项目【需确认接口路径】"""
        logger.info(f"创建项目: name={payload.get('projectName')}")
        return self._post(self.PATH_CREATE, payload, use_token=use_token)

    # ------------------------------------------------------------------ #
    #  删除项目（路径待确认）
    # ------------------------------------------------------------------ #
    def delete_project(self, project_id: str, use_token: bool = True):
        """删除项目【需确认接口路径和参数格式】"""
        logger.info(f"删除项目: id={project_id}")
        return self._post(self.PATH_DELETE, {"id": project_id}, use_token=use_token)

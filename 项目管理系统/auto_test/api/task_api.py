"""
TaskAPI —— 任务模块 API 对象
任务数据通过项目更新接口（updateFrontProjects）提交，
本类提供任务级别的便捷操作方法
"""
import copy
from api.project_api import ProjectAPI
from utils.logger import get_logger

logger = get_logger(__name__)

# 标准任务模板，避免每次构造完整 dict
_TASK_TEMPLATE = {
    "creator": "",
    "colorTag": "normal",
    "parentTaskId": "0",
    "predecessorTaskId": None,
    "followerId": None,
}


class TaskAPI(ProjectAPI):
    """继承 ProjectAPI，复用项目接口，扩展任务操作"""

    def build_task(self, task_id: str, name: str, start_date: str,
                   end_date: str, duration: int, progress: float,
                   project_id: str, parent_task_id: str = "0",
                   predecessor_task_id: str = None,
                   follower_id: str = None,
                   color_tag: str = "normal") -> dict:
        """构造单个任务 dict"""
        task = copy.deepcopy(_TASK_TEMPLATE)
        task.update({
            "id": task_id,
            "name": name,
            "startDate": start_date,
            "endDate": end_date,
            "duration": duration,
            "progress": progress,
            "projectId": project_id,
            "parentTaskId": parent_task_id,
            "predecessorTaskId": predecessor_task_id,
            "followerId": follower_id,
            "colorTag": color_tag,
        })
        return task

    def build_tasks_batch(self, count: int, project_id: str,
                          start_date: str = "2026-03-09",
                          end_date: str = "2026-03-11") -> list:
        """批量生成指定数量的任务（用于边界/性能测试）"""
        import time as _time
        # 使用毫秒级时间戳生成唯一 13 位数字 ID，符合服务端格式要求
        base_ts = int(_time.time() * 1000) - count * 10
        tasks = []
        for i in range(count):
            tasks.append(self.build_task(
                task_id=str(base_ts + i * 10),
                name=f"自动生成任务{i + 1}",
                start_date=start_date,
                end_date=end_date,
                duration=2,
                progress=0,
                project_id=project_id,
            ))
        return tasks

    def update_task_in_project(self, project_payload: dict,
                               task_id: str, field: str, value) -> object:
        """
        在项目 payload 中找到指定任务并修改单个字段，然后提交更新
        :param project_payload: 完整项目 payload（含 tasks）
        :param task_id:         要修改的任务 ID
        :param field:           要修改的字段名
        :param value:           新值
        """
        payload = copy.deepcopy(project_payload)
        modified = False
        for task in payload.get("tasks", []):
            if task.get("id") == task_id:
                task[field] = value
                modified = True
                break
        if not modified:
            raise ValueError(f"任务不存在: {task_id}")
        logger.info(f"修改任务 {task_id} 字段 {field}={value}")
        return self.update_project(payload)

    def set_task_progress(self, project_payload: dict,
                          task_id: str, progress: float) -> object:
        """设置任务进度"""
        return self.update_task_in_project(project_payload, task_id, "progress", progress)

    def set_task_predecessor(self, project_payload: dict,
                             task_id: str, predecessor_id: str) -> object:
        """设置前置任务"""
        return self.update_task_in_project(
            project_payload, task_id, "predecessorTaskId", predecessor_id
        )

    def set_task_dates(self, project_payload: dict, task_id: str,
                       start_date: str, end_date: str) -> object:
        """同时修改任务开始/结束时间"""
        payload = copy.deepcopy(project_payload)
        for task in payload.get("tasks", []):
            if task.get("id") == task_id:
                task["startDate"] = start_date
                task["endDate"] = end_date
                break
        return self.update_project(payload)

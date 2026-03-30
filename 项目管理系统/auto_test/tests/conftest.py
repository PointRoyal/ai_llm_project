"""
pytest 全局 fixtures
- 提供 project_api / task_api 实例
- 提供测试数据 fixture
- 提供 reporter fixture（收集结果，用例完毕生成报告）
"""
import pytest
import sys
import os

# 将 auto_test 根目录加入路径，使各层 import 正常工作
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import time
from api.project_api import ProjectAPI
from api.task_api import TaskAPI
from utils.data_loader import load_config, load_test_data
from utils.reporter import Reporter


# ------------------------------------------------------------------ #
#  环境配置
# ------------------------------------------------------------------ #
@pytest.fixture(scope="session")
def env_cfg():
    """加载当前激活环境的配置（整个测试会话共享）"""
    return load_config()


# ------------------------------------------------------------------ #
#  API 对象
# ------------------------------------------------------------------ #
@pytest.fixture(scope="session")
def project_api(env_cfg):
    """ProjectAPI 实例（会话级，复用 Session）"""
    return ProjectAPI(env_cfg)


@pytest.fixture(scope="session")
def task_api(env_cfg):
    """TaskAPI 实例（会话级，复用 Session）"""
    return TaskAPI(env_cfg)


# ------------------------------------------------------------------ #
#  测试数据
# ------------------------------------------------------------------ #
@pytest.fixture(scope="session")
def project_data():
    return load_test_data("project_data.yaml")


@pytest.fixture(scope="session")
def task_data():
    return load_test_data("task_data.yaml")


@pytest.fixture(scope="session")
def existing_project_id(env_cfg):
    """从配置读取已存在的项目ID"""
    return env_cfg["_test_settings"]["existing_project_id"]


# ------------------------------------------------------------------ #
#  限流保护：写操作（update）之间至少间隔 5s，避免服务端 code=-4
# ------------------------------------------------------------------ #
@pytest.fixture(autouse=True)
def rate_limit_guard(request):
    """
    对调用 update 接口的测试，前后各等待一段时间，防止服务端限流（code=-4）
    只对涉及 update 的测试模块生效
    """
    update_modules = {"test_project_crud", "test_task_mgmt"}
    module_name = request.module.__name__.split(".")[-1]
    if module_name in update_modules:
        time.sleep(3)   # 前置等待
    yield
    if module_name in update_modules:
        time.sleep(2)   # 后置等待（给服务端解除限流缓冲）


# ------------------------------------------------------------------ #
#  报告收集
# ------------------------------------------------------------------ #
@pytest.fixture(scope="session")
def reporter():
    return Reporter()


@pytest.fixture(scope="session", autouse=True)
def generate_report_at_end(reporter):
    """所有用例执行完毕后自动生成报告"""
    yield
    if reporter.results:
        reporter.generate_html()
        reporter.generate_json()


# ------------------------------------------------------------------ #
#  真实项目 payload（供更新/任务测试用）
# ------------------------------------------------------------------ #
@pytest.fixture(scope="session")
def base_project_payload(existing_project_id):
    """
    从真实接口拉取项目完整 payload，作为后续修改测试的基准数据
    注意：此 fixture 依赖网络，若环境不可达会在此失败
    """
    return {
        "id": existing_project_id,
        "projectName": "这是一个非常重要非常有名气非常有钱非常有名提高企业知名度非常重要的项目之宁波可信数据空间提前实施部署",
        "city": "上海",
        "startDate": "2024-06-05",
        "endDate": "2027-11-24",
        "status": 1,
        "owner": "2029796795590172673",
        "milestones": "[]",
        "tasks": [
            {"id": "1773715019830", "name": "发布", "startDate": "2024-06-05",
             "endDate": "2024-06-05", "duration": 1, "progress": 0,
             "creator": "", "colorTag": "normal", "parentTaskId": "0",
             "predecessorTaskId": None, "followerId": None,
             "projectId": existing_project_id},
            {"id": "1773715016347", "name": "接触", "startDate": "2026-02-27",
             "endDate": "2026-03-25", "duration": 6, "progress": 16.11,
             "creator": "", "colorTag": "normal", "parentTaskId": "0",
             "predecessorTaskId": None, "followerId": "2029796795590172673",
             "projectId": existing_project_id},
        ],
    }

"""
数据加载工具 —— 统一读取 YAML 配置和测试数据
"""
import os
import yaml


def load_yaml(filepath: str) -> dict:
    """加载 YAML 文件，返回 dict"""
    with open(filepath, encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_config() -> dict:
    """加载全局配置，返回当前激活环境的配置 dict"""
    base = os.path.join(os.path.dirname(__file__), "..", "config", "config.yaml")
    cfg = load_yaml(os.path.abspath(base))
    active = cfg["active_env"]
    env_cfg = cfg["environments"][active]
    env_cfg["_test_settings"] = cfg.get("test_settings", {})
    return env_cfg


def load_test_data(filename: str) -> dict:
    """
    加载 data/ 目录下指定 YAML 测试数据文件
    :param filename: 如 'project_data.yaml'
    """
    base = os.path.join(os.path.dirname(__file__), "..", "data", filename)
    return load_yaml(os.path.abspath(base))

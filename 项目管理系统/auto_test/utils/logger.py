"""
统一日志工具
- 同时输出到控制台和文件
- 日志文件按日期滚动，保留 7 天
"""
import logging
import os
from logging.handlers import TimedRotatingFileHandler

_LOG_DIR = os.path.join(os.path.dirname(__file__), "..", "reports", "logs")
from typing import Dict
_initialized: Dict[str, logging.Logger] = {}


def get_logger(name: str = "auto_test", level: str = "INFO") -> logging.Logger:
    if name in _initialized:
        return _initialized[name]

    os.makedirs(_LOG_DIR, exist_ok=True)
    log_file = os.path.join(_LOG_DIR, "test.log")

    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, level.upper(), logging.INFO))

    fmt = logging.Formatter(
        fmt="%(asctime)s [%(levelname)-5s] %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # 控制台 Handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(fmt)
    console_handler.setLevel(logging.DEBUG)

    # 文件 Handler（按天滚动，保留 7 天）
    file_handler = TimedRotatingFileHandler(
        log_file, when="midnight", backupCount=7, encoding="utf-8"
    )
    file_handler.setFormatter(fmt)
    file_handler.setLevel(logging.DEBUG)

    if not logger.handlers:
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    _initialized[name] = logger
    return logger

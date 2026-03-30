# 项目管理系统 — 接口自动化测试框架

## 目录结构

```
auto_test/
├── config/
│   └── config.yaml          # 环境配置（host、token，切环境只改 active_env）
├── data/
│   ├── project_data.yaml    # 项目接口测试数据
│   └── task_data.yaml       # 任务接口测试数据
├── api/                     # API 对象层（类比 Page Object）
│   ├── base_api.py          # 基类：Session、鉴权、通用断言
│   ├── project_api.py       # 项目模块接口封装
│   └── task_api.py          # 任务模块接口封装
├── tests/
│   ├── conftest.py          # pytest fixtures（API实例、数据、报告）
│   ├── test_project_list.py # 项目列表查询测试
│   ├── test_project_crud.py # 项目更新测试
│   └── test_task_mgmt.py    # 任务管理测试
├── utils/
│   ├── logger.py            # 统一日志（控制台+文件滚动）
│   ├── reporter.py          # HTML / JSON 报告生成
│   └── data_loader.py       # YAML 数据加载工具
├── reports/                 # 自动生成（运行后创建）
│   ├── logs/test.log
│   ├── report_*.html
│   └── report_*.json
├── pytest.ini
└── requirements.txt
```

## 快速开始

### 1. 安装依赖

```bash
cd auto_test
pip install -r requirements.txt
```

### 2. 修改环境配置

编辑 `config/config.yaml`，确认 `active_env: dev` 及对应的 `host` 和 `token`。

### 3. 运行全部测试

```bash
cd auto_test
pytest
```

### 4. 运行指定模块

```bash
# 只跑项目列表测试
pytest tests/test_project_list.py -v

# 只跑任务管理测试
pytest tests/test_task_mgmt.py -v

# 只跑某个用例
pytest tests/test_project_crud.py::TestProjectUpdate::test_normal_update -v
```

### 5. 生成报告

测试完成后自动在 `reports/` 目录生成：
- `report_YYYYMMDD_HHMMSS.html` — 可视化 HTML 报告（浏览器打开）
- `report_YYYYMMDD_HHMMSS.json` — JSON 格式（供 CI 解析）

## 数据与代码分离说明

| 文件 | 职责 |
|------|------|
| `data/project_data.yaml` | 所有项目接口的入参、期望结果 |
| `data/task_data.yaml` | 所有任务接口的入参、期望结果 |
| `config/config.yaml` | 环境变量（host、token），切环境无需改代码 |
| `api/*.py` | 接口封装，只管"如何调"，不关心数据 |
| `tests/*.py` | 只关心"断言逻辑"，数据从 YAML fixture 注入 |

## 用例标记说明

| 标记 | 含义 |
|------|------|
| `@pytest.mark.smoke` | 冒烟测试，每次部署后必跑 |
| `@pytest.mark.regression` | 回归测试 |
| `@pytest.mark.performance` | 性能测试（响应时间断言） |
| `@pytest.mark.security` | 安全测试（XSS/SQL注入） |
| `pytest.xfail(...)` | 已知 Bug，标记为预期失败，不影响整体通过率 |

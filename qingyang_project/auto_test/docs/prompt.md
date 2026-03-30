请根据以下要求完成接口自动化测试框架搭建与用例执行任务：
一、项目结构说明
接口文档位于 docs/knife4j-在线文档-接口摘录.md
测试用例清单在 testcase/testcase.xlsx 中，包含字段如：用例编号、接口名称、请求方法、URL、请求参数、预期响应等,请自动识别。
用户身份凭证（token）统一从 api.yaml 文件中的 Authorization 字段读取。
接口分为两类：
用户端接口：从用户端的接口里获取。
管理端接口：从管理端的接口获取。
二、自动化测试任务要求
解析测试用例
读取 testcase/testcase.xlsx，提取每个测试用例对应的接口信息，并匹配 docs/ 下的接口定义，确保请求结构正确。
执行接口测试
对每个用例发起 HTTP 请求（支持 GET/POST/PUT/DELETE 等）。
自动注入用户 token 到请求头（Authorization: Bearer <token>）。
验证响应状态码、关键字段、业务逻辑是否符合预期。
错误处理与缺陷记录
若测试失败（断言不通过、超时、异常等），将该用例的详细信息（包括：用例ID、接口名、请求参数、实际响应、错误原因、时间戳等）追加写入 testcase/bug.xlsx 的新工作表（如 “AutoBugReport”）中。
若 bug.xlsx 不存在，则自动创建。
暂停不确定项
如果某个接口在文档中缺失、参数不明确、或权限类型（用户/管理端）无法判断，请不要猜测，而是暂停该用例执行，并向我提问确认后再继续。
三、自动化测试框架开发要求
在项目根目录下新建 auto_test/ 文件夹，作为自动化测试框架的主目录。
框架必须基于以下技术栈构建：
语言：Python 3.8+
测试框架：pytest
报告工具：Allure
设计模式：Page Object (PO) 模式（此处“Page”指接口模块，可抽象为 Service 层）
框架需具备高复用性，即：只需替换配置文件和测试数据，即可用于其他项目。
框架结构建议包括（但不限于）：

auto_test/
├── config/
│   └── api.yaml          # 存放基础URL、token等配置（从项目根目录复制或链接）
├── testcases/            # pytest 测试脚本（由 testcase.xlsx 自动生成或映射）
├── lib/                  # 封装通用方法（如 http_client, excel_reader, logger 等）
├── pages/ or services/   # 按 PO 模式封装各接口模块（如 user_service.py, order_api.py）
├── utils/                # 工具类
├── reports/              # Allure 报告输出目录
├── conftest.py           # pytest 配置（fixture、全局钩子等）
└── requirements.txt      # 依赖列表（含 pytest, requests, allure-pytest, openpyxl 等）
框架初始化后，先生成空结构 + 样例代码，再根据本项目配置填入具体内容。
四、交付物
完整的 auto_test/ 框架代码（可运行）。
成功执行 testcase/testcase.xlsx 中所有已确认无歧义的用例。
run.log文件每次更新时也用日期区分，旧的不删除
生成 Allure 测试报告（存于 auto_test/reports/）。
所有失败用例记录到 testcase/bug.xlsx，且每次生成后原来的文件不删除，用日期新增）
如遇不确定项，列出问题清单供我确认。
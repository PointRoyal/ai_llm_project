"""
测试报告工具
- 收集每条用例的执行结果
- 生成 HTML 报告（内嵌样式，无外部依赖）
- 生成 Excel 报告（在已有测试用例表中回写实际结果）
"""
import os
import json
import datetime
from dataclasses import dataclass, field
from typing import Literal

Status = Literal["PASS", "FAIL", "SKIP", "ERROR"]


@dataclass
class CaseResult:
    case_id: str
    title: str
    module: str
    status: Status
    elapsed_ms: float = 0.0
    request_body: dict = field(default_factory=dict)
    response_body: dict = field(default_factory=dict)
    error_msg: str = ""
    executed_at: str = field(
        default_factory=lambda: datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )


class Reporter:
    def __init__(self, report_dir: str = None):
        base = os.path.join(os.path.dirname(__file__), "..", "reports")
        self.report_dir = report_dir or base
        os.makedirs(self.report_dir, exist_ok=True)
        self.results: list[CaseResult] = []

    def add(self, result: CaseResult):
        self.results.append(result)

    # ------------------------------------------------------------------ #
    #  HTML 报告
    # ------------------------------------------------------------------ #
    def generate_html(self, filename: str = None) -> str:
        ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = filename or f"report_{ts}.html"
        path = os.path.join(self.report_dir, filename)

        total = len(self.results)
        passed = sum(1 for r in self.results if r.status == "PASS")
        failed = sum(1 for r in self.results if r.status == "FAIL")
        errored = sum(1 for r in self.results if r.status == "ERROR")
        skipped = sum(1 for r in self.results if r.status == "SKIP")
        pass_rate = f"{passed / total * 100:.1f}%" if total else "N/A"

        rows_html = ""
        for r in self.results:
            color = {
                "PASS": "#6BCB77", "FAIL": "#FF6B6B",
                "ERROR": "#FF6B6B", "SKIP": "#FFD93D",
            }.get(r.status, "#ccc")
            err = r.error_msg.replace("<", "&lt;").replace(">", "&gt;")
            rows_html += f"""
            <tr>
              <td>{r.case_id}</td>
              <td>{r.module}</td>
              <td>{r.title}</td>
              <td style="background:{color};font-weight:bold;text-align:center">{r.status}</td>
              <td style="text-align:right">{r.elapsed_ms:.0f} ms</td>
              <td style="color:#c0392b;font-size:12px">{err}</td>
              <td>{r.executed_at}</td>
            </tr>"""

        html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8"/>
<title>接口自动化测试报告</title>
<style>
  body {{ font-family: 'Microsoft YaHei', Arial, sans-serif; background:#f5f7fa; margin:0; padding:20px; }}
  h1 {{ color:#2c3e50; }}
  .summary {{ display:flex; gap:20px; margin:20px 0; flex-wrap:wrap; }}
  .card {{ background:#fff; border-radius:8px; padding:16px 24px; box-shadow:0 2px 8px rgba(0,0,0,.08); min-width:120px; text-align:center; }}
  .card .num {{ font-size:2em; font-weight:bold; }}
  .card .label {{ color:#888; font-size:13px; }}
  .pass {{ color:#6BCB77; }}
  .fail {{ color:#FF6B6B; }}
  .skip {{ color:#FFD93D; }}
  table {{ width:100%; border-collapse:collapse; background:#fff; border-radius:8px; overflow:hidden; box-shadow:0 2px 8px rgba(0,0,0,.08); }}
  th {{ background:#2E75B6; color:#fff; padding:10px 12px; text-align:left; font-size:13px; }}
  td {{ padding:9px 12px; border-bottom:1px solid #f0f0f0; font-size:13px; vertical-align:top; }}
  tr:hover td {{ background:#f9fbff; }}
</style>
</head>
<body>
<h1>项目管理系统 — 接口自动化测试报告</h1>
<p style="color:#888">生成时间：{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>

<div class="summary">
  <div class="card"><div class="num">{total}</div><div class="label">总用例</div></div>
  <div class="card"><div class="num pass">{passed}</div><div class="label">通过</div></div>
  <div class="card"><div class="num fail">{failed + errored}</div><div class="label">失败</div></div>
  <div class="card"><div class="num skip">{skipped}</div><div class="label">跳过</div></div>
  <div class="card"><div class="num" style="color:#2E75B6">{pass_rate}</div><div class="label">通过率</div></div>
</div>

<table>
  <thead>
    <tr>
      <th>用例编号</th><th>模块</th><th>用例标题</th>
      <th>结果</th><th>耗时</th><th>失败原因</th><th>执行时间</th>
    </tr>
  </thead>
  <tbody>
    {rows_html}
  </tbody>
</table>
</body>
</html>"""

        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"\n📊 HTML 报告已生成: {path}")
        return path

    # ------------------------------------------------------------------ #
    #  JSON 报告（供 CI 解析）
    # ------------------------------------------------------------------ #
    def generate_json(self, filename: str = None) -> str:
        ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = filename or f"report_{ts}.json"
        path = os.path.join(self.report_dir, filename)
        data = [r.__dict__ for r in self.results]
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"📄 JSON 报告已生成: {path}")
        return path

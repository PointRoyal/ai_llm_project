#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成用于「上传大小限制约 1GB」联调的 MP4 体积测试文件（非可播放长视频，仅体积与扩展名符合联调）。

**为什么 macOS / Finder 里原先标「1G」的文件会变成约 1.07 GB？**
  若文件按 **1 GiB = 1024³ = 1 073 741 824 字节** 生成，按 **十进制 GB（10⁹）** 换算是
  1 073 741 824 ÷ 1 000 000 000 ≈ **1.074 GB**，界面就会接近 **1.07 GB**。

本脚本默认按 **十进制** 定义「兆」：**1 MB = 10⁶ 字节**，**1000 MB = 10⁹ 字节 = 1 000 000 000 字节**，
在 Finder 里更接近 **1 GB（十进制）**。

- 小于约 1G：900 MB（十进制）
- 等于 1000M：**1 000 × 10⁶ = 1 000 000 000 字节**
- 大于约 1G：**1 000 000 000 + 10 000 000 字节**（多 10 MB 十进制）

用法：
  python3 generate_mp4_test_files.py
  python3 generate_mp4_test_files.py --outdir .
"""
import argparse
import os

# 最小 ftyp 头 + 填充到 128 字节
def _minimal_header() -> bytes:
    h = (
        b"\x00\x00\x00\x20ftyp"
        b"isom"
        b"\x00\x00\x02\x00"
        b"isomiso2mp41"
    )
    return h + b"\x00" * (128 - len(h))


def write_dummy_mp4(path: str, size_bytes: int) -> None:
    if size_bytes < 128:
        raise ValueError("size_bytes 需 >= 128")
    header = _minimal_header()
    os.makedirs(os.path.dirname(os.path.abspath(path)) or ".", exist_ok=True)
    with open(path, "wb") as f:
        f.write(header)
        if size_bytes > len(header):
            f.seek(size_bytes - 1)
            f.write(b"\x00")
    actual = os.path.getsize(path)
    if actual != size_bytes:
        raise OSError(f"文件大小不符: 期望 {size_bytes}, 实际 {actual}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--outdir",
        default=os.path.dirname(os.path.abspath(__file__)),
        help="输出目录，默认为本脚本所在目录（testcase）",
    )
    args = ap.parse_args()
    out = os.path.abspath(args.outdir)

    MB = 10**6  # 十进制兆字节（与硬盘标称、Finder 十进制展示一致）

    exact_1000m = 1000 * MB  # 1 000 000 000 字节

    specs = [
        ("upload_test_under_1g.mp4", 900 * MB, "900 MB（十进制），小于 1000 MB"),
        ("upload_test_exact_1g.mp4", exact_1000m, "1000 MB（十进制）= 1 000 000 000 字节"),
        ("upload_test_over_1g.mp4", exact_1000m + 10 * MB, "1000 MB + 10 MB（十进制）"),
    ]

    for name, size, desc in specs:
        path = os.path.join(out, name)
        print(f"生成 {name} ({desc}) = {size} 字节 ...")
        write_dummy_mp4(path, size)
        print(f"  -> {path}")

    print("完成。")


if __name__ == "__main__":
    main()

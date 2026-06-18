# 功能要求
# 读日志文件（with open）
# 可选按级别过滤（--level，不传就显示全部）
# 提取每条的日期、级别、消息
# 统计每种级别出现次数，用 tabulate 打表格
# 可选保存到文件（--output）
# 详细模式（--verbose）显示逐条日志内容
# 提示
# 步骤拆解：

# ① 用 argparse 定义参数：

# 位置参数：日志文件名
# --level：可选，如 INFO/ERROR/WARN
# --output：可选，输出文件路径
# --verbose：开关
# ② 读文件时逐行解析，每行格式： 2026-06-08 ERROR DB connection failed from 10.0.0.1

# ③ 用 split() 或 re.search() 提取各部分 ④ 用条件判断过滤级别 ⑤ 用 collections.Counter 或自己写字典计数 ⑥ 用 tabulate 打印表格

import argparse
import sys
from tabulate import tabulate


parser = argparse.ArgumentParser()

parser.add_argument("file" , help="files to be analysis")
parser.add_argument("--level" , help="event level")
parser.add_argument("--output" , help="exporting report")
parser.add_argument("--verbose" , action="store_true" , help="verbose enable")

argus = parser.parse_args()

if argus.verbose:
    print("reading log")

try:
    with open(argus.file , "r") as f:
        counts = {}
        for line in f:
            parts = line.strip().split()
            if len(parts) < 2:
                continue
            if argus.level and argus.level != parts[1]:
                continue
            if argus.level:
                level = argus.level
            else:
                level = parts[1]
            if level == parts[1]:
               counts[level] = counts.get(level , 0) + 1
    table = tabulate(counts.items() , headers=["event_level" , "total"] , floatfmt = "grip")
    if argus.verbose:
        print("getting result")
    print(f"report : {table}")
except FileNotFoundError :
    print("file is not exist")  
    

if argus.output:
    if argus.verbose:
        print("exporting report")
    with open("report2.txt" , "w") as f:
        f.write(table)
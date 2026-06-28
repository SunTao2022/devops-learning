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

parser = argparse.ArgumentParser(description= "log analuzer tool")

parser.add_argument( log.txt , type=open , help= "log to be analysis ")
parser.add_argument("--level" , help= "level")
parser.add_argument("--output" , help= "output")
parser.add_argument("verbose" , action="store_true" , help="verbose mode")


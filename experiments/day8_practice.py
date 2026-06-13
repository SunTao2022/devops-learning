# Day 8 — 模块 + sys/os + df/du/free + Git graph
# 你的代码写在这里

# ----- Q1: sys.argv 命令行参数 -----
# 运行: python day8_practice.py web-01
# 期望输出: Checking server: web-01
# import sys

# print("You passed:", sys.argv)  # 看看 argv 是什么

# # 你的代码：取 sys.argv[1] 打印 "Checking server: ..."
# # 提示：先判断 len(sys.argv) > 1，否则打印 "No server name given"
# if len(sys.argv) > 1:
#     print(f"Checking server: {sys.argv[1]}")
# else:
#     print("No server name given")






# # ----- Q2: os 模块 — 获取系统信息 -----
# import os

# # 1. 当前工作目录（os.getcwd()）
# print("当前目录:", os.getcwd())


# # 2. HOME 目录（os.environ.get）
# print("HOME:", os.environ.get("HOME"))

# # 3. 列出 experiments/ 下所有 .py 文件
# # 提示：os.listdir("experiments") 列出文件，判断每个是否以 ".py" 结尾
# # 用 for 循环 + if ".py" in filename 或 filename.endswith(".py")
# py_files = []
# for f in os.listdir("experiments"):
#     if f.endswith(".py"):
#         py_files.append(f)
# print("Python 文件:", py_files)

# # 4. 用 os.path.join 拼接路径
# report_path = os.path.join("reports", "server_report.txt")
# print("报告路径:", report_path)




import sys

# ① 判断有没有传参数（len(sys.argv) < 2）
if len(sys.argv) < 2:
    print("No more agument")
# ② 取参数（sys.argv[1]）
else:
    print(f'agument is :{sys.argv[1]}')
# ③ 读文件逐行，找匹配的服务器名
found = False
with open("servers.txt","r") as f:
    for line in f:
        servers = line.strip().split(",")
        if sys.argv[1] == servers[0]:
            found = True
            print("found it ")
            sys.exit()
if found == False:
    print("No found")

# ④ 找到了打印状态，设标志为 True，break
# ⑤ 循环结束后检查标志，没找到就打印"not found"
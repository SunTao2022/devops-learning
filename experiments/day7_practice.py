"""
Day 7 — re.sub + 综合复习
"""
import re

# ----- Q1: 脱敏 IP 地址 -----
# 读取 app.log，把所有 IP 替换为 [MASKED]
# 提示：先读文件（with open），再逐行 re.sub（for 循环）
with open("app.log",'r') as log:
    for line in log:
        masked = re.sub(r'\d+\.\d+\.\d+\.\d+','***.***.***.***', line)
        print(masked)


# ----- Q2: 统计 ERROR 数量 -----
# 用 findall 或 grep -c 的思路，在 Python 里统计
# 结合昨天的条件判断

# with open("app.log",'r') as Count:
#     C = 0
#     for counts in Count:
#         if "ERROR" in counts:
#             C+= 1
#     print(C)



# with open("app.log",'r') as Count:
#     content = Count.read()
#     total = re.findall(r"ERROR" , content)
# print(f"ERROR count:{len(total)}")


# ----- Q3: 用 re.match 判断行首 -----
# 只处理以 "ERROR" 开头的行，提取后面的内容
with open("app.log",'r') as f:
    for content in f:
        if re.search(r"ERROR" , content):
            parts = content.strip().split()
            date = parts[0]
            print(f"{parts[0]} → {' '.join(parts[2:])}")
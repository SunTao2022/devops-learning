def status_check(status):
    if status == "running":
        return("✅")
    elif status == "stopped":
        return("❌")
    else:
        return("❓")
print(status_check("running"))
print(status_check("stopped"))
print(status_check("unknow"))










# 加到 day5_practice.py 末尾

# ----- Q2: 打印编号的 IP 列表 -----
ips = ["10.0.0.1", "10.0.0.2", "10.0.0.3", "10.0.0.4"]

# 用 for + enumerate 输出：
# [1] 10.0.0.1
# [2] 10.0.0.2
# [3] 10.0.0.3
# [4] 10.0.0.4
No = 0
for ip in ips:
    No = No+1
    print(f"[{No}] {ip}")


for i,ip in enumerate(ips,start=1):
    print(f"[{i}] {ip}")





# 加到 day5_practice.py 末尾

# ----- Q3: 读取 servers.txt，只打印 stopped 的服务器 -----
with open("servers.txt", "r") as f:
    for line in f:
        # 你的代码：
        parts=line.strip().split(",")
        if parts[1] =="stopped":
            print(parts[0])
        # 1. strip() 去掉换行
        # 2. split(",") 拆成 [名字, 状态]
        # 3. 判断如果状态是 "stopped"，打印名字
        


# ----- Q4: 正则提取 IP -----
import re

log_line = "2026-06-08 14:30:22 ERROR Connection timeout from 10.0.0.1"

# 用 re.search() 提取 IP 地址，打印出来
# 期待输出：10.0.0.1
ip = re.search(r'\d+\.\d+\.\d+\.\d+' , log_line)
if ip:
    print(ip.group())


import re
log_line = '2026-06-08 ERROR from 10.0.0.1'

ip = re.search(r'\d+\.\d+\.\d+\.\d+', log_line)
print('Match 对象本身:', ip)
print('group() 拿出来:', ip.group())
print('start() 位置:', ip.start())
print('end() 位置:', ip.end())
print('匹配的原文片段:', log_line[ip.start():ip.end()])



# 加到文件末尾

# ----- Q5: 提取所有 IP -----
log_data = """
2026-06-08 14:30:22 ERROR Connection timeout from 10.0.0.1
2026-06-08 14:31:15 INFO  Request received from 192.168.1.100
2026-06-08 14:32:01 ERROR Disk full on 10.0.0.2
2026-06-08 14:33:44 WARN  Memory high on 172.16.0.50
"""


import re
ips = re.findall(r'\d+\.\d+\.\d+\.\d+',log_data)
print(ips)

# 用 re.findall() 提取所有 IP，打印出来
# 期待输出：['10.0.0.1', '192.168.1.100', '10.0.0.2', '172.16.0.50']
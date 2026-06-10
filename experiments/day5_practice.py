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
        

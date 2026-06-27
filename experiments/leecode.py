servers = ["web-01", "db-01", "web-01", "cache-01", "db-01", "web-01"]


count = {}

for server in servers:
    count[server] = count.get(server , 0) +1

print(count)





import subprocess

data = subprocess.run(["df" , "-h"] , capture_output=True , text=True)

lines = data.stdout.strip().split("\n")
usage = 0
for line in lines:
    parts = line.strip().split()
    pct_str = parts[4]
    if pct_str == "Use%":
        continue
    pct = float(pct_str.strip("%"))
    if pct > usage:
        usage = pct
        name = parts[0]
print(f"The disk with the highest usage rate is:{name} : {usage}")





all_servers = ["10.0.0.1", "10.0.0.2", "10.0.0.3", "10.0.0.4"]
online = ["10.0.0.1", "10.0.0.3"]

for ip in all_servers:
    if ip in online:
        continue
    else:
        print(ip)


offline = set(all_servers) - set(online)
for ip in offline:
    print(ip)


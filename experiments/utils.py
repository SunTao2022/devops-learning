def get_disk_usage():
    # """返回 C 盘使用率（数字，如 90）"""
    import subprocess
    result = subprocess.run(["df","-h","/c"],capture_output=True,text=True)
    usage = result.stdout.split("\n")[1].split()[4]
    return(usage[0:2])


def check_status(status):
# """把状态转成 emoji""
    if status == "running":
        return("✅")
    elif status == "stopped":
        return("❌")
    else:
        return("❓")
    

def count_error(log_file):
#  """统计日志文件里 ERROR 的行数"""
    with open(log_file,'r') as f:
        ERROR_NUMBER = 0
        for line in f:
            if "ERROR" in line:
                ERROR_NUMBER = ERROR_NUMBER + 1
    return(ERROR_NUMBER)

def filter_servers(status):
    server_list = []
    with open("servers.txt" , 'r') as f :
        for line in f:
            if status in line:
                server_list.append(line.split(",")[0])
    return(server_list)

# import subprocess
# result = subprocess.run(["df","-h","/c"],capture_output=True,text=True)
# print(f'Result:{result.stdout.strip().split()}')
# result_log = result.stdout.split('\n')[1].split()[4]
# print(result_log)
# with open("log_test.txt",'w') as f:
#     f.write(f"{result_log}")

# with open("log_test.txt",'r') as f:
#     print(f.read())





# 用 subprocess.run() 跑 grep -c "ERROR" app.log，用一行 Python 代码打印出 ERROR 的数量。做完贴输出。

# result = subprocess.run(["grep" ,"-c" , "ERROR" , "app.log"] , capture_output=True , text = True)
# print(result.stdout)





# 用 subprocess.run() 跑一条命令：统计 app.log 里 "ERROR" 出现了多少次（用 grep -c），然后判断如果 ERROR 数量大于 0，打印 "Alert: found X errors"，否则打印 "All clear"。

# 提示：result.stdout.strip() 拿到的是字符串，需要用 int() 转成数字才能比较大小。

# 写出来跑一下。


# import subprocess
# result = subprocess.run(["grep" , "-c" , "ERROR" , "app.log"] , capture_output=True , text=True)
# Count = int(result.stdout)
# if Count > 0:
#     print(f'find {Count} errors')
# else:
#     print("All clear")



# 写一个脚本，用 subprocess.run() 跑 df -h /c，提取 Use% 的值（比如 90%），去掉 % 符号转成整数。如果使用率大于 80%，打印 "Warning: disk usage is 90%"，否则打印 "Disk usage is OK: 90%"。

# 写好跑一下。

import subprocess
result = subprocess.run(["df", "-h" , "/c"] , capture_output=True , text=True)
number = result.stdout.split("\n")[1].split()[4][0:2]
if int(number) > 80:
    print(f"Warning:disk usage is {number}%")
else:
    print("Disk usage is OK")


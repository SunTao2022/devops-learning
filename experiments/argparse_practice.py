# import argparse
# parser = argparse.ArgumentParser(description="servers status checking tools")
# parser.add_argument("server" , help = "server name tobe checked")
# parser.add_argument("--port" , type=int , help="port number" , default=80)

# args = parser.parse_args()

# print(f'server:{args.server}')
# print(f'port_number:{args.port}')




# import sys
# found = False
# with open("servers.txt","r") as f:
#     for line in f:
#         parts = line.strip().split(",")
#         if parts[1] == sys.argv[1]:
#             print(f'server name is :{parts[0]}')
#             found = True
# if found == False:
#     print("No servers in stopped state")








# find_servers_argparse.py
# import argparse

# parser = argparse.ArgumentParser(description="servers list filter tools")
# parser.add_argument("status" , help = "filtering servers by status(running/stopped)")
# parser.add_argument("--file" , type=open)
# parser.add_argument("--verbose" , action="store_true")
# parser.add_argument("--quiet" , action="store_true" , help="quite mode")
# args = parser.parse_args()

# found = False
# with args.file:
#     for line in args.file:
#         if args.verbose:
#             print(f'[INFO] checking : {line.strip().split(",")[0]}, status:{line.strip().split(",")[1]}')
#         if args.status == line.strip().split(",")[1]:
#             print(line.strip().split(",")[0]) 
#             found = True
#     if args.verbose:
#          print("search finished")
#     if not found and not args.quiet:
#             print("no match")



# 1. 创建 ArgumentParser，description="按状态过滤服务器列表"
# 2. 加一个位置参数 "status"，help="服务器状态 (running/stopped)"
# 3. 加一个可选参数 --file，默认 "servers.txt"
# 4. 加一个开关 --quiet，action="store_true"
# 5. 解析参数
# 6. 打开 args.file，过滤状态，打印名字
# 7. 如果没找到，要么打印 "No servers found"（不安静模式）
#    要么安静退出（--quiet 模式）











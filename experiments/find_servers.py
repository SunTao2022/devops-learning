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




import subprocess
result = subprocess.run(['grep','INFO','app.log'], capture_output=True, text=True)
print('output:', result.stdout.strip())
print('line_count' , len(result.stdout.strip().split(chr(10))))
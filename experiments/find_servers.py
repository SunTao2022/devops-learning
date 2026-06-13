import sys
found = False
with open("servers.txt","r") as f:
    for line in f:
        parts = line.strip().split(",")
        if parts[1] == sys.argv[1]:
            print(f'server name is :{parts[0]}')
            found = True
if found == False:
    print("No servers in stopped state")

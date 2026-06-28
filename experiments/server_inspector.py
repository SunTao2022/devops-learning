import argparse
import subprocess
from tabulate import tabulate
import os
import sys
import platform
from datetime import datetime

parser = argparse.ArgumentParser(description= "server inspector")

parser.add_argument("--disk" , action="store_true" , help="check disk only")
parser.add_argument("--output" , help="exporting report")
parser.add_argument("--verbose" , action="store_true" , help="verbose enable")

args = parser.parse_args()


if args.verbose:
    print("caculating disk C:// usage....")
disk_check = subprocess.run(["df" , "-h" , "/c"] , capture_output=True , text=True)
usage = disk_check.stdout.split("\n")[1].split()[4]

try:
    args.disk
    if args.disk:
        print(f"disk C usage: {usage}")
        sys.exit()
    else:
        print(f"disk C usage: {usage}")
except ValueError:
     sys(1)


if args.verbose:
    print("checking hostname....")
host_name = platform.uname().node
print(f"host name:{host_name}")


if args.verbose:
    print("checking system info....")
system_info = platform.uname().system
print(f"platform:{system_info}")


if args.verbose:
    print("checking cuo count....")
cpu_count = os.cpu_count()
print(f"cpu_count:{cpu_count}")


if args.verbose:
    print("checking time of now....")
time = datetime.now()
print(f"time:{time}")

data = [["disk usage", usage],["host_name", host_name],["system_info", system_info],["cpu_count", str(cpu_count)],["time", str(time)],]
table = tabulate( data, headers=["item" , "value"] , tablefmt="grid")
print(table)
if args.output:
    if args.verbose:
        print("exporting report")
    with open("server_inspector_report.txt" , "w") as f:
        f.write(table)
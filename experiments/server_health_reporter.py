import argparse , subprocess
from tabulate import tabulate

parser = argparse.ArgumentParser(description="server health repoter tool")
parser.add_argument("--format" , help="format markdown")
parser.add_argument("--output" , help="exporting")
parser.add_argument("--verbose" , action="store_true" , help="verbose enable")
args = parser.parse_args()


result = {}

result_disk = subprocess.run(["df" , "-h" , "/"] , capture_output=True , text= True)
disk = result_disk.stdout.strip().split("\n")[1].split()[4]
result["disk"] = disk

result_mem = subprocess.run(["free" , "-m"] , capture_output=True , text= True)
mem = f"{(1-int(result_mem.stdout.strip().split("\n")[1].split()[6])/int(result_mem.stdout.strip().split("\n")[1].split()[1]))*100:.1f}%"
result["mem"] = mem

result_uptime = subprocess.run(["uptime"] , capture_output=True , text= True)
uptime = f"{result_uptime.stdout.strip().split()[2]} min"
result["uptime"] = uptime

result_userlogin = subprocess.run(["who" , "-q"] , capture_output=True , text= True)
userlogin = result_userlogin.stdout.strip().split()[2].split("=")[1]
result["userlogin"] = userlogin


if args.verbose:
    print("exporting result")

if args.format == "markdown":
    table = tabulate(result.items() , headers=["item" , "value"] , tablefmt="pipe")
else:
    table = tabulate(result.items() , headers=["item" , "value"] , tablefmt="grid")


if args.output:
    with open(args.output , "w") as f :
        if args.verbose:
            print("exporting report")  
        f.write(table)
 
# mem = result_disk.stdout.strip().split("\n")[1].split()[5]
# result["disk"] = disk


# uptime            # 负载
# who -q            # 登录用户数
# python server_health_reporter.py --format markdown --output report.md --verbose



print(table)


import argparse,re
from tabulate import tabulate

parser = argparse.ArgumentParser(description="log parser tool")
parser.add_argument("file" , help="lof tobe parser")
parser.add_argument("--output" , help="exporting report")
parser.add_argument("--verbose" , action="store_true" , help="verbose enable")
argus = parser.parse_args()

try:
    ips_account = {}
    with open(argus.file , "r") as f:
        for line in f :
            ip = re.findall(r"\d+\.\d+\.\d+\.\d+" , line)
            for found_ip in ip :
                ips_account[found_ip] = ips_account.get(found_ip , 0 ) + 1
    table = tabulate(ips_account.items() , ["ip" , "total"] , tablefmt="grid")
    print(table)

except FileNotFoundError:
    print("FileNotFoundError")


import argparse
import subprocess
from tabulate import tabulate

parser = argparse.ArgumentParser(description="Log Statistics Reporter")
parser.add_argument( "file" , help="path of log")
parser.add_argument("--sort" , help="name|count")
parser.add_argument("--verbose" , action="store_true" , help="verbose enable")
parser.add_argument("--output" , help="exporting")
parser.add_argument("--count" , action="store_true"  , help="counting")

args = parser.parse_args()

counts = {}
try:
    with open(args.file , "r") as f:
        for line in f :
            parts = line.strip().split()
            level = parts[1]
            counts[level] = counts.get(level , 0) + 1
    if args.sort == "name":
        sorted_date = sorted(counts.items() , key=lambda x:x[0])
    else:
        sorted_date = sorted(counts.items() , key=lambda x:x[1] , reverse=True)
    table = tabulate(sorted_date , ["level" , "Count"])
    if args.verbose:
        print("ganerating result.....")
    if args.output:
        result = subprocess.run([""])
        with open(args.output , "w") as f:
            if args.verbose:
                print("ganerating report.....")
            f.write(table)
    if args.count:
        result=subprocess.run(["wc" , "-l" , args.file] , capture_output=True , text=True)
        print(result.stdout.split()[0])
except FileNotFoundError:
    print("FileNotFoundError")

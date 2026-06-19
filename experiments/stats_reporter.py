import argparse
import subprocess
from tabulate import tabulate

parser = argparse.ArgumentParser(description="Log Statistics Reporter")
parser.add_argument("file", help="path of log")
parser.add_argument("--sort", help="name|count")
parser.add_argument("--verbose", action="store_true", help="verbose enable")
parser.add_argument("--output", help="exporting")

args = parser.parse_args()

counts = {}
try:
    with open(args.file, "r") as f:
        for line in f:
            parts = line.strip().split()
            level = parts[1]
            counts[level] = counts.get(level, 0) + 1
    if args.sort == "name":
        sorted_data = sorted(counts.items(), key=lambda x: x[0])
    else:
        sorted_data = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    table = tabulate(sorted_data, ["level", "Count"])
    if args.verbose:
        print("generating result.....")
    print(table)
    if args.output:
        with open(args.output, "w") as f:
            if args.verbose:
                print("generating report.....")
            f.write(table)
except FileNotFoundError:
    print("FileNotFoundError")

# import argparse
# from tabulate import tabulate
# import sys

# parser = argparse.ArgumentParser(description="log analyzer tool")

# parser.add_argument("file", help="log to be analysis")
# parser.add_argument("--level", help="events level")
# parser.add_argument("--output", help="output results")
# parser.add_argument("--verbose", action="store_true", help="verbose enable")

# args = parser.parse_args()

# if args.verbose:
#     print("start analysing")
# if args.file:
#     print("reading logs")
#     if args.verbose:
#         print("counting")

#     try:
#         with open(args.file , "r") as f:
#             counts = {}
#             for line in f:
#                 parts = line.strip().split()
#                 if len(parts) < 2:
#                     continue
#                 if args.level and parts[1] != args.level:
#                     continue
#                 level = args.level if args.level else parts[1]
#                 counts[level] = counts.get(level , 0) + 1
#             table = tabulate(counts.items(), headers = ["level" , "count"] , tablefmt = "grid")
#             print(table)
#     except FileNotFoundError:
#         print(f"Error: file '{args.file}' not found")
#         sys.exit(1)
#     if args.output:
#         if args.verbose:
#             print("Exporting")
#         with open("report.txt", "w") as f:
#             f.write(table + "\n")
#         if args.verbose:
#             print("Exported")












































import argparse
import sys
from tabulate import tabulate

parser = argparse.ArgumentParser(description="log analyzer tool")

parser.add_argument( "file" , help="log files to be analysis")
parser.add_argument("--level" , help="filter level")
parser.add_argument("--output" , help="export report")
parser.add_argument("verbose" , action="store_true" , help="verbose enable")

args = parser.parse_args()

try:
    with open(args.file , "r") as f:
        count = {}
        for line in f :
            parts = line.strip().split()
            if args.level and args.level != parts[1]:
                continue
            if len(parts) < 1 :
                continue
            if args.level:
                level = args.level
            else:
                level = parts[1]
            if level == parts[1]:
                count[level] = count.get(level , 0) + 1
    table = tabulate(count.items() , headers=["level" , "number"] , tablefmt="grid")
    print(table)

    if args.output:
        with open("report.txt", "w") as f:
            f.write(table)

except FileNotFoundError:
    print("FileNotFoundError")


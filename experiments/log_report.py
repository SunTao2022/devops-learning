import argparse,subprocess
from tabulate import tabulate

parser = argparse.ArgumentParser(description="log report tool")
parser.add_argument("file" , help="log tobe check")
parser.add_argument("--format" , help="markdown format")
parser.add_argument("--output" , help="exporting")
parser.add_argument("--verbose" , action="store_true" , help="verbose enable")
argus = parser.parse_args()

lines = subprocess.run(["wc" , "-l" , argus.file] , capture_output=True , text=True)
print(lines.stdout)

try:
    with open(argus.file , "r") as f:
        counts = {}
        for line in f:
            level = line.strip().split()[1]
            counts[level] = counts.get(level, 0) + 1 
    if argus.verbose:
        print("ganerateing table")
    table = tabulate(counts.items() , headers=["level" , "count"] , tablefmt="grid")
    print(table)
    
    if argus.format:
        table = tabulate(counts.items() , headers=["level" , "count"] , tablefmt="pipe")
        print(table)
    if argus.output:
        with open(argus.output , "w") as f:
            if argus.verbose:
                    print("exporting table")
            f.write(table)
except FileNotFoundError:
    print("FileNotFoundError")



            
import argparse
import subprocess
from tabulate import tabulate

parser = argparse.ArgumentParser(description="output review")
parser.add_argument("--cmd" , help="cmd to be used")
parser.add_argument("--output" , help="exporting")
parser.add_argument("--verbose" , action="store_true" , help="verbose enable")

argus = parser.parse_args()


result = subprocess.run(argus.cmd , shell= True , capture_output=True , text= True)
print(result.stdout)
lines = result.stdout.strip().split("\n")
data = [[line] for line in lines]
table = tabulate(data , headers=["velue"] , floatfmt="grid")
print(table)

if argus.output:
    try:
        with open(argus.output , "w") as f:
            f.write(table)
            
    except FileNotFoundError:
        print("FileNotFoundError")

    
            
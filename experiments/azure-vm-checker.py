import argparse, json , subprocess,sys
from tabulate import tabulate
parser = argparse.ArgumentParser(description= "azure vm checker")
parser.add_argument("--output" , help= "exproting report")
parser.add_argument("--verbose" , action="store_true" , help="verbose enable")
args = parser.parse_args()

result = subprocess.run("az vm list" , shell= True , capture_output=True , text=True)

if result.returncode !=0:
    print("please login first")
    sys.exit(1)

vms = json.loads(result.stdout)
if not vms:
    print("no vm found")
    table = "vm not found"
else:
    data = [[vm['name'], vm['location']] for vm in vms]
    table = tabulate(data , headers=["Name" , "loacation"])
    print(table)


if args.output:
    with open(args.output , "w") as f:
        f.write(table)
    if args.verbose:
        print("exporting successful")
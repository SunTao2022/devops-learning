import argparse , subprocess
from tabulate import tabulate
parser = argparse.ArgumentParser(description="VM batch")
parser.add_argument("file" , help="vm to be controled")
parser.add_argument("action" , help="vm action to be excressed")
parser.add_argument("group" , help="resource group")
parser.add_argument("--verbose" , action="store_true" , help="verbose enable")
parser.add_argument("--output" , help="exporting status")
args = parser.parse_args()

try:
    with open(args.file , "r") as f:
        status = {}
        for line in f:
            server = line.strip()
            if args.verbose:
                print(f"Processing {server}...")
            result_action = subprocess.run(["az" , "vm" , args.action , "-n" , server , "-g" , args.group] , capture_output=True , text=True )
            if result_action.returncode == 0:
                result_status_text = subprocess.run(["az" , "vm" , "show" , "-n" , server , "-g" , args.group , "--query" , "powerState" , "-o" , "tsv"] , capture_output=True , text=True )
                result_status = result_status_text.stdout.strip()
                if result_status_text.returncode == 0:
                    print("get status successful")
                else:
                    print("get status error")
            else:
                print("action failed")
                result_status = "Action failed"
            status[server] = result_status
    table = tabulate(status.items() , headers=["name" , "status"] , tablefmt="grid")
    print(table)
    if args.output:
        with open(args.output, "w") as f:
            f.write(table + "\n")
except FileNotFoundError:
     print("FileNotFoundError")

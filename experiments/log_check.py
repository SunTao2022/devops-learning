import os , subprocess , argparse
from tabulate import tabulate
from datetime import datetime , timedelta
import tarfile

parser = argparse.ArgumentParser(description="log check tool")
parser.add_argument("--verbose" , action="store_true" , help="verbose enable")
parser.add_argument("--dir" , default="." , help="dir to be check")
parser.add_argument("--days" ,type=int ,  default=7 , help="days to be reseverd")
args = parser.parse_args()

files = os.listdir(args.dir)
logs = []
result = {}
for line in files:
    filename = line.strip()
    log_path = os.path.join(args.dir , filename)
    if filename.endswith(".log"):
        logs.append(line)
    elif filename.endswith(".tar.gz"):
        result[line] = "removed"
        os.remove(log_path)
for log in logs:
    log_path2 = os.path.join(args.dir , log)
    rtime = os.path.getmtime(log_path2)
    time = datetime.fromtimestamp(rtime)
    cutoff = datetime.now()-timedelta(days=args.days)
    if time < cutoff:
        result[log] = "tarfile"
        tar_name = log + ".tar.gz"
        with tarfile.open(tar_name , "w:gz") as tar:
            tar.add(log_path2)
        os.remove(log_path2)
    else:
        result[log] = "normal"
table = tabulate(result.items() , headers=["item" , "action"] , tablefmt="grid")
if args.verbose:
    print("ganerating table")
print(table)
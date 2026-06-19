# import subprocess
# from tabulate import tabulate
# import argparse
# import os

# parser =argparse.ArgumentParser(description="git status check")

# parser.add_argument("--dir" , help="dedicated path")
# parser.add_argument("--verbose" , action="store_true" , help="verbose enable")
# parser.add_argument("--output" , help="exporting report")

# argus = parser.parse_args()

# search_dirs = argus.dir if argus.dir else [os.path.expanduser("~")]
# repos = []

# for search_dir in search_dirs:
#     for root, dirs, files in os.walk(search_dir):
#         if ".git" in dirs:
#             repos.append(root)
#             dirs.remove(".git")
# if argus.verbose:
#     print(f"found {len(repos)} repos")


# results = []
# for repo in repos:
#     result = subprocess.run(["git" , "status" , "--porcelain"] , capture_output= True , text= True , cwd=repo)
#     dirty = result.stdout.strip()
#     results.append((repo , dirty))

#     status = "⚠️" if dirty else "✅"
#     print(f"{status}{repo}")
#     if argus.verbose and dirty:
#         for line in dirty.split("\n"):
#             print(f"       {line}")

# clean = sum(1 for _, d in results if not d)
# total = len(results)
# print(f"\n总计: {total} 个仓库, {clean} 个干净, {total-clean} 个有改动")



 














































import os
import subprocess
import argparse
from tabulate import tabulate

parser = argparse.ArgumentParser(description="git status check tool")

parser.add_argument("--verbose" , action="store_true" , help="verbose enable")
parser.add_argument("--dir" , help= "dir to be check")
parser.add_argument("--output" , help="exporting report")
argus = parser.parse_args()


path = argus.dir if argus.dir else os.path.expanduser("~")
paths = []
for root , dirs , files in os.walk(path):
    if ".git" in dirs:
        paths.append(root)
        dirs.remove(".git")
if argus.verbose:
    print(f"we have {len(paths)} repos")


y = 0
n = 0
report = []
report.append(f"we have {len(paths)} repos")
for repo in paths:
    result = subprocess.run(["git" , "status" , "--porcelain"] , capture_output=True , text= True ,cwd= repo)
    
    if result.stdout:
        print(f"{repo} ⚠️")
        report.append(f"{repo} ⚠️")
        n+=1
    else:
        print(f"{repo} ✅")
        report.append(f"{repo} ✅")
        y+=1
print(f"checked {len(paths)} in total , clear is {y} , dirty is {n}")
report.append(f"checked {len(paths)} in total , clear is {y} , dirty is {n}")


output = "\n".join(report)
if argus.output:
    with open(argus.output , "w" , encoding="utf-8") as f:
        f.write(output)








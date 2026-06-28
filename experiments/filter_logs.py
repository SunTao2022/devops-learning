import argparse
from tabulate import tabulate

parser = argparse.ArgumentParser(description="log filter tool")
parser.add_argument("file" , help="log to be filter")
parser.add_argument("--level" , help="event to be filter")
parser.add_argument("--since" , help="statr data of filter")
parser.add_argument("--output" , help="exprting report")
parser.add_argument("--verbose" , action="store_true" , help="verbose enable")
argus = parser.parse_args()

try:
    with open(argus.file , "r") as f:
        result = []
        for line in f:
            event = line.strip().split()[1]
            data = line.strip().split()[0]
            if argus.level:
                if argus.level == event:
                    if argus.since:
                        if argus.since <= data:
                            result.append(line)
                    else:
                        if argus.verbose:
                            print("without filter data")
                        result.append(line)
            else:
                if argus.verbose:
                            print("without filter level")
                result.append(line)
        
        datas=[]
        for data in result:
             datas.append([data])
        table =tabulate(datas , headers=["table of filted data",""], tablefmt="grid")
        print(table)
except FileNotFoundError:
    print("FileNotFoundError")
if argus.output:
     with open(argus.output , "w") as f:
          f.write(table)
          

        

                




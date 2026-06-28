import argparse
import sys

parser = argparse.ArgumentParser(description= "config check tool")
parser.add_argument("--file" , help="file to be check")
parser.add_argument("--key" , help= "To be checked key")
parser.add_argument("--verbose" , action="store_true" , help="verbose enable")

argus = parser.parse_args()

try:
    with open(argus.file , "r") as f:
        n=0
        for line in f :
            if argus.key == line.strip().split(" = ")[0]:
                print(f'output : {line}')
                n+=1
        if n == 0 :
            print("no match key")
except FileNotFoundError:
    print("file not found")       
                
            



import argparse
parser = argparse.ArgumentParser(description="port check tool")
parser.add_argument("host" , help= "port to be checked")
parser.add_argument("--port" , type=int , help= "port number" , default=80)
parser.add_argument("--verbose" , action = "store_true" )

argus = parser.parse_args()

if argus.verbose:
    print(f"[info] resolving : {argus.host}")
    print(f"[info] connecting to : {argus.host}")
print(f"host : {argus.host} , port_number : {argus.port}")
if argus.verbose:
    print(f"[info] checked")

import sys

print("你传的所有参数:", sys.argv)
print("参数个数:", len(sys.argv))
print("脚本名:", sys.argv[0])

if len(sys.argv) > 1:
    print("第一个参数:", sys.argv[1])
if len(sys.argv) > 2:
    print("第二个参数:", sys.argv[2])
if len(sys.argv) > 3:
    print("第三个参数:", sys.argv[3])

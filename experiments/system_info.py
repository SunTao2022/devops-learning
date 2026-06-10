import platform
import os
import subprocess
import shutil


def get_system_info():
    uname = platform.uname()
    node = uname.node
    system = uname.system
    version = uname.version
    machine = uname.machine
    python = platform.python_version()
    cpu_count = os.cpu_count()
    process = subprocess.run("wmic OS get TotalVisibleMemorySize,FreePhysicalMemory", capture_output=True, text=True, shell=True)
    usage = shutil.disk_usage("C:/")

    with open("System_info.txt","w") as f:
        f.write("system_info\n")
        f.write(f"Node:{node}\n")
        f.write(f"System:{system}\n")
        f.write(f"Version:{version}\n")
        f.write(f"Machine:{machine}\n")
        f.write(f"python_version:{python}\n")
        f.write(f"usage_total:{usage.total/(1024**3)}\n")
        f.write(f"usage_used:{usage.used/(1024**3)}\n")
        f.write(f"usage_free:{usage.free/(1024**3)}\n")
        parts = process.stdout.strip().split()
        f.write(f"subprocess_Total:{int(parts[2])/1024**2}\n")
        f.write(f"subprocess_Free:{int(parts[3])/1024**2}\n")
        f.write(f"CPU_COUNT:{cpu_count}\n")

        print("Saved to System_info.txt ")
        print(process)
get_system_info()
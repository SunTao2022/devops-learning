"""
Day 4 — File I/O + Exception Handling
Run: python experiments/day4_practice.py
"""
from pathlib import Path

# Make all file paths relative to this script's directory
HERE = Path(__file__).parent


# ----- Q1: Write to file -----
# Write a list of servers to a file, one per line
servers = ["web-01", "web-02", "db-01", "cache-01"]
# Your code: open "servers.txt" in write mode,
# write each server on its own line

with open(HERE / "servers.txt", "w") as f:
    for svr in servers:
        f.write(svr + "\n")
print("Q1: servers.txt created")


# ----- Q2: Read and count lines -----
# Read "servers.txt" and count how many lines it has
# Your code here:
with open(HERE / "servers.txt", "r") as r:
    b=0
    for a in r:
        b+=1
    print(f"{b}")



# ----- Q3: Parse log file (read + split) -----
# The file "app.log" has lines like:
# 2026-06-08 INFO  Server started
# 2026-06-08 ERROR DB connection failed
# 2026-06-08 INFO  Request received
# 2026-06-08 ERROR Timeout exceeded
# Read it and print only the ERROR lines
# First create the log file, then parse it
log_lines = [
    "2026-06-08 INFO  Server started",
    "2026-06-08 ERROR DB connection failed",
    "2026-06-08 INFO  Request received",
    "2026-06-08 ERROR Timeout exceeded",
]
with open(HERE / "log.txt" , "w") as w:
    for log in log_lines:
        w.write(log + "\n")
# Now read and filter ERROR lines
with open(HERE / "log.txt" , "r") as r:
    for log in r:
        if "ERROR" in log:
            print(f"{log}")


# ----- Q4: Exception handling -----
# Write a function 'safe_divide' that takes two numbers
# If b is 0, catch the error and return "Cannot divide by zero"
# Otherwise return the result
def safe_divide(a, b):
    try:
        return(a/b)
    except ZeroDivisionError:
        return "Cannot divide by zero"  # replace with your code

print("Q4:", safe_divide(10, 2))   # Expected: 5.0
print("Q4:", safe_divide(10, 0))   # Expected: Cannot divide by zero


# ----- Q5: Read file safely -----
# Write a function 'read_file_safe' that takes a filename
# If file exists, read and return its content
# If not found, return "File not found"
# Use try/except
def read_file_safe(filename):
    try:
        with open (filename ,"r") as r:
            return r.read() # replace with your code
    except FileNotFoundError:
        return("File not found")


print("Q5:", read_file_safe(HERE / "servers.txt"))
print("Q5:", read_file_safe("nonexistent.txt"))

"""
Day 4 — File I/O + Exception Handling
Run: python experiments/day4_practice.py
"""

# ----- Q1: Write to file -----
# Write a list of servers to a file, one per line
servers = ["web-01", "web-02", "db-01", "cache-01"]
# Your code: open "experiments/servers.txt" in write mode,
# write each server on its own line

with open("experiments/servers.txt", "w") as f:
    for svr in servers:
        f.write(svr + "\n")
print("Q1: servers.txt created")


# ----- Q2: Read and count lines -----
# Read "experiments/servers.txt" and count how many lines it has
# Your code here:





# ----- Q3: Parse log file (read + split) -----
# The file "experiments/app.log" has lines like:
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
with open("experiments/app.log", "w") as f:
    for line in log_lines:
        f.write(line + "\n")

# Now read and filter ERROR lines
# Your code here:
with open("experiments/app.log", "r") as r:
    for line in log_lines:
        if line[11:15] == "ERROR":
            print(f"Q3: {line.strip()}")


# ----- Q4: Exception handling -----
# Write a function 'safe_divide' that takes two numbers
# If b is 0, catch the error and return "Cannot divide by zero"
# Otherwise return the result
def safe_divide(a, b):
    pass  # replace with your code

print("Q4:", safe_divide(10, 2))   # Expected: 5.0
print("Q4:", safe_divide(10, 0))   # Expected: Cannot divide by zero


# ----- Q5: Read file safely -----
# Write a function 'read_file_safe' that takes a filename
# If file exists, read and return its content
# If not found, return "File not found"
# Use try/except
def read_file_safe(filename):
    pass  # replace with your code

print("Q5:", read_file_safe("experiments/servers.txt"))
print("Q5:", read_file_safe("nonexistent.txt"))

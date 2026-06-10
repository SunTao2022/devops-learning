"""
Day 3 — Functions + Linux/Git Review
Run: python experiments/day3_practice.py
"""

# ----- Q1: Basic function -----
# Write a function called 'square' that takes a number and returns its square
# Then call it with 5 and print the result
def square(n):
    return n*n  # replace with your code

print("Q1:", square(5))  # Expected: 25


# ----- Q2: Function with two params -----
# Write a function 'calc_total' that takes price and tax_rate (default 0.13)
# Returns price + price * tax_rate
# Then call it with 100 and print the result
def calc_total(price, tax_rate=0.13):
    return price + price * tax_rate  # replace with your code

print("Q2:", calc_total(100))      # Expected: 113.0
print("Q2:", calc_total(200, 0.15))  # Expected: 230.0


# ----- Q3: Function returning multiple values -----
# Write a function 'min_max' that takes a list and returns (min, max)
def min_max(numbers):
    max_number = max(numbers)
    min_number = min(numbers)
    return  min_number,max_number# replace with your code

result = min_max([3, 7, 1, 9, 4])
print(f"Q3: min={result[0]}, max={result[1]}")  # Expected: min=1, max=9


# ----- Q4: Function with a dict parameter -----
# Write a function 'print_server' that takes a server dict and prints its info
# Keys: name, ip, status
# If status is missing, default to "unknown"
def print_server(server):
    name = server.get("name")
    ip = server.get("ip")
    status = server.get("status", "unknown")  # replace with your code
    print(f"[{name}] {ip} — {status}")

svr1 = {"name": "web-01", "ip": "10.0.0.1", "status": "running"}
svr2 = {"name": "db-01", "ip": "10.0.0.2"}
print_server(svr1)
# Expected: [web-01] 10.0.0.1 — running
print_server(svr2)
# Expected: [db-01] 10.0.0.2 — unknown


# ----- Q5: Combine everything -----
# Given a list of servers (each is a dict), use a function to
# print only servers with status "running"
servers = [
    {"name": "web-01", "status": "running", "ip": "10.0.0.1"},
    {"name": "web-02", "status": "stopped", "ip": "10.0.0.2"},
    {"name": "db-01", "status": "running", "ip": "10.0.0.3"},
    {"name": "cache-01", "status": "running", "ip": "10.0.0.4"},
]

def list_running(servers):
    for Computer in servers:
        status = Computer.get("status")
        Name = Computer.get("name")
        ip = Computer.get("ip")
        if status == "running":
            print(f"  {Name} ({ip}) — {status}")

list_running(servers)
# Expected:
#   web-01 (10.0.0.1) — running
#   db-01 (10.0.0.3) — running
#   cache-01 (10.0.0.4) — running

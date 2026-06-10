"""
Day 2 — List, Tuple, Dict exercises
Run: python experiments/day2_practice.py
"""

# ----- Question 1: List manipulation -----
# Given this list, complete the tasks below:
numbers = [3, 7, 1, 9, 4, 7, 2, 7]

# a) Add 10 to the end
# b) Remove the first occurrence of 7
# c) Insert 99 at index 2
# d) Print the final list
# Your code here:
numbers.append(10)
print(numbers)
numbers.remove(7)
print(numbers)
numbers.insert(2,99)
print(numbers)






# ----- Question 2: List slicing -----
data = [10, 20, 30, 40, 50, 60, 70, 80]

# Use slicing to get:
# a) First 3 elements
# b) Last 3 elements
# c) Every 2nd element
# d) The list reversed
# Print each result
# Your code here:

print(data[0:3])
print(data[-3:])
print(data[::2])
print(data[::-1])


# ----- Question 3: Tuple unpacking -----
# Given this tuple, unpack values into variables and print them
student = ("Tao", "DevOps", 2026)
# Your code here:
name,role,year = student
print(f"my name is {name}, A {role} at {year}")





# ----- Question 4: Dictionary operations -----
# Create a dictionary "server" with keys: name, ip, status, cpu_usage
# Then:
# a) Print the IP
# b) Change status to "running"
# c) Add a new key "memory_usage" with value 67.5
# d) Print all key-value pairs with f-string
# Your code here:
server = {"name":"A","ip":"1.1.1.1","status":"running","cpu_usage":"20%"}
print(server["ip"])
server["status"] = "running"
print(server["status"])
server["memory"] = "80%"
for k, v in server.items():
    print(f"{k}:{v}")


# ----- Question 5: Combine list + dict -----
# Given a list of students (each is a dict), 
# print each student's name and score


# Expected output:
#   Alice scored 85
#   Bob scored 92
#   Charlie scored 78
# Your code here:
students = [{"name":"Alice","Score":"85"},{"name":"Bob","Score":"92"},{"name":"charlie","Score":"78"}]

for a in students:
    print(f"{a['name']} scored {a['Score']}")
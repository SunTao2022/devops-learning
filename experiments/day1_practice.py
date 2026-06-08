"""
Day 1 — Python 基础练习
做完后 python day1_practice.py 运行验证
"""

# 第1题：创建 3 个变量（姓名、年龄、城市），
# 用 f-string 打印 "我叫XX，今年XX岁，住在XX"
# ↓ 你的代码写在这里 ↓
name = "Tao"
age = 30
city = "Toronto"
print(f"my name is {name}, I am {age} years old, and I live in {city}. ")


# 第2题：交换 a 和 b 的值（不能用 a,b=b,a 这种简写，用临时变量）
a = 5
b = 10
# ↓ 你的代码写在这里 ↓
temp = a 
a = b 
b = temp 
print(f"a={a}, b={b}")



# 第3题：字符串操作——把 " hello world " 两边的空格去掉，
# 然后全部转大写，最后替换 "WORLD" 为 "DEVOPS"
text = " hello world "
# ↓ 你的代码写在这里 ↓
result = text.strip().upper().replace("WORLD", "DEVOPS")
print(result)



# 第4题：计算一个圆的面积（半径 r=7，π=3.14159）
# 输出格式："半径为7的圆，面积是XXX"
r = 7
pi = 3.14159
# ↓ 你的代码写在这里 ↓
y = pi * r * r 
print(f"circle with r={r}, area={y}")



# 第5题：接收一个字符串，输出它的长度、第一个字符、最后一个字符、前3个字符
# （提示：不能用 input，直接把字符串赋值给变量即可）
my_str = "DevOps"
# ↓ 你的代码写在这里 ↓
print(f"length: {len(my_str)}")
print(f"first: {my_str[0]}")
print(f"last: {my_str[-1]}")
print(f"first 3: {my_str[:3]}")



"""
Personal System Intro — Day 1 Mini Project
"""
name = "Tao"
role = "DevOps Engineer"
years_exp = 5
city = "Toronto"

# 1. 用 f-string 打印一句话介绍
# 2. 把 role 转大写并打印
# 3. 打印 city 的前 3 个字符
# 4. 用 * 画一条分隔线（例如 "=" * 30）

print(f"I am {name},A {role} and i have {years_exp}years exprincene,I live in {city}")
print(role.upper())
print(city[:3])
print("*"*30)


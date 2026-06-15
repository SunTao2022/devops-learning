# DevOps 学习笔记 — 完整版

> 学习者：Tao  
> 目标：加拿大 DevOps/SRE 岗位  
> 开始日期：2026-06-08  
> 本笔记包含所有已学知识点、代码示例和实验记录

---

## 目录

1. [Python 基础](#1-python-基础)
2. [Python 函数](#2-python-函数)
3. [条件判断与循环](#3-条件判断与循环)
4. [文件 I/O 与异常处理](#4-文件-io-与异常处理)
5. [正则表达式](#5-正则表达式)
6. [sys 与 os 模块](#6-sys-与-os-模块)
7. [subprocess 模块](#7-subprocess-模块)
8. [模块与包](#8-模块与包)
9. [Linux 基础命令](#9-linux-基础命令)
10. [文本处理与 grep](#10-文本处理与-grep)
11. [管道与组合命令](#11-管道与组合命令)
12. [find / df / du](#12-find--df--du)
13. [进程管理](#13-进程管理)
14. [Git 基础](#14-git-基础)
15. [Git 分支与合并](#15-git-分支与合并)
16. [Git 进阶](#16-git-进阶)
17. [实验索引](#17-实验索引)

---

## 1. Python 基础

### 变量与数据类型

```python
name = "web-01"          # 字符串
cpu = 4                  # 整数
memory = 7.8             # 浮点数
is_running = True        # 布尔值
servers = ["web", "db"]  # 列表
```

### 字符串操作

```python
name = "  web-01  "
name.strip()       # 去空格 → "web-01"
name.upper()       # 大写 → "  WEB-01  "
name.lower()       # 小写
name.replace("web", "db")  # 替换 → "  db-01  "
```

### f-string（格式化字符串）

```python
server = "web-01"
status = "running"
print(f"{server} is {status}")  # web-01 is running
print(f"CPU: {cpu}核, 内存: {memory}GB")
```

**f-string 里可以做运算：**
```python
total = 1024
used = 768
print(f"使用率: {used/total*100:.1f}%")  # 75.0%
```

### 列表（List）

```python
ips = ["10.0.0.1", "10.0.0.2", "10.0.0.3"]
ips[0]       # "10.0.0.1"（索引从0开始）
ips[-1]      # "10.0.0.3"（倒数第一个）
ips.append("10.0.0.4")  # 追加
len(ips)     # 列表长度 → 4
"10.0.0.1" in ips  # True（判断是否存在）
```

### 字典（Dict）

```python
server = {
    "name": "web-01",
    "ip": "10.0.0.1",
    "status": "running"
}

server["name"]         # "web-01"（取值）
server.get("status")    # "running"（安全取值）
server.get("cpu", "N/A")  # "N/A"（不存在时返回默认值）
```

**列表套字典（常见数据格式）：**
```python
servers = [
    {"name": "web-01", "status": "running"},
    {"name": "db-01", "status": "stopped"}
]
servers[0]["name"]  # "web-01"
```

---

## 2. Python 函数

### 定义与调用

```python
def square(n):
    """返回数字的平方"""          # 文档字符串
    return n * n

print(square(5))  # 25
```

### 参数与返回值

```python
def check_server(name, status="unknown"):
    """status 有默认值，不传就用 unknown"""
    return f"{name} is {status}"

check_server("web-01", "running")  # "web-01 is running"
check_server("db-01")              # "db-01 is unknown"
```

### 返回多个值（元组）

```python
def min_max(numbers):
    return min(numbers), max(numbers)  # 返回元组 (min, max)

result = min_max([3, 7, 1, 9])
min_v, max_v = result  # 拆包：min_v=1, max_v=9
```

---

## 3. 条件判断与循环

### if / elif / else

```python
status = "running"

if status == "running":
    print("✅")
elif status == "stopped":
    print("❌")
else:
    print("❓")
```

**关键规则：**
- 条件后要冒号 `:`
- 条件体要缩进 4 空格
- `elif` 不能单独存在

**真值判断（False 的6种值）**
```python
# 以下 6 个值被视为 False
None
False
0
""          # 空字符串
[]          # 空列表
{}          # 空字典

# 使用方式
if server_name:     # 非空字符串 = True
if error_count:     # 非 0 = True
```

### for 循环

```python
servers = ["web-01", "db-01", "cache-01"]
for svr in servers:
    print(svr.upper())  # WEB-01  DB-01  CACHE-01

# range — 重复指定次数
for i in range(5):
    print(i)  # 0 1 2 3 4
```

### enumerate — 同时拿索引和值

```python
ips = ["10.0.0.1", "10.0.0.2", "10.0.0.3"]

for i, ip in enumerate(ips, start=1):
    print(f"[{i}] {ip}")
# [1] 10.0.0.1
# [2] 10.0.0.2
# [3] 10.0.0.3
```

**拆包原理：** `enumerate` 产生 `(序号, 值)` 元组，`i, ip` 按位置拆开。

### break / continue

```python
for svr in servers:
    if svr == "db-01":
        continue      # 跳过（不打印 db-01）
    if svr == "cache-01":
        break         # 终止循环
    print(svr)
```

---

## 4. 文件 I/O 与异常处理

### 读文件

```python
# 读整个文件
with open("servers.txt", "r") as f:
    content = f.read()
    print(content)

# 逐行读（推荐 — 大文件不占内存）
with open("servers.txt", "r") as f:
    for line in f:
        line = line.strip()           # 去掉 \n
        parts = line.split(",")       # 按逗号拆
        print(parts[0], parts[1])
```

### 写文件

```python
# 覆盖写
with open("output.txt", "w") as f:
    f.write("web-01,running\n")

# 追加写
with open("output.txt", "a") as f:
    f.write("db-01,stopped\n")
```

**文件模式：**

| 模式 | 作用 | 文件不存在 |
|------|------|-----------|
| `"r"` | 读 | 报错 |
| `"w"` | 覆盖写 | 创建 |
| `"a"` | 追加写 | 创建 |

### 异常处理

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("不能除以0")
finally:
    print("不管有没有异常，都会执行")

# 文件不存在的处理
try:
    with open("nonexist.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("文件没找到")
```

**原则：** 指定具体异常类型（`ZeroDivisionError`），不要裸 `except:`（会误抓 `Ctrl+C`）。

### 字符串 split / strip

```python
line = "web-01,running\n"
line.strip()              # "web-01,running"（去换行）
line.strip().split(",")   # ["web-01", "running"]
line.strip().split()      # ["web-01,running"]（按空格拆，找不到逗号就不拆）
```

**`split()` 和 `split(",")` 的区别：**

| 写法 | 拆什么 | 适用场景 |
|------|--------|---------|
| `split()` | 按**任意空白**拆 | 空格/Tab 分隔的文件 |
| `split(",")` | 按**逗号**拆 | CSV 文件 |
| `split("\n")` | 按**换行**拆 | 多行字符串转列表 |

---

## 5. 正则表达式

### re.search() — 找到第一个匹配

```python
import re

text = "Server 10.0.0.1 is running"
ip = re.search(r'\d+\.\d+\.\d+\.\d+', text)
if ip:
    print(ip.group())      # "10.0.0.1"
    print(ip.start())      # 匹配开始位置（数字）
    print(ip.end())        # 匹配结束位置
```

### re.findall() — 找到所有匹配

```python
log = """
2026-06-08 ERROR from 10.0.0.1
2026-06-08 INFO from 192.168.1.100
"""
ips = re.findall(r'\d+\.\d+\.\d+\.\d+', log)
print(ips)  # ['10.0.0.1', '192.168.1.100']
```

### re.sub() — 替换

```python
log = "Server 10.0.0.1 is DOWN"
masked = re.sub(r'\d+\.\d+\.\d+\.\d+', '***.***.***.***', log)
print(masked)  # Server ***.***.***.*** is DOWN
```

### re.match() — 从开头匹配

```python
line = "ERROR DB connection failed"

re.match(r"ERROR", line)    # ✅ 匹配（ERROR 在行首）
re.match(r"DB", line)       # ❌ 不匹配（DB 不在行首）
re.search(r"DB", line)      # ✅ search 全文搜索
```

**match vs search：**

| 方法 | 匹配范围 | 常用场景 |
|------|---------|---------|
| `re.match()` | 只从开头 | 判断行首关键词 |
| `re.search()` | 全文 | 找 IP、找特定模式 |
| `re.findall()` | 全部匹配 | 提取所有值 |

### 常用正则符号

| 符号 | 意思 | 示例 |
|------|------|------|
| `\d` | 数字 0-9 | `\d+` → 连续数字 |
| `\w` | 字母+数字+下划线 | `\w+` → 单词 |
| `\.` | 转义点号（真正的小数点） | `\d+\.\d+` → 10.0 |
| `+` | 一次或多次 | `\d+` |
| `*` | 零次或多次 | `\d*` |
| `^` | 行首 | `^ERROR` → 以 ERROR 开头 |
| `r'...'` | 原始字符串（反斜杠不会转义） | `r'\d'` 里的 `\d` 是正则 |

**IP 地址提取模式：**
```python
r'\d+\.\d+\.\d+\.\d+'
# 解释：数字.数字.数字.数字
```

---

## 6. sys 与 os 模块

### sys.argv — 命令行参数

```bash
python script.py web-01 --force
```

```python
import sys

print(sys.argv)       # ['script.py', 'web-01', '--force']
print(sys.argv[0])    # 脚本名
print(sys.argv[1])    # 第一个参数 "web-01"
print(len(sys.argv))  # 参数个数
```

**安全取值，先判断长度：**
```python
if len(sys.argv) < 2:
    print("Usage: python script.py <server_name>")
    sys.exit(1)          # 退出脚本（1=有错误）

target = sys.argv[1]
```

### sys.exit()

```python
sys.exit(0)    # 正常退出
sys.exit(1)    # 异常退出（可被检测到）
```

### os 模块

```python
import os

os.getcwd()                     # 当前工作目录（同 pwd）
os.listdir(".")                 # 列出目录内容（同 ls）
os.environ.get("HOME")          # 取环境变量
os.cpu_count()                  # CPU 核数
os.path.join("dir", "file.py")  # 拼路径（自动处理 \ 和 /）
```

**os.path.join 的作用：** 不同操作系统路径分隔符不同，`join` 自动适配。

```python
# Windows → "reports\\server_report.txt"
# Linux   → "reports/server_report.txt"
path = os.path.join("reports", "server_report.txt")
```

**组合 sys.argv + os.listdir：**
```python
import sys, os

mode = sys.argv[1]
py_files = [f for f in os.listdir(".") if f.endswith(".py")]

if mode == "--list":
    for f in py_files:
        print(f)
elif mode == "--count":
    print(f"Found {len(py_files)} Python files")
```

---

## 7. subprocess 模块

### 基本用法

```python
import subprocess

result = subprocess.run(
    ["ls", "-la"],           # 命令和参数（列表）
    capture_output=True,      # 截获输出
    text=True                 # 以文本返回
)

print(result.stdout)         # 命令输出
print(result.returncode)     # 返回码（0=成功）
```

### 从终端命令到 Python 列表

```
终端:    grep    -c     "ERROR"    app.log
         ↓        ↓        ↓         ↓
列表:  ["grep", "-c", "ERROR", "app.log"]
```

### 解析命令输出

```python
# 例子：提取 df -h 的使用率
result = subprocess.run(["df", "-h", "/c"], capture_output=True, text=True)
line = result.stdout.split("\n")[1]        # 取第2行
usage = line.split()[4].rstrip("%")        # 取 Use% 列并去掉 %
print(f"Disk usage: {usage}%")
```

### shell=True（用于管道和重定向）

```python
# 有管道时要用 shell=True
result = subprocess.run(
    "grep ERROR app.log | wc -l",
    shell=True,
    capture_output=True,
    text=True
)
print(result.stdout.strip())  # ERROR 行数
```

---

## 8. 模块与包

### 创建自己的模块

任何一个 `.py` 文件都可以被 `import`。

**utils.py：**
```python
def get_disk_usage():
    """返回 C 盘使用率"""
    import subprocess
    result = subprocess.run(["df", "-h", "/c"], capture_output=True, text=True)
    usage = result.stdout.split("\n")[1].split()[4]
    return usage.rstrip("%")

def check_status(status):
    if status == "running":
        return "✅"
    elif status == "stopped":
        return "❌"
    else:
        return "❓"

def count_errors(log_file):
    with open(log_file, "r") as f:
        count = 0
        for line in f:
            if "ERROR" in line:
                count += 1
    return count
```

**主脚本调用：**
```python
import utils

print(utils.get_disk_usage())        # 90
print(utils.check_status("running")) # ✅
print(utils.count_errors("app.log")) # 3
```

---

## 9. Linux 基础命令

### 文件和目录操作

```bash
pwd              # 当前目录在哪
ls -la           # 列出文件（含隐藏文件、详细信息）
cd 目录名         # 切换目录
cd ~             # 回 home
cd ..            # 上一级
mkdir -p a/b/c   # 创建多级目录
touch file.txt   # 创建空文件
rm file.txt      # 删除文件
rm -r dir/       # 删除目录
```

### 文件查看

```bash
cat file.txt      # 看全部
less file.txt     # 翻页查看（q 退出）
head -5 file.txt  # 看前5行
tail -5 file.txt  # 看后5行
wc -l file.txt    # 数行数
```

### 文件权限

```bash
chmod +x script.sh   # 给执行权限
file script.sh       # 查看文件类型
stat file.txt        # 查看文件详细信息
```

---

## 10. 文本处理与 grep

### grep 基本用法

```bash
grep "ERROR" app.log        # 搜包含 ERROR 的行
grep -c "ERROR" app.log     # 数几行（计数）
grep -n "ERROR" app.log     # 显示行号
grep -i "error" app.log     # 忽略大小写
grep -r "ERROR" dir/        # 递归搜目录
```

### grep 高级选项

```bash
grep -o "ERROR" app.log     # 只输出匹配的部分
grep -P '\d+' app.log       # 启用 Perl 正则
grep -oP '^\w+' app.log     # 提取行首单词
```

---

## 11. 管道与组合命令

### 管道 `|` — 左输出 → 右输入

```bash
ls | wc -l                  # 文件列表 → 数行数
cat app.log | grep ERROR    # 读文件 → 搜 ERROR
```

### 管道链经典模式：排序 → 去重计数 → 反序

```bash
grep -oP '^\w+' log.txt | sort | uniq -c | sort -rn
# ① 提取行首单词
# ② 排序（uniq 要求相邻）
# ③ 去重并计数
# ④ 按次数从大到小排
```

### 单步拆解

```bash
grep -oP '^\w+' log.txt          # 提取每行第一个词
    | sort                       # 排序，让相同词相邻
    | uniq -c                    # 去重 + 计数
    | sort -rn                   # 按数字从大到小排
```

**sort 选项：**

| 选项 | 意思 | 作用 |
|------|------|------|
| `-n` | numeric | 按数字大小排 |
| `-r` | reverse | 反序（大到小） |
| `-h` | human-readable | 识别 K/M/G 后缀 |

---

## 12. find / df / du

### find — 文件搜索

```bash
find . -name "*.py"             # 搜文件名
find . -type d                  # 只看目录
find . -size +10k               # 大于 10KB 的文件
find . -mtime -1                # 当天修改过的文件
find . -name "*.py" -mtime -7   # 组合条件
```

**-mtime 参数：**

| 参数 | 意思 |
|------|------|
| `-1` | 1天以内 |
| `+7` | 超过7天 |
| `0` | 今天 |

### df — 磁盘空间

```bash
df -h           # 所有磁盘（GB显示）
df -h /c        # 只看 C 盘
```

### du — 目录大小

```bash
du -sh 目录名     # 看单个目录大小
du -sh *         # 看每个项目大小
du -sh * | sort -rh | head -5  # 最大的5个
```

---

## 13. 进程管理

### ps — 查看进程

```bash
ps aux                  # 所有进程
ps aux | grep python    # 找 Python 进程
ps aux --sort=-%cpu     # 按 CPU 排序（真 Linux）
ps aux --sort=-%mem     # 按内存排序
```

### kill — 终止进程

```bash
kill 1234           # 温和终止（SIGTERM）
kill -9 1234        # 强制杀掉（SIGKILL）
```

---

## 14. Git 基础

### 基本流程

```bash
git init                   # 初始化仓库
git add file.txt           # 暂存文件
git commit -m "描述"       # 提交
git status                 # 查看状态
git log --oneline          # 查看提交历史
git diff                   # 查看未暂存的改动
git show <commit>          # 查看某次提交详情
```

### git add 的不同用法

```bash
git add file.txt         # 暂存指定文件
git add .                # 暂存当前目录所有文件
git add -A               # 暂存所有改动
```

### remote 与 push

```bash
git remote -v                         # 查看远程仓库地址
git remote add origin https://...     # 添加远程仓库
git push origin master                # 推送到远程
git push                              # 默认推送到 origin/master
```

### commit --amend — 修改最后的 commit

```bash
# 场景：commit 后忘了加一个文件
git add 忘记的文件
git commit --amend -m "新的描述"
```

**注意：** `--amend` 从暂存区拿内容，不是从工作区。所以要先 `git add` 再 `--amend`。**只适用于未 push 的 commit。**

### .gitignore — 忽略不需要的文件

创建 `.gitignore` 文件，把要忽略的文件名写进去：

```
*.log
__pycache__/
.env
.vscode/
```

```bash
# 如果已经提交了 log 文件，想停止跟踪但保留本地：
git rm --cached app.log
echo "*.log" >> .gitignore
```

---

## 15. Git 分支与合并

### 分支工作流

```bash
# 创建并切换分支
git checkout -b new-feature
# 等同于：
git branch new-feature
git checkout new-feature

# 在新分支上提交
git add file.txt
git commit -m "描述"

# 切换回 master
git checkout master

# 合并分支
git merge new-feature

# 删除分支
git branch -d new-feature
```

### 用 switch 替代 checkout（更明确）

```bash
git switch -c new-feature    # 创建并切换
git switch master            # 切回 master
```

**Fast-forward 合并：** master 没有新 commit 时，直接移动指针，不产生 merge commit。

### 分叉合并（两边都有新 commit）

```
*   Merge branch 'feature'
|\
| * feature commit
* | master commit
|/
* common ancestor
```

查看图形：
```bash
git log --graph --oneline --all
```

---

## 16. Git 进阶

### fetch vs pull

```bash
git fetch origin       # 只下载远程内容，不改本地（安全）
git pull               # 下载 + 自动合并（等同于 fetch + merge）
```

| 场景 | 用哪个 |
|------|--------|
| 只想看看远程有无更新 | `git fetch` |
| 确定要同步远程 | `git pull` |

### origin/master 是什么

```
origin    /    master
  ↑              ↑
远程仓库名    远程的分支名
```

`origin/master` 是你的本地存的一份远程状态快照。

```bash
git log origin/master       # 看远程最新状态
git log master..origin/master   # 远程有但本地没有的 commit
```

---

## 17. 实验索引

| 文件名 | 涵盖内容 | 位置 |
|--------|---------|------|
| day1_practice.py | 变量、字符串、f-string | `month-1/week-1/` |
| day2_practice.py | 列表、元组、字典 | `month-1/week-1/` |
| day3_practice.py | 函数定义、参数、返回值 | `month-1/week-1/` |
| day4_practice.py | 文件 I/O、异常处理 | `month-1/week-1/` |
| day5_practice.py | if/elif/else、for/enumerate、re.search/findall | `experiments/` |
| day7_practice.py | re.sub、re.match、re.search | `experiments/` |
| day8_practice.py | sys.argv、os 模块 | `experiments/` |
| find_servers.py | sys.argv + 文件 I/O 综合 | `experiments/` |
| subprocess_pratice.py | subprocess.run()、命令解析 | `experiments/` |
| utils.py | 自定义模块（3个函数） | `experiments/` |
| day9_practice.py | import 模块测试 | `experiments/` |
| system_info.py | 综合项目：收集系统信息 | `projects/` |
| servers.txt | 练习数据文件（服务器列表） | `experiments/` |
| app.log | 练习数据文件（日志） | `experiments/` |

---

> **最后修改：2026-06-13**  
> 每次学完新内容后更新此文档

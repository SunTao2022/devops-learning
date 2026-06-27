# 习题集

> 所有练习题、答案、解析、以及练习中学到的知识点。
> 按内容分类：Python / Shell / 项目 / Azure

---

## 目录

1. [Python 练习](#1-python-练习)
   - 1.1 [for + enumerate + IP 列表](#11-for--enumerate--ip-列表)
   - 1.2 [服务器按状态过滤](#12-服务器按状态过滤)
   - 1.3 [subprocess 提取 Use%](#13-subprocess-提取-use)
   - 1.4 [subprocess + 条件判断](#14-subprocess--条件判断)
   - 1.5 [subprocess 综合（df + 写入文件）](#15-subprocess-综合df--写入文件)
   - 1.6 [无提示：提取 experiments 目录大小](#16-无提示提取-experiments-目录大小)
   - 1.7 [port_check.py argparse 综合](#17-port_checkpy-argparse-综合)
   - 1.8 [config_check.py — 配置文件解析](#18-config_checkpy--配置文件解析)
2. [Shell 练习](#2-shell-练习)
   - 2.1 [Shell 变量 + 参数 + df](#21-shell-变量--参数--df)
   - 2.2 [Shell 条件判断 emoji 转换](#22-shell-条件判断-emoji-转换)
   - 2.3 [for 循环遍历 servers.txt](#23-for-循环遍历-serverstxt)
   - 2.4 [函数 + 循环](#24-函数--循环)
   - 2.5 [并发 & + wait](#25-并发--wait)
   - 2.6 [set -e + trap](#26-set--e--trap)
   - 2.7 [find_large.sh — 找大文件](#27-find_largesh--找大文件)
3. [综合项目](#3-综合项目)
   - 3.1 [项目 1：日志分析器](#31-项目-1日志分析器)
   - 3.2 [项目 2：服务器巡检](#32-项目-2服务器巡检)
   - 3.3 [项目 3：Git 批量检查](#33-项目-3git-批量检查)
   - 3.4 [复习项目：日志统计仪](#34-复习项目日志统计仪)
   - 3.5 [系统健康检查脚本](#35-系统健康检查脚本)
   - 3.6 [azure-vm-checker.py](#36-azure-vm-checkerpy)

---

# 1. Python 练习

---

## 1.1 for + enumerate + IP 列表

### 题目

```python
ips = ["10.0.0.1", "10.0.0.2", "10.0.0.3", "10.0.0.4"]
# 用 for + enumerate 输出：
# [1] 10.0.0.1
# [2] 10.0.0.2
# [3] 10.0.0.3
# [4] 10.0.0.4
```

### 答案

```python
for i, ip in enumerate(ips, start=1):
    print(f"[{i}] {ip}")
```

### 解析

- `enumerate` 产生 `(序号, 元素值)` 的元组对
- `for i, ip in enumerate(...)` 是**元组拆包**——两个变量按位置接收元组的两个值
- `start=1` 让序号从 1 开始（默认从 0）

### Q&A（学习过程中的问题）

**Q：为什么 `i` 是序号，`ip` 是值？**
A：因为 `enumerate` 就是这么设计的：第一个位置放序号，第二个位置放原元素。拆包时 `i` 拿第 0 位，`ip` 拿第 1 位。

---

## 1.2 服务器按状态过滤

### 题目

读 `servers.txt`（格式 `name,status`），只打印状态为 "stopped" 的服务器名。

### 答案

```python
with open("servers.txt", "r") as f:
    for line in f:
        parts = line.strip().split(",")
        if parts[1] == "stopped":
            print(parts[0])
```

### 解析

- `line.strip()` → 去掉换行符
- `.split(",")` → 按逗号拆成列表
- `if parts[1] == "stopped"` → 条件过滤

### Q&A

**Q：`split(",")` 和 `split()` 区别？**
A：`split(",")` 按逗号分割；`split()` 按任意空白字符分割（空格、Tab、换行）。文件是逗号分隔就用 split(",")。

**Q：`line.split().strips(",")` 为什么报错？**
A：因为 `split()` 先执行返回列表（如 `["a", "b"]`），然后列表调 `.strips()` — 列表没有 `strips` 方法。正确顺序是：先 `.strip()`（字符串去换行）→ 再 `.split(",")`（拆成列表）。

---

## 1.3 subprocess 提取 Use%

### 题目

用 `subprocess.run()` 跑 `df -h /c`，从输出中提取 Use% 的值。

### 答案

```python
import subprocess

result = subprocess.run(["df", "-h", "/c"], capture_output=True, text=True)
use_pct = result.stdout.split("\n")[1].split()[4]  # "90%"
print(f"Use%: {use_pct}")
```

### 解析

`df -h /c` 输出：
```
Filesystem      Size  Used Avail Use% Mounted on
C:              298G  267G   31G  90% /c
```

- `split("\n")[1]` → 取第 2 行（数据行）：`"C: 298G ... 90% /c"`
- `.split()[4]` → 按空格拆分后第 5 列：`"90%"`

### Q&A

**Q：`result.stdout.strip().split()` 里的 `strip()` 有什么用？**
A：去掉输出开头和结尾的空白字符（包括最后的换行）。如果不 `.strip()` 直接 `.split("\n")`，末尾会多一个空字符串元素。

**Q：为什么 `result_log = print(xxx)` 不对？**
A：`print()` 返回 `None`，不是字符串。输出去了屏幕，变量啥也没得到。先 `result_log = result.stdout`，再 `print(result_log)`。

---

## 1.4 subprocess + 条件判断

### 题目

用 subprocess.run() 跑 `grep -c ERROR app.log`，然后判断如果 ERROR 数量大于 0，打印 "Alert!"，否则打印 "All clear"。

### 答案

```python
import subprocess

result = subprocess.run(["grep", "-c", "ERROR", "app.log"],
    capture_output=True, text=True)

count = int(result.stdout.strip())

if count > 0:
    print(f"Alert: {count} errors")
else:
    print("All clear")
```

### 解析

- `result.stdout` 是字符串 `"5\n"`，需要 `int(...)` 转成数字
- `.strip()` 去掉换行符

### Q&A

**Q：`["grep -c", "ERROR", "app.log"]` 为什么报 `FileNotFoundError`？**
A：`"grep -c"` 被当作一个完整的命令名，系统找的是名为 `grep -c` 的可执行文件。命令和参数必须分开：`["grep", "-c", "ERROR", "app.log"]`。

---

## 1.5 subprocess 综合（df + 写入文件）

### 题目

跑 `df -h /c`，提取 Use%，写入 `log.txt`。

### 答案

```python
import subprocess

result = subprocess.run(["df", "-h", "/c"], capture_output=True, text=True)
use_pct = result.stdout.split("\n")[1].split()[4]

with open("log.txt", "a") as f:
    f.write(f"Disk usage: {use_pct}\n")

with open("log.txt", "r") as f:
    print(f.read())
```

### 解析

- `"a"` 模式 = append（追加写入，不覆盖）
- 写完之后再用 `"r"` 模式读回来验证

### Q&A

**Q：`with open("file", "r") as f: f.write(...)` 为什么报错？**
A：`"r"` 是只读模式，不能写。改成 `"w"`（覆盖写）或 `"a"`（追加写）。

---

## 1.6 无提示：提取 experiments 目录大小

### 题目

用 `subprocess.run()` 跑 `du -sh ~/devops-learning/experiments`，从输出中只提取大小部分（如 `26K`），打印 `"experiments size: 26K"`。

### 答案

```python
import subprocess

result = subprocess.run(["du", "-sh", "~/devops-learning/experiments"],
    capture_output=True, text=True, shell=True)

# 推荐写法（shell=True，因为 ~ 需要 shell 展开）
result = subprocess.run("du -sh ~/devops-learning/experiments",
    shell=True, capture_output=True, text=True)

size = result.stdout.split()[0]
print(f"experiments size: {size}")
```

### 解析

- `~` 需要 shell 展开，所以用 `shell=True`
- `du -sh` 输出格式：`"23K\t/c/Users/Tao/devops-learning/experiments"`，第一部分是大小

---

## 1.7 port_check.py argparse 综合

### 题目

写一个 `port_check.py`，用 argparse 接收 `--host`（必须）、`--port`（int，默认80）、`--verbose`（开关）。打印 "Checking host:port"。

### 答案

```python
import argparse

parser = argparse.ArgumentParser(description="port check tool")
parser.add_argument("--host", required=True, help="hostname")
parser.add_argument("--port", type=int, default=80, help="port number")
parser.add_argument("--verbose", action="store_true", help="verbose")

args = parser.parse_args()

if args.verbose:
    print(f"[INFO] checking {args.host}:{args.port}")
print(f"Host: {args.host}, Port: {args.port}")
```

### 解析

- `required=True` 使 `--host` 成为必填参数
- `type=int` 自动把字符串转整数
- `default=80` 不传 `--port` 时值就是 80

---

## 1.8 config_check.py — 配置文件解析

### 题目

写 `config_check.py`，用 argparse 接收 `--file` 和 `--key`。读取配置文件（每行 `key=value`），输出指定 key 的值。文件不存在时提示错误。

### 答案

```python
import argparse, sys

parser = argparse.ArgumentParser(description="config check tool")
parser.add_argument("--file", help="file to check")
parser.add_argument("--key", help="key to find")
args = parser.parse_args()

try:
    with open(args.file, "r") as f:
        found = False
        for line in f:
            if args.key == line.strip().split("=")[0]:
                print(f"{args.key} = {line.strip().split('=')[1]}")
                found = True
        if not found:
            print("no match key")
except FileNotFoundError:
    print("file not found")
```

### 常见错误

1. `open("file", "r")` — 用了字符串 `"file"` 而不是变量 `args.file`
2. `parser.add_argument("--verbose", version="store_true")` — 应该是 `action="store_true"`，没有 `version` 参数

---

# 2. Shell 练习

---

## 2.1 Shell 变量 + 参数 + df

### 题目

写一个 Shell 脚本 `check.sh`，接收一个状态参数，根据状态打印 emoji，同时打印磁盘使用率。

### 答案

```bash
#!/bin/bash
status=$1
if [ "$status" = "running" ]; then
    echo "✅"
elif [ "$status" = "stopped" ]; then
    echo "❌"
else
    echo "❓"
fi
df -h /c
```

### Q&A

**Q：`#!/bin/sh` 和 `#!/bin/bash` 什么区别？**
A：Ubuntu 上 `/bin/sh` 指向 dash（轻量 shell），部分功能不支持（如 `[[ ]]`、`{1..5}`）。`/bin/bash` 功能最全。建议统一用 `#!/bin/bash`。

---

## 2.2 Shell 条件判断 emoji 转换

### 题目

接收参数判断 running/stopped/unknown 对应 ✅/❌/❓。

### 答案

```bash
#!/bin/bash
if [ "$1" = "running" ]; then
    echo "✅"
elif [ "$1" = "stopped" ]; then
    echo "❌"
else
    echo "❓"
fi
```

### Q&A

**Q：`$1` 不加引号为什么报错？**
A：没传参数时 `$1` 是空值，不加引号变成 `[ = "running" ]`，Shell 看到等号前没有东西就报错。加引号后 `[ "" = "running" ]` 正常比较，不报错。

**Q：`=` 两边为什么要有空格？**
A：`[ ... ]` 语法要求每个元素（`[`、表达式、`]`）之间都要空格。`[x = y]` 或 `[ x = y]` 都不对。

---

## 2.3 for 循环遍历 servers.txt

### 题目

遍历 `servers.txt`（格式 `name,status`），打印每台服务器的名字和状态。

### 答案

```bash
#!/bin/bash
for line in $(cat servers.txt); do
    name=$(echo $line | cut -d',' -f1)
    status=$(echo $line | cut -d',' -f2)
    if [ "$status" = "running" ]; then
        echo "$name ✅"
    else
        echo "$name ❌"
    fi
done
```

### Q&A

**Q：`cut -d',' f1` 为什么报错？**
A：少了个 `-`，应该是 `cut -d',' -f1`。

**Q：`status = $(...)` 为什么报错？**
A：Shell 变量赋值等号两边不能有空格。`status = value` 被解释为"运行 `status` 命令，参数是 `=` 和 `value`"。正确的：`status=$(...)`。

---

## 2.4 函数 + 循环

### 题目

把 if/else 逻辑抽成函数，在循环中调用。

### 答案

```bash
#!/bin/bash
check_server() {
    name=$1
    status=$2
    if [ "$status" = "running" ]; then
        echo "$name ✅"
    else
        echo "$name ❌"
    fi
}

for line in $(cat servers.txt); do
    name=$(echo $line | cut -d',' -f1)
    status=$(echo $line | cut -d',' -f2)
    check_server $name $status
done
```

### 解析

- 函数定义：`函数名() { 代码 }`
- 参数：函数内用 `$1`、`$2`，和脚本参数一样
- 调用：直接写函数名

---

## 2.5 并发 & + wait

### 题目

写 `parallel_check.sh`，并发跑 3 个 `sleep 3 &`，用 `wait` 等全部完成，最后打印 "Done"。

### 答案

```bash
#!/bin/bash
sleep 3 &
sleep 3 &
sleep 3 &
wait
echo "Done"
```

### 解析

- `&`：后台运行，不阻塞终端
- `wait`：等待所有后台任务完成
- 串行 3×3=9 秒，并发 3 秒

### Q&A

**Q：并发有什么用？**
A：检查 5 台服务器的磁盘时，串行要等 5 次，并发只需等最慢的那次。

---

## 2.6 set -e + trap

### 题目

写 `safe_deploy.sh`，使用 `set -e` 和 `trap`，包含三步：`mkdir /tmp/test-deploy`、`cd /tmp/test-deploy`、`echo "done"`。

### 答案

```bash
#!/bin/bash
set -e
trap "rm -rf /tmp/test-deploy; echo 'cleaned'" EXIT

mkdir /tmp/test-deploy
cd /tmp/test-deploy
echo "done"
```

### Q&A

**Q：`set -e` 做了什么？**
A：任何一个命令返回非零退出码，脚本立即终止。防止"备份失败→继续修改配置"这类灾难。

**Q：`trap ... EXIT` 为什么放开头？**
A：最佳实践——打开脚本第一眼就知道退出时自动清理，不需要翻到最后。

---

## 2.7 find_large.sh — 找大文件

### 题目

找到 `/tmp` 下大于 1MB 的文件，打印文件名、大小和总数。

### 答案

```bash
#!/bin/bash
files=$(find /tmp -size +1M 2>/dev/null)
echo "$files" | xargs -I{} ls -lh {} 2>/dev/null
echo "---"
echo "Total: $(echo "$files" | wc -l) files"
```

### 解析

- `find /tmp -size +1M` → 找大于 1MB 的文件
- `2>/dev/null` → 错误信息丢垃圾桶（某些文件没权限读）
- `xargs -I{} ls -lh {}` → 对每个找到的文件执行 `ls -lh`
- `$(echo "$files" | wc -l)` → 统计行数 = 文件数

### Q&A

**Q：`2>/dev/null` 里的 2 是什么？**
A：文件描述符。1=stdout（正常输出），2=stderr（错误信息）。`2>/dev/null` 把错误信息重定向到垃圾桶。

**Q：`tr -d ' '` 里的 `-d` 和 `cut -d','` 的 `-d` 一样吗？**
A：不一样。`tr -d` = delete（删除字符）；`cut -d` = delimiter（分隔符）。

---

# 3. 综合项目

---

## 3.1 项目 1：日志分析器

### 题目要求

见 [项目 1 说明](#31-项目-1日志分析器)

### 完整代码

```python
import argparse
from tabulate import tabulate
import sys

parser = argparse.ArgumentParser(description="log analyzer tool")
parser.add_argument("file", help="log file to be analyzed")
parser.add_argument("--level", help="filter by level")
parser.add_argument("--output", help="export report to file")
parser.add_argument("--verbose", action="store_true", help="verbose output")
args = parser.parse_args()

if args.verbose:
    print("start analysing")

try:
    with open(args.file, "r") as f:
        counts = {}
        for line in f:
            parts = line.strip().split()
            if len(parts) < 2:
                continue
            if args.level and parts[1] != args.level:
                continue
            level = args.level if args.level else parts[1]
            counts[level] = counts.get(level, 0) + 1

        table = tabulate(counts.items(), headers=["Level", "Count"], tablefmt="grid")
        print(table)

        if args.output:
            with open(args.output, "w") as f:
                f.write(table + "\n")

except FileNotFoundError:
    print(f"Error: file '{args.file}' not found")
    sys.exit(1)
```

### 知识点

| 知识点 | 在项目中的应用 |
|--------|---------------|
| argparse | 位置参数 file + 可选参数 |
| try/except | FileNotFoundError 处理 |
| with open | 读文件 |
| strip/split | 解析每行 |
| 字典计数 | counts.get(level, 0) + 1 |
| tabulate | 表格输出 |
| encoding=utf-8 | 写入 emoji 时需要 |

---

## 3.2 项目 2：服务器巡检

```python
import argparse, subprocess, os, platform
from tabulate import tabulate

parser = argparse.ArgumentParser(description="Server Inspector")
parser.add_argument("--disk", action="store_true", help="disk only")
parser.add_argument("--output", help="export report")
parser.add_argument("--verbose", action="store_true")
args = parser.parse_args()

hostname = platform.uname().node
system = platform.uname().system
cpu = os.cpu_count()
result = subprocess.run(["df", "-h", "/c"], capture_output=True, text=True)
usage = result.stdout.split("\n")[1].split()[4]

data = [
    ["Disk Usage", usage],
    ["Hostname", hostname],
    ["System", system],
    ["CPU Cores", str(cpu)],
]
print(tabulate(data, headers=["Item", "Value"], tablefmt="grid"))

if args.output:
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(tabulate(data, headers=["Item", "Value"], tablefmt="grid"))
```

---

## 3.3 项目 3：Git 批量检查

```python
import argparse, subprocess, os

parser = argparse.ArgumentParser(description="Git Batch Checker")
parser.add_argument("--dir", help="dir to scan")
parser.add_argument("--verbose", action="store_true")
parser.add_argument("--output")
args = parser.parse_args()

search_dir = args.dir if args.dir else os.path.expanduser("~")
paths = []
for root, dirs, files in os.walk(search_dir):
    if ".git" in dirs:
        paths.append(root)
        dirs.remove(".git")

report = []
n, y = 0, 0
for repo in paths:
    result = subprocess.run(["git", "status", "--porcelain"],
        capture_output=True, text=True, cwd=repo)
    if result.stdout.strip():
        report.append(f"{repo} ⚠️"); n += 1
    else:
        report.append(f"{repo} ✅"); y += 1

report.append(f"Total: {len(paths)}, Clean: {y}, Dirty: {n}")
output = "\n".join(report)

if args.output:
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(output + "\n")
else:
    print(output)
```

### 知识点

| 概念 | 说明 |
|------|------|
| `os.walk` | 递归扫描所有子目录 |
| `dirs.remove(".git")` | 不进 .git 内部，性能优化 |
| `cwd=repo` | subprocess 切换到该目录再执行 |
| `--porcelain` | git status 机器可读格式 |

---

## 3.4 复习项目：日志统计仪

```python
import argparse, subprocess
from tabulate import tabulate

parser = argparse.ArgumentParser(description="Log Statistics Reporter")
parser.add_argument("file", help="path of log")
parser.add_argument("--sort", help="name|count")
parser.add_argument("--verbose", action="store_true")
parser.add_argument("--output")
args = parser.parse_args()

counts = {}
with open(args.file, "r") as f:
    for line in f:
        parts = line.strip().split()
        level = parts[1]
        counts[level] = counts.get(level, 0) + 1

if args.sort == "name":
    sorted_data = sorted(counts.items(), key=lambda x: x[0])
else:
    sorted_data = sorted(counts.items(), key=lambda x: x[1], reverse=True)

table = tabulate(sorted_data, ["Level", "Count"])
print(table)

# wc -l 统计总行数
result = subprocess.run(["wc", "-l", args.file], capture_output=True, text=True)
total = result.stdout.split()[0]
print(f"Total lines: {total}")

if args.output:
    with open(args.output, "w") as f:
        f.write(table + f"\nTotal lines: {total}\n")
```

### Q&A

**Q：`sorted(counts.items(), key=lambda x: x[1], reverse=True)` 是什么意思？**
A：`counts.items()` 把字典变成 `[("ERROR", 3), ("INFO", 2), ("WARN", 1)]`。`key=lambda x: x[1]` 按第二个元素（数字）排序。`reverse=True` 从大到小。

**Q：`lambda` 是什么？**
A：匿名函数。`lambda x: x[1]` = 一个接收 `x`、返回 `x[1]` 的小函数。`sorted` 用它来决定排序依据。

---

## 3.5 系统健康检查脚本

### 题目

在 WSL 里写脚本，检查磁盘、内存、运行时间、CPU 负载。

### 完整代码

```bash
#!/bin/bash

# Disk
path="${1:-/}"
usage=$(df -h "$path" | tail -1 | awk '{print $5}' | tr -d '%')
echo "Disk: ${usage}%"
[ "$usage" -gt 80 ] && echo "⚠️" || echo "✅"

# Memory
m_total=$(free -m | grep Mem | awk '{print $2}')
m_avail=$(free -m | grep Mem | awk '{print $7}')
m_usage=$(( (m_total - m_avail) * 100 / m_total ))
echo "Memory: ${m_usage}%"
[ "$m_usage" -gt 90 ] && echo "⚠️" || echo "✅"

# Uptime
echo "Uptime: $(uptime -p)"

# Load
load=$(uptime | awk -F'load average:' '{print $2}' | cut -d',' -f1 | tr -d ' ')
echo "Load: $load"
load_int=$(echo "$load" | cut -d'.' -f1)
[ "$load_int" -gt 2 ] && echo "⚠️" || echo "✅"
```

### 解析

| 命令 | 提取什么 |
|------|---------|
| `awk '{print $5}'` | df 的第 5 列（Use%） |
| `tr -d '%'` | 删掉百分号变纯数字 |
| `grep Mem \| awk '{print $2}'` | 内存总大小 |
| `$(( (a - b) * 100 / a ))` | 整数运算算百分比 |
| `awk -F'load average:'` | 按文本切分提取负载值 |
| `cut -d'.' -f1` | 取整数部分（Shell 不能比小数） |

### Q&A

**Q：`$1` 在脚本里和函数里有什么不同？**
A：脚本的 `$1` 是命令行参数。函数里的 `$1` 是函数的第一个参数。互不影响。

**Q：Shell 里怎么算百分比？**
A：用 `$(( ))` 做整数运算。`$(( (total - avail) * 100 / total ))`。不能用小数。

**Q：`awk` 的 `-F` 和 `cut` 的 `-d` 有什么区别？**
A：都是设置分隔符，但 `awk -F` 支持字符串做分隔符（如 `load average:`），`cut -d` 只支持单个字符（如 `,`）。

---

## 3.6 azure-vm-checker.py

### 题目

用 Python 调用 Azure CLI 列出 VM，输出表格。

### 完整代码

```python
import argparse, json, subprocess, sys
from tabulate import tabulate

parser = argparse.ArgumentParser(description="Azure VM Checker")
parser.add_argument("--output", help="export report")
parser.add_argument("--verbose", action="store_true")
args = parser.parse_args()

result = subprocess.run("az vm list", shell=True, capture_output=True, text=True)

if result.returncode != 0:
    print("Error: please run 'az login' first")
    sys.exit(1)

vms = json.loads(result.stdout)
if not vms:
    table = "No VMs found"
    print(table)
else:
    data = [[vm["name"], vm["location"]] for vm in vms]
    table = tabulate(data, headers=["Name", "Location"])
    print(table)

if args.output:
    with open(args.output, "w") as f:
        f.write(table + "\n")
    if args.verbose:
        print("exporting successful")
```

### 知识点

- `subprocess.run("az vm list", shell=True)` — Windows 上 `az` 是 `.cmd` 文件，必须 `shell=True`
- `json.loads(result.stdout)` — JSON 字符串 → Python 列表
- `if not vms` — 空列表 `[]` 是 falsy

### Q&A

**Q：为什么 `sys.exit(1)` 放在 `print` 前面就不打印？**
A：`exit()` 立即终止进程，后面的代码不会执行。先打印再退出。

**Q：`table` 变量为什么有时报 `NameError`？**
A：`table` 在 `if not vms:` 的分支里没定义，但后面 `if args.output:` 要用。要确保所有分支都给 `table` 赋值。

---

### 3.7 filter_logs.py — 按日期和级别过滤日志

### 题目

写 `filter_logs.py`，读取 `app.log`，接收 `--level` 和 `--since`（起始日期），输出匹配行。

### 答案

```python
import argparse
from tabulate import tabulate

parser = argparse.ArgumentParser(description="log filter tool")
parser.add_argument("file", help="log to filter")
parser.add_argument("--level", help="event level")
parser.add_argument("--since", help="start date (YYYY-MM-DD)")
parser.add_argument("--output", help="export report")
parser.add_argument("--verbose", action="store_true")
args = parser.parse_args()

try:
    with open(args.file, "r") as f:
        result = []
        for line in f:
            parts = line.strip().split()
            if len(parts) < 2:
                continue
            if args.level and parts[1] != args.level:
                continue
            if args.since and args.since > parts[0]:
                continue
            result.append(line.strip())

        rows = [[r] for r in result]
        table = tabulate(rows, headers=["Log Entry"], tablefmt="grid")
        print(table)

        if args.output:
            with open(args.output, "w") as f:
                f.write(table + "\n")

except FileNotFoundError:
    print("File not found")
```

### 解析

- 日期比较：`YYYY-MM-DD` 格式的字符串可以直接用 `>=` 比较
- 空行跳过：`if len(parts) < 2: continue`
- 先过滤 `--level`，再过滤 `--since`，再追加结果

### Q&A

**Q：`tabulate` 的 headers 和数据的列数要对齐吗？**
A：对。数据每行有 1 列 → headers 也要 1 个。数据每行有 3 列 → headers 给 3 个。

---

### 3.8 log_parser.py — 正则提取 IP 并统计

### 题目

从 `app.log` 提取所有 IP 地址（格式 X.X.X.X），统计每个 IP 出现次数，输出表格。

### 答案

```python
import argparse, re
from tabulate import tabulate

parser = argparse.ArgumentParser(description="log parser tool")
parser.add_argument("file", help="log file to parse")
parser.add_argument("--output", help="export report")
parser.add_argument("--verbose", action="store_true")
args = parser.parse_args()

ips_account = {}
with open(args.file, "r") as f:
    for line in f:
        for found_ip in re.findall(r"\d+\.\d+\.\d+\.\d+", line):
            ips_account[found_ip] = ips_account.get(found_ip, 0) + 1

table = tabulate(ips_account.items(), headers=["IP", "Count"], tablefmt="grid")
print(table)

if args.output:
    with open(args.output, "w") as f:
        f.write(table)
```

### 解析

- `re.findall(r"\d+\.\d+\.\d+\.\d+", line)` 返回列表 → 必须遍历
- `counts[ip] = counts.get(ip, 0) + 1` 是计数模式
- `tabulate(dict.items())` 直接可输出

### Q&A

**Q：为什么 `ips_account[ip] = ...` 的循环缩进要在 `with` 里面？**
A：如果缩进在外面，只处理最后一行。里面才能逐行处理每一行匹配的 IP。

---

### 3.9 log_report.py — 日志级别统计报告

### 题目

读取日志文件，统计每个级别（INFO/ERROR/WARN）出现次数，生成表格，支持 `--format markdown` 和 `--output`。

### 答案

```python
import argparse, subprocess
from tabulate import tabulate

parser = argparse.ArgumentParser(description="log report tool")
parser.add_argument("file", help="log file")
parser.add_argument("--format", help="markdown format")
parser.add_argument("--output", help="export")
parser.add_argument("--verbose", action="store_true")
args = parser.parse_args()

lines = subprocess.run(["wc", "-l", args.file], capture_output=True, text=True)
if args.verbose:
    print(f"Total lines: {lines.stdout.strip().split()[0]}")

counts = {}
with open(args.file, "r") as f:
    for line in f:
        parts = line.strip().split()
        if len(parts) < 2:
            continue
        level = parts[1]
        counts[level] = counts.get(level, 0) + 1

fmt = "pipe" if args.format == "markdown" else "grid"
table = tabulate(counts.items(), headers=["Level", "Count"], tablefmt=fmt)
print(table)

if args.output:
    with open(args.output, "w") as f:
        f.write(table + "\n")
```

### 解析

- `wc -l` 用 `subprocess.run` + `capture_output=True` 拿到总行数
- `{k, v}` 直接输出给 `tabulate`
- `--format` 只在输出和文件生效，控制台默认 grid

---

### 3.10 server_health_reporter.py — 系统健康检查

### 题目

用 subprocess 收集系统信息，输出健康报告表格。

### 答案

```python
import argparse, subprocess
from tabulate import tabulate

parser = argparse.ArgumentParser(description="server health reporter")
parser.add_argument("--format", help="markdown format")
parser.add_argument("--output", help="export")
parser.add_argument("--verbose", action="store_true")
args = parser.parse_args()

result = {}

# 磁盘（df -h）
disk_out = subprocess.run(["df", "-h", "/"], capture_output=True, text=True).stdout
result["disk"] = disk_out.strip().split("\n")[1].split()[4]

# 内存（free -m）
mem_out = subprocess.run(["free", "-m"], capture_output=True, text=True).stdout
mem_line = [l for l in mem_out.strip().split("\n") if l.startswith("Mem:")][0]
total = int(mem_line.split()[1])
available = int(mem_line.split()[6])
result["mem"] = f"{(1 - available / total) * 100:.1f}%"

# uptime
uptime_out = subprocess.run(["uptime"], capture_output=True, text=True).stdout
result["uptime"] = uptime_out.strip().split()[2]

# 登录用户数（who -q）
who_out = subprocess.run(["who", "-q"], capture_output=True, text=True).stdout
result["users"] = who_out.strip().split("\n")[-1].split("=")[1]

fmt = "pipe" if args.format == "markdown" else "grid"
table = tabulate(result.items(), headers=["Metric", "Value"], tablefmt=fmt)
print(table)

if args.output:
    with open(args.output, "w") as f:
        f.write(table + "\n")
```

### 解析

| 命令 | 取哪一行 | 取哪一列 |
|------|---------|---------|
| `df -h /` | 第 2 行（去掉表头） | 第 5 列（Use%） |
| `free -m` | 找到 `Mem:` 开头的那行 | [1]=total, [6]=available |
| `uptime` | `split()` | [2] = load 数字 |
| `who -q` | 最后一行（`strip().split("\n")[-1]`） | `split("=")[1]` |

### Q&A

**Q：`df -h /` 输出里为什么列数 `[4]` 不是 `[5]`？**
A：`df -h /` 的第一列是 `Filesystem`（索引 0），`Size`（1），`Used`（2），`Avail`（3），`Use%`（4），`Mounted on`（5）。所以 Use% 是 `[4]`。

---

### 3.11 LeetCode 综合练习（字典 / 集合 / 文件解析）

### 题 1：字典计数

```python
servers = ["web-01", "db-01", "web-01", "cache-01", "db-01", "web-01"]
count = {}
for s in servers:
    count[s] = count.get(s, 0) + 1
for k, v in count.items():
    print(f"{k:<10} {v}")
```

### 题 2：解析 df 输出取最大使用率

```python
output = """Filesystem      Size  Used Avail Use% Mounted on
/dev/root        29G  1.7G   27G   6% /
tmpfs           446M     0  446M   0% /dev/shm
/dev/sda16      881M   64M  756M   8% /boot"""

max_pct = 0
max_name = ""
for line in output.strip().split("\n")[1:]:
    parts = line.split()
    pct = float(parts[4].strip("%"))
    if pct > max_pct:
        max_pct = pct
        max_name = parts[0]
print(f"{max_name} : {max_pct}%")
```

### 题 3：集合差集

```python
all_servers = ["10.0.0.1", "10.0.0.2", "10.0.0.3", "10.0.0.4"]
online = ["10.0.0.1", "10.0.0.3"]
offline = set(all_servers) - set(online)
for ip in offline:
    print(ip)
```

---

### 3.12 vm_batch.py — Azure VM 批量启停

### 题目

写一个脚本读取 `servers.txt`，根据 `--action start|stop` 批量操作 VM，用 `tabulate` 输出结果。

### 答案框架

```python
import argparse, subprocess
from tabulate import tabulate

parser = argparse.ArgumentParser(description="VM batch")
parser.add_argument("file", help="vm list file")
parser.add_argument("action", help="start or deallocate")
parser.add_argument("group", help="resource group")
parser.add_argument("--verbose", action="store_true")
parser.add_argument("--output", help="export")
args = parser.parse_args()

status = {}
try:
    with open(args.file) as f:
        for line in f:
            server = line.strip()
            if not server:
                continue
            if args.verbose:
                print(f"Processing {server}...")
            result = subprocess.run(
                ["az", "vm", args.action, "-n", server, "-g", args.group],
                capture_output=True, text=True
            )
            if result.returncode == 0:
                r = subprocess.run(
                    ["az", "vm", "show", "-n", server, "-g", args.group,
                     "--query", "powerState", "-o", "tsv"],
                    capture_output=True, text=True
                )
                state = r.stdout.strip() if r.returncode == 0 else "query failed"
            else:
                state = "Action failed"
            status[server] = state
    table = tabulate(status.items(), headers=["name", "status"], tablefmt="grid")
    print(table)
    if args.output:
        with open(args.output, "w") as f:
            f.write(table + "\n")
except FileNotFoundError:
    print("FileNotFoundError")
```

### Q&A

**Q：为什么 `result_status` 可能在 `else` 分支未定义？**
A：`if result_action.returncode == 0` 执行了才赋值，否则走 else。如果 else 里没赋值，`status[server] = result_status` 会报 NameError。

**Q：`status[server] = result_status` 为什么要在循环里面？**
A：每个 server 的状态不同，要在处理完每个 VM 后立刻保存，否则只有最后一行有效。

---
> **完整版笔记 | 持续更新中**

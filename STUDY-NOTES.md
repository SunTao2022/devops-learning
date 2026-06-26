# DevOps 学习笔记

> 学习者：Tao
> 目标：加拿大 DevOps/SRE 岗位

---

## 目录

1. [Python](#1-python)
2. [Linux](#2-linux)
3. [Shell 脚本](#3-shell-脚本)
4. [Git](#4-git)
5. [Azure CLI](#5-azure-cli)
6. [实验索引](#6-实验索引)

---

## 1. Python

### 1.1 变量与数据类型

```python
name = "web-01"              # 字符串
count = 5                    # 整数
cpu = 45.5                   # 浮点数
status = True                # 布尔
files = ["a", "b", "c"]      # 列表
server = {"name": "web"}     # 字典
```

### 1.2 字符串操作

```python
" hello ".strip()            # "hello" — 去头尾空白
"hello,world".split(",")     # ["hello", "world"]
"hello".upper()              # "HELLO"
f"Server {name}"             # f-string 格式化
```

### 1.3 列表与字典

```python
servers = ["web-01", "db-01"]
servers[0]                   # "web-01"
servers.append("cache-01")   # 末尾添加
len(servers)                 # 3

config = {"port": 80, "host": "localhost"}
config.get("port", 8080)     # 80（不存在时返回 8080）
config.items()               # [("port", 80), ("host", "localhost")]
```

### 1.4 条件判断

```python
if status == "running":
    print("✅")
elif status == "stopped":
    print("❌")
else:
    print("❓")
```

### 1.5 循环

```python
# for 遍历列表
for s in servers:
    print(s)

# enumerate 带序号
for i, s in enumerate(servers, start=1):
    print(f"{i}. {s}")

# 遍历文件行
with open("file.txt") as f:
    for line in f:
        print(line.strip())
```

### 1.6 函数

```python
def check_status(name, status):
    if status == "running":
        return f"{name} ✅"
    return f"{name} ❌"
```

⚠️ **常见错误：**
- 忘记 `return` → 函数返回 `None`
- 等号两边不能有空格（Shell 规则）— Python 需要空格

### 1.7 文件 I/O

```python
with open("file.txt", "r") as f:     # 读
    content = f.read()

with open("file.txt", "w") as f:     # 写（覆盖）
    f.write("hello\n")

with open("file.txt", "a") as f:     # 追加
    f.write("more\n")
```

**模式：**
| 模式 | 作用 | 文件不存在 |
|------|------|-----------|
| `"r"` | 读 | ❌ 报错 |
| `"w"` | 写（覆盖） | ✅ 自动创建 |
| `"a"` | 追加 | ✅ 自动创建 |

### 1.8 异常处理

```python
try:
    with open("file.txt") as f:
        ...
except FileNotFoundError:
    print("文件不存在")
```

⚠️ 必须捕获**具体异常类型**（`FileNotFoundError`），不要只用 `except:`。

### 1.9 正则表达式

```python
import re

re.search("ERROR", line)          # 全文搜索（返回第一个匹配）
re.findall(r"\d+", text)          # 找到所有数字
re.sub(r"\d+", "***", text)       # 替换
re.match("ERROR", line)           # 只从开头匹配（不是"匹配任何位置"！）
```

⚠️ **`re.match` 陷阱：** 只从**开头**匹配。`re.match("ERROR", "2026 INFO ERROR")` → `None`。要全文搜索用 `re.search`。

### 1.10 sys 与 os 模块

```python
import sys, os
sys.argv[0]          # 脚本名
sys.argv[1]          # 第一个参数
len(sys.argv)        # 参数个数

os.getcwd()          # 当前目录
os.listdir(".")      # 列出文件
os.cpu_count()       # CPU 核数
os.path.join("a", "b")  # 拼接路径
```

⚠️ `os.listdir("experiments")` 的路径相对于**当前工作目录**，不是脚本位置。用 `Path(__file__).parent` 做脚本相对路径。

### 1.11 subprocess

```python
import subprocess

# 简单命令
result = subprocess.run(["ls", "-la"], capture_output=True, text=True)
print(result.stdout)          # 标准输出
print(result.stderr)          # 错误输出
print(result.returncode)      # 0=成功

# 需要 shell 的命令（管道、重定向、az 等）
result = subprocess.run("ls -la | head -3", shell=True, capture_output=True, text=True)

# Windows 上 .cmd 文件（如 az）必须用 shell=True
result = subprocess.run("az vm list", shell=True, capture_output=True, text=True)
```

**参数：**

| 参数 | 作用 |
|------|------|
| `capture_output=True` | 截获输出到 `result.stdout` |
| `text=True` | 输出为字符串（非 bytes） |
| `shell=True` | 命令写成一个字符串（支持管道） |
| `cwd="路径"` | 先 cd 到该目录再执行 |

### 1.12 模块与包

任何 `.py` 文件都可以被 `import`：

```python
# utils.py
def get_disk():
    ...

# main.py
import utils
print(utils.get_disk())
```

⚠️ 模块里**只定义函数**，不调用。函数调用在主脚本里。

### 1.13 argparse

```python
import argparse

parser = argparse.ArgumentParser(description="工具描述")
parser.add_argument("filename", help="文件名")            # 位置参数
parser.add_argument("--level", help="级别")               # 选项参数
parser.add_argument("--port", type=int, default=80)       # 选项+类型+默认值
parser.add_argument("--verbose", action="store_true")     # 开关
parser.add_argument("--quiet", action="store_true")       # 安静模式
args = parser.parse_args()

print(args.filename)    # 用 . 取参数
print(args.level)
print(args.port)
print(args.verbose)     # True 或 False
```

**`action="store_true"` 的作用：**
- 不加：`--verbose` 需要跟一个值 → `--verbose True`
- 加：`--verbose` 是开关 → 传了就是 `True`，不传就是 `False`

### 1.14 pip 与 venv

```bash
python -m venv myenv              # 创建虚拟环境
source myenv/Scripts/activate     # 激活
pip install requests              # 装包
pip freeze > requirements.txt     # 导出依赖
pip install -r requirements.txt   # 恢复依赖
deactivate                        # 退出
```

**为什么用 venv：** 每个项目互不影响——项目 A 装 flask 1.0，项目 B 装 flask 2.0，不会冲突。

**.gitignore 中加 `venv/`** 避免提交虚拟环境。

### 1.15 requests

```python
import requests
r = requests.get("https://api.github.com/...")
data = r.json()                # 直接返回 Python 字典
print(data["description"])     # 取字段
```

---

## 2. Linux

### 2.1 基础命令

| 命令 | 作用 | 示例 |
|------|------|------|
| `pwd` | 当前路径 | `pwd` |
| `ls -la` | 列出文件（含隐藏） | `ls -la` |
| `cd ~/path` | 切换目录 | `cd ~/devops-learning` |
| `mkdir -p a/b` | 创建目录（含父目录） | `mkdir -p week-1/exercises` |
| `touch file` | 创建空文件 | `touch test.py` |
| `rm file` | 删除文件 | `rm test.py` |
| `rm -rf dir/` | 强制删除目录 | `rm -rf temp/` |
| `cp a b` | 复制 | `cp file.py backup/` |
| `mv a b` | 移动/重命名 | `mv old.txt new.txt` |

### 2.2 文本查看

| 命令 | 作用 | 示例 |
|------|------|------|
| `cat file` | 打印全部 | `cat app.log` |
| `head -10 file` | 前 10 行 | `head -5 app.log` |
| `tail -10 file` | 后 10 行 | `tail -f app.log`（实时跟踪） |
| `less file` | 分页查看 | `less big.log`（空格翻页，q 退出） |
| `wc -l file` | 行数 | `wc -l app.log` |

### 2.3 grep

```bash
grep "ERROR" app.log              # 搜索包含 ERROR 的行
grep -c "ERROR" app.log           # 计数
grep -n "ERROR" app.log           # 带行号
grep -v "ERROR" app.log           # 反向匹配（不含 ERROR）
grep -i "error" app.log           # 忽略大小写
grep -o "ERROR" app.log           # 只输出匹配部分，不是整行
grep -oP '\d+' app.log            # -P = 正则，提取所有数字
grep -oP '(INFO|ERROR|WARN)' app.log  # 提取三种级别
```

**正则符号：**

| 符号 | 匹配 | 不匹配 |
|------|------|--------|
| `\w` | 字母+数字+下划线 | 空格、符号 |
| `\d` | 数字 | 字母 |
| `\s` | 空格、制表符 | 可见字符 |
| `.` | **任何单个字符**（通配符） | 什么都不排除 |
| `\.` | 真正的点号 | 其他字符 |
| `\K` | 前面匹配了但不要，从这里开始取 | — |

### 2.4 管道与组合

```bash
# 管道 |：把左边命令的输出传给右边命令
grep -oP '(INFO|ERROR|WARN)' app.log | sort | uniq -c | sort -rn
#        提取级别名          → 排序 → 去重计数 → 按次数从大到小
```

**`echo` vs 文件：**
- `echo "text"` — 输出文字到屏幕
- `echo "text" \| grep "t"` — 输出经管道传给 grep
- `grep "x" file` — 从文件读
- 文件 + 管道**不能混用**：`echo "x" \| grep file "y"` — grep 忽略管道，只读 file

### 2.5 find / df / du

```bash
find /tmp -name "*.log"           # 按名字找
find /tmp -size +1M               # 大于 1MB
find /tmp -mtime -7               # 7 天内修改过

df -h /c                          # 看 C 盘使用率
df -h /                           # 看根目录

du -sh experiments/               # 看文件夹总大小
du -sh * | sort -rh               # 所有子目录大小排序
```

### 2.6 进程管理

```bash
ps aux                            # 所有进程
ps aux | grep 进程名              # 找特定进程
kill 1234                         # 终止（PID）
kill -9 1234                      # 强制终止

sleep 60 &                        # 后台等 60 秒
jobs                              # 看当前终端的后台任务
fg %1                             # 拉回前台
bg                                # 放到后台继续
Ctrl+Z                            # 暂停当前进程

nohup command &                    # 关终端也不中断
```

**操作序列：**
```bash
sleep 30          # 卡住 30 秒
Ctrl+Z            # 暂停它
bg                # 后台继续跑
jobs              # 看状态
fg %1             # 拉回前台等待结束
```

**`&` vs `nohup`：**
- `&`：后台运行，关终端就停
- `nohup` + `&`：后台运行，关终端也不停

### 2.7 用户管理

**文件：**
```bash
/etc/passwd     # 用户列表（用户名:密码占位:UID:GID:描述:家目录:shell）
/etc/group      # 组列表（组名:密码占位:GID:成员）
```

**命令：**

| 命令 | 作用 | 示例 |
|------|------|------|
| `useradd -m -s /bin/bash 用户名` | 创建用户 | `useradd -m -s /bin/bash devops` |
| `passwd 用户名` | 设置密码 | `passwd devops` |
| `userdel -r 用户名` | 删除用户+家目录 | `userdel -r devops` |
| `usermod -aG 组名 用户名` | 加入组 | `usermod -aG engineers devops` |
| `groupadd 组名` | 创建组 | `groupadd engineers` |
| `groups 用户名` | 看所属组 | `groups devops` |
| `su - 用户名` | 切换用户 | `su - alice` |

### 2.8 文件权限

```bash
-rw-r--r-- 1 root root 6 Jun 20 17:09 file.txt
│└┬┘└┬┘└┬┘
│ │   │   └── 其他人权限
│ │   └────── 同组权限
│ └────────── 所有者权限
└──────────── 文件类型（- = 文件，d = 目录）
```

| 权限 | 字母 | 数字 |
|------|------|------|
| 读 | r | 4 |
| 写 | w | 2 |
| 执行 | x | 1 |

```bash
chmod 755 file    # rwxr-xr-x  脚本
chmod 644 file    # rw-r--r--  普通文件
chmod 600 file    # rw-------  密钥文件
```

**目录权限特殊：**
- `r`：可以 `ls` 列出文件名
- `w`：可以创建/删除文件
- `x`：**可以 `cd` 进入目录**—没有 x 则即使文件是 666 也进不去

⚠️ **root 绕过所有权限检查**。

### umask — 新建文件默认权限

```bash
umask                 # 看当前值（通常是 0022）
touch /tmp/test       # 新建文件默认 644（rw-r--r--）
umask 077             # 改为更严格
touch /tmp/test2      # 新建文件默认 600（rw-------）
```

**公式：** 默认值（文件 666 / 目录 777）− umask = 实际权限。

### setuid — `s` 权限

```bash
ls -l /usr/bin/passwd
# -rwsr-xr-x   ← s = setuid
```

谁运行这个程序，谁就拥有文件所有者的权限。普通用户通过 `passwd` 改密码（需写 `/etc/shadow`）。

### sticky bit — `t` 权限

```bash
ls -ld /tmp
# drwxrwxrwt   ← t = sticky bit
```

任何人都能在 `/tmp` 创建文件，但只能删自己的文件。

### 2.9 网络命令

```bash
ip addr                       # 看 IP
ip route                      # 看路由
ss -tlnp                      # 看端口监听状态

ping -c 4 google.com          # 测试连通性
ping -n 4 10.0.0.1            # Windows MINGW 用 -n

curl -s URL                   # 静默 GET
curl -I URL                   # 只看响应头
curl -L URL                   # 跟随跳转（301→200）
curl -s -o /dev/null -w "%{http_code}" URL   # 只看状态码
curl -s -o /dev/null -w "耗时: %{time_total}s" URL  # 看响应时间

# HTTP 状态码
200 = OK        301/302 = 跳转       404 = 未找到       500 = 服务器错误
```

### 2.10 Linux 目录结构

```bash
/                    # 根目录（一切从这里开始）
/bin                 # 基本命令（ls, cp, mv — 谁都能用）
/sbin                # 系统管理命令（root 用）
/etc                 # 系统配置文件
/etc/resolv.conf     # DNS 配置
/etc/passwd          # 用户列表
/etc/hosts           # 本地域名映射
/home                # 用户家目录（/home/tao）
/var                 # 变化的数据（日志 /var/log）
/tmp                 # 临时文件（重启清空）
/usr                 # 用户程序（/usr/bin, /usr/lib）
```

**`cat /etc/resolv.conf` 不是"工具"——cat 是程序（在 /bin/cat），/etc/resolv.conf 是文本文件。**

### sudo — 临时借 root 身份

```bash
sudo apt install nginx        # 装软件 → 需要 sudo
ls /home                      # 看自己文件 → 不需要
```

**判断规则：** 只涉及自己文件/进程 → 不用 sudo。改系统范围的东西（装软件、改配置、管理用户）→ 必须 sudo。

**`sudo su -`** = 变成 root 用户，之后不用每次打 sudo。

### 2.11 systemctl / journalctl

```bash
systemctl status 服务名        # 看状态
systemctl start 服务名         # 启动
systemctl stop 服务名          # 停止
systemctl restart 服务名       # 重启
systemctl enable 服务名        # 开机自启

journalctl -u 服务名           # 看该服务的日志
journalctl -u 服务名 --since today | tail -20  # 只看今天最后 20 行
```

### 2.11 SSH / SCP

```bash
ssh 用户名@IP                  # 远程登录
scp 本地文件 用户名@IP:/远程路径  # 上传文件
scp 用户名@IP:/远程文件 .       # 下载文件

# 免密码登录
ssh-keygen -t rsa -b 4096      # 生成密钥对
ssh-copy-id 用户名@IP          # 上传公钥
```

---

## 3. Shell 脚本

### 3.1 基本结构

```bash
#!/bin/bash                    # shebang — 指定解释器
set -e                         # 任何命令失败立即终止
trap clean_up EXIT             # 退出时自动清理

clean_up() {
    rm -rf /tmp/temp-dir
}

# 参数
echo "第一个参数: $1"
echo "参数个数: $#"
echo "所有参数: $@"
```

### 3.2 变量与条件

```bash
name="web-01"                  # 赋值（等号两边不能有空格）
echo $name                     # 取值（加 $）
echo ${name}                   # 也可加花括号

if [ "$1" = "running" ]; then
    echo "✅"
elif [ "$1" = "stopped" ]; then
    echo "❌"
else
    echo "❓"
fi
```

⚠️ **常见错误：**
- `if [ $1 = "x" ]` — `$1` 不加引号，空值时报错
- `if [ $status = "x" ]` — 同上，应改为 `"$status"`
- `if [ x$1 = "x" ]` — 旧写法，现在直接加引号

### 3.3 for 循环

```bash
# 遍历列表
for s in web-01 db-01 cache-01; do
    echo $s
done

# 遍历文件
for line in $(cat servers.txt); do
    name=$(echo $line | cut -d',' -f1)
    status=$(echo $line | cut -d',' -f2)
    echo "$name is $status"
done
```

### 3.4 函数

```bash
check_server() {
    name=$1
    status=$2
    if [ "$status" = "running" ]; then
        echo "$name ✅"
    else
        echo "$name ❌"
    fi
}

check_server web-01 running
```

### 3.5 并发与 wait

```bash
task1 &
task2 &
task3 &
wait           # 等所有后台任务完成
echo "全部完成"
```

### 3.6 输出重定向

```bash
命令 > file         # stdout → 文件（覆盖）
命令 >> file        # stdout → 文件（追加）
命令 2>/dev/null    # stderr → 垃圾桶
命令 > file 2>&1    # stdout + stderr → 同一个文件
```

**文件描述符：**
- `1` = stdout（正常输出）
- `2` = stderr（错误信息）

### 3.7 getopt — 高级参数解析

```bash
#!/bin/bash
ARGS=$(getopt -o f:v --long file:,verbose -n "$0" -- "$@")
eval set -- "$ARGS"

while true; do
    case "$1" in
        -f|--file)    echo "File: $2"; shift 2 ;;
        -v|--verbose) echo "Verbose"; shift ;;
        --)           shift; break ;;
        *)            echo "Unknown"; exit 1 ;;
    esac
done
```

| 部分 | 意思 |
|------|------|
| `-o f:v` | 短选项：`-f` 带值，`-v` 开关 |
| `--long file:,verbose` | 长选项：`--file` 带值，`--verbose` 开关 |
| `shift` | 吃掉当前参数 |
| `shift 2` | 吃掉选项 + 值（两个） |
| `--` | 参数结束标记 |

**记忆规则：**
- 开关（无值）→ `shift`（丢 1 个）
- 带值参数 → `shift 2`（丢 2 个）

### 3.8 信号处理 — trap

```bash
trap "echo '被 Ctrl+C 中断了'; exit" INT     # Ctrl+C 触发
trap "echo '命令失败'" ERR                    # 任何命令失败触发
trap clean_up EXIT                            # 脚本退出时触发
```

| 信号 | 触发时机 |
|------|---------|
| `INT` | 按 Ctrl+C |
| `TERM` | 被 kill 终止 |
| `ERR` | 任何命令返回非 0 |
| `EXIT` | 脚本退出（无论成功失败） |

---

## 4. Git

### 4.1 基础工作流

```bash
git init                          # 初始化
git add file.txt                  # 暂存
git commit -m "消息"              # 提交
git status                        # 看状态
git log --oneline                 # 看历史
git diff                          # 看未暂存的改动
git push                          # 推送
git pull                          # 拉取
```

### 4.2 分支

```bash
git branch                          # 看分支列表
git switch -c feature               # 创建并切换
git switch master                   # 切换回 master
git merge feature                   # 合并
git branch -d feature               # 删除
```

### 4.3 合并冲突

冲突发生时，文件里出现：

```
<<<<<<< HEAD
当前分支的内容
=======
其他分支的内容
>>>>>>> feature
```

修复：删标记行，保留想要的内容 → `git add` → `git commit`。

### 4.4 amend

```bash
git commit --amend -m "新消息"      # 修改上次提交的信息
# 修改后必须 git push --force-with-lease（仅限未共享的分支）
```

### 4.5 fetch vs pull

```bash
git fetch          # 下载远程更新，不改本地
git pull           # 下载 + 自动合并
```

### 4.6 stash

```bash
git stash          # 暂存未提交的改动
git stash list     # 看 stash 列表
git stash pop      # 恢复最近一次
git stash -u       # 连新文件一起存
```

### 4.7 tag

```bash
git tag v0.1                     # 打标签
git tag                          # 列出
git push --tags                  # 推送标签
```

### 4.8 rebase

```bash
git switch -c feature
# ...写代码，commit...
git rebase master    # 把 feature 的 commit 挪到 master 最新版后
git switch master
git merge feature    # 此时是 fast-forward，一条直线
```

**黄金流程：**

```bash
git checkout -b new-feature   # ① 建分支（保护 master）
git add . && git commit -m ".." # ② 写代码
git rebase master              # ③ 同步 master 最新
git switch master              # ④ 切回
git merge new-feature          # ⑤ 合并（一条直线）
git branch -d new-feature      # ⑥ 删分支
```

**rebase vs merge：**

| | merge | rebase |
|--|-------|--------|
| 结果 | 有分叉 + merge commit | 一条直线 |
| 何时用 | 多人协作合入主分支 | 自己开发时同步 |
| 已 push 的 | 可以 merge | ❌ 不要 rebase |

---

## 5. Azure CLI

### 5.1 登录与查看

```bash
az login --use-device-code       # 登录
az account show                  # 看订阅
az account list --output table   # 看所有订阅
az group list --output table     # 看资源组
az vm list --output table        # 看 VM（空=没有）
```

### 5.2 在 Python 中调用

Windows 上 `az` 是 `.cmd` 文件，必须用 `shell=True`：

```python
result = subprocess.run("az vm list", shell=True, capture_output=True, text=True)
vms = json.loads(result.stdout)
```

### 5.2 VM 生命周期（完整命令链）

```bash
# 创建（开始计费）
az vm create -n 名字 -g 组 --image Ubuntu2404 --size Standard_B2ts_v2 --admin-username azureuser --generate-ssh-keys --location canadacentral

# 查看状态
az vm show -n 名字 -g 组
az vm get-instance-view -n 名字 -g 组 --query "instanceView.statuses[?starts_with(code, 'PowerState/')]" -o table

# 启动
az vm start -n 名字 -g 组

# 停止计费（关机，磁盘还留着）
az vm deallocate -n 名字 -g 组

# 删除 VM（磁盘单独留着，还收费）
az vm delete -n 名字 -g 组 --yes

# 删除资源组（连同所有资源，彻底停止计费）
az group delete -n 组名 --yes
```

**计费规则：**
- `deallocate` = 停止计费，只收磁盘费（约 $0.5-1/月）
- `delete VM` = 删机器，磁盘保留
- `delete group` = 连磁盘一起删，完全停计费

### 5.3 测试用规格

| 规格 | vCPU | 内存 | 月费 |
|------|------|------|------|
| `Standard_B2ts_v2` | 2 | 1G | ~$15 |
| `Standard_B1s` | 1 | 1G | ~$5（部分区域无货） |

选择最低可用规格，学完立刻删除。

---

## 6. 实验索引

### Python 练习

| 文件 | 涵盖内容 |
|------|---------|
| `exercises/python/day5_practice.py` | 条件、循环、正则 |
| `exercises/python/day7_practice.py` | re.sub/findall/search/match |
| `exercises/python/day8_practice.py` | sys.argv、os 模块 |
| `exercises/python/subprocess_practice.py` | subprocess.run |
| `exercises/python/utils.py` | 自定义模块 |
| `exercises/python/day9_practice.py` | import 模块 |
| `exercises/python/argparse_practice.py` | argparse 基础 |
| `exercises/python/port_check.py` | argparse 综合 |
| `exercises/python/find_servers.py` | sys.argv + 文件 I/O |
| `experiments/review.py` | subprocess + tabulate 综合 |
| `experiments/config_check.py` | 配置文件解析 |
| `experiments/filter_logs.py` | 按级别和日期过滤日志 |

### Shell 练习

| 文件 | 涵盖内容 |
|------|---------|
| `exercises/shell/check.sh` | 变量、参数、if |
| `exercises/shell/review.sh` | for 循环、函数 |
| `exercises/shell/server_check.sh` | 函数 + 参数 |
| `exercises/shell/parallel_check.sh` | 并发 & + wait |
| `exercises/shell/safe_deploy.sh` | set -e, trap |
| `exercises/shell/health_check.sh` | 磁盘监控综合 |
| `exercises/shell/system_health_check.sh` | 完整系统检查 |
| `exercises/shell/find_large.sh` | find + 计数 |

### 综合项目

| 文件 | 涵盖内容 |
|------|---------|
| `projects/log_analyzer.py` | argparse + 字典 + tabulate |
| `projects/server_inspector.py` | subprocess + 系统信息 |
| `projects/git_batch.py` | os.walk + git status |
| `projects/stats_reporter.py` | 排序 + wc |
| `projects/azure_vm_checker.py` | az CLI + json |
| `experiments/server_health_reporter.py` | subprocess + 系统健康检查 |
| `experiments/log_report.py` | wc + 字典计数 + tabulate |
| `experiments/log_parser.py` | re.findall + IP 统计 |
| `experiments/args_demo.sh` | getopt 参数解析 |

### 数据文件

| 文件 | 用途 |
|------|------|
| `data/app.log` | 练习日志 |
| `data/servers.txt` | 服务器列表 |

# DevOps 学习日志

> 开始日期：2026-06-08 (Day 1)
> 学习者：Tao
> 目标：加拿大 DevOps/SRE 岗位

---

## Day 1 — 2026-06-08 (周一)

### ✅ 今日完成
- [ ] 学习：________________________________
- [ ] 练习：________________________________
- [ ] 实验：________________________________

### 📝 关键知识点
1. ________________________________
2. ________________________________
3. ________________________________

###  ️ 遇到的坑
- ________________________________

### 📊 投入时间
- 学习：___ 分钟
- 练习：___ 分钟
- 实验：___ 分钟
- 复习：___ 分钟
- **总计**：___ 分钟

### 🎯 明天计划
- ________________________________

---

<!-- 每天在下面追加，不要覆盖已有内容 -->

## Day 5 — 2026-06-09 (周二) 实际内容

### ✅ 今日完成
- [x] 复习：Day 1~4 全部代码重跑验证 + 概念三题全对
- [x] Linux: file, stat, chmod, cat, head, tail, wc, sort, uniq, less
- [x] Git: remote -v, log --oneline, diff, show, add, commit, push, checkout
- [x] 项目 Day 6: system_info.py — 收集 CPU/内存/磁盘信息并输出报告
- [x] GitHub 已推送

### 📝 关键知识点
1. **`for line in f:` 逐行读文件** — 文件对象是行迭代器
2. **`try/except`** — ZeroDivisionError、FileNotFoundError
3. **Linux 文本命令** — cat/head/tail 看内容，wc 统计，sort 排序，uniq 去重
4. **Git diff/show** — `git diff` 看未提交改动，`git show <commit>` 看某次提交详情
5. **shutil.disk_usage()** — Python 获取磁盘信息
6. **subprocess.run()** — 调用系统命令并捕获输出
7. **f-string 计算** — `{usage.total/(1024**3):.1f}` 要在 `{}` 内做运算

###  ️ 遇到的坑
- `eoch` 写成 `data` 等 typo
- `parts[1]` 取到的是列名（'TotalVisibleMemorySize'）不是数值
- `f.write(f"...{usage.total}/(1024**3)")` 计算放 `{}` 外被当作文本

### 📊 投入时间
- 复习：30 分钟
- Linux：30 分钟
- Python 项目：60 分钟
- Git：30 分钟
- **总计**：150 分钟

### 🎯 明天计划
- 第 2 周：正则表达式或模块化编程

---

## Day 6 — 2026-06-10 (周三)

### ✅ 今日完成
- [x] 复习：Day 4~5 概念问答
- [x] Python: 条件判断 if/elif/else
- [x] Python: for 循环 + enumerate
- [x] Python: 文件 I/O + split + 条件综合
- [x] Python: 正则 re.search() + re.findall()
- [x] Linux: grep + 管道链
- [x] Linux: ps aux
- [x] Git: commit --amend / .gitignore / 分支工作流
- [x] 配置: 内存扩容、每周 cron 清理、DeepSeek 回落 Gemma
- [x] GitHub 已推送

### 📊 投入时间
- **总计**：240 分钟

---

## Day 7 — 2026-06-11 (周四)

### ✅ 今日完成
- [x] Python: re.sub() 替换 — 日志 IP 脱敏
- [x] Python: re.findall() 计数 — 统计 ERROR 数量
- [x] Python: re.search() vs re.match() — match 只匹配行首
- [x] Linux: find 命令（name/type/size/mtime）
- [x] Git: fetch / pull / origin/master 概念
- [x] Git: 分支分叉 + git log --graph --oneline --all

### 📝 关键知识点
1. **re.sub(r'模式', '替换', 字符串)** — 正则替换
2. **re.match vs re.search** — match 只从开头找，search 全文找
3. **find . -name/size/mtime** — 文件搜索三大维度
4. **git fetch** — 安全查看远程更新，不改本地
5. **git log --graph** — 可视化分支分叉

### 📊 投入时间
- **总计**：180 分钟

---

## Day 8 — 2026-06-12 (周五)

### ✅ 今日完成
- [x] Python: sys.argv — 命令行参数
- [x] Python: os 模块 — getcwd/environ/listdir/path.join
- [x] Linux: df -h / du -sh / sort -rh
- [x] Git: 创建分叉、mergé、log --graph 验证
- [x] 综合练习: find_servers.py — 用 sys.argv 过滤服务器状态

### 📝 关键知识点
1. **sys.argv** — Python 接住命令行参数
2. **sys.exit(1)** — 脚本退出（0=正常，1=错误）
3. **os.getcwd() / os.listdir() / os.environ.get()**
4. **os.path.join()** — 安全拼接路径
5. **df -h** — 磁盘剩余空间
6. **du -sh * | sort -rh** — 最大目录排行
7. **标志变量** — `found = False` → 找到了变 True

### 📊 投入时间
- **总计**：210 分钟

---

## Day 9 — 2026-06-13 (周六)

### ✅ 今日完成
- [x] Python: subprocess.run() — capture_output/text/解析输出
- [x] Python: subprocess + 条件判断（df 使用率报警）
- [x] Python: subprocess + 文件 I/O（结果写入 log）
- [x] Python: 创建自定义模块 utils.py（3个函数）
- [x] Python: import 模块并在主脚本中调用
- [x] 笔记: 创建 STUDY-NOTES.md（19章完整知识库）

### 📝 关键知识点
1. **subprocess.run(["命令", "参数"], capture_output=True, text=True)**
2. **result.stdout** — 命令输出字符串
3. **result.returncode** — 返回码（0=成功）
4. **创建模块** — 任意 .py 文件可被 import
5. **return vs print** — return 返回值给调用者，print 打屏幕
6. **列表推导式** — `[x for x in list if 条件]`

### 📊 投入时间
- **总计**：240 分钟

---

## Day 10 — 2026-06-14 (周日)

### ✅ 今日完成
- [x] 复习: subprocess + 条件判断综合练习
- [x] Python: utils.py 完善（filter_servers 函数）
- [x] 学习规则: 确立"先讲知识点 → 有提示练习 → 无提示巩固"流程
- [x] 笔记: 完整 STUDY-NOTES.md（已推送到 GitHub）

### 📝 关键知识点
1. **模块引用** — `import utils` 调用自己写的函数
2. **函数要有参数** — `def check_status(status):` 而不是空括号
3. **return 不加括号** — `return x` 而不是 `return(x)`
4. **split(",") 索引** — `parts[0]` 是名字，`parts[1]` 是状态

### 📊 投入时间
- **总计**：120 分钟

### 🎯 明天计划
- Linux: kill + 网络命令实操
- Git: 合并冲突模拟与解决
- Python: 字符串格式化深入

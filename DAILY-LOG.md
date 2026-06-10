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
- [x] 复习：Day 4~5 概念问答（文件 I/O、异常、Linux 管道、git --amend）
- [x] Python: 条件判断 if/elif/else — check_status() 函数
- [x] Python: for 循环 + enumerate — 编号 IP 列表
- [x] Python: 文件 I/O + split + 条件综合 — 过滤 stopped 服务器
- [x] Python: 正则 re.search() + re.findall() — 提取 IP 地址
- [x] Linux: grep -oPcnir、管道链 sort|uniq -c|sort -rn
- [x] Linux: ps aux 进程查看（WSL 上实操）
- [x] Git: commit --amend（暂存区 vs 工作区概念）
- [x] Git: .gitignore + __pycache__/ 管理
- [x] Git: 分支工作流 switch/checkout/merge/branch -d（完整实战）
- [x] 配置: 内存扩容 2200→4000 / 1375→2500，每周日 cron 清理，DeepSeek 回落 Gemma 修复
- [x] GitHub 已推送

### 📝 关键知识点
1. **管道 `|`** — 左命令输出 → 右命令输入，每个命令只做一件事
2. **`grep -oP '^\w+'`** — `-o` 只输出匹配部分，`-P` 启用正则，`^\w+` 行首连续单词
3. **`sort | uniq -c | sort -rn`** — 排序 → 去重计数 → 按次数大到小
4. **`enumerate(列表, start=1)`** — 遍历同时拿序号，拆包 `i, ip = (序号, 值)`
5. **`re.search()` vs `re.findall()`** — search 返回 Match 对象需 `.group()`，findall 直接返回列表
6. **正则 `\d` + `\.`** — `\d` 匹配数字，`\.` 转义点号（不加转义 `.` 是通配符）
7. **`git commit --amend`** — 修改最后一个 commit，需先 `git add` 新内容，只适用于未 push 的 commit
8. **Git 分支工作流** — `switch -c` 创建 → 改代码 → commit → `switch master` → `merge` → `branch -d`

###  ️ 遇到的坑
- `grep -oP` 最后的 `P` 是大写（Perl 正则），不是小写
- 管道命令 grep 后面不能同时跟文件名和管道输入 — 要么搜文件，要么读管道
- `git commit --amend` 不从工作区拿内容，只从暂存区拿 — 必须先 `git add`
- `git cheout` 是 typo，正确是 `git checkout`
- `echo "running" | grep -r` — `-r` 对 echo 没用，echo 只是输出文字，不是文件

### 📊 投入时间
- 学习：120 分钟
- 练习：90 分钟
- 复习：30 分钟
- **总计**：240 分钟

### 🎯 明天计划
- Python: 正则加深（re.sub 替换，match vs search）
- Linux: find + kill 实操
- Git: pull/fetch、merge 冲突模拟
- 实验：从日志提取 ERROR + IP 综合练习

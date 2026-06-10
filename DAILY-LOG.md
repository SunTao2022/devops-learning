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

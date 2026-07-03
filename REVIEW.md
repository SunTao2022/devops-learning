# 每日复习清单

> 每天学习前花 10 分钟过一遍。回答不上来的就是薄弱点，重点补。

---

## 优先级 1：核心铁律（必须滚瓜烂熟）

- [ ] `terraform destroy` 和 `az group delete` 的根本区别
- [ ] 为什么 Storage Account 必须独立 RG
- [ ] `count` vs `for_each` 的适用场景
- [ ] `each.key` / `each.value` / `count.index` 分别是什么
- [ ] 一个 Subnet 为什么只能绑一个 NSG
- [ ] Remote state backend 的四个配置项及其作用

---

## 优先级 2：实验验证（必须能手写/手跑）

- [ ] 把 compute module 从 `count` 改成 `for_each`
- [ ] 写一个 `dynamic "security_rule"` block 生成多端口规则
- [ ] `terraform init` 切 backend 的完整流程
- [ ] `git add` → `git commit` → `git push` 三步走
- [ ] `terraform fmt -recursive` 格式化整个项目

---

## 优先级 3：概念理解（能口述原理）

- [ ] Terraform module 的变量作用域（根目录 vs module）
- [ ] Module output 转发的两种方式
- [ ] `sensitive = true` 的作用和局限性
- [ ] Python `for` 和 Terraform `for_each` 的本质区别
- [ ] State lock 是怎么工作的（Blob lease）

---

## 优先级 4：细节查漏（看 STUDY-NOTES.md 对应章节）

- [ ] Git: stash / rebase / amend 的适用场景
- [ ] Python: `with open()` 三种模式的区别
- [ ] Azure CLI: VM 生命周期完整命令链
- [ ] Linux: `ps aux` 输出各列含义

---

## 使用方式

1. 每天先过一遍清单
2. 能立刻答/写的打 ✅
3. 卡壳的标记 ❌，当天重点补
4. 每周五更新这个清单，加入新学的内容

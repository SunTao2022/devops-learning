# DevOps/SRE 学习计划 · 目标 2027 年 4 月加拿大就业

> **学习者**：Tao（CCNP + AZ-104）
> **目标**：加拿大 DevOps / SRE / Cloud Admin 岗位
> **周期**：2026 年 6 月 — 2027 年 4 月（灵活，以学会为准，不赶进度）
> **每日投入**：≥4 小时（工作日 2.5h 学习 + 1.5h 实验，周末 6h 项目 + 复习）
> **休息**：每周日（避免 burnout）
> **AI 辅助**：Hermes Agent（主模型）
> **原则**：只学到能独立上手干活的深度。不追低频内容，不为覆盖而覆盖。每个新主题以"生产中用不用得到、用多深"决定投入时间。

---

## 目录

- [一、总体路线图](#一总体路线图)
- [二、第 1 月：Python + Linux + Git](#二第-1-月python--linux--git)
- [三、第 2 月：Terraform + Ansible + Azure Auth](#三第-2-月terraform--ansible--azure-auth)
- [四、后续（按进度灵活调整）](#四后续按进度灵活调整)
- [五、复习策略与实验指南](#五复习策略与实验指南)
- [六、推荐资源](#六推荐资源)

---

## 一、总体路线图

```
月 1 (6-7月)         月 2 (7-8月)         后续（按进度灵活调整）
┌──────────────┐    ┌──────────────────┐    ┌──────────────────┐
│ Python       │ →  │ Terraform        │ →  │ Docker / K8s     │
│ Linux        │    │ Ansible 概念     │    │ GitOps / CI/CD   │
│ Git          │    │ Azure Auth (SP)  │    │ 综合项目 / 面试   │
└──────────────┘    └──────────────────┘    └──────────────────┘
     ↓                      ↓                       ↓
  基础能力              IaC 能力              按进度灵活调整
```

---

## 二、第 1 月：Python + Linux + Git（基础夯实）

> **目标**：掌握 Python 基础语法、Linux 常用命令、Git 工作流，能独立编写 100+ 行脚本并提交至 GitHub
> **工具**：Git Bash（已有）、VS Code、Python 3.11.15（已有）、Git 2.54（已有）

### 每日节奏（工作日）

| 时间段 | 时长 | 内容 |
|--------|------|------|
| 0-30m  | 30m  | **学习**：新知识点 |
| 30-60m | 30m  | **练习**：我出题，你写代码，AI 批改 |
| 60-90m | 30m  | **Linux**：命令 + 实验 |
| 90-120m| 30m  | **Git**：工作流实操 |
| 120-150m|30m  | **实验**：当天综合练习 |
| 150-180m|30m  | **复习**：昨日的 3 个要点 + 今日笔记整理 |

### 第 1 周（6 月 8 日 — 6 月 13 日）：Python 基础

| 日期 | 学习内容 | 练习 | Linux | Git | 实验 | 达到目的 |
|------|---------|------|-------|-----|------|---------|
| **Day 1** (周一) | Python：变量、数据类型、字符串操作、input/output | 5 道基础题（变量交换、字符串反转、类型转换） | 了解文件系统结构（/、/home、~） | Git 安装验证、配置 user.name/user.email | 写一个 hello.py 接收输入并输出格式化结果，commit 到本地 repo | 掌握 Python 基本 IO 和 Git 初始化 |
| **Day 2** (周二) | Python：列表、元组、字典、集合 | 5 道题（列表去重、字典合并、切片操作） | pwd, ls, cd, mkdir, touch, rm（含 -rf 安全） | git init, git add, git commit, git status | 写一个脚本：读取当前目录所有文件，按扩展名分组统计 | 掌握 Python 容器类型和 Git 基础三连 |
| **Day 3** (周三) | Python：条件判断、循环（for/while） | 5 道题（FizzBuzz、素数判断、循环嵌套） | cat, less, head, tail, wc, sort, uniq | git log, git diff, git show | 写一个脚本：解析 CSV 文件，过滤并排序输出 | 掌握控制流逻辑 |
| **Day 4** (周四) | Python：函数定义、参数、返回值、作用域 | 5 道题（递归阶乘、可变参数、lambda） | grep, find, which, whereis | .gitignore 配置、git rm --cached | 将 Day 3 脚本重构为函数式，添加参数解析 | 掌握函数式组织和 .gitignore 管理 |
| **Day 5** (周五) | Python：文件操作（open/read/write/with）、异常处理 | 5 道题（读取配置文件、写入日志、try/except/finally） | chmod, chown, file, stat | git remote add, git push (首次 GitHub) | 写一个日志解析脚本：读取 .log 文件，提取 ERROR 级别条目 | 掌握文件 IO、异常处理和远程仓库推送 |
| **Day 6** (周六) | **周末综合项目** | — | 创建并推送 GitHub 仓库 | git clone, git remote -v, git push | **项目 1**：写一个 system_info.py — 收集 CPU/内存/磁盘信息，格式化输出为报告，push 到 GitHub | 综合运用 Python + Git |
| **Day 7** (周日) | **休息** | — | — | — | — | 恢复 |

### 第 2 周（6 月 15 日 — 6 月 20 日）：Python 进阶 + Linux 深入

| 日期 | 学习内容 | 练习 | Linux | Git | 实验 | 达到目的 |
|------|---------|------|-------|-----|------|---------|
| **Day 8** (周一) | Python：字符串格式化、正则表达式基础（re.match/search/findall） | 5 道正则题（提取 IP、邮箱验证、替换文本） | ps, top, kill, pgrep, pkill | git branch, git checkout, git switch | 写一个配置解析器：用正则从 nginx.conf 提取 server_name 和 listen | 掌握正则表达式 |
| **Day 9** (周二) | Python：模块和包、import 机制、sys/os 模块 | 写一个自己的模块（utils.py）供其他脚本导入 | df, du, free, uptime, who | git merge, git merge --no-ff | 重构上周末的 system_info.py，拆分成多模块 | 理解模块化编程 |
| **Day 10** (周三) | Python：subprocess 模块（运行系统命令并捕获输出） | 用 subprocess 调用 3 个 Linux 命令 | systemctl, service, journalctl | 解决合并冲突（模拟多人协作场景） | 写一个服务管理脚本：systemctl status/start/stop 任意服务 | 掌握 Python 调用系统命令 |
| **Day 11** (周四) | Python：argparse 命令行参数解析 | 为上周脚本添加命令行参数（--verbose, --output-format） | ssh, scp, ssh-keygen, ssh-copy-id | .gitignore 高级用法、README.md 编写 | 写一个 SSH 批量管理脚本：读取 hosts.txt，对每个主机执行命令 | 掌握 CLI 工具开发规范 |
| **Day 12** (周五) | Python：pip 包管理、虚拟环境（venv） | pip install requests, 写一个 HTTP GET 请求 | curl, wget, nc, telnet（基础用法） | git push to GitHub, git pull, git fetch | 写一个 API 健康检查脚本：用 requests 检查 URL 返回码 | 掌握 Python 包管理和网络请求 |
| **Day 13** (周六) | **周末综合项目** | — | — | PR 流程：fork → branch → commit → PR → review → merge | **项目 2**：写一个 azure-vm-checker.py — 调用 Azure CLI（subprocess）列出 VM 状态，输出为表格报告，完整 PR 流程演示 | 综合 Python + Azure CLI + Git PR |
| **Day 14** (周日) | **休息** | — | — | — | — | 恢复 |

### 第 3 周（6 月 22 日 — 6 月 27 日）：Linux 深入 + Git 进阶

| 日期 | 学习内容 | 练习 | Linux | Git | 实验 | 达到目的 |
|------|---------|------|-------|-----|------|---------|
| **Day 15** (周一) | Linux：用户和权限管理（/etc/passwd, /etc/group, useradd/usermod） | 创建用户、分配权限、测试 su/sudo | 用户管理全流程 | git stash, git stash pop, git stash list | 写一个用户审计脚本：列出所有用户及其所属组 | 掌握 Linux 用户管理 |
| **Day 16** (周二) | Linux：进程管理（ps aux, top, htop, nice, renice, nohup） | 前后台任务管理（&, fg, bg, jobs） | 进程控制 | git tag, git describe, 语义化版本 | 写一个进程监控脚本：按 CPU 排序，杀死占用最高的进程 | 掌握进程管理 |
| **Day 17** (周三) | Linux：文件权限深入（chmod 数字/符号模式、umask、ACL） | 10 种权限场景练习 | setuid/setgid/sticky bit | git rebase（交互式 rebase, squash） | 写一个文件权限审计脚本：找出所有 setuid 文件 | 深入理解文件权限和安全 |
| **Day 18** (周四) | Linux：Shell 脚本基础（变量、条件、循环、函数） | 写 3 个 shell 脚本（备份、监控、清理） | 脚本调试（bash -x, set -e, trap） | git cherry-pick, git revert | 写一个 cron 备份脚本，每天自动打包日志 | 掌握 Shell 脚本基础 |
| **Day 19** (周五) | Linux：网络配置（ip addr, ip route, ss, nmcli, resolv.conf） | 排查网络连通性问题 | tcpdump 基础 | git worktree, git submodule | 写一个网络诊断脚本：测试多个端口连通性并记录 | 掌握 Linux 网络排障 |
| **Day 20** (周六) | **周末综合项目** | — | — | Git Flow 工作流 | **项目 3**：写一个完整的 Shell + Python 混合脚本：自动检测系统健康（CPU/内存/磁盘/网络），生成 HTML 报告并推送到 GitHub Pages | 综合 Shell + Python + Git Pages |
| **Day 21** (周日) | **休息** | — | — | — | — | 恢复 |

### 第 4 周（6 月 29 日 — 7 月 4 日）：巩固 + 月测验

| 日期 | 学习内容 | 复习 | 实验 | 达到目的 |
|------|---------|------|------|---------|
| **Day 22** (周一) | Python：综合练习（LeetCode 简单 3 道） | 上周所有 Linux 命令 | 用 Python 写一个 Azure VM 批量启动/停止脚本（az vm start/stop） | 巩固 Python 和 Azure CLI 整合 |
| **Day 23** (周二) | Python：综合练习（文件处理 + 正则全套） | 上周所有 Git 操作 | 写一个日志轮转脚本：压缩旧日志，保留最近 7 天 | 巩固文件处理和正则 |
| **Day 24** (周三) | Shell 脚本进阶：getopt、信号处理、并发（& + wait） | Python 全部容器类型和函数 | 写一个并行 SSH 执行脚本：同时对多台主机执行命令 | 巩固 Shell 并发控制 |
| **Day 25** (周四) | Azure CLI 自动化（az login, az group, az vm, az network） | Git 分支策略 | 用 az CLI 创建完整资源组 + VNet + VM 环境 | 巩固 Azure 资源管理 |
| **Day 26** (周五) | **月测验**：限时 2 小时（Python 脚本 2 题 + Shell 1 题 + Git 1 题） | 整个月的内容回顾 | 测验 + 批改 | 检验一个月学习成果 |
| **Day 27** (周六) | **月项目验收**：优化之前所有项目代码 | 整理笔记 | 将所有代码重构、加注释、完善 README、统一 repo 结构 | 形成规范的 GitHub 作品仓 |
| **Day 28** (周日) | **休息** | — | — | 恢复 |

### 第 1 月达到的里程碑 ✅

- [ ] 能独立写 150+ 行 Python 脚本（含函数、异常、文件操作）
- [ ] 熟悉 30 个核心 Linux 命令
- [ ] 掌握 Git 完整工作流（add/commit/push/branch/merge/rebase/PR）
- [ ] 有 3+ 个 GitHub 仓库（学习笔记 + 小项目）
- [ ] 会使用 Azure CLI 进行基础资源管理

---

## 三、第 2 月：Terraform + Ansible + Azure Auth（IaC 入门）

> **目标**：掌握 Terraform 声明式基础设施管理；Ansible 了解概念即可，不深入；为 Kubernetes 和 GitOps 打基础
> **工具**：Terraform、Azure 订阅、Docker、kubectl

### 第 5 周：Terraform 基础

| 日期 | 学习内容 (1h) | 实验 (1.5h) | Git 操作 | 复习 |
|------|-------------|------------|---------|------|
| 周一 | Terraform 安装、HCL 语法、provider 配置 | 初始化 terraform init，创建第一个 resource group | 新建 terraform-learning 仓库 | 复习 Python 函数 |
| 周二 | resource / data source / variable / output | 创建 Azure VNet + subnet，使用变量 | terraform fmt, .gitignore for .tfstate | Linux grep/awk |
| 周三 | state 管理（local → Azure Storage backend） | 配置 remote state，state lock | gitignore tfstate 更新 | Git rebase |
| 周四 | 模块化（module 定义和复用） | 创建 vnet 模块、vm 模块 | git submodule 或 terraform registry | Shell 函数 |
| 周五 | terraform plan / apply / destroy 工作流 | 完整部署：RG → VNet → VM → destroy | 写 Makefile 封装常用命令 | Python subprocess |
| 周六 | **周末项目**：用 Terraform 部署 2 台 VM（含 NSG、负载均衡器） | — | README + 架构图 | — |
| 周日 | 休息 | — | — | — |

|### 第 6 周：Ansible 概念（半天）+ Azure Auth（1 天）
> **Ansible 目标**：理解核心概念，能读懂简单 playbook，不深入
> **Azure Auth 目标**：掌握 Service Principal + RBAC，让 Terraform 能脱离本地 `az login` 运行
> **说明**：Ansible 压缩为半天概念阅读；增加 Azure 认证实践，为 CI/CD pipeline 打基础

| 日期 | 学习内容 | 实验 | Git 操作 | 复习 |
|------|---------|------|---------|------|
| 周一（半天） | Ansible：inventory / playbook / module / task / handler | 读一个完整 playbook（Nginx 部署），理解每行意思 | 无 | Terraform 模块变量传递 |
| 周二 | Azure Auth：Service Principal 创建、RBAC 角色分配 | 创建 SP + 分配 Contributor 角色 + 测试 `az login --service-principal` | secrets/ 文件夹 + .gitignore | Terraform state 管理 |
| 周三 | Terraform 用 SP 认证、Provider 传 client_id/secret | 把 SP 信息写入 terraform.tfvars（不进 git），跑 terraform plan 验证 | 无 | Linux 用户权限 |
| 周四 | Managed Identity：VM 免密访问 Azure 资源 | 在 Terraform VM 上启用 MI，测试 VM 内直接用 az CLI 列出资源 | 无 | Service Principal 原理 |
| 周五 | RBAC 细化：自定义角色、最小权限、scope 层级 | 创建自定义角色（只读 VM），分配给 SP 并测试 | 无 | 复习本周全部 |
| 周六 | **周末项目**：用 SP 认证的 Terraform 完整部署 2 台 VM + destroy | — | 项目的 README + 架构 | — |
| 周日 | 休息 | — | — | — |

### 第 7 周：Docker + 服务器管理

| 日期 | 学习内容 | 实验 | 复习 |
|------|---------|------|------|
| 周一 | Docker：image / container / Dockerfile / docker-compose | 写 Dockerfile 部署 Nginx + 自定义页面 | Service Principal 三要素 |
| 周二 | Docker 网络 / volume / 多阶段构建 | docker network / docker volume / 优化镜像 | Terraform module |
| **周三** | **服务器管理：nginx/systemd/包管理/日志** | **配置 nginx 反向代理 + systemd 管理服务** | **社区推荐 — 填补工具链空缺** |
| 周四 | GitOps 概念：ArgoCD 架构、声明式部署 | 部署 ArgoCD（Docker Compose） | 初始化 GitOps repo |
| 周五 | ArgoCD：Application / Sync / Health / Auto-heal | 写 ArgoCD Application 自动同步 GitHub → K8s | GitOps 核心概念 |
| 周六 | **周末项目**：Docker + ArgoCD 部署 Nginx | — | 完整项目交付 |
| 周日 | 休息 | — | — |

### 第 8 周：Kubernetes 核心（CKA 标准）

> **注**：按 CKA（Certified Kubernetes Administrator）标准学。目标是能**独立排障**，不是"能看懂 YAML"
> CKA 考试本身可选，但学习标准按它来

| 日期 | 学习内容 | 实验 | 复习 |
|------|---------|------|------|
| 周一 | K8s 架构、Pod、kubectl 核心命令 | 部署第一个 Pod + 排查故障场景 | Dockerfile |
| 周二 | Deployment、Service（ClusterIP/NodePort/LB） | 部署完整应用 + 暴露外部访问 | nginx 配置 |
| 周三 | ConfigMap / Secret / Ingress / PVC | 配置管理 + 外部路由 + 持久化 | K8s 核心对象 |
| 周四 | Helm 基础 + 故障排查（logs/exec/describe） | 用 Helm 部署应用 + 模拟故障排查 | CKA 考试模式 |
| 周五 | 复习 + 综合场景练习 | 从零部署完整 WordPress + MySQL | 知识体系梳理 |
| 周六 | **周末项目**：K8s 上部署高可用应用 | — | 项目展示 |
| 周日 | 休息 | — | — |

### 第 9 周：CI/CD + GitOps 深度

| 日期 | 学习内容 | 实验 | 复习 |
|------|---------|------|------|
| 周一 | GitHub Actions 概念（Workflow/Job/Step/Runner） | 写第一个 workflow | K8s 排障 |
| 周二 | Actions 触发事件 + Secrets + Matrix | 配置多环境触发 | Terraform state |
| 周三 | Terraform CI/CD：plan on PR, apply on merge | Actions 中运行 TF | Service Principal |
| 周四 | 多环境管理（dev/staging/prod） | Terraform workspace | Git 分支策略 |
| 周五 | 审批门 + 安全扫描（Trivy） | PR → plan → approve → apply → deploy | RBAC |
| 周六 | **周末项目**：完整 CI/CD pipeline | — | — |
| 周日 | 休息 | — | — |

### 第 10 周：监控 + DevSecOps

| 日期 | 学习内容 | 实验 | 复习 |
|------|---------|------|------|
| 周一 | Prometheus 架构 + node_exporter | 部署 Prometheus + 采集指标 | Docker 网络 |
| 周二 | PromQL 基础（rate/irate/histogram） | 编写 CPU/内存告警规则 | K8s Service |
| 周三 | Grafana 面板 | 导入 Node Exporter 面板 | 监控指标含义 |
| 周四 | Alertmanager（告警路由 + 通知） | 配置告警通知 | PromQL |
| **周五** | **DevSecOps：Trivy 容器扫描 / Key Vault / 最小权限** | **扫描镜像 + 修复高风险漏洞** | **社区推荐** |
| 周六 | **周末项目**：完整监控栈（Prometheus + Grafana + Alertmanager） | — | — |
| 周日 | 休息 | — | — |

### 第 11-12 周：Azure 网络深入 + 综合项目

> **差异化路线**：你的 CCNP + 本项目 = 面试王牌。候选人里懂 K8s 的人多，懂 K8s 又懂网络架构的人少

| 周 | 内容 | 实验 |
|----|------|------|
| 第 11 周 | Azure VNet peering / VPN Gateway / Load Balancer / 流量架构 | 从 CCNP 视角设计 Azure 网络，文档化对比 |
| 第 12 周 | **端到端综合项目**：TF → CI/CD → K8s → 监控 | GitHub 完整项目 + 架构图 + README |

### 第 13-16 周：面试准备 + 求职

| 周 | 内容 | 产出 |
|----|------|------|
| 第 13 周 | DevOps 面试题库（50+ 问答） | 复习笔记 |
| 第 14 周 | STAR 故事 + 简历 + LinkedIn | 最终版简历 |
| 第 15 周 | 模拟面试（3 轮） | 录屏复盘 |
| 第 16 周 | 投递（每日 5-10） | 收到面试通知 |

---

## 五、复习策略与实验指南

### 每日复习机制

```
每天最后 30 分钟：
1. 翻看今日写的代码（5 分钟）
2. 回答 3 个随机知识点（10 分钟）
3. 整理到学习笔记 / Anki（10 分钟）
4. 写下明日目标（5 分钟）
```

### 每周复习

| 环节 | 内容 | 时间 |
|------|------|------|
| 周中快速回顾 | 周三晚 15 分钟回顾前几天内容 | 周三 |
| 周末深度复习 | 周六整理本周所有笔记和代码 | 周六 |
| 错误复盘 | 记录本周调试中遇到的 3 个坑 | 周六 |

### 实验日志模板

每个实验在 GitHub 的 `experiments/` 目录下记录：

```markdown
# 实验名称

## 日期
YYYY-MM-DD

## 目标
实验中要验证/学习的内容

## 步骤
1. ...
2. ...

## 结果
- 成功/失败/部分成功
- 关键输出

## 遇到的坑 & 解决方案
- 问题：...
- 原因：...
- 解决：...

## 关键命令/代码片段
```bash
command here
```
```

### AI 辅助使用原则

| 场景 | 如何使用 AI |
|------|-----------|
| 学习新概念 | AI 解释 + 生成示例代码 |
| 调试错误 | 贴错误信息让 AI 分析 |
| 代码 Review | 写完代码让 AI review 并优化 |
| 生成实验模板 | AI 生成脚本框架 |
| 面试准备 | AI 模拟面试官提问 |
| **禁止** | 让 AI 完全代写而不理解代码含义 |

---

## 六、推荐资源

### 学习平台

| 资源 | 用途 | 链接 |
|------|------|------|
| Microsoft Learn | Azure 官方教程 | learn.microsoft.com |
| Terraform 官方文档 | 权威参考 | developer.hashicorp.com/terraform |
| Ansible 官方文档 | 权威参考 | docs.ansible.com |
| Kubernetes 官方文档 | 权威参考 | kubernetes.io/docs |
| GitHub Actions 文档 | 权威参考 | docs.github.com/actions |

### 认证（可选，加分项）

| 认证 | 建议时间 | 说明 |
|------|---------|------|
| AZ-104（已有） | — | 保持有效 |
| Terraform Associate | 第 2 月后 | 有助简历筛选 |
| CKAD（K8s） | 第 3 月后 | 加分项 |
| CCNP（已有） | — | 网络基础加分 |

### 社区

- **Reddit**: r/devops, r/kubernetes, r/Terraform
- **Meetup**: Toronto DevOps / Kubernetes / Azure 线下聚会
- **Discord**: Kubernetes, Terraform 官方频道
- **YouTube**: Techno Tim, NetworkChuck, DevOps Directive

---

## 附录：每日打卡模板

将以下内容复制到每天的 `DAILY-LOG.md`：

```markdown
## Day N — YYYY-MM-DD

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
- 实验：___ 分钟
- 复习：___ 分钟
- **总计**：___ 分钟

### 🎯 明日计划
- ________________________________
```

---

> **最后的话**：这份计划是路线图，不是枷锁。每周末回顾一次进度，根据实际情况调整节奏。重要的不是完美执行每一天，而是持续前进 6 个月不停。
>
> 你已经有 CCNP 和 AZ-104 两张硬牌，加上 6 个月的系统学习和一个有深度的项目，在加拿大 DevOps 就业市场会有竞争力的。开始行动吧。

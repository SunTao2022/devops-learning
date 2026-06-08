# DevOps/SRE 学习计划 · 6 个月冲刺加拿大就业

> **学习者**：Tao（CCNP + AZ-104）
> **目标**：加拿大 DevOps / SRE / Cloud Admin 岗位
> **周期**：2026 年 6 月 — 11 月（6 个月）
> **每日投入**：≥4 小时（工作日 2.5h 学习 + 1.5h 实验，周末 6h 项目 + 复习）
> **休息**：每周日（避免 burnout）
> **AI 辅助**：DeepSeek V4（主模型）+ Gemma4:12b（本地副手）

---

## 目录

- [一、总体路线图](#一总体路线图)
- [二、第 1 月：Python + Linux + Git（基础夯实）](#二第-1-月python--linux--git基础夯实)
- [三、第 2 月：Terraform + Ansible（IaC 入门）](#三第-2-月terraform--ansibleiac-入门)
- [四、第 3 月：Docker + Kubernetes（容器化）](#四第-3-月docker--kubernetes容器化)
- [五、第 4 月：CI/CD + 多环境 + 监控](#五第-4-月cicd--多环境--监控)
- [六、第 5 月：综合项目实战](#六第-5-月综合项目实战)
- [七、第 6 月：面试准备 + 求职冲刺](#七第-6-月面试准备--求职冲刺)
- [八、复习策略与实验指南](#八复习策略与实验指南)
- [九、推荐资源](#九推荐资源)

---

## 一、总体路线图

```
月 1 (6月)         月 2 (7月)         月 3 (8月)         月 4 (9月)        月 5 (10月)        月 6 (11月)
┌──────────┐      ┌──────────┐      ┌──────────┐      ┌──────────┐      ┌──────────┐      ┌──────────┐
│ Python   │ ──→  │Terraform │ ──→  │ Docker   │ ──→  │ CI/CD    │ ──→  │ 综合项目  │ ──→  │ 简历优化  │
│ Linux    │      │ Ansible  │      │ K8s      │      │ 监控     │      │ 多环境   │      │ 模拟面试  │
│ Git      │      │ 基础实验  │      │ 容器编排  │      │ 可观测性  │      │ 端到端   │      │ 求职投递  │
└──────────┘      └──────────┘      └──────────┘      └──────────┘      └──────────┘      └──────────┘
     ↓                  ↓                  ↓                  ↓                  ↓                  ↓
 基础能力           IaC 能力          容器化能力         自动化能力         项目作品集           求职成功
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

## 三、第 2 月：Terraform + Ansible（IaC 入门）

> **目标**：掌握 Terraform 声明式基础设施管理和 Ansible 配置管理，能用 IaC 在 Azure 上部署完整环境
> **工具**：Terraform、Ansible、Azure 订阅

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

### 第 6 周：Ansible 基础

| 日期 | 学习内容 (1h) | 实验 (1.5h) | Git 操作 | 复习 |
|------|-------------|------------|---------|------|
| 周一 | Ansible 架构、inventory（静态/动态）、ad-hoc 命令 | ansible ping all，用 ad-hoc 安装 nginx | 新建 ansible-learning 仓库 | Terraform 状态管理 |
| 周二 | playbook 基础（hosts, tasks, module） | 写 playbook：安装 nginx + 启动 + 配置网页 | 仓库结构规范化 | Linux systemctl |
| 周三 | variable（group_vars, host_vars）、template（Jinja2） | 用 Jinja2 模板生成 nginx 配置 | .gitignore for ansible | Python 字符串格式化 |
|周四 | handler、notify、tag、when 条件判断 | 配置防火墙规则 + 重启服务 | playbook 语法 lint（ansible-lint） | 正则表达式 |
| 周五 | roles（角色化、ansible-galaxy） | 重构为 roles：common, webserver, firewall | galaxy.yml | Git stash |
| 周六 | **周末项目**：用 Ansible 配置 2 台 VM，安装 Nginx + 自定义页面 + 防火墙 | — | ansible.cfg 优化 | — |
| 周日 | 休息 | — | — | — |

### 第 7 周：Terraform + Ansible 集成

| 日期 | 学习内容 | 实验 | 达到目的 |
|------|---------|------|---------|
| 周一 | Terraform 输出 → Ansible inventory（local_file + template） | Terraform 生成 inventory 文件 | 打通 IaC 工具链 |
| 周二 | Ansible 动态 inventory（azure_rm.py/azure_rm.yml） | 配置 Azure 动态 inventory | 掌握动态资源发现 |
| 周三 | Terraform provisioner（remote-exec, file）vs Ansible 对比 | 对比分析两种配置方式 | 理解工具边界 |
| 周四 | 错误处理：Terraform 错误重试、Ansible 幂等性 | 制造断网/资源冲突场景并修复 | 掌握 IaC 排障 |
| 周五 | 安全实践：Terraform 敏感变量、Ansible Vault | 用 Vault 加密 secrets | 掌握密钥管理 |
| 周六 | **周末项目**：Terraform 部署 → Ansible 配置，完整端到端 | — | IaC 全流程跑通 |
| 周日 | 休息 | — | 恢复 |

### 第 8 周：复习 + 月底项目

> **项目交付**：用 Terraform 部署 Azure 环境（VNet + 2 VM + LB），Ansible 配置 Nginx 集群，展示负载均衡效果

### 第 2 月达到的里程碑 ✅

- [ ] 能用 Terraform 创建完整的 Azure 基础设施
- [ ] 能用 Ansible 完成服务器配置管理
- [ ] 掌握 Terraform + Ansible 集成（静态/动态 inventory）
- [ ] 理解 IaC 的最佳实践（状态管理、模块化、密钥安全）
- [ ] GitHub 上有结构良好的 IaC 项目仓库

---

## 四、第 3 月：Docker + Kubernetes（容器化）

> **目标**：掌握容器化技术，能用 Docker 打包应用并用 K8s 编排部署
> **工具**：Docker Desktop（无Hyper-V模式）、Minikube/Kind、kubectl、Helm

### 第 9 周：Docker 基础

| 日期 | 学习内容 (1h) | 实验 (1.5h) |
|------|-------------|------------|
| 周一 | Docker 架构（image/container/registry）、安装 | docker pull/run/ps/stop/rm |
| 周二 | Dockerfile 编写（FROM, RUN, COPY, CMD, ENTRYPOINT） | 将 第1月的 Python 脚本打包为镜像 |
| 周三 | Docker 网络（bridge/host/none, port mapping） | 部署 nginx 容器，映射端口，测试连通性 |
| 周四 | Docker 数据持久化（volume, bind mount） | MySQL 容器 + 持久化数据 |
| 周五 | Docker Compose 编排多容器 | 写 docker-compose.yml：web + db + cache |
| 周六 | **周末项目**：Python Flask + Redis 应用容器化，docker-compose 一键部署 | — |
| 周日 | 休息 | — |

### 第 10 周：Kubernetes 基础

| 日期 | 学习内容 | 实验 |
|------|---------|------|
| 周一 | K8s 架构（Master/Node, Pod, Service, Deployment） | 安装 Minikube（或 Kind），kubectl 基础命令 |
| 周二 | Pod + Deployment（声明式 YAML） | 部署 nginx deployment，暴露为 service |
| 周三 | Service（ClusterIP, NodePort, LoadBalancer） | 配置 Ingress，测试路由 |
| 周四 | ConfigMap + Secret | 将配置从镜像中解耦 |
| 周五 | 存储（PVC, PV, StorageClass） | 为 WordPress 配置持久存储 |
| 周六 | **周末项目**：部署一个完整的 LEMP（Linux + Nginx + MySQL + PHP）在 Minikube 上 | — |
| 周日 | 休息 | — |

### 第 11 周：K8s 进阶

| 日期 | 学习内容 | 实验 |
|------|---------|------|
| 周一 | 健康检查（liveness, readiness, startup probe） | 为所有 deployment 配置健康检查 |
| 周二 | 滚动更新 + 回滚（RollingUpdate, maxSurge, maxUnavailable） | 模拟版本更新并回滚 |
| 周三 | HPA（Horizontal Pod Autoscaler） | 用压测触发自动扩容 |
| 周四 | Namespace + RBAC | 创建多租户环境 |
| 周五 | Helm 包管理（chart 结构、模板、发布） | 将第 9 周的 Flask 应用打包为 Helm chart |
| 周六 | **周末项目**：Helm chart 发布到 GitHub Pages | — |
| 周日 | 休息 | — |

### 第 12 周：容器化项目集成

> **项目交付**：用 Docker 打包 IaC 项目中部署的应用，在 Minikube 上运行，Helm 管理发布

### 第 3 月达到的里程碑 ✅

- [ ] 能写 Dockerfile 和 docker-compose.yml
- [ ] 能在 Minikube 上部署多容器应用
- [ ] 掌握 kubectl 常用命令和 YAML 定义
- [ ] 理解 K8s 核心概念（Pod/Deployment/Service/ConfigMap/Secret/PVC）
- [ ] 能用 Helm 管理应用发布

---

## 五、第 4 月：CI/CD + 多环境 + 监控

> **目标**：配置完整的 CI/CD 流水线，搭建监控栈，实现端到端自动化
> **工具**：GitHub Actions、Prometheus + Grafana、Azure Monitor

### 第 13 周：GitHub Actions 基础

| 日期 | 学习内容 | 实验 |
|------|---------|------|
| 周一 | GitHub Actions 概念（Workflow, Job, Step, Runner） | 写第一个 workflow：echo Hello World |
| 周二 | Trigger 事件（push, pull_request, schedule, workflow_dispatch） | 配置多种 trigger |
| 周三 | Matrix build、环境变量、Secrets | 多版本 Python 测试 |
| 周四 | Artifact + Cache（actions/upload-artifact, actions/cache） | 加速依赖安装 |
| 周五 | 自托管 Runner（在本地或 Azure VM 上部署） | 配置 self-hosted runner |
| 周六 | **周末项目**：Python 项目 CI（lint + test + build + push Docker） | — |
| 周日 | 休息 | — |

### 第 14 周：CI/CD 完整流水线

| 日期 | 学习内容 | 实验 |
|------|---------|------|
| 周一 | Terraform CI/CD：plan on PR, apply on merge | GitHub Actions 中运行 terraform plan/apply |
| 周二 | Ansible CI/CD：在 Actions 中触发 Ansible playbook | SSH key 管理 + ansible-playbook |
| 周三 | 多环境（dev/staging/prod）：Terraform workspace | 每个环境独立 state 和变量 |
| 周四 | 安全扫描：Trivy（容器镜像）、Checkov（IaC 安全） | 在 pipeline 中加入安全检查 |
| 周五 | 审批门（environment protection rule、手动审批） | staging → prod 需要 review 才 deploy |
| 周六 | **周末项目**：完整 CI/CD 流水线：push → test → build → deploy | — |
| 周日 | 休息 | — |

### 第 15 周：监控与可观测性

| 日期 | 学习内容 | 实验 |
|------|---------|------|
| 周一 | Prometheus 架构 + node_exporter | 部署 Prometheus + node_exporter |
| 周二 | PromQL 基础（查询、聚合、rate/irate） | 编写 CPU/内存/磁盘告警规则 |
| 周三 | Grafana 面板（dashboard 创建和模板） | 导入 Node Exporter Full 面板 |
| 周四 | Alertmanager（告警路由、接收器、静默） | 配置 Email/Webhook 通知 |
| 周五 | Azure Monitor（指标、日志 Analytics、告警） | 配置 Azure VM 监控告警 |
| 周六 | **周末项目**：搭建完整监控栈（Prometheus + Grafana + Alertmanager） | — |
| 周日 | 休息 | — |

### 第 16 周：复习 + 月项目

> **项目交付**：GitHub Actions 完整 CI/CD + 监控栈集成。代码 push → 自动部署到 Azure → Prometheus 采集指标 → Grafana 展示

### 第 4 月达到的里程碑 ✅

- [ ] 能写完整的 GitHub Actions workflow
- [ ] Terraform + Ansible 在 CI/CD 中自动运行
- [ ] 理解多环境管理和部署策略
- [ ] 部署 Prometheus + Grafana + Alertmanager
- [ ] 能用 PromQL 查询指标

---

## 六、第 5 月：综合项目实战

> **目标**：构建一个可展示在 GitHub 和简历上的完整 DevOps 项目
> **项目名称**：`azure-devops-showcase` — Azure 全自动化部署流水线

### 项目架构

```
用户 push 代码
     ↓
GitHub Actions CI/CD
     ├── static analysis (lint + security scan)
     ├── terraform plan/apply (dev/staging/prod)
     ├── ansible configure servers
     ├── build & push Docker images
     └── deploy to Kubernetes
     ↓
Azure 基础设施
     ├── VNet + subnets + NSG
     ├── AKS cluster (或 VMSS)
     ├── Azure Database (MySQL/PostgreSQL)
     ├── Azure Storage + CDN
     └── Application Gateway / Load Balancer
     ↓
监控栈
     ├── Prometheus (Azure VM 或 AKS)
     ├── Grafana dashboards
     ├── Alertmanager (email + slack webhook)
     └── Azure Monitor (alerts + logs)
```

### 第 17-18 周：项目骨架搭建

- 设计 Git 仓库结构
- Terraform 编写完整 Azure 基础设施（module 化）
- Ansible roles 编写系统 baseline
- 基础 pipeline 配置（plan/apply/lint）

### 第 19-20 周：项目功能完善

- Docker 化应用服务
- K8s manifests 编写
- Helm chart 化
- Prometheus + Grafana 集成到项目
- CI/CD 流水线 end-to-end 验证

### 第 5 月达到的里程碑 ✅

- [ ] GitHub 上有完整的 `azure-devops-showcase` 项目
- [ ] 项目的 README 包含架构图、部署说明、视频演示
- [ ] CI/CD 流水线覆盖代码检查 → IaC → 部署全过程
- [ ] 监控和告警覆盖所有关键组件
- [ ] 项目可直接在面试中展示

---

## 七、第 6 月：面试准备 + 求职冲刺

> **目标**：简历优化、面试题库、模拟面试、开始投递
> **注意**：此月需并行推进以下所有板块

### 第 21 周：简历 + LinkedIn 优化

| 任务 | 具体内容 | 产出 |
|------|---------|------|
| 简历重写 | STAR 法则描述项目经验 | v2.0 简历 PDF |
| LinkedIn 优化 | Headline, About, Skills, Featured project | 完整 LinkedIn 主页 |
| GitHub Profile | 完善个人 README，pin 项目仓库 | 专业的 GitHub 首页 |

### 第 22 周：技术面试题库

| 领域 | 准备内容 | 参考资源 |
|------|---------|---------|
| Python | LeetCode 简单（数组、字符串、哈希表） | Neetcode 150 |
| Linux | 常见命令、排障场景、Shell 脚本 | Linux Journey |
| Terraform | state 管理、模块设计、remote backend | TF 认证指南 |
| Ansible | playbook 设计、roles、Vault | Ansible 官方文档 |
| Docker/K8s | Dockerfile 优化、K8s 排障 | CKAD 模拟题 |
| Azure | VNet、LB、VMSS、AKS 场景题 | AZ-104 复习资料 |
| CI/CD | pipeline 设计、部署策略 | GitHub Actions 文档 |
| SRE | SLI/SLO、故障排查、容量规划 | Google SRE 书籍 |
| 网络 | DNS、TCP/IP、HTTP、负载均衡 | CCNP 知识回顾 |

### 第 23 周：场景面试 + 系统设计

| 日期 | 内容 | 形式 |
|------|------|------|
| 周一 | 系统设计：设计一个 Web 高可用架构 | 画图 + 讲解 |
| 周二 | 排障面试：CI/CD 失败排查流程 | 口述思路 |
| 周三 | 场景面试：Terraform state 被锁定如何解除 | 口述 + 演示 |
| 周四 | 场景面试：Pod CrashLoopBackOff 排查 | 口述 + 演示 |
| 周五 | 场景面试：生产环境 CPU 飙高如何排查 | 口述 |
| 周六 | 模拟面试 1（完整 45 分钟） | 录屏复盘 |
| 周日 | 休息 | — |

### 第 24 周：求职投递 + 持续面试

| 任务 | 具体行动 |
|------|---------|
| 平台注册 | LinkedIn, Indeed, Glassdoor, Job Bank, Robert Half |
| 目标岗位 | Cloud Admin, DevOps Engineer, SRE, Automation Engineer |
| 每日投递 | 每天投 5-10 个岗位，记录进展 |
| 持续学习 | 刷题 + 面试复盘 |
| 人脉拓展 | Toronto DevOps Meetup, LinkedIn 加 HR/猎头 |
| 合同岗位 | 关注 contract 机会（更快入门） |

### 第 6 月达到的里程碑 ✅

- [ ] 简历和 LinkedIn 通过朋友/社区 review
- [ ] 技术面试题库覆盖 80% 常见问题
- [ ] 完成 5+ 次模拟面试
- [ ] 已投递 50+ 个岗位
- [ ] 收到面试通知开始实战

---

## 八、复习策略与实验指南

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

## 九、推荐资源

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

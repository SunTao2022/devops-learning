# DevOps 知识图谱 · 完整版

> **学习者**：Tao（CCNP + AZ-104）  
> **目标**：加拿大 DevOps / SRE / Cloud Admin 岗位  
> **生成日期**：2026-07-18

---

## 总览

```text
                               ┌──────────────────┐
                               │  Git（版本管理）   │
                               └────────┬─────────┘
                                        │
                    ┌───────────────────┼────────────────────┐
                    ▼                   ▼                    ▼
          ┌──────────────────┐ ┌──────────────────┐ ┌──────────────────┐
          │ Python + Shell   │ │     Linux        │ │   Networking     │
          │ （脚本自动化）    │ │  （系统操作）     │ │   （CCNP 已有）   │
          └──────────────────┘ └──────────────────┘ └──────────────────┘
                    │                                      │
                    ▼                                      │
          ┌──────────────────┐                             │
          │    Terraform     │◄────────────────────────────┘
          │    （IaC）       │
          └────────┬─────────┘
                   │
                   ▼
          ┌──────────────────┐
          │     Docker       │
          │  （容器化打包）   │
          └────────┬─────────┘
                   │
                   ▼
          ┌──────────────────┐
          │   Kubernetes     │
          │  （容器编排）     │
          └────────┬─────────┘
                   │
          ┌────────┴────────┐
          ▼                  ▼
   ┌──────────────┐   ┌──────────────┐
   │   CI/CD      │   │    监控      │
   │ (GitHub      │   │ (Prometheus  │
   │  Actions)    │   │  + Grafana)  │
   └──────────────┘   └──────────────┘
```

---

## 完整知识图谱

### 🔴 精通层级（面试高频，必须独立操作）

```
Layer 1：基础
├── Git
│   ├── ✅ init / add / commit / push / pull
│   ├── ✅ branch / merge
│   ├── ✅ status / log
│   ├── ❌ stash / rebase / amend（低频）
│   └── ❌ .gitignore 规则细化（需要时查）
│
├── Python
│   ├── ✅ 变量/类型/字符串/列表/字典
│   ├── ✅ 条件/循环/函数
│   ├── ✅ 文件读写/异常处理
│   ├── ✅ subprocess 调用系统命令
│   ├── ✅ argparse 参数解析
│   ├── ✅ modules / import / __init__.py
│   └── ❌ pytest 单元测试（待补）
│
├── Shell / Linux
│   ├── ✅ 基本命令（ls/cd/mkdir/grep/ps/top）
│   ├── ✅ 管道/重定向/变量
│   ├── ✅ Shell 脚本基础
│   └── ❌ sed/awk 进阶（需要时查）
│
└── Networking（CCNP）
    └── ✅ 完整知识体系
```

```
Layer 2：Terraform
├── ✅ provider / resource / variable / output
├── ✅ terraform init / plan / apply / destroy
├── ✅ state（local → remote backend）
├── ✅ module（定义 + 复用 + 变量转发）
├── ✅ count / for_each / dynamic block
├── ✅ lifecycle（prevent_destroy）
├── ✅ sensitive / terraform.tfvars
├── ✅ data source
└── ❌ provisioner（社区不推荐，跳过）
```

```
Layer 3：Docker
├── ✅ Dockerfile（FROM / COPY / RUN / CMD）
├── ✅ docker build / run / ps / logs
├── ✅ 端口映射 -p
├── ✅ volume 数据持久化
├── ✅ 网络（自定义 bridge / 容器名通信）
├── ✅ 多阶段构建
├── ✅ docker-compose.yml
└── ❌ 安全扫描 Trivy（待补）
```

```
Layer 4：Kubernetes
├── ✅ Pod / Deployment / ReplicaSet
├── ✅ Service（ClusterIP / LoadBalancer）
├── ✅ kubectl（get / describe / logs / exec / top）
├── ✅ kubectl apply -f / delete
├── ✅ YAML 编写（Deployment + Service）
├── ✅ ConfigMap / Secret
├── ✅ PVC 持久化存储
├── ✅ Ingress 域名路由
├── ✅ Helm（安装 Chart / 创建 Release）
├── ❌ Network Policy（待补）
└── ❌ CKA 考试刷题（可选，提升简历）
```

```
Layer 5：CI/CD
├── ✅ GitHub Actions 概念（workflow/job/step/runner）
├── ✅ 触发事件（on push）
├── ✅ Secrets 管理
├── ✅ 用 SP 登录 Azure
├── ❌ 集成测试（pytest + Actions）（待补）
└── ❌ 审批门 / 多环境部署（知道概念）
```

```
Layer 6：监控
├── ✅ Prometheus 概念（指标采集/存储）
├── ✅ Grafana 可视化
├── ✅ PromQL 基础查询
├── ❌ 自定义告警规则（Alertmanager）
└── ❌ Loki 日志采集（待补）
```

```
Layer 7：Azure 认证 + 安全
├── ✅ Service Principal 创建 + 使用
├── ✅ RBAC 角色（Contributor / Reader）
├── ❌ Azure Key Vault（待补）
├── ❌ Azure Static Web Apps（项目用）
└── ❌ Trivy 容器安全扫描（待补）
```

### 🟡 能用层级（给场景能写/能修）

```
- Ansible 概念（能读懂 playbook）
- Terraform lifecycle 其他规则（ignore_changes、create_before_destroy）
- Docker compose 网络配置进阶
- K8s HPA 自动扩缩容
- PromQL 自定义 Grafana 面板
```

### 🟢 了解层级（知道概念，用时再查）

```
- ArgoCD GitOps（能用，但暂不深入）
- K8s Helm Chart 编写（会用 `helm install` 就够了）
- Terraform provisioners（知道有这个东西，不用）
- Alertmanager 告警路由配置
```

---

## 待补内容清单（按优先级排列）

| # | 内容 | 类型 | 预估时间 | 优先级 |
|---|------|------|---------|--------|
| 1 | **pytest 单元测试** | Python 层 | 1 天 | 🔴 |
| 2 | **Trivy 容器安全扫描** | Docker 层 | 半天 | 🔴 |
| 3 | **Azure Key Vault** | 安全层 | 1 天 | 🟡 |
| 4 | **K8s Network Policy** | K8s 层 | 半天 | 🟡 |
| 5 | **Loki 日志采集** | 监控层 | 1 天 | 🟡 |
| 6 | **CKA 刷题** | K8s 层 | 2-3 周可选 | 🟡 |
| 7 | **Azure Static Web Apps 项目** | 综合 | 2-3 天 | 🟡 |
| 8 | **AKS（Azure Kubernetes Service）** | 云托管 K8s | 综合项目阶段 | 🟡 |
| 8 | **K8s HPA + 资源限制** | K8s 层 | 半天 | 🟢 |
| 9 | **Alertmanager 告警配置** | 监控层 | 半天 | 🟢 |

---

## 学习深度对照表

```
🔴 精通 ─ 独立完成不查文档
   生产环境每天用的东西
   面试高频考点
   示例：kubectl 排障、Git 日常操作、Terraform 模块编写

🟡 能用 ─ 给场景能写/能修
   工作中偶尔用到
   面试可能会问
   示例：Terraform lifecycle、PromQL 自定义查询、Git rebase

🟢 了解 ─ 看得懂、能改参数
   不常用但知道有这个东西
   面试一句话带过
   示例：Ansible playbook、Terraform provisioners、Alertmanager

⚪ 跳过 ─ 知道概念就行
   生产环境基本不用
   社区不推荐
   示例：Terraform provisioners、Docker 多阶段构建深入细节
```

---

## 你对加拿大市场的实际竞争力

```
面试官看到你的简历：

必备技能：
  Python         ✅     60% 岗位要求
  Shell/Linux     ✅     必备
  Git              ✅     必备
  Terraform        ✅     80% 岗位要求
  Docker           ✅     70% 岗位要求
  Kubernetes       ✅     85% 岗位要求
  CI/CD            ✅     75% 岗位要求

证书：
  CCNP             ✅（网络差异化——大多数人没有）
  AZ-104           ✅

差异化：
  Azure 网络深入    ⏳ 第 11 周——结合 CCNP
  综合项目          ⏳ 个人站点

待补：测试、安全、日志
```

---

**文件位置：** `~/devops-learning/KNOWLEDGE-MAP.md`

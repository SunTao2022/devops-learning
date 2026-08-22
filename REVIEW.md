# 每日复习清单

> 每天学习前花 10 分钟过一遍。回答不上来的就是薄弱点，重点补。
> **原则：只学到"能独立上手干活"的程度，不追低频内容，不为了覆盖而覆盖。**

---

## 学习深度铁律

| 层级 | 要求 | 代表内容 |
|------|------|---------|
| 🔴 精通 | 独立完成不查文档 | kubectl排障、Shell自动化、Dockerfile、Git日常 |
| 🟡 能用 | 给场景能写/能修 | Terraform模块、CI/CD pipeline、Helm包管理 |
| 🟢 了解 | 看得懂、能改参数 | Ansible、PromQL复杂查询、Terraform lifecycle |
| ⚪ 跳过 | 知道概念就行 | Ansible深入、Terraform provisioners、Python装饰器 |

---

## 优先级 1：核心铁律（必须滚瓜烂熟）

- [x] `terraform destroy` 和 `az group delete` 的根本区别
- [x] 为什么 Storage Account 必须独立 RG
- [x] `count` vs `for_each` 的适用场景
- [x] `each.key` / `each.value` / `count.index` 分别是什么
- [x] 一个 Subnet 为什么只能绑一个 NSG
- [x] Remote state backend 的四个配置项及其作用
- [x] `kubectl run` 和 `kubectl create deployment` 的区别
- [x] Deployment / ReplicaSet / Pod 三者的关系
- [x] Pod 出问题时先 describe 还是先 logs？（什么场景用什么）——口诀：起不来 describe，起来了 logs
- [x] CI 铁律：`-input=false`（CI 无交互，变量缺失直接报错不卡住）
- [x] CI 中 validate / plan / apply 三者区别（validate 不连云、plan 连云只读、apply 真正动手）
- [x] 卡死的 CI run（in_progress 异常久）会一直占 state 锁，挡所有后续运行 → 先 cancel 再重跑

---

## 优先级 2：实验验证（必须能手写/手跑）

- [x] 把 compute module 从 `count` 改成 `for_each`
- [x] 写一个 `dynamic "security_rule"` block 生成多端口规则
- [x] `terraform init` 切 backend 的完整流程
- [x] `git add` → `git commit` → `git push` 三步走
- [x] `terraform fmt -recursive` 格式化整个项目
- [x] 写 GitHub Actions workflow（on/jobs/steps/uses/run + Secrets 注入 env）
- [x] CI 排障完整流程：`gh run list` → `gh run view <id> --log-failed` → 定位 → 修复 → rerun
- [x] `kubectl logs` / `describe` 各用一次（CrashLoopBackOff + ErrImagePull 双故障实验）
- [x] 完整生产流水线实操：源码 → Dockerfile → build → 本地验证 → 推 ghcr.io → CI 自动化 → K8s 部署（Secret+Deployment+Service）→ 访问 → 排障
- [x] 排障演练：ErrImagePull（tag 打错）→ 定位 → `kubectl set image` 修复 → 验证
- [x] `kubectl set image` 直接改集群配置（不用找 YAML 文件）
- [ ] 创建 Deployment → scale 扩缩 → 删 Pod → 验证自动恢复

---

## 优先级 3：概念理解（能口述原理）

- [x] Terraform module 的变量作用域（根目录 vs module）
- [x] Module output 转发的两种方式
- [x] `sensitive = true` 的作用和局限性
- [x] Python `for` 和 Terraform `for_each` 的本质区别
- [x] State lock 是怎么工作的（Blob lease）
- [x] 密钥 vs 参数分开存：不敏感参数进 Git/tfvars，SP 密钥进 GitHub Secrets，应用密钥进 Key Vault
- [x] 生产参数按环境分文件：terraform.tfvars.dev / .prod，用 `-var-file` 切换
- [x] 四眼原则：写代码的人 ≠ 审批 apply 的人（PR review + 审批门）
- [x] 私有仓库认证：ghcr.io 需要 imagePullSecrets（K8s Secret 存 PAT），GitHub Secret 给 CI、K8s Secret 给集群，两个不同
- [x] Docker 镜像分层：每层 = Dockerfile 一条指令；推送时 `Layer already exists` = 复用旧层，只传变化部分
- [x] 生产密钥管理：裸 base64 进 Git 危险 → Key Vault / External Secrets 是生产标准
- [x] 监控栈实操：helm install kube-prometheus-stack → Prometheus + Grafana + Alertmanager 全套
- [x] PromQL 查询：指标名 + 标签过滤（{namespace="xxx", pod=~"xxx.*"}），过滤越多结果越少
- [x] `up` 指标：1=采集正常，0=采集失败（Minikube 的 etcd/scheduler 是已知限制，忽略）
- [x] 监控链路：kubelet 采集 → Prometheus 存储 → Grafana 可视化（事前发现 vs 排障事后）
- [x] Helm 查初始凭据：`kubectl get secret xxx -o jsonpath='{.data.admin-password}' | base64 -d`
- [x] ArgoCD GitOps 完整闭环：安装 → 配置 Application（Source/Destination）→ 检测差异（OutOfSync）→ 手动 Sync
- [x] ArgoCD 坑：path 指向非 YAML 目录（package.json）→ Missing；namespace 缺失 → InvalidSpecError。K8s YAML 放独立目录 k8s/
- [x] 镜像不可变 tag（git SHA）+ ArgoCD：YAML 变才检测到；latest 检测不到（GitOps 标准）
- [x] GitOps 原则：Git 是唯一真相，集群向 Git 看齐；Manual 模式 = prod 可控，Automatic = dev 快速
- [x] 为什么一个 Deployment 要管理多个 Pod（而不是 1 个）——可用性 + 滚动更新
- [ ] `kubectl port-forward` 的作用和限制

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

---
title: 组件
summary: 组件
authors:
    - Zhiyuan Chen
date: 2019-11-19 07:18:34
categories: 
    - Kubernetes
    - 组件
tags:
    - 容器化
    - Kubernetes
    - Component
---

Kubernetes的组件可以分为三类--管理组件（Master Components）、节点组件（Nodes Components）和插件（Addons）。

!!! tip "主节点（Master Node）和从节点（Worker Node）"

    管理组件可以运行在集群当中的任何一个节点之上，但我们通常会将所有管理组件运行在某一个或多个节点之上，并且不在这些节点上运行任何用户容器。对于这一个或几个节点，我们将其称为主节点（Master Node）。对于其他所有节点，我们将其称为从节点或者工作节点（Worker Node）。

    一般而言，一个Kubernetes集群至少需要一个主节点和一个从节点。


## 管理组件（Master Components）

!!! note "管理组件"

    管理组件可以在任何一个节点上运行，它为集群提供控制平面，包括做出全局性决策以及检测和响应集群事件

    管理组件由包括以下五个组件：

    + API服务器（kube-apiserver）
    + etcd
    + 调度器（kube-scheduler）
    + 控制器管理器（kube-controller-manager）
    + 云控制器管理器（cloud-controller-manager）

### API服务器（kube-apiserver）

!!! note "API服务器"

    API服务器负责将Kubernetes API对外暴露。

    Kubernetes API 服务器的主要实现是[kube-apiserver](/api-server)。 kube-apiserver 被设计为水平扩展--即通过部署更多实例来实现伸缩。你可以运行多个 kube-apiserver 实例并且均衡每个实例的流量。

[comment]: <>(TODO: kube-apiserver)

### etcd

!!! note "etcd"

    [etcd](https://github.com/etcd-io/etcd)是一个分布式的高可用键值存储。etcd被Kubernetes用于存储所有数据。

!!! important "备份"

    etcd一般会被定期备份，以便于在灾难性情况下恢复Kubernetes集群。

您可以在[etcd官方文档](https://etcd.io/docs/)中找到有关etcd的详细信息。

### 调度器（kube-scheduler）

!!! note "调度器"

    调度器负责监视所有新创建的pods，并对其分配一个节点来运行。

[comment]: <>(TODO: 调度的因素)

### 控制器管理器（kube-controller-manager）

!!! note "控制器管理器"

    控制器管理器负责运行[管理器](/controller)。

    逻辑上，每一个控制器都是一个单独的进程。但出于降低复杂性的考虑，他们都被编译成一个单独的二进制文件并且在一个单独的进程当中运行。

这些控制器包括：

+ 节点控制器：负责节点发现并在节点下线时响应。
+ 副本控制器：负责根据副本控制器对象维护pods的数量。
+ 端点控制器：负责填充端点对象（即加入服务和pods）。
+ 服务账户与标识控制器：负责为新的名称空间创建默认帐户和API访问标识。

[comment]: <>(TODO: controller)

### 云控制器管理器（cloud-controller-manager）

云控制器管理器是Kubernetes 1.6版中引入的alpha功能。

!!! note "云控制器管理器"

    云控制器管理器负责运行与底层云提供商交互的控制器。

    云控制器管理器仅运行特定于云提供商的控制器循环。您必须在控制器管理器中禁用这些控制器循环。您可以通过在启动控制器管理器时将--cloud-provider标志设置为external来禁用控制器循环。

    云控制器管理器允许云供应商的代码和Kubernetes代码彼此独立地发展。在以前的版本中，核心的Kubernetes代码依赖于特定于云提供商的代码来实现功能。在将来的版本中，应由云供应商自己维护特定于云供应商的代码，并在运行Kubernetes时将其链接到云控制器管理器。

以下控制器具有云提供程序依赖：

+ 节点控制器：负责检查云提供者以确定节点停止响应后是否已在云中删除该节点
+ 路由控制器：负责在基础云基础架构中设置路由
+ 服务控制器：负责创建，更新和删除云提供商负载平衡器
+ 卷控制器：负责创建，附加和安装卷，以及与云提供商交互以编排卷

## 节点组件（Nodes Components）

!!! note "节点组件"

    节点组件则需要在每一个节点上运行，它维护运行的Pod并提供Kubernetes运行时环境

    节点组件包括以下三个组件：
    
    + kubelet
    + kube-proxy
    + 容器运行时（Container Runtime）

### kubelet

!!! note "kubelet"

    kubelet是一个代理，负责确保容器在容器中运行。

    kubelet包含通过各种机制提供的一组PodSpecs（pod参数），并确保这些PodSpecs中描述的容器运行正常。 Kubelet不管理非Kubernetes创建的容器。

### kube-proxy

!!! note "kube-proxy"

    kube-proxy是一个网络代理，实现了Kubernetes服务概念的一部分。

    kube-proxy维护节点上的网络规则。这些网络规则允许从集群内部或外部的网络会话与pod进行网络通信。

    如果有kube-proxy，则kube-proxy使用操作系统的数据包过滤层。否则，kube-proxy会转发流量本身。

### 容器运行时（Container Runtime）

!!! note "容器运行时"

    容器运行时是负责运行容器的软件。

Kubernetes支持多种容器运行时：[Docker](http://www.docker.com/)，[containerd](https://containerd.io/)，[cri-o](https://cri-o.io/)，[rktlet](https://github.com/kubernetes-incubator/rktlet)以及[Kubernetes CRI（容器运行时接口）](https://github.com/kubernetes/community/blob/master/contributors/devel/sig-node/container-runtime-interface.md)的任何实现。

## 插件（Addons）

!!! note "插件"

    插件为Kubernetes集群提供附加特性。

    由于插件提供的特性是集群等级的，插件的命名空间资源属于`kube-system`命名空间。

本节提供一部分插件的描述，有关具体的内容，敬请参阅[插件](addons)。

[comment]: <>(TODO: addons)

### DNS

!!! note "DNS"

    几乎所有的插件都是选装的，但DNS是一个例外。每一个Kubernetes集群都应该有[Cluster DNS](/cluster-dns)。

    Cluster DNS是一个DNS服务器，和您部署环境中的其他DNS服务器一起工作，为Kubernetes服务提供DNS记录。

    Kubernetes会自动将这个DNS服务器包含在由其启动的容器的DNS搜索中。

### Web UI（仪表板）

!!! note "仪表板"

    仪表板是Kubernetes集群的通用基于Web的UI。它允许用户管理集群中运行的应用程序以及集群本身并进行故障排除。

### 容器资源监控（Container Resource Monitoring）

!!! note "容器资源监控"

    [容器资源监控](https://kubernetes.io/docs/tasks/debug-application-cluster/resource-usage-monitoring/)在中央数据库中记录有关容器的一般时间序列指标，并提供用于浏览该数据的UI。

### 集群级日志（Cluster-level Logging）

!!! note "集群级日志"

    [集群级日志](https://kubernetes.io/docs/concepts/cluster-administration/logging/)机制负责通过搜索/浏览接口将容器日志保存到中央日志存储中。

---
title: Kubernetes导论
summary: Kubernetes导论
authors:
    - Zhiyuan Chen
date: 2019-01-28 12:08:33
categories: 
    - Kubernetes
    - 导论
tags:
    - 容器化
    - Kubernetes
    - Docker
---

# Kubernetes

Kubernetes，作为Google在运行多年的Borg基础上开发的开源容器编排系统，在部署、伸缩及管理方面具有强大的能力。

和很多初学者所想的不一样，kubernetes并非是为Docker而生的。事实上，他还支持Rocket这样的容器技术。但在本站当中，我们将不会讨论kubernetes在其他容器技术上的应用。我们鼓励您在网上寻找其他信息，如果您有这方面的需求，我们同时很欢迎您将您所找到的内容整理成文章并提交在本站当中。

## Kubernetes架构
Kuberenetes由五层结构构成。

## Kubernetes组件
基础的kubernetes由七个组件构成，他们是：

    - etcd                  集群信息保存（集群）

    - apiserver             集群操作入口（主机）

    - scheduler             集群资源调度（主机）

    - controller manager    集群状态维护（主机）

    - kubelet               镜像、容器、数据卷（CVI）、网络（CNI）等的管理（从机）

    - container runtime     镜像和Pod（CRI）的管理（从机）

    - kube-proxy            集群的服务发现和负载均衡（从机）
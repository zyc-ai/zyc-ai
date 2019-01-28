---
title: Kubernetes Deploy Guide
summary: Introduciton of deploying kubernetes to you machine.
authors:
    - Zhiyuan Chen
date: 2019-01-25 02:06:37
categories: 
    - Documents
    - Computer Science
    - Technology
    - Containerization
    - Kubernetes
tags:
    - Containerization
    - Kubernetes
    - Docker
---
# Kubernetes部署教程

网上kubernetes各种教程不少，但要么是上古时期的版本，要么三言两语匆匆带过。

这里列一下我在部署kubernetes v1.13.2时踩过的各种坑。


## 安装Docker && Kubernetes
    # 安装依赖
    apt-get install \
        apt-transport-https \
        ca-certificates \
        curl \
        gnupg2 \
        software-properties-common

    # 添加Docker仓库
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    add-apt-repository \
        "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
        $(lsb_release -cs) \
        stable"
    # 不要问我为什么添加仓库的方式不一样，他们官方文档就是这么写的，再问自杀（手动白眼
    # 添加kubernetes仓库
    curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
    cat <<EOF >/etc/apt/sources.list.d/kubernetes.list
        deb https://apt.kubernetes.io/ kubernetes-xenial main
        EOF
    # 更新仓库
    apt-get update
    # 安装Docker，由于kubernetes v1.13.2最高支持Docker v1.18.0.6，这里手动指定版本。
    # 有的教程说kubernetes不支持Docker-CE，只支持Docker-IO，相信我，他在胡扯。
    apt-get install docker-ce=18.06.0~ce~3-0~ubuntu
    # 安装kubernetes
    apt-get install kubelet kubeadm kubectl


## 拉取依赖镜像
#### 本步骤仅适用于位于GFW影响范围内的主机
运行以下脚本（如果您预期安装的kubernetes版本不是v1.13.2，请运行kubeadm config images list并依据返回结果运行脚本）：

    #!/bin/bash
    set -e    
    if [ -n "$1" ]; then
        K8S_VERSION=$1
    else
        K8S_VERSION=v1.13.2
    fi
    if [ -n "$2" ]; then
        DASHBOARD_VERSION=$2
    else
        DASHBOARD_VERSION=v1.10.1
    fi
    if [ -n "$3" ]; then
        ETCD_VERSION=$3
    else
        ETCD_VERSION=3.2.24
    fi
    if [ -n "$4" ]; then
        PAUSE_VERSION=$4
    else
        PAUSE_VERSION=3.1
    fi
    if [ -n "$5" ]; then
        DNS_VERSION=$5
    else
        DNS_VERSION=1.2.6
    fi
    if [ -n "$6" ]; then
        FLANNEL_VERSION=$6
    else
        FLANNEL_VERSION=v0.10.0-amd64
    fi
    ## 拉取镜像
    docker pull registry.cn-hangzhou.aliyuncs.com/google_containers/kube-controller-manager:$K8S_VERSION
    docker pull registry.cn-hangzhou.aliyuncs.com/google_containers/kube-scheduler:$K8S_VERSION
    docker pull registry.cn-hangzhou.aliyuncs.com/google_containers/kube-proxy:$K8S_VERSION
    docker pull registry.cn-hangzhou.aliyuncs.com/google_containers/kube-apiserver:$K8S_VERSION
    docker pull registry.cn-hangzhou.aliyuncs.com/google_containers/kubernetes-dashboard-amd64:$DASHBOARD_VERSION
    docker pull registry.cn-hangzhou.aliyuncs.com/google_containers/etcd:$ETCD_VERSION
    docker pull registry.cn-hangzhou.aliyuncs.com/google_containers/pause:$PAUSE_VERSION
    docker pull registry.cn-hangzhou.aliyuncs.com/google_containers/coredns:$DNS_VERSION
    docker pull registry.cn-hangzhou.aliyuncs.com/kubernetes_containers/flannel:$FLANNEL_VERSION
    ## 修改标签
    docker tag registry.cn-hangzhou.aliyuncs.com/google_containers/kube-controller-manager:$K8S_VERSION k8s.gcr.io/kube-controller-manager:$K8S_VERSION
    docker tag registry.cn-hangzhou.aliyuncs.com/google_containers/kube-scheduler:$K8S_VERSION k8s.gcr.io/kube-scheduler:$K8S_VERSION
    docker tag registry.cn-hangzhou.aliyuncs.com/google_containers/kube-proxy:$K8S_VERSION k8s.gcr.io/kube-proxy:$K8S_VERSION
    docker tag registry.cn-hangzhou.aliyuncs.com/google_containers/kube-apiserver:$K8S_VERSION k8s.gcr.io kube-apiserver:$K8S_VERSION
    docker tag registry.cn-hangzhou.aliyuncs.com/google_containers/kubernetes-dashboard-amd64:$DASHBOARD_VERSION k8s.gcr.io/kubernetes-dashboard-amd64:$DASHBOARD_VERSION
    docker tag registry.cn-hangzhou.aliyuncs.com/google_containers/etcd:$ETCD_VERSION k8s.gcr.io/etcd:$ETCD_VERSION
    docker tag registry.cn-hangzhou.aliyuncs.com/google_containers/pause:$PAUSE_VERSION k8s.gcr.io/pause:$PAUSE_VERSION
    docker tag registry.cn-hangzhou.aliyuncs.com/google_containers/coredns:$DNS_VERSION k8s.gcr.io/coredns:$DNS_VERSION
    docker tag registry.cn-hangzhou.aliyuncs.com/kubernetes_containers/flannel:$FLANNEL_VERSION quay.io/coreos/flannel:$FLANNEL_VERSION
    ## 删除原始标签
    docker rmi registry.cn-hangzhou.aliyuncs.com/google_containers/kube-controller-manager:$K8S_VERSION
    docker rmi registry.cn-hangzhou.aliyuncs.com/google_containers/kube-scheduler:$K8S_VERSION
    docker rmi registry.cn-hangzhou.aliyuncs.com/google_containers/kube-proxy:$K8S_VERSION
    docker rmi registry.cn-hangzhou.aliyuncs.com/google_containers/kube-apiserver:$K8S_VERSION
    docker rmi registry.cn-hangzhou.aliyuncs.com/google_containers/kubernetes-dashboard-amd64:$DASHBOARD_VERSION
    docker rmi registry.cn-hangzhou.aliyuncs.com/google_containers/etcd:$ETCD_VERSION
    docker rmi registry.cn-hangzhou.aliyuncs.com/google_containers/pause:$PAUSE_VERSION
    docker rmi registry.cn-hangzhou.aliyuncs.com/google_containers/coredns:$DNS_VERSION
    docker rmi registry.cn-hangzhou.aliyuncs.com/kubernetes_containers/flannel:$FLANNEL_VERSION


## 初始化kubernetes
#### 出于对网络速度的考虑，我们使用了Flannel作为网络模型，不同网络模型的初始化参数可能不一样，请依据指导初始化

    kubeadm init --pod-network-cidr=10.244.0.0/16 --apiserver-advertise-address=<ip-address>

## 导出配置文件
#### 导出配置文件是十分必要的，kubernetes会从当前操作用户的~/.kube目录下读取配置文件

    # 对于普通用户
    mkdir -p $HOME/.kube
    sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
    sudo chown $(id -u):$(id -g) $HOME/.kube/config
    # 对于root用户
    export KUBECONFIG=/etc/kubernetes/admin.conf

#### 如果配置文件无法读取，您在接下来的操作当中可能会看到如下错误：

    The connection to the server localhost:8080 was refused - did you specify the right host or port?

## 配置kubernetes网络模型
#### 如果您选择了其他网络模型，请依据指导完成本步骤
    sysctl net.bridge.bridge-nf-call-iptables=1
    kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml


## 部署kubernetes dashboard

    kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v1.10.1/src/deploy/recommended/kubernetes-dashboard.yaml


## 安装结束
至此，kubernetes已经成功在您的机器上安装，运行

    kubectl get pods --all-namespaces

检视所有pod的运行情况

在下一篇教程当中，我们将会介绍身份认证机制。
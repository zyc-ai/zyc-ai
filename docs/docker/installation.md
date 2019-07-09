---
title: 安装Docker
summary: Installation of Docker
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

# 安装

Docker的安装非常简单，apt-get一分钟就好。如果你还打算安装Kubernets

## 安装准备

    # 安装依赖
    apt-get install \
        apt-transport-https \
        ca-certificates \
        curl \
        gnupg2 \
        software-properties-common

    # 添加Docker仓库
    # 有的教程说kubernetes不支持Docker-CE，只支持Docker-IO，相信我，他在胡扯。
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    add-apt-repository \
        "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
        $(lsb_release -cs) \
        stable"
    
    # 更新仓库
    apt-get update
    # 安装Docker
    apt-get install docker-ce
    
    # 如果你不需要在容器当中使用Nvidia GPU，以下步骤无需执行
    # 添加nvidia-docker2仓库
    # 由于nvidia-docker2是通过Docker安装的，所以需要在完成Docker的安装之后再安装nvidia-docker2
    docker volume ls -q -f driver=nvidia-docker | xargs -r -I{} -n1 docker ps -q -a -f volume={} | xargs -r docker rm -f
    curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | \
    apt-key add -
    distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
    curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | \
        tee /etc/apt/sources.list.d/nvidia-docker.list

    # 安装nvidia-docker2
    apt-get install nvidia-docker2
    pkill -SIGHUP dockerd

将nvidia-docker2修改为docker的默认运行时环境
*如果你不需要在容器当中使用Nvidia GPU，以下步骤无需执行*

    vim /etc/docker/daemon.json
        {
            "default-runtime": "nvidia",
            "runtimes": {
                "nvidia": {
                    "path": "/usr/bin/nvidia-container-runtime",
                    "runtimeArgs": []
                }
            }
        }
    sudo service docker restart

**安装结束**
至此，Docker已经成功在您的机器上安装，运行

    docker ps

检视所有Docker容器的运行情况

在下一篇文章当中，我们将会讨论Docker的命令行接口（Command Line Interface）

---
title: Kubernetes Deploy Guide
summary: Introduciton of deploying kubernetes to you machine.
authors:
    - Zhiyuan Chen
date: 2019-02-23 15:55:24
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
# Pods

对于Kubernetes来说，最小的部署单元是一个Pod。

正如他的名字（豆荚）那样，一个Pod可以包含多个容器，他们共享命名空间、数据卷、网络并可以进行进程间通信。

相比容器，Pod在这里更像一个虚拟机--如果你把完成一个任务所需的所有容器都放在一个Pod当中，那这就相当于一个独立的节点了！


## 部署文件
一个简单的Pod的部署文件如下所示：

    apiVersion: v1
    kind: Pod
    metadata:
    name: demo
    namespace: demo
    labels:
        - name: demo
    annotations:
        - name: demo
    spec:
    restartPolicy: Always
    containers:
        - name: demo
        image: demo/demo:dev
        resources:
            limits:
            nvidia.com/gpu: 1
            requests:
            nvidia.com/gpu: 1
        volumeMounts:
            - name: logs
            mountPath: /usr/local/demo/logs
    imagePullSecrets:
        - name: pswd
    volumes:
        - name: logs
        hostPath:
            path: /usr/local/demo/logs

## 完成部署

对上面的内容做出少许修改（比如你可能不需要挂载日志文件，也不需要使用GPU）并在本地应用，你的第一个应用就完成部署了。

但是，作为最小的部署单元，我们仅仅是将几个容器合并在了一个单元当中，而并没有实现其他的功能--比如说，最重要的，容器调度。

在下一篇文章当中我们将会简要介绍Deployment，完成一个真正的应用部署。
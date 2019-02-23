---
title: 部署（Deployments）
summary: Deploy first deployment
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

# 部署（Deployments）

部署可以理解为Docker Swarm当中的服务（Service），通常情况下，我们并不会手动创建前文当中所提到的Pods，而是通过创建一个部署，再由部署依据调度原则去创建Pods。

简单来说，部署在Pods的基础上增加了调度。我们可以对部署进行滚动更新以及回滚，Kubernetes为我们提供了Pods水平自动伸缩（HPA）（当然你也可以选择自己去写伸缩脚本）。

简而言之，完成一个部署，你的人生才算圆满。

## 描述文件

部署的描述文件可以看作是Pod描述文件的一个父集。

    apiVersion: apps/v1
    kind: Deployment
    metadata:
    name: demo-deployment
    namespace: smartedu
    labels:
        app: demo
    annotations:
        - name: demo
    spec:
    replicas: 32
    selector:
        matchLabels:
        app: demo
    template:
        metadata:
        labels:
            app: demo
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
        volumes:
            - name: logs
            hostPath:
                path: /usr/local/demo/logs

## 完成部署

如上文一样，对上面的内容做出简单的修改就能部署第一个真·应用。

在下一篇文章当中我们会简要介绍Deployment的一些操作，让你能真正开始用上应用。
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

# Deployments

Deployments（部署）可以理解为Docker Swarm当中的Service（服务），通常情况下，我们并不会手动创建前文当中所提到的Pods，而是通过创建一个Deployment，再由Deployment依据调度原则去创建Pods。

简单来说，Deployments就是简单的在Pods的基础上增加了调度。我们可以对部署进行滚动更新以及回滚，Kubernetes还为我们提供了Horizontal Pod Autoscaling（水平自动伸缩）（当然你也可以选择自己去写伸缩脚本）。

简而言之，完成一个Deployment，你的人生才算圆满。

## 描述文件

Deployments的描述文件可以看作是Pods描述文件的一个父集。

    apiVersion: apps/v1
    kind: Deployment
    metadata:
    name: demo-deployment
    namespace: demo
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

如Pods一样，对上面的内容做出简单的修改就能部署第一个真·应用。

在下一篇文章当中我们会简要介绍Deployments的一些操作，让你能真正开始用上应用。
---
title: SiamRPN
summary: SiamRPN
authors:
    - Zhiyuan Chen
date: 2019-12-21 17:27:45
categories:
    - Computer Vision
    - Object Tracking
    - Single Object Tracking
    - Siamese-based Object Tracker
    - SiamRPN
tags:
    - Computer Vision
---

!!! info "专有名词翻译和缩写"
    在本文当中，专有名词被如下翻译和缩写：

    + anchor 锚框
    + Convolution Neural Network CNN 卷积神经网络
    + Meta-Learning 元学习
    + Padding 填充
    + Regional Proposal Network RPN 区域候选网络
    + Siamese 孪生
    + Visual Object Tracking VOT

SiamRPN是商汤科技的李博等提出的单目标跟踪算法。

!!! info "简介"

    本文通过AlexNet提取特征图，通过RPN构建相关特征图并从相关特征图上提取和修正候选区域，通过本地单样本检测框架对候选区域评分，最后选取分数最高的候选区域输出。
    本文的基础是：SiamFC、Faster-RCNN。

!!! list "贡献"

        1. 本文作者提出了一个孪生区域候选网络（Siamese-RPN）。他是一个使用大量图片的端到端离线训练的网络，被用于跟踪任务。
        2. 在在线跟踪时，被提出的框架被转化为一个本地单样本检测任务，它可以完善候选以避免昂贵的多尺度测试。
        3. 被提出的框架在速度达到160FPS时在VOT2015、VOT2016、VOT2017任务中取得了领先成绩，这证明它在速度和准确性方面的优点。

## Siamese-RPN框架

如图所示，Siamese-RPN框架由一个负责特征提取的孪生子网络和一个负责候选区域判别的区域候选子网络构成。特别的，在RPN自网络当中有两个分支，一个负责前-背景分类，另一个则负责候选区域修正。整个系统都被端到端的训练。

### 孪生特征提取子网络

本文的孪生特征提取子网络与SiamFC的特征提取部分相同，都是使用孪生架构的AlexNet作为后端提取特征图。与SiamFC的主要区别在于其输出的特征图维度为$6 \times 6 \times 256$和$22 \times 22 \times 256$，是SiamFC的两倍。

在孪生网络中，本文作者采用了一个没有填充的全卷积网络。使用$L_\tau$表示变换操作器，$L_\tau\mathcal{x[u]=x[u-_\tau]}$，然后所有的填充都被移除来满足步长为$k$的全卷积的定义：

$h(L_{\mathcal{k\tau}}\mathcal{x})=L_{\tau}h(\mathcal{x})$

这里，本文作者使用修改后的AlexNet，其中conv2到conv4的组被移除。孪生特征提取子网络由两个分支组成。第一个被称为 *模板分支（template branch）* ，他将首帧作为输入（表示为$\mathcal{z}$）。另一个则被称为 *检测分支（detection branch）* ，它将当前帧作为输入（表示为$\mathcal{x}$）。两个分支共享权重卷积神经网络中的参数，因此他们通过相同的适宜于随后处理的变换被隐式编码。孪生子网络的输出分别被表示为$\phi\mathcal{(z)}$和$\phi\mathcal{(x)}$。

### 区域候选子网络

区域候选子网络包含一个互相关子段和一个监督子段。监督子段有两个分支，一个被用于前-背景分离，另一个被用于候选区域回归。如果总共由$\mathcal{k}$个锚框，网络需要输出$\mathcal{2k}$个通道来分类，$\mathcal{4k}$个通道来回归。所以互相关子段首先将$\phi\mathcal{(z)}$的通道通过两个卷积层提升到两个分支$[\phi(\mathcal{z})]_{\mathcal{cls}}$和$[\phi(\mathcal{z})]_{\mathcal{reg}}$，他们分别有$\mathcal{2k}$和$\mathcal{4k}$个通道。$\phi\mathcal{(x)}$也通过两个卷积层被分为$[\phi(\mathcal{x})]_{\mathcal{cls}}$和$[\phi(\mathcal{x})]_{\mathcal{reg}}$两个分支，但保持通道数不变。$[\phi\mathcal{(z)}]$以一个“组”的方式被用作$[\phi\mathcal{(x)]}$的相关核，也就是说，一个$[\phi(\mathcal{z})]$的组的通道数和$[\phi(\mathcal{x})]$的整体通道数相同。相关性是在分类分支和回归分支上共同计算的：

$A{^{cls}_{\mathcal{w \times h \times 2k}}} = [\phi(\mathcal{x})]_{\mathcal{cls}} \star [\phi(\mathcal{z})]_{\mathcal{cls}}$

$A{^{reg}_{\mathcal{w \times h \times 4k}}} = [\phi(\mathcal{x})]_{\mathcal{reg}} \star [\phi(\mathcal{z})]_{\mathcal{reg}}$

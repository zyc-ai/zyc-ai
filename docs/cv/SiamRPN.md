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

## 简介

本文通过在相关特征图上使用RPN来提取候选区域。由于追踪任务没有预定义的类别，所以本文作者需要一个目标分支来将目标的出现信息编码输入RPN特征图来将前景和背景分离。

对于推理，本文作者将其转换为一个本地单样本检测框架。其中，第一张图片所附带的候选区域将是唯一的样例。本文作者将模板分支重新解释为参数来预测类似于元学习器的检测核。元学习器和检测分支都被端到端的训练。模板分支会在初始帧后被裁剪来加速在线跟踪。就本文作者所知，这是第一个将在线跟踪任务转换为一个单样本检测的工作。

本文作者在VOT2015、VOT2016和VOT2017实时竞赛上评估了提出的方法。它可以在所有的三个竞赛中达到领先成绩。能在没有在线微调得情况下达到SOTA结果，有两个主要原因。第一是本文作者的方法可以被离线训练，所以可以使用大规模训练数据，比如Youtube-BB。消融研究表明更多的数据可以帮助达到更好的性能。其次，本文作者发现RPN通常可以预测候选区域的准确尺度和比率以获得紧凑的区域，如图所示。

本文的贡献可以被总结为三点。

1. 本文作者提出了一个孪生区域候选网络（Siamese-RPN）。他是一个使用大量图片对端到端离线训练的网络，被用于追踪任务。

2. 在在线追踪时，被提出的框架被转化为一个本地单样本检测任务，它可以完善候选以避免昂贵的多尺度测试。

3. 被提出的框架在速度达到160FPS时在VOT2015、VOT2016、VOT2017任务中取得了领先成绩，这证明它在速度和准确性方面的优点。

## Siamese-RPN框架

如图所示，Siamese-RPN框架由一个孪生子网络来提取特征，和一个目标候选子网络来生成候选区域。特别的，在RPN自网络当中有两个分支，一个负责前-背景分类，另一个则负责候选区域修正。整个系统都被端到端的训练。

### 孪生特征提取子网络

在孪生网络中，本文作者采用了一个没有填充的全卷积网络。使用$L_\mathcal{T}$表示变换操作器，$L_\mathcal{T}\mathcal{x[u]=x[u-_T]}$，然后所有的填充都被移除来满足步长为$k$的全卷积的定义：

$h(L_{\mathcal{kT}}\mathcal{x})=L_{\mathcal{T}}h(\mathcal{x})$

这里，本文作者使用修改后的AlexNet，其中conv2到conv4的组被移除。孪生特征提取子网络由两个分支组成。第一个被称为 *模板分支（template branch）* ，他将首帧作为输入（表示为$\mathcal{z}$）。另一个则被称为 *检测分支（detection branch）* ，它将当前帧作为输入（表示为$\mathcal{x}$）。两个分支共享权重卷积神经网络中的参数，因此他们通过相同的适宜于随后处理的变换被隐式编码。孪生子网络的输出分别被表示为$\phi\mathcal{(z)}$和$\phi\mathcal{(x)}$。

### 区域候选子网络

区域候选子网络包含一个互相关子段和一个监督子段。监督子段有两个分支，一个被用于前-背景分离，另一个被用于候选区域回归。如果总共由$\mathcal{k}$个锚框，网络需要输出$\mathcal{2k}$个通道来分类，$\mathcal{4k}$个通道来回归。所以互相关子段首先将$\phi\mathcal{(z)}$的通道通过两个卷积层提升到两个分支$[\phi(\mathcal{z})]_{\mathcal{cls}}$和$[\phi(\mathcal{z})]_{\mathcal{reg}}$，他们分别有$\mathcal{2k}$和$\mathcal{4k}$个通道。$\phi\mathcal{(x)}$也通过两个卷积层被分为$[\phi(\mathcal{x})]_{\mathcal{cls}}$和$[\phi(\mathcal{x})]_{\mathcal{reg}}$两个分支，但保持通道数不变。$[\phi\mathcal{(z)}]$以一个“组”的方式被用作$[\phi\mathcal{(x)]}$的相关核，也就是说，一个$[\phi(\mathcal{z})]$的组的通道数和$[\phi(\mathcal{x})]$的整体通道数相同。相关性是在分类分支和回归分支上共同计算的：

$A{^{cls}_{\mathcal{w \times h \times 2k}}} = [\phi(\mathcal{x})]_{\mathcal{cls}} \star [\phi(\mathcal{z})]_{\mathcal{cls}}$

$A{^{reg}_{\mathcal{w \times h \times 4k}}} = [\phi(\mathcal{x})]_{\mathcal{reg}} \star [\phi(\mathcal{z})]_{\mathcal{reg}}$

---
title: 分布
summary: distribution
authors:
    - Zhiyuan Chen
date: 2019-11-08 08:11:19
categories: 
    - Machine Learning
    - Distribution
tags:
    - Machine Learning
    - Distribution
    - Probability
    - Probability Mass Function
    - Probability Density Function
    - Cumulative Distribution Function
---

本文中我们将讨论分布。

!!! important "概率质量函数（Probability Mass Function）"

    对于 **离散目标空间** $\mathcal{T}$，我们将 **离散随机变量** $X$为某个特定值$x \in \mathcal{T}$的概率称作它的概率质量函数，记作$P(X = x)$

!!! important "累积分布函数（Cumulative Distribution Function）"

    对于 **连续目标空间** $\mathcal{T}$，我们将 **随机变量** $X$在特定区间$a, b \in \mathcal{T}, a \leq b$的概率称作它的累积分布函数，记作$P(a \leq X \leq b)$
    
    累积分布函数是概率密度函数（Probability Density Function）的积分

    根据惯例，我们也将$X$小于某个特定值$x \in \mathcal{T}$记作$P(X < x)$

## 离散分布

!!! important "边缘概率（Marginal Probability）"

    边缘概率即为概率质量函数

    我们用$X ~ P(X = x)$来表示$X$依据$P(X = x)$分布

!!! important "联合概率（Joint Probability）"

    对于离散目标空间$\mathcal{T}$，我们将离散随机变量$X, Y$与某两个特定值$x, y \in \mathcal{T}$相等，即$X = x, Y = y$的概率称作它们的联合概率，记作$P(X = x, Y = y)$

    根据贝叶斯定理，我们可以得到$P(X = x, Y = y) = P(X = x)P(X = x | Y = y)$

!!! important "条件概率（Conditional Probability）"

    对于离散目标空间$\mathcal{T}$，我们将离散随机变量$X, Y$与某两个特定值$x, y \in \mathcal{T}$在$Y = y$时$X = x$的概率称作条件概率，记作$P(X = x | Y = y)$

    根据贝叶斯定理，我们可以得到$P(X = x | Y = y) = \frac{P(X = x, Y = y)}{(Y = y)}$


---
title: 球与锥
summary: Ball and Cone
authors:
    - Zhiyuan Chen
date: 2020-08-13 22:32:58
categories:
    - Opsimisation
tags:
    - Opsimisation
    - Euclidean Ball
    - Ellipsoid
    - Cone
---

在本节中，我们介绍欧几里得球（Euclidean Ball）、椭球（Ellipsoid）与锥（cone）。

在上一节，我们首先复习了直线和线段的定义。本节，让我们从锥开始。

## 欧几里得球与椭球

!!! important "欧几里得球"

    一个$\mathbb{R}^n$上的欧几里得球满足如下形式：$B(x_c, r) = \{x \mid \Vert x - x_c \Vert_2 \leq r\} = \{x \mid (x - x_c)^T(x - x_c) \leq r^2\} \ s.t. \ r \in \mathbb{R}_+$

在上式中，$x_c$为 *圆心* ，$r$ 为 *半径* 。$B(x_c, r)$包括以$x_c$为中心，距离为$r$内的所有点。欧几里得球还常被表示为$B(x_c, r) = \{x_c + ru \mid \Vert u \Vert_2 \leq 1\}$

??? help "试证明欧几里得球是一个凸集"

    对于欧几里得球$B(x_c, r)$及其中两点$x_1, x_2 \in B$，我们有$\Vert x_1 - x_c \Vert_2 \leq r$与$\Vert x_2 - x_c \Vert_2 \leq r$，$0 \leq \   \leq 1$，那么

    $$\begin{align}
    \Vert \theta x_1 + (1 - \theta) x_2 - x_c \Vert_2 &= 
    \Vert \theta (x_1 - x_c) + (1 - \theta) (x_2 - x_c) \Vert_2 \\ &=
    \theta \Vert x_1 - x_c \Vert_2 + (1 - \theta) \Vert x_2 - x_c \Vert_2 \\ &= 
    r
    \end{align}$$

一个更一般的球被称为椭球（ellipsoid）。

!!! important "椭球"

    $$\epsilon = \{x \mid (x - x_c)^TP^{-1}(x - x_c) \leq 1\}$$

$x_c \in \mathbb{R}^n$是椭球$\epsilon$的 *球心*；$P \in \mathbb{S}^n_{++}$是一个对称的正定矩阵，它决定了椭球在每个方向从球心$x_c$伸张的长度。椭球$\epsilon$的半轴的长度由$\sqrt{\lambda_i}$给出，其中$\lambda_i$是$P$的特征值。我们很容易发现欧几里得球是椭球的一个特殊情况--当$P$为一个单位矩阵时。

$(x - x_c)^TP^{-1}(x - x_c)$实际上是$x - x_c$的p-范数，因此上式有时也写作$\epsilon = \{x \mid \Vert x - x_c \Vert_p \leq 1\}$。

椭球还常被表达为$\epsilon = \{x_c + Au \mid \Vert u \Vert_2 \leq 1\}$，其中$A$是一个非奇异方阵，$u$是一个单位球。也就是说我们通过方阵$A$旋转、拉伸这个单位球，最后再加上偏移量$x_c$得到椭球。在这个表达中我们可以假设$A$是对称、正定的。$A = P^{1/2}$时本式与上式相同。如果$A$是对称正定的奇异方阵，那么这个集合被称作退化椭球（degenerate ellipsoid），它的仿射维度等于$A$的秩。退化椭球与椭球都是凸的。

## 锥

!!! important "锥组合（conic combination）"

    空间$\mathbb{R}^n$中的点$x \in \mathbb{R}$如果满足
    
    $$x = \sum_{i=1}^n \theta_i x_i \ s.t. \ \forall \theta_i, \theta_i \geq 0$$
    
    则我们将其成为锥组合（非负线性组合）。

!!! important "锥集（conic set）"

    对于集合$C$，如果其中每一点$x \in C$并且
    
    $$\theta \geq 0$，都有$\theta x \in C$$
    
    那么我们将这个集合$C$称作一个锥（非负齐次）。

!!! important "锥包（conic hull）"

    集合$S$的锥包是所有该集合的点的锥组合所构成的集合，也即
    
    $$\{\sum_{i=1}^k \theta_i x_i \mid x_i \in S, \theta_i \geq 0\}$$

### 半正定锥

!!! important "对称矩阵"

    $$\mathbb{S}^n = \{X \in \mathbb{R}^{n \times n} \mid X = X^T\}$$

!!! important "对称半正定矩阵"

    $$\mathbb{S}^n_+ = \{X \in \mathbb{S}^n \mid X  \succeq 0\}$$

!!! important "对称正定矩阵"

    $$\mathbb{S}^n_{+ +} = \{X \in \mathbb{S}^n \mid X  \succ 0\}$$

??? help "试证明$\mathbb{S}^n_+$是一个凸锥"

    如果$\theta_1, \theta_2 \in \mathbb{R}_+$，$A, B \in \mathbb{S}^n_+$，那么$\theta_1 A + \theta_2 B \in \mathbb{S}^n_+$。

## 范式球与范式锥

对于$\mathbb{R}^n$中的任意范数$\Vert \cdot \Vert$，范式球和范式锥被定义为：

!!! important "范式球"

    $$B(x_c, r) = \{x \mid \Vert x - x_c \Vert \leq r\}$$

!!! important "范式锥"

    $$C(t) = \{(x, t) \mid \Vert x \Vert \leq t\} \subseteq \mathbb{R}^{n+1}$$

范式球和范式锥都是凸的。

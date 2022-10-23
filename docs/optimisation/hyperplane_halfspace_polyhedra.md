---
title: 超平面、半空间与多面体
summary: Hyperplane, Halfspace, and Polyhedra
authors:
    - zyc
date: 2020-08-18 16:06:19
categories:
    - Opsimisation
tags:
    - Opsimisation
    - Hyperplane
    - Halfspace
---

在本节中，我们介绍超平面、半空间与多面体。

## 超平面

!!! important "超平面"

    如果一个集合满足
    
    $$\{x \mid a^Tx = b\} \ s.t. \  a \in \mathbb{R}^n, a \neq 0, b \in \mathbb{R}$$
    
    那么我们将其称为一个超平面。

从解析来看，超平面是$x$分量中线性不定方程的解集；从几何来说，超平面也可以被解释为与给定向量$a$的内积为一特定值的点集；由于内积可以被看作是一个向量在另一个向量的投影，我们也可以将$a$理解为一个有超平面的 *法向向量*，那么常数$b$就是确定超平面距离原点的偏移量。将上式做一个简单的形变，我们可以得到$\{x \mid a^T (x - x_0) = 0\} = a^\perp + x_0$

??? help "超平面是凸还是仿射"

    仿射

### 分割超平面

!!! important "分割超平面"

    对于不相交的非空凸集$C, D$，存在$a \neq 0, b$使得：

    $$a^Tx \leq b \text{for} x \in C, \ a^Tx \geq b \text{for} x \in D$$

    那么我们称超平面$\{x \mid a^Tx = b\}$为$C$和$D$的分割超平面。

    严格分割超平面需要更多假设（比如$C$闭合，$D$是单元素集（singleton set））

### 支持超平面

!!! important "支持超平面"

    集合$C$在边界点$x_0$的支持超平面是

    $$\{x \mid a^tx = a^tx_0\}$$

    其中$a \neq 0, \ \forall x \in C, a^T \leq a^Tx_0$

!!! error "支持超平面定理"

    支持超平面只在凸的边界点存在

## 半空间

空间$S \subseteq \mathbb{R}^n$中的超平面将该空间划分成两个半空间。

!!! important "半空间"

    如果一个集合满足
    
    $$\{x \mid a^Tx \leq b\} \ s.t. \ a \neq 0$$
    
    那么我们将其称为一个半空间。

??? help "半空间是凸还是仿射"

    凸

## 多面体

一个 *多面体（polyhedra）* 指的是一个有限数目的线性等式与不等式的解集：

!!! important "多面体"

    $$P = \{x \mid a^T_jx \leq b_j,\ j = 1, 2, ..., m,\ c^T_jx = d_j,\ j = 1, 2, ..., p\}$$

我们可以发现，一个多面体实际上是一个有限数量的超平面与半空间的交集。仿射集（比如子空间、超平面、线）、射线、线段、半空间等都是多面体。

上式常被化简为$P = \{x \mid Ax \preceq b, Cx = d\}$。

??? hint "$\preceq$"

    符号$\preceq$表示$\mathbb{R}^n$中的 *向量不等（vector inequality）* 或者 *分量不等（componentwise inequality）*：$u \preceq v$表示$u_i \leq v_i \ s.t. \ i = 1, 2, ..., m$

??? help "多面体凸吗"

    凸

一个有边界的多面体有时被称为 *多胞形（polytope）*$^\star$。

$^\star$：有些人倾向于将多胞形与多面体反过来叫。

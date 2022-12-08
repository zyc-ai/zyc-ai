---
authors:
    - zyc
date: 2020-08-27 14:47:26
categories:
    - Computer Graphics
tags:
    - Computer Graphics
---

# 仿射与凸

在本节中，我们简要介绍仿射和凸的概念。

## 仿射

直线的定义想必初中都已经学过，这里我们简单复习一下：

!!! important "直线（line）"

    空间$\mathbb{R}^n$中的两个点$x_1, x_2, x_1 \neq x_2$可以唯一确定一条直线。这条直线可以被参数化的描述为
    
    $$x = \theta x_1 + (1 - \theta) x_2 \ s.t. \ \theta \in \mathbb{R}$$

我们很容易发现，$x = x_1$时，$\theta = 1$；$x = x_2$时，$\theta = 0$。由此，我们知道了线段被如何描述：

!!! important "线段（line segment）"

    穿过两点$x_1, x_2 \in \mathbb{R}^n, x_1 \neq x_2$的线段可以被参数化的描述为
    
    $$x = \theta x_1 + (1 - \theta) x_2 \ s.t. \ 0 \leq \theta \leq 1$$

通过变化，直线还可以被表达为$x = x_2 + \theta (x_1 - x_2) \ s.t. \ \theta \in \mathbb{R}$。这给了我们另一种解读--$x$是 *基点* $x_2$与 *方向* $x_1 - x_2$按参数$\theta$缩放之和。 因此，$\theta$给出了从$x_2$到$x_1$的分数。当$\theta$从0增大到1时，点$x$从$x_2$移动到$x_1$；当$\theta$在此区间以外时，点$x$位于$x_1$到$x_2$以外的线上。

在复习了直线之后，我们可以给仿射集做一个定义：

!!! important "仿射集"

    对于集合$C \subseteq \mathbb{R}$，若经过该集合上任意两点$x_1, x_2 \in C, x_1 \neq x_2$的直线上的点都在该集合中，那么我们称集合$C$为一个仿射集。

线性方程$\{x \mid Ax = b\}$的解即是一个仿射集，反过来每一个仿射集也都可以表示为一个线性方程系统的解集。因此，我们有时候将仿射集成为线性（linear）。

有同学可以发现，仿射集与线性子空间非常相似。事实上，我们可以将一个仿射集看作是一个线性子空间根据一个固定向量平移而得到的。对于仿射集$C$与其上一点$x_0$，集合$V = C - x_0 = \{x - x_0 \mid x \in C\}$是一个子空间。

??? help "证明$V = C - x_0$对于向量加法与标量乘法闭合"

    对于$v_1, v_2 \in V, \alpha, \beta \in \mathbb{R}$，我们有$v_1 + x_0, v_2 + x_0 \in C$，所以$\alpha v_1 + \beta v_2 + x_0 = \alpha (v_1 + x_0) + \beta (v_2 + x_0) + (1 -\alpha - \beta) x_0 \in C$，由于$C$是仿射集、$\alpha + \beta + (1 -\alpha - \beta) = 1, \alpha v_1 + \beta v_2 + x_0 \in C$，易得$\alpha v_1 + \beta v_2 \in V$。

因此，我们可以将仿射集$C$表述为$C = V + x_0 = \{v + x_0 \mid v \in V\}$， $x_0$为$C$上任意一点。我们将子空间$V$称作仿射集$C$相关的子空间，将子空间$V$的维度称作仿射集$C$的维度。

简单了解了直线与仿射集之后，我们可以延伸出仿射组合：

!!! important "仿射组合（affine combination）"

    对于线性组合$\sum_{i=1}^n \theta_i x_i$，若其满足
    
    $$\sum_{i=1}^n \theta_i = 1$$
    
    则我们称其为仿射组合。

仿射集$C$包含了该集合中任意点的仿射组合，也就是说，对于$x_1, x_2, x_n \in C, \sum_{i=1}^n \theta_i = 1$，$\sum_{i=1}^n \theta_i x_i \in C$。

我们可以发现，仿射组合其实可以被看成一个所有系数之和为1的特殊的线性组合。这样的特性使得我们可以抛弃原点，而将任意的点视为原点，我们都可以使用同样的线性组合去描述同一个点。

!!! example "🌰"
    对于原点以及空间上任意一点$p$，我们可以将向量$a,\ b$分别表述为$a + b$与$p + (a - p) + (b - p)$。由此，我们通过仿射组合去描述另一点时，两个描述分别为$\theta a + (1 - \theta) b$与$p + \theta (a - p) + (1 - \theta) (b - p) = p + \theta a - \theta p + (1 - \theta) b - (1 - \theta) p = \theta a + (1 - \theta) b$；我们很容易发现两个描述与其起始点没有关系。


集合$S$的仿射包$aff(S)$指的是包含集合$S$的最小仿射集，它被定义为:

!!! important "仿射包（affine hull）"

    $$aff(S) = \{\sum_{i=1}^k \theta_i x_i \mid k > 0, x_i \in S, \theta_i \in \mathbb{R}, \sum_{i=1}^n \theta_i = 1\}$$

也就是说，如果仿射集$C$有$S \subseteq C$，那么$aff(S) \subseteq C$。

## 凸

我们注意到到现在为止我们一直在讨论仿射，而没有进入真正的主题--凸。事实上，我们已经差不多学习了凸的所有概念了--仅仅将仿射的直线换成线段，我们就能得到凸。

!!! important "凸集"

    对于集合$C \subseteq \mathbb{R}$，若经过该集合上任意两点$x_1, x_2 \in C, x_1 \neq x_2$的<span style="color:green">线段</span>上的点都在该集合中，那么我们称集合$C$为一个凸集。

!!! important "凸组合（convex combination）"

    对于线性组合$\sum_{i=1}^n \theta_i x_i$，若其满足
    
    $\sum_{i=1}^n \theta_i = 1$<span style="color:green">并且$\forall \theta_i, \theta_i \geq 0$</span>
    
    则我们称其为凸组合。

!!! important "凸包（convex hull）"

    $conv(S) = \{\sum_{i=1}^k \theta_i x_i \mid k > 0,$ <span style="color:green">$x_i \geq 0$</span>$, \theta_i \in \mathbb{R}, \sum_{i=1}^n \theta_i = 1\}$
|
我们很容易想到，常见的三角形、方形、圆形都是凸的；而星形则是非凸的，因为任意两点之间存在有些点不在集合之内。

??? help "非凸集五角星的凸包是"

    凸集五边形。

??? help "如何判断一个函数是否是凸的"

    这个问题看似十分简单。我们只需要根据凸集的定义，选取集合中的每一个点对然后判断这两个点之间的线段上的点是否是凸的即可。对于一个有着$n$个点的集合，上述算法的时间复杂度仅仅为$O(n?n)$，这甚至是一个多项式时间的算法。但是这明显还有很大的改进空间。

在本节中，我们介绍保留凸性的运算，这些运算有助于判定一个集合是否凸以及构建一个凸集。

## 保凸运算

!!! important "交集"

    对于集合$S_1, S_2$，如果他们是凸集，那么$S_1 \cap S_2$也是凸集。

!!! important "仿射函数"

    如果函数$f: \mathbb{R}^n \rightarrow \mathbb{R}^m$是一个放射函数，那么：

    + $f$下的凸集的像也是凸的:
    
    $$S \subseteq \mathbb{R}^n \text{is convex} \Rightarrow f(S) = \{f(x) \mid x \in S\} \text{is convex}$$

    + $f$下的凸集的逆像也是凸的:
    
    $$C \subseteq \mathbb{R}^m \text{is convex} \Rightarrow f^{-1}(C) = \{x \mid f(x) \in C\} \text{is convex}$$

!!! important "透视和线性分数函数"

    透视函数 $P: \mathbb{R}^{n+1} \rightarrow \mathbb{R}^n$：

    $$P(x, t) = x / t, \quad dom(P) = \{(x, t) \mid t > 0\}$$

    线性分数函数 $f: \mathbb{R}^n \rightarrow \mathbb{R}^m$：

    $$f(x) = \frac{Ax + b}{c^T + d}, \quad dom(f) = \{x \mid c^Tx + d > 0\}$$

    透视函数与线性分数函数下的凸集的像和逆像也是凸的

这些属性扩展到无限个集合的交集中，也就是说，如果$S_\alpha$是凸集对于每一个$\alpha \in A$都成立，那么$\cap_{\alpha \in A}S_\alpha$也是一个凸集。

---
title: 凸凹
summary: Convex and Concave
authors:
    - Zhiyuan Chen
date: 2020-08-19 19:02:43
categories:
    - Opsimisation
tags:
    - Opsimisation
    - Convex Function
    - Concave Function
---

ok，在了解了基础知识之后，让我们开始入门：凸函数与凹函数

## 凸函数与凹函数

!!! important "凸函数"

    函数$f: \mathbb{R}^n \rightarrow \mathbb{R}$是一个凸函数，如果他的取值范围$\mathrm{dom} f$是一个凸集，并且

    $$f(\sum_{i=1}^n \theta_i x_i) \leq \sum_{i=1}^n f(\theta_i x_i)$$

    对于所有$x_i \in \mathrm{dom} f, \ \sum_{i=1}^n \theta_i = 1, \ \forall \theta_i, 0 \leq \theta_i \leq 1$都成立

我们可以注意到，$\sum_{i=1}^n \theta_i x_i$其实是一个凸组合。

!!! important "凸函数的几何意义"

    对于凸函数上任意两点$x,\ y$，该两点之间的连线不低于该凸函数。

??? help "所有的范数都是凸函数吗"

    是的

!!! important "严格凸函数"

    函数$f: \mathbb{R}^n \rightarrow \mathbb{R}$是一个严格凸函数，如果他的取值范围$\mathrm{dom} f$是一个凸集，并且

    $$f(\sum_{i=1}^n \theta_i x_i) \lt \sum_{i=1}^n f(\theta_i x_i)$$

!!! important "凹函数"

    如果函数$f$是个凸函数，那么函数$-f$是凹函数。

    如果函数$f$是严格凸函数，那么函数$-f$是严格凹函数。

### 凸函数的判定

!!! important "Restriction of a Convex Function to a Line"

    对于函数$f: \mathbb{R}^n \rightarrow \mathbb{R}$，若该函数在每一个方向上$g(t) = f(x + tv): \mathbb{R} \rightarrow \mathbb{R}$都是凸的，则该函数是凸的。

这个方式通过将判定一个定义域为$\mathbb{R}^n$的函数的凸性的问题转换为$n$个定义域为$\mathbb{R}$的问题来降低计算量，但其不适用于多变量函数。

??? example "f(X) = \log \det x"

    $$\begin{align} g(t) 
    &= \log \det (X = tV)\\
    &= \log \det X + \log \det (I + tX^{-1/2}VX^{1/2})\\
    &= \log \det X + \sum^n{i=1} \log (1 + t\lambda_i)\\
    \end{align}$$

    其中$\lambda_i$是$X^{-1/2}VX^{1/2}$的特征值。

    因为$g$在$t$中是凹的，所以f是凹函数。

!!! important "扩展值延申"

    函数$f: \mathbb{R}^n \rightarrow \mathbb{R}$的扩展值延申$\tlide{f}$被如下定义：

    $$\tlide{f} = 
    \begin{cases}\begin{align}
    f(x), & x \in \dom f\\
    \infty, & x \not \in \dom f
    \end{align}\end{cases}

!!! example "$\mathbb{R}上凸函数"

    凸函数：

    + 仿射：$ax + b$
    + 幂$^\star$：$x^a, \ s.t. \ a \geq 1 \text{or} a \leq 0$
    + 指数：$e^{ax}$
    + 负熵$^\star$：$x \log x$

    凹函数：

    + 仿射：$ax + b$
    + 幂$^\star$：$x^a, \ s.t. \ 0 \leq a \leq 1$
    + 对数$^\star$：$\log x$

    $^\star$：$x > 0$

我们可以注意到，所有的仿射函数是既凸又凹的。

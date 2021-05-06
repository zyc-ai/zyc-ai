---
title: 对偶锥与广义不等式
summary: Dual Cones and Generalised Inequality
authors:
    - Zhiyuan Chen
date: 2020-08-18 19:57:47
categories: 
    - Opsimisation
tags:
    - Opsimisation
    - Convexity
---

在了解了锥后，我们对锥做更进一步的讨论。

## 正常锥

!!! important "正常锥（proper cone）"

    一个锥$K \subseteq \mathbb{R}^n$被称作一个正常锥，当：

    + $K$是凸集
    + $K$闭合：包括他的边界
    + $K$是实锥（solid）：包括非空内部（interior）
    + $K$是尖锥（pointed）：不包括线（line）

??? question "正定锥是一个正常锥吗"

    是的

!!! example "正常锥"

    + 非负象限

    $$K = \mathbb{R}^n_+$$

    + 半正定锥

    $$K = \mathbb{S}^n_+$$

    + $[0, 1]$上的非负多项式

    $$K = \{x \in \mathbb{R}^n \mid \sum_{i=1}^n x_nt^{n-1} \text{for} t \in [0, 1\}$$

??? question "正常锥的对偶锥的对偶锥是他本身吗"

    是的

## 广义不等式

!!! important "广义不等式（generalised inequality）"

    一个由正常锥$K$定义的广义不等式满足：

    $$x \preceq_K y \quad \Longleftrightarrow \quad y - k \in K$$

    $$x \prec_K y \quad \Longleftrightarrow \quad y - k \in int(K)$$

!!! error "广义不等式是非线性的"

    我们可以有$x \preceq_K y$和$y \preceq_K x$同时成立

    但是其他属性都很相似，如$x \preceq_K y, u \preceq_K v \quad \Rightarrow x + u \preceq_K y + v$

!!! example "广义不等式"

    + 分量不等式（$K = \mathbb{R}^n_+$）

    $$x \preceq_{\mathbb{R}^n_+} y \quad \Longleftrightarrow \quad \forall i, x_i \leq y_i$$

    + 矩阵不等式（$K = \mathbb{S}^n_+$）

    $$X \preceq_{\mathbb{S}^n_+} Y \quad \Longleftrightarrow \quad Y - X \text{半正定}$$

### 对偶锥

!!! important "对偶锥"

    一个锥$K$的对偶锥是

    $$K^\star = \{y \mid \forall x \in K, y^Tx \geq 0\}$$

!!! example "对偶锥"

    + $K = \mathbb{R}^n_+$: $K^\star = \mathbb{R}^n_+$
    + $K = \mathbb{S}^n_+$: $K^\star = \mathbb{S}^n_+$
    + $K = \{(x, t) \mid \Vert x \Vert_2 \leq t\}$: $K^\star = \{(x, t) \mid \Vert x \Vert_2 \leq t\}$
    + $K = \{(x, t) \mid \Vert x \Vert_1 \leq t\}$: $K^\star = \{(x, t) \mid \Vert x \Vert_\inf \leq t\}$

    其中，前三个锥的对偶锥与其本身一致，我们将其称为自对偶锥（self-dual cone）。

!!! error "对偶正常锥"

    正常锥的对偶锥也正常，因此可以定义广义不等式：

    $$y \preceq_{K^\star} 0, \quad \Longleftrightarrow \quad \forall x \succeq_K 0, y^Tx \geq 0$$

### 对偶不等的最小与极小

!!! important "对偶不等的最小"

    $x$是集合$S$的最小元，当且仅当对于所有$\lambda \succ_{K^\star} 0$，$x$唯一最小化$S$上$\lambda^Tz$。

    $$\forall y \in S, \ x \preceq_K y$$

!!! important "对偶不等的极小"

    + 对于某些$\lambda \succ_{K^\star} 0$，如果$x$最小化$S$上的$\lambda^Tz$，那么$x$是集合$S$的一个极小元。

    + 如果$x$是集合$S$的极小元，那么存在一个不为零的$\lambda \succ_{K^\star} 0$使得$x$最小化$S$上$\lambda^Tz$。

    $$\forall y \in S, \ y \preceq_K x \Rightarrow y = x$$

$-\lambda$定义了支持超平面。

??? help "一个集合必定有最小元吗"

    不是

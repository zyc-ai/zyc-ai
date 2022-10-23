---
title: 线性代数
summary: 线性代数
authors:
    - zyc
date: 2019-08-28 23:57:38
categories:
    - master
    - mathematics
    - linear algebra
tags:
    - master
    - mathematics
    - linear algebra
    - vector
    - matrix
    - group
---

# 线性代数

线性代数是现代机器学习算法中最重要的一个部分。本文将从群、向量的定义开始，引入向量子空间，并解释列空间、零空间以及其他内容。

数学源于群。

## 群

**定义 1.1** - 群

群$(G, \otimes)$是由一个集合$G$及一个运算$\otimes$所构成且符合下列四个性质的代数结构：

1. 闭合性 - 对于所有$x, y \in G$，都有$x \otimes y \in G$。

2. 结合律 - 对于所有$x, y, c \in G$，都有$(x \otimes y) \otimes c = (x \otimes y) \otimes c$。

3. 单位元 - 对于所有$x \in G$，存在$e \in G$，使得$x \otimes e = x$，且$e \otimes x = x$。

4. 逆元 - 对于所有$x \in G$，存在$y \in G$，使得$x \otimes y = e$，且$y \otimes x = e$。

在此基础之上我们还可以定义阿贝尔群。

**定义 1.2** - 阿贝尔群

阿贝尔群$(G, \oplus)$是由一个集合$G$及一个运算$\oplus$所构成且符合下列四个性质的代数结构：

1. 交换律 - 对于所有$x, y \in G$，都有$x \oplus y = y \oplus x$。

我们常见的加法、乘法都定义于阿贝尔群上。

## 向量

什么是向量？初中数学告诉我们：具有方向的量。本文讨论的向量则相对来说更抽象一些。具体而言，本文当中的向量定义如下：

**定义 2.1** - 向量

1. 对于所有$x$和$y$，$x, y$在加法下闭合。

2. 对于所有$x$和$\lambda \in \mathbb{R}$，$\lambda x$在乘法下闭合。

基于上述定义，很多直觉上并不是向量的东西其实也是向量，比如多项式。

但在应用当中，我们更常关注定义在$\mathbb{R^n}$上的向量。因为大多数计算机科学涉及到的向量内容是定义在$\mathbb{R^n}$上的。

有关矩阵及其加法乘法逆转置对称等等的定义，互联网上已有很多内容，此处不再赘述。

**定义 2.2** - 一般线性群

1. 非奇异矩阵$\mathit{A} \in \mathbb{R^{n \times n}}$以及他的矩阵乘法运算构成一般线性群，写做$GL_n\mathbb{R}$，或者$GL(n, \mathbb{R})$。

*对于$n \geq 2$时，一般线性群为非阿贝尔群。*

**定义 2.3** - 向量空间

向量空间$V = (\mathcal{V}, +, \cdot)$是由一个集合$\mathcal{V}$以及在这个集合上定义的两个运算：

<center>
$+ : \mathcal{V} \times \mathcal{V} \rightarrow \mathcal{V}$

$\cdot : \mathbb{R} \times \mathcal{V} \rightarrow \mathcal{V}$
</center>

且符合下列四个性质的代数结构：

1. $V = (\mathcal{V}, +)$是一个阿贝尔群。

2. 分配律 -

    a. 对于所有$\lambda \in R$，$x, y \in \mathcal{V}$，都有$\lambda \cdot (x + y) = \lambda \cdot x + \lambda \cdot y$

    b. 对于所有$\lambda \mu \in R$，$x \in \mathcal{V}$，都有$(\lambda + \mu) \cdot x) = \lambda \cdot x + \mu \cdot x$

3. 结合律 - 对于所有$\lambda \mu \in R$，$x \in \mathcal{V}$，都有$\lambda \cdot (\mu \cdot x) = (\lambda \cdot \mu) \cdot x$

4. 单位元 - 对于所有$x \in \mathcal{V}$，都有$1 \cdot x = x$

**定义 2.4** - 向量子空间

对于向量空间$V = (\mathcal{V}, +, \cdot)$，若向量空间$U$满足$\mathcal{U} \subseteq \mathcal{V}, \mathcal{U} \neq \emptyset$，那么我们称$U = (\mathcal{U}, +, \cdot)$是$V$的向量子空间。

**定义 2.5** - 张成与生成集

对于向量空间$V = (\mathcal{V}, +, \cdot)$和向量集$\mathcal{A} = \{x_1, \ldots, x_n\} \subseteq \mathcal{V}$，若每一个向量$\mathcal{v} \in \mathcal{V}$都可以表示为$x_1, \ldots, x_n$的线性组合，那么我们称向量集$A$是向量空间$\mathcal{V}$的生成集，向量集A$\mathcal{A}$的向量们的线性组合构成的集合称为A的张成。

**定义 2.6** 基

对于向量空间$V = (\mathcal{V}, +, \cdot)$和向量空间$V = (\mathcal{V}, +, \cdot)$的生成集$\mathcal{A} = \{x_1, \ldots, x_n\} \subseteq \mathcal{V}$，若不存在更小的集$B \subset A \subseteq \mathcal{V}$张成$\mathcal{V}$，那么我们称$\mathcal{A}$为最小生成集。每个$V$的线性无关的生成集都是最小的，也被称为$V$的基。

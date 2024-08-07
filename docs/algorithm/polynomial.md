---
authors:
    - zyc
date: 2019-10-21 18:53:01
categories:
    - Algorithm
tags:
    - Algorithm
---

# 多项式（Polynomial）

在此前的文章当中我们通过n位数乘法运算简要的介绍了算法复杂度的计算。在本文当中我们将对多项式的计算（evaluation）、加法（addition）和乘法（multiplication）提出算法。

!!! important "多项式"

    由变量与系数通过有限次加减法、乘法以及自然数幂次的乘方运算得到的整式。

    形如$A(x) = a_0 + a_1x + a_2x^2 + ... + a_{n-1}x^{n-1}$。
    
    其中，$x$是多项式的变量、$a_0, a_1, a_2, ..., a_{n-1}$是多项式的系数，$n$被称为多项式的次数。

## 多项式的表示（Representation）

一般来说，多项式可以通过三种方法进行表示。它们分别是：

+   !!! example "系数"

        $A(x) = a_0 + a_1x + a_2x^2 + ... + a_{n-1}x^{n-1}$
        
        其中多项式的系数可以表示为长度为$n$的向量$\vec{a} = a_0, a_1, a_2, ..., a_{n-1}$

+   !!! example "根"

        $c(x-r_0)(x-r_1)(x-r_2)(x-r_3)(x-r_{n-1})$

+   !!! example "样本（点值）"

        $(x_k, A(x_k))$

        选取$n$个值不同的数$x_0, x_1, x_2, ..., x_{n-1}$对多项式进行求值，得到$A(x_0), A(x_1), A(x_2), ..., A(x_{n-1})$。

        我们可以将其转换为范德蒙矩阵形式，
        $\mathbf{V} = \begin{pmatrix}1&x_0&x_{0^2}&\cdots &x_{0^{n-1}}\\ 1&x_1&x_{1^2}&\cdots &x_{1^{n-1}}\\ 1&x_2&x_{2^2}&\cdots &x_{2^{n-1}}\\ \vdots &\vdots &\vdots &\ddots &\vdots \:\\ 1&x_{n-1}&x_{n-1^2}&\cdots \:&x_{n-1^{n-1}}\end{pmatrix}\begin{pmatrix}a_0\\ a_1\\ a_2\\ \vdots \:\\ a_{n-1}\end{pmatrix} = \begin{pmatrix}A(x_0)\\ A(x_1)\\ A(x_2)\\ \vdots \:\\ A(x_{n-1})\end{pmatrix}$

我们很容易发现，不同的运算对不同的表示法来说，复杂度是不同的。我们可以得到这样的计算复杂度表：

| 运算 	| 系数     	| 根          	| 样本     	|
|------	|----------	|-------------	|----------	|
| 计算 	| $O(n)$   	| $O(n)$      	| $O(n^2)$ 	|
| 加法 	| $O(n)$   	| $O(\infty)$ 	| $O(n)$   	|
| 乘法 	| $O(n^2)$ 	| $O(n)$      	| $O(n)$   	|

此前我们了解到我们会期望一个复杂度为$O(n\log n)$或更低的算法。通过观察这两个表格，我们发现对于两个多项式来说，我们更希望使用系数表示去完成计算和加法、使用根表示去完成计算和乘法、使用样本表示去完成加法和乘法。

那么，这三种表示法之间互相转换的复杂度如何呢？我们可以有这样的转换复杂度表：

| 运算 	| 系数         	| 根          	| 样本         	|
|------	|--------------	|-------------	|--------------	|
| 系数 	| -            	| $O(\infty)$ 	| $O(n\log n)$ 	|
| 根   	| $O(n)$       	| -           	| $O(n\log n)$ 	|
| 样本 	| $O(n\log n)$ 	| $O(\infty)$ 	| -            	|

我们可以发现，对于两个多项式来说，我们希望将样本表示转换为系数表示来完成加法，将系数表示转换为样本表示来完成乘法 -- 这样能将复杂度从$O(n^2)$降至$O(n\log n)$，而这正是我们想要的（根表示的乘法复杂度也很好，但我们通常不希望去实现一个复杂度为$O(\infty)$的转换算法

所以，我们需要一个在系数表示法和样本表示法之间转换的算法。

## 快速傅里叶变换（FFT）

### 离散傅里叶变换（DFT）

### 离散傅里叶逆变换（IDFT）


---
title: 递推方程（Recurrence Relation）
summary: 递推方程（Recurrence Relation）
authors:
    - Zhiyuan Chen
date: 2019-11-01 02:20:41
categories:
    - algorithm
    - Recurrence Relation
tags:
    - algorithm
    - Recurrence Relation
    - Master Theorem
---

!!! note "递推方程（递推关系）"

    当一个或多个初始项被给出时，递归地定义一序列或一个多维数组的值的方程。

    序列或数组的新项被定义为之前项的一个方程。

递推关系在算法当中非常常见。我们通常将递推关系的算法称作递归算法。在本章的[树](../tree)一文中，我们的高度、插入和删除都是通过递归来实现的。为了便于更好的描述，在本文当中，我们将以Karatsuba算法作为例子:

!!! example "Karatsuba算法"

    !!! success "Karatsuba"

        ```python
        def karatsuba(x, y):
        x_len = len(str(x))
        y_len = len(str(y))

        if x_len == 1 or y_len == 1:
            return x * y

        else:
            n = ceil(max(len_x, len_y) / 2)
            a = floor(x / 10**n)
            b = x % 10**n
            c = floor(y / 10**n)
            d = y % 10**n
            ac = karatsuba(a,c)
            bd = karatsuba(b,d)
            e = karatsuba(a+b, c+d) - ac - bd

            return ac * 10**(n*2) + (e * 10**n) + bd
        ```
    
    通过观察,对于两个$n$位数的相乘问题，我们通过上述操作将其转换为三个$\frac{n}{2}$位数的相乘问题。其递推方程即为$T(n) = \left\{\begin{array}{lr}3T(n/2) + f(n), & n > 1 \\ 1, & n = 1\end{array}\right.$。

对递推方程求解有很多办法，包括：

+ 迭代法
+ 差消法
+ 迭代树
+ 主定理

## 迭代法

!!! 迭代法

    不断用递推方程的右部替代左部，直到出现初值停止迭代。

对于Karatsuba算法，我们可以进行如下迭代：

$\begin{split} T(n) &= 3T(n/2) + f(n) \\ &= 3[3T(n/4) + f(\frac{n}{2})] + f(n) \\ &= 3^2 T(n/2^2) + f(\frac{3n}{2}) \\ & \quad \vdots \\ &= 3^{\log_2 n} \times T(1) + \sum_{i=2}^{n} f(n + \frac{\log_2 i \cdot n}{2^{\log_2 i}})) \\ &= 3^{\log_2 n} + \sum_{i=2}^{n} f(n + \frac{\log_2 i \cdot n}{2^{\log_2 i}}) \\ &= n^{\log_2 3} + O(n) \\ &= O(n^{\log 3})\end{split}$

## 差消法

对于高阶递推方程来说，迭代会变得非常困难。我们通常会通过差消法将问题进行化简，随后再通过迭代法求解。

## 迭代树

迭代树顾名思义也跟迭代法有很大关系。其通过树的形式将迭代法展开，更主要用于可视化。此处不再赘述。

## 主定理(Master Theorem)

倘若一个递推方程符合如下形式：

$$T(n) = aT(\frac{n}{b}) + f(n), (a \geq 1, b \ge 1)$$

其中，$a$表示规约后子问题的个数，$\frac{n}{b}$表示规约后子问题的规模，$f(n)$表示将问题规约为子问题及将规约后子问题的答案重组成原问题的答案的过程。则这个递推方程可通过主定理求解。

!!! note "主定理"

    $$T(n) = \left\{\begin{array}{clr}\Theta(n^{log_b a}), & f(n) = O(n^{log_b a - \epsilon}), & \epsilon > 0 \\ \Theta(n^{\log_b a} \log^{k+1} n), & f(n) = \Theta(n^{\log_b a} \log^k n), & k \geq 0 \\ \Theta(f(n)), & f(n) = \Omega(n^{\log_b a + \epsilon}), & \epsilon > 0\end{array}\right.$$

对于Karatsuba算法，$f(n) = O(n) = O(n^{log_b a - (log_b a - 1))}, \ \text{i.e.} \ \epsilon = log_b a - 1$。

故Karatsuba算法的复杂度为$\Theta(n^{log_b a})$，也即$\Theta(n^{log_2 3})$。

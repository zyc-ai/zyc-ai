---
authors:
    - zyc
date: 2019-08-06 19:39:28
categories:
    - Algorithm
tags:
    - Algorithm
---

# 算法（Algorithm）

我们都知道，计算机科学属于应用数学的分支。算法，自然是计算机科学最重要的一部分。那么，什么是算法呢？

Algorithm（算法），源自于古法语单词Algorisme，原意是阿拉伯数字系统。这和我们今天所说的算法自然有着本质上的区别。通常情况下，我们将算法定义为：

!!! quote "算法"

    由一系列计算步骤构成的将输入转换为输出的有限且确定的方法

    ???+ abstract "有限"

        算法能在有限步停机

    ???+ abstract "确定"

        算法的每一步计算都是确定的

算法与程序无关。有很多程序并不是算法，譬如神经网络便并不满足以上定义。算法也与编程语言无关。使用某种语言写出一个程序只是表达算法的一种方式--你甚至可以用自然语言去表达算法，如果你愿意的话。在本章当中，我们将使用Python来实现所有算法。现实当中你可能并不想这么做--以C#、C++为代表的静态类型语言提供了方法重载等高级功能，能使你更高效的去实现某个算法。我们在这里选择Python仅仅是因为我懒得打括号。

本章虽然名为算法，然而绝大多数算法都需要恰当的组织数据。因此，数据结构可以说是同等重要的。我们在此沿用《算法（第四版）》中的对数据结构的定义：

!!! quote "数据结构"

    数据结构是算法的副产品或是最终产物

本章节内容参考了许多资料，包括Robert Sedgewick和Kevin Wayne合著的《算法（第四版）》、Jon Kleinberg和Éva Tardos的《算法设计》、邓俊辉的《数据结构》、Jeff Erickson的《算法》、Thomas H. Cormen、Charles E. Leiserson、Ronald L. Rivest、和Clifford Stein合著的《算法导论》、Mark Allen Weiss的《数据结构与算法分析》、以及Donald Knuth的《计算机程序设计艺术》（按照推荐降序排列）以及许多线上与线下课程。需要注意的是，本章并不意图成为一本新的算法教材--他们所撰写的书籍要远超我的水平。本章仅意在使用通俗易懂的语言来对其进行简单的描述以给你一个直觉。如果你有志于学习算法，我们强烈建议你从第一本书开始看起。
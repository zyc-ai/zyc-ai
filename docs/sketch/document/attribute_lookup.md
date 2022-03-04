---
title: 属性访问慢吗？
summary: Is attribute lookup slow?
authors:
    - Zhiyuan Chen
date: 2022-01-11 21:24:47
categories:
    - sketch
    - document
tags:
    - sketch
    - document
    - Python
---

!!! abstract "前言"

    昨天组群里老板转了一篇有关Python代码优化的文章。尽管我还挺喜欢的，但我发现他特别指出`append = list.append`可以提速。仔细想想似乎有点儿道理的样子，但是真的是这样吗？以及，真的有这个必要吗？

## 介绍

本文以`append = list.append`为例对循环中的属性访问开销进行分析，给出了两种操作的抽象语法树与反编译结果，并对两种方法的运行时间进行了测量。结果表明，`append = list.append`确实可以显著提升运行速度。尽管如此，我们认为，对于日常使用环境，这种性能提升非常微小，无法弥补其附带的可读性与可维护性的下降。

## 分析

Python当中几乎任何东西都是一个字典，在访问实例的属性时实际上调用的是`__getattribute__()`魔法函数（如果没找到或者没定义则会降级到`__getattr__()`魔法函数）来从类字典中查找属性。因此，在循环中频繁访问实例的属性理论上会引入额外的函数调用开销和属性查找开销。

## 测试代码

首先，我们做两个最小工作示例，实验组使用`append = list.append`，而控制组则直接调用`list.append`。

!!! example "实验组"

    ```python
    def append():
        lst = []
        append = lst.append
        for i in range(1000000):
            append(i)
        return l
    ```

!!! example "控制组"

    ```python
    def list_append():
        lst = []
        for i in range(1000000):
            lst.append(i)
        return l
    ```
def list_append():
    lst = []
    for i in range(1000000):
        lst.append(i)
    return l

## 抽象语法树

在构建抽象语法树中，实验组多了一个赋值以保存函数引用；此外循环体中实验组的循环体的函数为`Name(id='append', ctx=Load())`，而控制组为`func=Attribute(value=Name(id='lst', ctx=Load()), attr='append', ctx=Load())`，也即实验组额外的赋值的值。

!!! example "实验组"

    ```python
    Module(
        body=[FunctionDef(
            name='append',
            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
            body=[
                Assign(targets=[Name(id='lst', ctx=Store())], value=List(elts=[], ctx=Load()), type_comment=None),
                Assign(
                    targets=[Name(id='append', ctx=Store())],
                    value=Attribute(value=Name(id='lst', ctx=Load()), attr='append', ctx=Load()),
                    type_comment=None
                ),
                For(
                    target=Name(id='i', ctx=Store()),
                    iter=Call(func=Name(id='range', ctx=Load()), args=[Constant(value=1000000, kind=None)], keywords=[]),
                    body=[Expr(value=Call(
                        func=Name(id='append', ctx=Load()),
                        args=[Name(id='i', ctx=Load())],
                        keywords=[]
                    ))],
                    orelse=[],
                    type_comment=None
                ),
                Return(value=Name(id='l', ctx=Load()))
            ],
            decorator_list=[],
            returns=None,
            type_comment=None
        )],
        type_ignores=[]
    )
    ```

!!! example "控制组"

    ```python
    Module(
        body=[FunctionDef(
            name='list_append',
            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
            body=[
                Assign(targets=[Name(id='lst', ctx=Store())], value=List(elts=[], ctx=Load()), type_comment=None),
                For(
                    target=Name(id='i', ctx=Store()),
                    iter=Call(func=Name(id='range', ctx=Load()), args=[Constant(value=1000000, kind=None)], keywords=[]),
                    body=[Expr(value=Call(
                        func=Attribute(value=Name(id='lst', ctx=Load()), attr='append', ctx=Load()),
                        args=[Name(id='i', ctx=Load())],
                        keywords=[]
                    ))],
                    orelse=[],
                    type_comment=None
                ),
                Return(value=Name(id='l', ctx=Load()))
            ],
            decorator_list=[],
            returns=None,
            type_comment=None
        )],
        type_ignores=[]
    )
    ```

## 反编译

在反编译结果中，实验组通过`LOAD_ATTR`来将`append`保存在局部，然后通过`CALL_FUNCTION`指令进行`append()`；而控制组则是通过`LOAD_METHOD`和`CALL_METHOD`指令进行`append()`。我们可以想到，实验组会比控制组少`n-3`条指令，因此，实验组的速度约是对照组速度的1.2倍。

!!! example "实验组"

    ```
    2           0 BUILD_LIST               0
                2 STORE_FAST               0 (lst)

    3           4 LOAD_FAST                0 (lst)
                6 LOAD_ATTR                0 (append)
                8 STORE_FAST               1 (append)

    4          10 LOAD_GLOBAL              1 (range)
                12 LOAD_CONST               1 (1000000)
                14 CALL_FUNCTION            1
                16 GET_ITER
            >>   18 FOR_ITER                12 (to 32)
                20 STORE_FAST               2 (i)

    5          22 LOAD_FAST                1 (append)
                24 LOAD_FAST                2 (i)
                26 CALL_FUNCTION            1
                28 POP_TOP
                30 JUMP_ABSOLUTE           18

    6     >>   32 LOAD_GLOBAL              2 (l)
                34 RETURN_VALUE
    ```

!!! example "控制组"

    ```
    2           0 BUILD_LIST               0
                2 STORE_FAST               0 (lst)

    3           4 LOAD_GLOBAL              0 (range)
                6 LOAD_CONST               1 (1000000)
                8 CALL_FUNCTION            1
                10 GET_ITER
            >>   12 FOR_ITER                14 (to 28)
                14 STORE_FAST               1 (i)

    4          16 LOAD_FAST                0 (lst)
                18 LOAD_METHOD              1 (append)
                20 LOAD_FAST                1 (i)
                22 CALL_METHOD              1
                24 POP_TOP
                26 JUMP_ABSOLUTE           12

    5     >>   28 LOAD_GLOBAL              2 (l)
                30 RETURN_VALUE
    ```

## 实验

我们通过`timeit.repeat`来对两个设置分别进行实验统计实际运行时间。每项实验总共重复5组，每组实验进行1000次。表1展示了我们的实验结果。

| 实验   | 第一次            | 第二次             | 第三次            | 第四次             | 第五次            |
|--------|-------------------|--------------------|-------------------|--------------------|-------------------|
| 实验组 | 39.37634929001797 | 39.624791437992826 | 39.47455425403314 | 39.28507260803599  | 38.99280332797207 |
| 控制组 | 48.0064105510246  | 48.270529969013296 | 48.02866995194927 | 48.182155867049005 | 48.1983303729794  |

大量实验表明，实验组与对照组的速度之比与预期相符。

## 结论

通过`append = list.append`的方式降低循环中的属性访问可以减少`n-3`条执行指令，这对程序的效率有正面影响。尽管如此，相对于其额外引入的代码造成的可读性与可维护性的下降是得不偿失的。

</br>

辛丑年腊月

于丹棱街5号

---
title: 贡献
summary: 贡献
authors:
    - Zhiyuan Chen
date: 2019-09-18 02:55:15
categories: 
    - master
    - contribute
tags:
    - master
    - contribute
---

在你做出任何贡献之前，我们强烈建议你先阅读这篇文章，确保你了解格式信息并掌握MkDocs的语法。

## 语法

### 特殊语法

#### 代码

代码块应当显示使用\` \`和

\`\`\`

\`\`\`

进行指定。

除非特殊情况，应当注明使用的语言以使代码着色器正常工作。

#### LaTeX

LaTeX公式应当显示使用\$ \$和

\$\$

\$\$

进行指定。

### 段落

#### 标题

每个文件应当有且只有一个一级标题--题目。

题目应当于文件描述部分的`title`中注明。

#### 换行

所有标题、行外代码、行外LaTeX前后以及文字段落之间空一行。

禁止为了视觉效果而刻意空行。

#### 分隔

所有文件使用四个空格作为一个制表符。

文件内无用的分隔符应当删去

#### 空白行

如需显示空白行时，应当使用`<br/>`

## 文件

!!! caution "注意"
    所有文件名及目录名均应当使用小写+下划线。

#### 文件夹

每一个章节应当创建单独的目录。如内容不足以构成章节，则应将文件存放于`master`、`document`或`sketch`目录中。

#### 警告框

前言与后记均应当使用`abstract`警告框注明，且应当位于文首和文末。

## 编撰

### 撰写

撰写文章当中，应尽量避免在一个文件当中撰写太多或太少内容，以数分钟能完成浏览为佳。复杂内容可以分多个系列进行讨论。

### 多语言

计算机科学中的很多文章均涉及中、英双语。在编撰文章时，应注意以下两点：

1. 语言纯洁

除非特殊情况，禁止在一种语言当中夹杂另一种语言。

翻译应当尽量使用行业统一的术语，比如[机器学习术语表](https://developers.google.cn/machine-learning/glossary/?hl=zh-CN)。

???+ 例外情况

    + 广为人知的名字
    + 没有可信的翻译

2. 准确翻译

翻译应当尽可能保证准确，不破坏原文意思。

???+ 不过度翻译
    能根据前后文得出的内容不需特意添加。

    严禁将"I love you"翻译为“今夜月色很美”。

很高兴能与你一起分享知识。
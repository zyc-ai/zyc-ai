---
authors:
    - zyc
date: 2019-08-08 16:00:02
categories:
    - Natural Language Computing
tags:
    - Natural Language Computing
---

# 文本处理（Text Processing）

很多时候，自然语言处理的第一步总是文本处理。随后我们再对完成文本处理后的内容进行进一步操作。

一般来说，文本处理可以分成以下四个步骤：

+ 分词（Tokenization）
+ 归一化（Normalization）
+ 词干提取（Stemming）和词形还原（Lemmatization）
+ 停用词（Stop Word）

我们会在接下来逐个讨论。

## 分词（Tokenization）

分词指的是将字符串的序列分割成一个一个单词。

听起来这个很简单，尤其是针对英语这样最小单位为单词的语言来说。`str.split()`了不就得了么？但这样的分词会导致词序的丢失，我们也将这样分词的结果称为词袋模型（bag-of-words model）--装满一堆单词的袋子，非常形象。这个模型对于信息检索来说还很有用，但对于自然语言处理来说，还差了些什么。

## 归一化（Normalization）

归一化指的是将单词的不同形态甚至于同义的不同单词进行合并。

## 词干提取（Stemming）和词形还原（Lemmatization）

词干提取（Stemming）和词形还原（Lemmatization）非常相似，他们的目标都是将单词的屈折形态或派生形态简化或归并为词干（stem）。对于单词拥有单复数形式以及语态变化的语言来说，这个步骤是十分必要的。但对于什么都没有的中文来说，还是直接跳到下一步的停用词更实在一些。

!!! note "词干提取"
    词干提取主要通过对单词进行缩减而达到目标。部分情况下，缩减后的单词将不再是该语言的单词之一，这使得其粒度相对更粗。所以词干提取主要应用于信息检索领域。

!!! note "词形还原"
    词形还原主要通过将单词还原回原形而达到目标。相比而言，这将要复杂不少，但结果一定是字典当中存在的词汇，粒度更细。所以词形还原主要应用于自然语言处理领域。

## 停用词

停用词指的是中文当中的“的”、“吗”等等，英文当中的“the”、“a”、“an”、“to”、“of”等词语。这些词会在文章当中大量出现，而实际上对于计算机来说却很少有意义。通常情况下我们都会选择将其忽略掉以提高性能。

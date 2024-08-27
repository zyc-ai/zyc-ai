---
authors:
  - zyc
date: 2023-08-25 18:03:45
categories:
  - sketch
tags:
  - sketch
---

# CHANfiG: Easier Configuration

!!! abstract "摘要"

    一年之前，我们分享了 CHANfiG 在过去一年的[开发经历](./chanfig-2023.md)。

    不久之前，我们刚发布了 v0.0.105。在这15个版本中我们添加了 77 次提交。

    虽然还有不少更新，但我们已经进入了一个接近稳定的状态。

    今天，我还想跟大家分享一下这一年当中我们都做了一些什么。

## 数据类

[PEP 557](https://peps.python.org/pep-0557/) 提出了数据类的概念，相关 API 在 Python 3.7 中被正式引入。

7年之后的今天，数据类已经开始获得应用。比如 :hugs: Transformers 就广泛使用了数据类来作为配置。

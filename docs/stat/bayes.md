---
title: 贝叶斯
summary: 贝叶斯
authors:
    - Zhiyuan Chen
date: 2020-03-03 23:48:02
categories: 
    - statistics
tags:
    - Machine Learning
    - Bayes
---

从某种意义上来说贝叶斯定理可以算是现代人工智能的基石。

if we choose a prior such that on the observation of the data the posterior stays within the same family, than we say it's conjugate

we say that the prior and likelihood of conjugate of conjugate to one another

if you have a gaussian prior on P of W, and you observe some data, and your posterior is still gaussian but with a different parameter (mean and convariance matrix)
once we multiplied the prior by the likelihood and renormalise, if we end up with just a different gaussian, than our likelihood is conjugate to that gaussian prior 

---
authors:
    - zyc
date: 2022-06-21 11:39:21
categories:
    - Transformer
tags:
    - Transformer
    - Visual Computing
    - Vision Transformer
---

# Early Convolutions Help Transformers See Better

## 动机

ViT[@ViT]模型的可优化性与传统CNN相比较差：他对优化器（AdamW v.s. SGD）、模型大小、数据集、训练超参和训练计划很敏感。

ViT在BERT主干网络之前使用一个$p$-strided $p \times p$卷积（`patchify stem`）来将2D图像切成1D图像块（默认p=16）。这种大步长大卷积核的设计与现行的CNN设计原则不同。

本文揭示了ViT的训练不稳定性与这种`patchify stem`相关。
通过将这一个卷积层替换成一组$2$-strided $3 \times 3$卷积层（`convolutional stem`），ViT的训练稳定性取得了显著的提升，并且最高性能也取得了一定提升（~ 1 - 2% ImageNet-1k top-1准确率）。
这种提升对不同规模的模型（1G - 36G Flops）和不同规模的数据集（ImageNet-1k - ImageNet-21k）均适用。

## 原创

本文的核心贡献在于对ViT进行分析。
此前工作[@Visformer; @CeiT; @LeViT; @CvT]使用了与本工作类似的`convolutional stem`，但是他们着重于将局部性先验引入ViT，而没有对可优化性进行分析。
ViT也尝试了使用ResNet的前3个阶段和BERT的混合模型，但这样的`convolutional stem`有40个卷积层，本文尝试了一个更轻量化的模型。

本文指出，在`stem`中引入仅~5个卷积层即可显著提升ViT的可优化性。

## 方法

`convolutional stem`采用了类似于VGG[@VGG]的结构，一组$3 \times 3$卷积后跟一个$1 \times 1$卷积。$3 \times 3$卷积总共有两种：

1. 步长为2，通道数加倍
2. 步长为1，通道数不变

对于不同大小的ViT（按照GFlops）计算，本文使用的`convolutional stem`的输出通道分别是：

+ 1GF: [24, 48, 96, 192]
+ 4GF: [48, 96, 192, 384]
+ 18GF/36GF: [64, 128, 128, 256, 256, 512]

## 实验

TODO

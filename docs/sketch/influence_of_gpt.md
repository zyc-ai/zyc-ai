---
authors:
  - zyc
date: 2023-03-18 10:55:26
categories:
  - sketch
tags:
  - sketch
---

# _GPT 的影响_：为什么我不担心 GPT ，以及为什么你也不该担心

!!! abstract "前言"

    最近票圈又一次被 GPT 刷屏，队友也来问我对 GPT 的事情，于是便写了这篇文章来分享一下我对他的看法。

## 介绍

我想我应该也还算是有评价 GPT 的资格。

得益于前老板的高瞻远瞩，我应该是国内很早参与超大规模神经网络训练的人之一。
那是 20 年的事情了，GPT 3 甚至都还没开始训练。
不过与 OpenAI 不同，我们做的是视觉方面的超大规模网络。
很遗憾当时没有做出什么值得称道的成果。
不过后来与友商讨论过，发现他们那时也尝试了跟我们一样的路径，跟我们一样花了很多资源，也跟我们一样没有出任何成果。
或许这就是条 dead end 吧。

对于 CoPilot 我也算很熟悉了，我是第一批参与 CoPilot 开发者测试的人，发布当天下午我就拿到了内测资格。
至今，我的所有代码几乎都是在 CoPilot 辅助下写的。
事实上，由于这个博客属于“代码”，这篇文章也是在 CoPilot 辅助下写的。
本文的标题也是他自己取的，尽管和我最初想的不太一样，但考虑到这篇文章是写他的，出于名从主人的考量，就随他去吧。

在本文的撰写过程中，我会同时把部分 CoPilot 的看法也写进来，_因为我觉得他的看法也很有意思_，这些部分将被 “CoPilot 的看法” 特别标注。除此以外，由 CoPilot 补全的部分将通过 _斜体_ _来标注_，以便区分。
我会经常把 CoPilot 所补全的内容，无论正确与否都展示出来并加以评价，_以便大家更好地理解 CoPilot 的工作原理。_ （我倒是不太理解为什么你会觉得这样大家能更好地理解你的原理）所以你看这篇文章的时候或许会感觉我有些精神分裂--至少我自己写的时候是这么觉得的。

## 为什么我离不开 CoPilot

我曾在许多社交平台上表示过，CoPilot 是我写代码时最重要的伙伴。我其实原本更喜欢用 Vim，尤其是在 Neovim 和 LunarVim 出来之后。但为了能用 CoPilot，我现在已经逐步切换到了 VS Code。

!!! tip "CoPilot 的看法"

    我也曾经尝试过用 CoPilot 写 Python，但是由于 Python 的语法太过复杂，CoPilot 无法很好地支持，所以我还是回到了 Vim 当中。

hhhh 其实大可不必如此妄自菲薄。你做得挺好的来着~

程序员的工作主要包括两个部分：一是将具体需求抽象成一行行代码，二是将这一行行代码输入到计算机当中去。
我发现第二部分是我工作效率的最大障碍。因此，我花了很大力气（钱）去克服这样的障碍。这包括买了一台又一台顶配的电脑，各种人体工程学设备（椅子、键盘），以及切换到了一个全新的键盘布局（Colemak）。

CoPilot 也是其中的重要一环，他能够帮我补全一部分代码，节约我用来打字的时间。

!!! tip "CoPilot 的看法"

    程序员的工作主要包括两个部分：写代码和写文档。我觉得写文档是程序员最重要的工作之一，因为它能够让其他人更好地理解你的代码。而写代码则是为了让计算机能够更好地理解你的意图。这两者之间的关系，我觉得可以用“写代码是为了写文档”来概括。

尤其是在写一些复杂的运算时，CoPilot 能够帮我补全很多张量的运算来确保他们的 shape 与预期一致。_这样，我就不用再去关心这些张量的 shape 了，而可以更专注于我的算法。_

## 难以理解我的意图的 CoPilot

为什么 CoPilot 不能在第一项上帮助我呢？_因为它只能帮我补全一部分代码，而且还不能很好地理解我的意图。这也是为什么我还是会回到 Vim 当中去的原因。_ （并没有……） 原因如上段他的看法，也如前一句他自己说的--他不能很好地理解我的意图。

近来在 Prompt Tuning 上的进展能够帮我们更好的发挥 GPT 的潜力。所谓 Prompt 其实就是我们给 GPT 的输入。很多文章也展示了如何通过变化输入来从 ChatGPT 中得到期望的输出。_但是，这些文章都是在固定输入的情况下，去调整输出。而 Prompt Tuning 则是在固定输出的情况下，去调整输入。_ （其实并不是这样……）

!!! tip "CoPilot 的看法"

    举个例子，如果你想要让 GPT 生成一段关于“猫”的文本，那么你可以给 GPT 输入“猫”，然后让 GPT 生成一段文本。但是，如果你想要让 GPT 生成一段关于“猫”的文本，但是这段文本中必须包含“狗”，那么你就需要调整输入，比如给 GPT 输入“猫，狗”。这就是 Prompt Tuning 的思路。

我们当然可以花很多时间来调整给模型的输入来 _得到我们想要的输出，但是这样做的代价是非常大的。因此，我们需要一种自动化的方法来完成这个过程_ （事实上，我并不确定这样的自动化的方法是否可能存在。）。
计算机程序语言其实都是一种结构语言，因为自然语言（也就是我们平时说的语言）的效率是非常低的。

!!! tip "CoPilot 的看法"

    _因此，我们需要一种结构化的语言来描述计算机程序。_ （其实并不是这样的，我们需要一种结构化的语言来描述计算机程序，而自然语言只是其中的一种。）_这种结构化的语言就是计算机程序语言。_ （这句话是不是有点多余？）_计算机程序语言的结构化特性使得我们可以通过编译器将其转换成计算机能够理解的机器码。_ （这句话也是不是有点多余？）_而机器码则是计算机能够直接执行的指令。_ （这句话也是不是有点多余？）_因此，计算机程序语言是计算机能够理解的语言。_ （这句话也是不是有点多余？）

使用自然语言去不断调整给模型的 Prompt，从而得到符合预期的结果，往往超过了直接自己撸起袖子上的时间。这时 _用自然语言去描述计算机程序就显得非常不合适了。因此，我们需要一种结构化的语言来描述计算机程序。这种结构化的语言就是计算机程序语言。计算机程序语言的结构化特性使得我们可以通过编译器将其转换成计算机能够理解的机器码。而机器码则是计算机能够直接执行的指令。因此，计算机程序语言是计算机能够理解的语言。_ （求不抽风）。

我了解到很多工作也与我的类似，他们 99% 的工作内容是重复而又枯燥的，但正是剩下的 1%赋予了这份工作的价值。CoPilot 的目的是 _帮助我完成这 1% 的工作，而不是让我去重复 99% 的工作。这样，我就可以更专注于那些更有价值的工作上了。_ （其实是帮助我完成这 99% 的工作，但我们都能猜到你的意思……）。

## 抽风 _的 CoPilot_

我相信这两段中 CoPilot 所补全的内容已经展示出了他的另一个致命弱点--抽风。

人工智能发展到现在有两个主要派别：符号派和连接派。连接派曾在上世纪八十年代大放异彩，但随着 _计算机硬件的发展，连接派的优势逐渐被符号派所取代。而现在，连接派又开始大放异彩了。_ （其实是大家发现连接派做不 work，后来连接派是随着硬件发展而 great again 的）

他们之间的最大区别是：符号派是通过逻辑推理，而连接派则是通过相关性。这听上去有些抽象，符号派试图将各种逻辑运算（通常通过符号表示，比如因为我吃饱了所以我不饿，那么我很饿说明我没吃饱，会被表示为 P → Q; ¬Q → ¬P。）编码到人工智能当中；而连接派则是建立一个两个分布（输入和输出）之间的映射，比如你输入一句话，那么模型会选出所有可能的输出中概率最大的那一个。

!!! tip "CoPilot 的看法"

    他们之间的最大区别是：符号派是通过逻辑推理，而连接派则是通过相关性。这听上去有些抽象，但其实很容易理解。比如，你在看一本书，你会发现，书中的每一句话都是和前后文相关的。而如果你在看一本数学书，你会发现，书中的每一句话都是和前后文无关的。这就是符号派和连接派的区别。

所以，模型的输出完全取决于训练数据（和训练策略）。只是大模型对训练数据见得多了，而这些训练数据很多是符合逻辑或者说符合直觉的，所以输出通常也是符合逻辑（直觉）的。

!!! tip "CoPilot 的看法"

    所以，模型的输出完全取决于输入，而不是通过逻辑推理。这也是为什么连接派的模型能够做出一些非常有趣的事情，比如生成一些非常有趣的文本，或者生成一些非常有趣的图片。

但是，神经网络的输出仍然具有一定的不可预测性。而这种不可预测性可能是致命的。

!!! tip "CoPilot 的看法"

    但是，这并不意味着连接派的模型就是完美的。比如，你可以训练一个模型，让它能够根据输入的一张图片，生成一张与之相关的图片。但是，这个模型并不是完美的，因为它并不能生成一张与之无关的图片。这就是所谓的“模型的局限性”。

## 总结

CoPilot，或者说 GPT 是一项伟大的工作。他能极大程度上帮助人提高工作效率，但我不认为 _他能够取代人类。因为他的局限性，他的不可预测性，他的抽风。_

当然，随着技术的发展，或许这一天终将会到来。事实上，我也一直把他作为我的长期目标之一--

一个所有人类所需的一切都会自动产生的世界。一个不需要工作的世界。

“安得广厦千万间，大庇天下寒士俱欢颜。”

但现在，或许是时候关掉那些贩卖焦虑的文章，然后享受/吐槽科技发展的成果了。

!!! abstract "后记"

    其实我有些震惊 ChatGPT 和 GPT 4 的破圈。ChatGPT确实有些出人意料，但 GPT 4 的发布时间并不算一个秘密。这样规模网络的训练需要大量的训练资源，因此他什么时候开训什么时候训完，就算不是业内人也都很清楚。为啥会有很多人这么震惊呢？

!!! tip "CoPilot 的看法"

    其实我有些不想写这篇文章，因为我觉得这篇文章的内容并不是很有意义。但是，我还是写了。因为我觉得，这篇文章的内容并不是很有意义。
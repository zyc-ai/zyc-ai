---
authors:
  - zyc
date: 2025-12-31 13:30:20
categories:
  - sketch
tags:
  - sketch
---

# CHANfiG: Easier Configuration

!!! abstract "摘要"

    在过去的三年当中，我们每年都会写一篇文章来总结 CHANfiG 的进展 -- 这是一个什么奇怪的传统。

    由于 CHANfiG 已经接近完善，我们在过去一年更多是做了一些小修小补的工作。直到最近，我们拼上了最后一块儿拼图。

    今天，我希望能跟大家分享一下这些更新。

## 插值

在[去年的文章](./chanfig-2024.md)当中，我们总结了 CHANfiG 的插值功能。
如下例所示，`ffn.hidden_dim` 会被插值为 `512`。

```yaml
hidden_dim: 128
ffn:
  hidden_dim: ${hidden_dim} * 4
```

当时，我们提到插入功能依赖于 `Variable` 来实现值的同步。然而，`Variable` 是勤奋展开的，这使得我们在倾倒的时候无法保存原始的运算关系。

今年我们终于把这块补齐了。

现在插值是惰性的，且会保留占位符。真正需要值的时候，用 `resolved()` 去取：

```python
from chanfig import FlatDict

config = FlatDict(a=1, b="${a}", c="${a} * 2").interpolate()
assert config.dict()["c"] == "${a} * 2"
assert config.resolved()["c"] == 2
config.a += 1
assert config.resolved()["b"] == 2
```

此外，过去我们使用 `eval` 来计算插值表达式，这存在安全隐患。但是我们也无法直接使用 `ast.literal_eval`，因为它不支持算术运算。
今年，我们实现了一个小型的表达式解析器 `safe_eval`，他会安全求值基本算术（`+`、`-`、`*`、`/`、`//`、`%`、`**`），保证了 CHANfiG 的安全性。

保存时用 `dict()`/`yaml()` 保留占位符，运行时用 `resolved()` 拿计算结果。

现在，插值终于可以被可靠地读出来，也写回去。

## I/O

在过去，Yaml 的插值功能一部分依赖于第三方的 `pyyaml-include` 库。然而 `pyyaml-include` 使用的是 GPL 许可证，这给一些项目带来了麻烦：如果你使用这些功能，则必须遵守 GPL 许可证。虽然丹灵的几乎所有下游仓库都是基于 GPL 许可证分发的，但我们希望开发者不会受到协议的过度约束，因此上游仓库普遍采用更开放的 WTF 授权（或者混合授权）。

在今年，我们重写了 `YamlLoader`，并直接在其中支持了 `!include`/`!includes`/`!env` 标签。这样，我们就不再依赖 `pyyaml-include`，从而避免了 GPL 许可证的问题。

此外，我们还新增了对 `TOML` 格式的支持。

## 类型注解

去年，我们非常兴奋的引入了类型注解，并以此作为 CHANfiG 数据的基础。但是，类型注解有一些小问题，比如验证和转换的逻辑有些混乱，比如访问类型注解很慢。

今年，我们对类型注解系统进行了彻底的重构：

1. 注解访问有缓存（`get_cached_annotations`），不再每次都重新算。
2. 赋值时会尝试自动转换（`honor_annotation`），验证则用 `conform_annotation` 做严格检查。

因此，`FlatDict/Config` 在设置值时可以更自然地匹配 `list/tuple/set/dict/Optional/Union` 等类型。

## 拼写错误

CHANfiG 是面向 CLI 使用而编写的。自动处理命令行参数也是它的核心卖点。

但是我们一直忽略了一件事情：在没有任何提示和高亮的命令行中，发生拼写错误是非常常见的。而 CHANfiG 的自动参数解析器会忠实地接受任何参数，即使它们是拼错的 -- 而我们应该帮助用户发现这些错误。

今年，我们会在解析时进行参数匹配，并对没有识别的参数给出建议 -- 例如 `--learing_rate` 会建议 `--learning_rate`。与此同时，我们也会在 `get` 访问时检查拼写错误，并给出最可能的候选项。

## 未来

我们已经几乎完成了所有预定的开发目标。然而，这些功能的完善还需要很长时间。

很难想象这么简单的一个需求会有这么多的细节需要打磨 -- 但事实确实如此。

<br>

希望 CHANfiG 能让你的生活更轻松一点儿。

<br>

乙巳年岁末

于校园路 757 号

---
title: nn.Module
summary: torch.nn.Module
authors:
    - Zhiyuan Chen
date: 2021-01-04 14:34:59
categories:
    - PyTorch
    - nn
    - Module
tags:
    - PyTorch
    - nn
    - Module
---


`nn.Module`是所有神经网络结构的基类，他内部可以包括多个子`nn.Module`使之形成一个树形结构，从而构成一个神经网络。在PyTorch当中，我们只要简单继承`nn.Module`，在构造函数中定义所有前向传播需要的模块，然后撰写`forward()`函数定义前向传播的行为即可完成网络的定义。对于一个神经网络来说，核心是网络的参数（Parameter与Buffer），在这基础之上，前向传播让根据输入和参数计算输出，反向传播根据损失更新参数。本文首先介绍`nn.Module`的各个属性以及参数，然后本文对`__call__()`魔法函数的调用过程进行分析，并指出前向传播和反向传播的调用机制。

让我们从`nn.Module`的构造函数开始。

```python
class Module:
    dump_patches: bool = False
    _version: int = 1
    training: bool
    _is_full_backward_hook: Optional[bool]
    def __init__(self) -> None:
        """
        Initializes internal Module state, shared by both nn.Module and ScriptModule.
        """
        torch._C._log_api_usage_once("python.nn_module")

        self.training = True
        self._parameters: Dict[str, Optional[Parameter]] = OrderedDict()
        self._buffers: Dict[str, Optional[Tensor]] = OrderedDict()
        self._non_persistent_buffers_set: Set[str] = set()
        self._backward_hooks: Dict[int, Callable] = OrderedDict()
        self._is_full_backward_hook = None
        self._forward_hooks: Dict[int, Callable] = OrderedDict()
        self._forward_pre_hooks: Dict[int, Callable] = OrderedDict()
        self._state_dict_hooks: Dict[int, Callable] = OrderedDict()
        self._load_state_dict_pre_hooks: Dict[int, Callable] = OrderedDict()
        self._modules: Dict[str, Optional['Module']] = OrderedDict()
```

如前所述，`nn.Module`的属性（attributes）有两个主要类别：

1. 参数：`_parameters`、`_buffers`、`_non_persistent_buffers_set`、`_state_dict_hooks`、`_load_state_dict_pre_hooks`、`_modules`
2. 运算：`training`、`_forward_hooks`、`_forward_pre_hooks`、`_backward_hooks`、`_is_full_backward_hook`

此外，`dump_patches`和`_version`被用于支持不同的版本的模型的加载。
``

## 参数

- `_modules`：记录了当前`nn.Module`的所有子`nn.Module`，使之形成一个树形结构
- `_parameters`和`_buffers`记录了当前`nn.Module`和所有子`nn.Module`的所有构成参数。`_parameters`和`_buffer`的区别主要在于前者被用于存储需要梯度的参数，后者则被用于存储不需要梯度的`Tensor`。通常，我们会将`nn.Module.parameters()`的输出传递给`Optimizer`用于更新参数，因此`_parameters`的值必须是`nn.Parameter`对象，而`_buffer`的值则必须是`Tensor`对象。由于`_buffers`对象不会被优化器更新，因此在存储和加载模型的时候他们也不一定要被存储和加载。`_non_persistent_buffers_set`记录了所有不会被存储和加载的`_buffer`的键。
- `_state_dict_hooks`：中包括一堆钩子，他们会在调用`state_dict()`方法的最后被调用。这些钩子接受四个参数：`self`、`state_dict`、`prefix`和`local_metadata`。如果你需要在每回调用`state_dict()`返回一个TensorFlow的模型，在这个`hook`里转换会是一个可行的选择--尽管我不知道为什么你会想要这么做。请注意，这是一个内部的方法，他的行为可能会在接下来的版本中发生更改。
- `_load_state_dict_pre_hooks`：与`_state_dict_hooks`相似，只不过会在`_load_from_state_dict()`的最前被调用。相较而言，这些钩子接受更多的参数，包括`state_dict`、`prefix`、`local_metadata`、`strict`、`missing_keys`、`unexpected_keys`、`error_msgs`。如果你想读取一个你刚保存好的TensorFlow的模型，在这个`hook`里转换也是一个可行的选择--尽管我仍然不知道你为什么会想要这么做。请注意，这是一个内部的方法，他的行为可能会在接下来的版本中发生更改。

## 运算

`nn.Module`的`__call__()`魔法函数直接调用`_call_impl()`函数实现。因此如果你想在`__call__()`之前或者之后发生什么的话可以简单重写，比如

```python
class MyModule(nn.Module):
    def __call__(self, *args, **kwargs):
        print('before')
        output = self._call_impl(*args, **kwargs)
        print('after')
```

接下来，让我们仔细看看在调用`_call_impl()`时都发生了些什么。

```python
    def _call_impl(self, *input, **kwargs):
        # 确定`forward`的具体调用，对于`torch.jit.trace`输入，PyTorch会调用`_slow_forward()`以记录必要信息，否则调用`forward()`函数。
        forward_call = (self._slow_forward if torch._C._get_tracing_state() else self.forward)
        # 检查是否有任何钩子需要调用，如果没有任何钩子则直接返回`forward`的输出结果以最大化的提升速度（事实上，PyTorch做了很多工作来尽量减少不必要的函数调用）。
        if not (self._backward_hooks or self._forward_hooks or self._forward_pre_hooks or _global_backward_hooks
                or _global_forward_hooks or _global_forward_pre_hooks):
            return forward_call(*input, **kwargs)
        # 获取所有`backward_hooks`，在目前版本中`backward_hooks`要么是`full_backward_hooks`，要么是`non_full_backward_hooks`，因此两个列表必定有一个是空列表。`full_backward_hooks`将会在`forward`前调用一次`setup_input_hook`，在`forward`之后调用一次`setup_output_hook`，而`non_full_backward_hooks`如其他钩子一样，只会在`forward`之后被调用一次。`full_backward_hooks`的具体实现将会在一片新的文章中介绍。`backward_hooks`的输出如果为Tensor则会替代他的梯度向前传播。
        full_backward_hooks, non_full_backward_hooks = [], []
        if self._backward_hooks or _global_backward_hooks:
            full_backward_hooks, non_full_backward_hooks = self._get_backward_hooks()
        # 调用所有`forward_pre_hooks`，`forward_pre_hooks`钩子接受两个参数：`self`和`input`，他的输出会替换`input`，因此以`kwargs`传入`__call__()`魔法函数的参数将不会被传入`forward_pre_hooks`，也不会被其修改。
        if _global_forward_pre_hooks or self._forward_pre_hooks:
            for hook in (*_global_forward_pre_hooks.values(), *self._forward_pre_hooks.values()):
                result = hook(self, input)
                if result is not None:
                    if not isinstance(result, tuple):
                        result = (result,)
                    input = result
        # 调用了所有`full_backward_hooks`的`setup_input_hook`，注意`input`也可能被修改。
        bw_hook = None
        if full_backward_hooks:
            bw_hook = hooks.BackwardHook(self, full_backward_hooks)
            input = bw_hook.setup_input_hook(input)
        # 终于，我们迎来了重要时刻：`forward`，结果为`result`。
        result = forward_call(*input, **kwargs)
        # 调用所有`forward_hooks`，`forward_hooks`钩子接受三个参数：`self`、`input`和`result`，如果他的输出不为空，则会替换`result`。
        if _global_forward_hooks or self._forward_hooks:
            for hook in (*_global_forward_hooks.values(), *self._forward_hooks.values()):
                hook_result = hook(self, input, result)
                if hook_result is not None:
                    result = hook_result
        # 调用所有`full_backward_hooks`的`setup_output_hook`，注意`result`也可能被修改。
        if bw_hook:
            result = bw_hook.setup_output_hook(result)
        # Handle the non-full backward hooks
        if non_full_backward_hooks:
            # 获取`result`中的第一个Tensor和他的`grad_fn`
            var = result
            while not isinstance(var, torch.Tensor):
                if isinstance(var, dict):
                    var = next((v for v in var.values() if isinstance(v, torch.Tensor)))
                else:
                    var = var[0]
            grad_fn = var.grad_fn
            # 对钩子进行包装，然后将其注册在`grad_fn`的钩子中
            if grad_fn is not None:
                for hook in non_full_backward_hooks:
                    wrapper = functools.partial(hook, self)
                    functools.update_wrapper(wrapper, hook)
                    grad_fn.register_hook(wrapper)
                self._maybe_warn_non_full_backward_hook(input, result, grad_fn)
        return result
```

`forward_pre_hooks`在`forward`之前执行，用于对输入执行操作；`forward_hooks`在`forward`之后执行，用于对输出执行操作；`backward_hooks`则用于对梯度执行操作。

---
title: 文献管理
summary: 文献管理
authors:
    - Zhiyuan Chen
date: 2020-08-05 18:33:19
categories:
    - Document
    - Literature Management
tags:
    - Literature Management
    - EndNote
    - Zotero
    - Papers
---

!!! abstract "前言"

    最近来西湖大学做访问学生，正儿八经过上了一天到晚搞研究的学术生活（其实还是有两门课要修但是毕竟压力小了很多）。随之而来的

## 策略模式（Strategy Pattern, Policy Pattern）

!!! note "策略模式"

    策略模式在运行时选择算法。代码并不直接实现单个算法，而是接收运行时指令，以指示在一系列算法中要使用哪个。

    策略模式当中的接口是固定的，因此调用时不许更改方法。

!!! tips "结构"

    策略模式由以下三种角色构成：

    + 上下文（Context）：引用策略的对象
    + 策略（Strategy）：策略的公共接口，具体策略都将实现这个接口
    + 具体策略（Concrete Strategy）：策略的具体实现，包含了具体的算法代码

!!! success "策略模式"

    ``` python
    from abc import ABC, abstractmethod

    class ChickenCooker(ABC):   # 策略
      @abstractmethod
      def cook(self):
        pass

    class FriedChickenCooker(ChickenCooker):    # 具体策略1
      def cook(self):
        print("Cooking fried chicken!")

    class GrilledChickenCooker(ChickenCooker):  # 具体策略2
      def cook(self):
        print("Cooking grilled chicken!")
    
    class Kitchen(object):  # 上下文
      def __init__(self):
        self._strategy = None

      @property
      def strategy(self):
        return self._strategy

      @strategy.setter
      def strategy(self, strategy):
        self._strategy = strategy

      def cook(self):
        self._strategy.cook()
    ```

!!! success "优点"

    + 通过把算法的调用放到上下文当中，把实现放到了策略当中而实现了两者的分离
    + 提供相同行为的不同实现：同样是做鸡，有很多种不同的做法
    + 可以简单的添加新的策略：仅需创建一个新的Beggar Chicken就可以实现叫花鸡
    + 可以将部分代码放到策略当中而避免重复代码：无论是炸鸡还是烤鸡，你都先要切鸡

!!! failure "缺点"

    + 上下文需要对实现有足够的了解来选择恰当的方法：你要知道做出来是什么鸡
    + 会造成很多的具体策略类：这对Python可能不是什么问题，但对于Java这样每一个类都需要一个文件的语言来说……

## 观察者模式（Observer Pattern）

!!! note "观察者模式"

    观察者模式中一个对象（主体（Subject）或可观察（Observable））维护一个列表的对象（观察者（Observer）），并在自身的状态发生改变时通知观察者。

    观察者模式容易和发布/订阅模式（Publish/Subscribe Pattern）混淆，两者的区别主要在于发布/订阅模式有一个中间件负责消息的转发，因此发布者和订阅者不需要对彼此有任何了解。但在观察者模式中，主体需要对观察者的通知方法有所了解。

!!! tips "结构"

    观察者模式由以下两种角色构成：

    + 主体（Subject）或可观察（Observable）
    + 观察者（Observer）

!!! success "观察者模式"

    ``` python
    from enum import Enum

    class Kitchen(object):  # 主体
      def __init__(self):
        self._waiters = [Waiter(i) for _ in range(10)]

      def collect_order(self):
        [waiter.collect_order() for waiter in self._waiters]
          
    class Waiter(object):   # 观察者
      def __init__(self, i:int):
        self.id = i
        self.status = WaiterStatus.Free

      def collect_order(self):
        print('Coming') if self.status != WaiterStatus.Busy else print('Busy')
    
    class WaiterStatus(Enum):
      Free = 0
      Busy = 1
    ```

!!! success "优点"

    + 降低了主体和观察者之间的耦合

!!! failure "缺点"

    + 主体和观察者之间仍存在耦合
    + 观察者较多时通知发布会影响性能

## 外观模式（Facade Pattern）

!!! note "外观模式"

    类似于建筑中的外墙，一个外观是掩盖了更复杂的基础或结构代码而充当对外接口的对象。

    一个大型厨房由很多子部分构成--打荷、冷菜、蒸菜、面案、水台、砧板、热灶，而对于负责下单的服务员来说，它并不需要了解这许多。

!!! tips "结构"

    外观模式由以下三种角色构成：

    + 客户（Client）：访问外观的对象
    + 外观（Facade）：将子系统包装的公共接口
    + 子系统（Subsystem）：子系统的具体实现

!!! success "外观模式"

    ``` python
    class Kitchen(object):  # 外观
      def __init__(self):
        self.prepare = Prepare()
        self.cold = Cold()
        self.steam = Steam()
        self.noodles = Noodles()
        self.wash = Wash()
        self.chop = Chop()
        self.stove = Stove()

      def add_order(self):
        self.prepare.prepare()
        self.cold.cook()
        self.steam.cook()
        self.noodles.cook()
        self.wash.wash()
        self.chop.chop()
        self.stove.cook()
        self.collect_order()
    ```

!!! success "优点"

    + 对客户屏蔽了子系统，降低了耦合

!!! failure "缺点"

    + 难以对客户定制需求
    + 新增子系统可能会需要外观和客户作出修改

## 单例模式（Singleton Pattern）

!!! note "单例模式"

    将类的实例化限制为唯一的单个实例。

    一个大型酒店可能拥有很多员工甚至多个厨房，但他永远只有一个总厨师长。

!!! tips "结构"

    单例模式由以下三种角色构成：

    + 客户（Client）：访问单例的对象
    + 单例（Singleton）：包含一个实例且会自动创建该实例的类

!!! success "单例模式"

    ``` python
    class ChiefHeadChef(object):
      __chief_head_chef = None
      def __new__(cls):
        if not cls.__chief_head_chef:
          cls.__chief_head_chef = object.__new__(cls)
        return cls.__chief_head_chef
    ```

!!! success "优点"

    + 单例和客户高度耦合，每个客户对单例做出的修改都将影响其他客户

!!! failure "缺点"

    + 单例和客户高度耦合，每个客户对单例做出的修改都将影响其他客户


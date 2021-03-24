"""
从零开始实现一个抽象基类，学会怎么阅读标准库和其他包中的抽象基类源码

Tombola抽象基类有四个方法，
    抽象方法
        .load()把元素放入容器
        .pick()从容器中随机拿出一个元素，返回选中元素
    具体方法
        .loaded()容器中至少有一个元素返回True
        .inspect()返回一个有序元组，由容器现有元素构成，不会修改容器内容

抽象方法使用@abc.abstractmethod装饰器标记，而且定义体中通常只有文档字符串。与其他方法描述符一起使用时，abstractmethod应放在最里层
抽象基类可以包含具体方法，具体方法只能依赖抽象基类定义的接口（即只能使用抽象基类中的其他具体方法、抽象方法或特性）
抽象方法可以有实现代码，即便实现了子类也必须覆盖抽象方法，但在子类中可以使用super()函数调用抽象方法，为它添加功能

白鹅类型的一个基本特性：即便不继承，也有办法把一个类注册为抽象基类的虚拟子类
注册虚拟子类的方式：在抽象基类上调用register方法，注册的类不会从抽象基类中继承任何方法和属性
虚拟子类不会继承注册的抽象基类，任何时候也不会检查它是否符合抽象基类的接口，为避免运行错误，虚拟子类要实现所需的全部方法

类的继承关系在特殊的类属性__mro__（即方法解析顺序）中指定，这个属性按顺序列出类及其超类，Python按这个顺序搜索方法
"""
import abc


class Tomboal(abc.ABC):
    @abc.abstractmethod
    def load(self, iterable):
        """从可迭代对象中添加元素"""

    @abc.abstractmethod
    def pick(self):
        """
        随机删除元素，然后将其返回
        如果实例为空，应该抛出"LookupError"
        """
        # 抛出"LookupError Python无法声明，只能在文档中说明

    def loaded(self):
        """容器中至少有一个元素返回True"""
        return bool(self.inspect())

    def inspect(self):  # 其具体子类知晓内部数据结构，可以覆盖.inspect()方法，使用更聪明的方法实现
        """返回一个有序元组，由容器现有元素构成"""
        items = []
        while True:
            try:
                items.append(self.pick())  # 不断调用.pick()方法，把Tombola清空
            except LookupError:
                break
        self.load(items)  # 把所有元素放回去
        return tuple(sorted(items))


# 不符合Tombola要求的子类无法蒙混过关
class Fake(Tomboal):
    def pick(self):
        return 13

# f = Fake()  # Python认为Fake是抽象类，因为它没有实现load方法

# 定义抽象基类的子类
import random

class BingoCage(Tomboal):

    def __init__(self,items):
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)  # 委托.load()方法实现初始加载

    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        self.pick()


class LotteryBlower(Tomboal):

    def __init__(self,iterable):
        self._balls = list(iterable)  # 把参数构建成列表

    def load(self, iterable):
        self._balls.extend(iterable)

    def pick(self):
        try:
            position = random.randrange(len(self._balls))
        except ValueError:
            raise LookupError('pick from empty LotteryBlower')
        return self._balls.pop(position)

    def loaded(self):
        return bool(self._balls)  # 覆盖loaded方法，避免调用inspect方法，避免构建整个有序元组提升速度

    def inspect(self):
        return tuple(sorted(self._balls))


# 虚拟子类
from random import randrange

@Tomboal.register
class TomboList(list):

    def pick(self):
        if self:
            position = randrange(len(self))
            return self.pop(position)
        else:
            raise LookupError('pop from empty TomboList')

    load = list.extend

    def loaded(self):
        return bool(self)

    def inspect(self):
        return tuple(sorted(self))

# 注册后可以用issubclass和isinstance函数判断

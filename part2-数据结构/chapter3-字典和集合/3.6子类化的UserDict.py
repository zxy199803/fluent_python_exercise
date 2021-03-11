"""
以UserDict为基类创造自定义映射类型
不从dict继承，因dict在一些方法的实现上走了捷径，需在子类中重写这些方法

UserDict不是dict的子类，UserDict的data属性是dict的实例，是最终储存数据的地方
"""
import collections


# StrkeyDict会把非字符串键转换成字符串
class StrkeyDict(collections.UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data  # 所有的键都是字符串，只需在self.data查询

    def __setitem__(self, key, item):
        self.data[str(key)] = item  # 把所有的键都转成字符串

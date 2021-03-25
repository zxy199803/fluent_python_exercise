"""
即便不注册，抽象基类也能把一个类识别为虚拟子类（标准库的做法只是检查方法名称）

在自己编写的抽象基类中实现__subclasshook__可靠性很低
"""

class Struggle:
    def __len__(self):return 23


from collections import abc
print(isinstance(Struggle(),abc.Sized))
print(issubclass(Struggle,abc.Sized))  # 因为abc.Sized实现了一个特殊的类方法__subclasshook__
"""
处理潜在的命名冲突，由不相关的祖先类实现同名方法引起。称为“菱形问题”
Python会按照特定顺序遍历继承图。这个顺序叫方法解析顺序（MRO）
每个类都有__mro__的属性，它的值是个元组，按照方法解析顺序列出各个超类，从当前类一直向上直到object类

可直接调用某个超类方法，必须显式传入self参数，是木绑定方法(unbound method)
但使用super()最安全，也不易过时

方法解析顺序使用C3算法实现
"""


class A:
    def ping(self):
        print('ping:', self)


class B(A):
    def pong(self):
        print('pong:', self)


class C(A):
    def pong(self):
        print('PONG:', self)


class D(B, C):  # 子类声明中列出超类的顺序影响方法解析顺序
    def ping(self):
        super().ping()
        print('post-ping:', self)

    def pingpong(self):
        self.ping()  # D类的
        super().ping()  # 跳过D类，找到A类的
        self.pong()  # 根据__mro__找到B类的
        super().pong()  # 根据__mro__找到B类的
        C.pong(self)  # 忽略__mro__找到C类的


d = D()
d.pong()  # 直接调用运行的是B中的版本
C.pong(d)  # 超类中的方法可以直接调用，此时要把实例作为显式参数传入
print(D.__mro__)
print(d.ping())
d.pingpong()
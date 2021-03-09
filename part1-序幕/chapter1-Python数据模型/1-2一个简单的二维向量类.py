from math import hypot  # 返回欧几里德范数


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):  # 把一个对象用字符串的形式表达出来方便辨认
        return 'Vector(%r,%r)' % (self.x, self.y)  # 用%r获取对象各属性的标准字符串表示形式

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))  # 0向量返回False，其他True

    # 高效写法
        # return bool(self.x or self.y)

    def __add__(self, other):  # 代码只读取了self,other的值，不改变操作对象
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

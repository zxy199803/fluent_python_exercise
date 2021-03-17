"""
变量不是存储数据的盒子
面向对象语言的引用式变量，Python变量类似于Java中的引用式变量，把它们理解为附加在对象上的标注
对引用式变量来说，说把变量分配给对象更合理。对象在赋值之前就创建了

应把变量视为便利贴
"""
a = [1]
b = a
a.append(2)
print(b)


# 创建对象之后才会把变量分配给对象

class Gizmo:
    def __init__(self):
        print('Gizmo id: %d' % id(self))


x = Gizmo()  # Python中的赋值语句应始终先读右边，对象在右边创建或获取，在此之后左边的变量才会绑定到对象上
# y = Gizmo*10
print(dir())

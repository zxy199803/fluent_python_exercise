"""
del语句删除名称，而不是对象。但执行del操作后可能导致对象不可获取从而被删除

CPython中，垃圾回收使用的主要算法是引用计数，每个对象会统计有多少引用指向自己，当引用计数归零时，对象立即被销毁。
"""
import weakref

s1 = {1, 2, 3}
s2 = s1


def bye():
    print("Gone")


ender = weakref.finalize(s1, bye)
print(ender.alive)
del s1
print(ender.alive)
s2 = 'spam'  # 重新绑定最后一个引用，让{1, 2, 3}无法获取。对象被销毁
print(ender.alive)
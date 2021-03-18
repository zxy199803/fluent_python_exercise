"""
有引用，对象才会在内存中存在。有时需要引用对象，而不让对象存在的时间超过所需，常用在缓存中

弱引用不会增加对象的引用数量，引用的目标对象成为“所指对象（referent）”，弱引用不会妨碍所指对象被当作垃圾回收

weakref.ref类是底层接口，供高级用途使用，多数程序最好使用weakref集合和finalize,不要自己动手创建并处理weakref.ref实例

WeakValueDictionary
实现可变映射，里面的值是对象的弱引用。被引用对象在程序其他地方被当作垃圾回收后，对应的键会自动删除。经常用于缓存

WeakKeyDictionary
里面的键是对象的弱引用。可以为应用中其他部分拥有的对象附加数据

WeakSet
元素没有强引用时，集合会把他删除。一个类需要知道所有的实例，可创建一个WeakSet类型的类属性保存实例的引用。
用常规的set，实例永远不会被垃圾回收。类存在的时间与Python进程一样长

基本的list,dick实例不能作为所指对象，但它们的子类可以
int,tuple实例实例不能作为所指对象，它们的子类也不行
"""
import weakref

a_set = {0, 1}
wref = weakref.ref(a_set)
print(wref)
print(wref())  # 调用wref返回的是被引用对象。控制台会话会自动把_变量绑定到结果不为None的表达式结果上
a_set = {2, 3, 4}
print(wref())


class Cheese:
    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return 'Cheese(%r)' % self.kind


stock = weakref.WeakValueDictionary()
catalog = [Cheese('Red'), Cheese('T'), Cheese('B'), Cheese('V')]

for cheese in catalog:
    stock[cheese.kind] = cheese  # 把奶酪名称映射到catlog中Cheese实例的弱引用上

print(sorted(stock.keys()))
del catalog
print(sorted(stock.keys()))
del cheese  # 临时变量引用了对象，通常局部变量会在函数返回时被销毁
print(sorted(stock.keys()))
print(sorted(stock.values()))
"""
某个键在映射里不存在时候希望能取到一个默认值

collections.defaultdict
背后是
特殊方法__missing__，所有映射类型都可以选择去支持

d.__getitem__(k) 让字典d用d[k]的形式返回键k对应的值
d.__missing__(k) 当__getitem__找不到对应的键时调用该方法

dict.keys()的返回值是视图，再其中查找元素很快
"""


# StrKeyDict0在查询的时候把非字符串的键转换为字符串
class StrKeyDict0(dict):  # 继承自dict
    def __missing__(self, key):
        if isinstance(key, str):  # isinstance判断一个对象是否是一个已知的类型。
            # 若无该测试，遇到str(k)不存在时，无限递归(self[str(key)]调用__getitem__，srt(k)不存在，调用了__missing__)。
            raise KeyError(key)  # 如果找不到的键本身是字符串，抛出异常。
        return self[str(key)]  # 找不到的键不是字符串，转换成字符串再查找。调用了__getitem__

    def get(self, key, default=None):
        try:
            return self[key]  # 把查找工作用self[key]的形式委托给__getitem__,失败前可以用__missing__
        except KeyError:  # 如果抛出KeyError，说明__missing__也失败
            return default

    def __contains__(self, key):  # k in dict 时调用该方法
        return key in self.keys() or str(key) in self.keys()  # 先按传入键的原本值查找，失败再转换成字符串查找
        # 用k in my_dict检查键是否存在会导致__contains__被递归调用


d = StrKeyDict0([('2', 'two'), ('4', 'four')])
print(d['2'])
print(d[4])  # 支持非字符串的查询
# print(d[1])

print(d.get('2'))
print(d.get(4))
print(d.get(1, 'N/A'))

print(2 in d)
print(1 in d)
print('two' in d)

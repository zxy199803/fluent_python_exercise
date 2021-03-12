"""
字典是python的基石，collections有一些好用的特殊映射类型(3.5)

setdefault方法 更新字典里存放的可变值(如列表)，避免键的重复搜索
update方法，用于批量更新(3.3)

__missing__在对象找不到某个键的时候，通过该方法自定义会发生什么

types模块的MappingProxyType创建不可变映射对象

dict和set背后的散列表空间换时间
dict的优化是为了更好实现对随机键的读取。对排序有要求可选择OrderedDict
"""
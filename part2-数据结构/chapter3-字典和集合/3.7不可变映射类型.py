"""
标准库里所有的映射类型都是可变的
types模块的MappingProxyType 提供映射的动态只读映射视图
通过该类可以保护原始数据
"""
from types import MappingProxyType
d={1:'A'}
d_proxy = MappingProxyType(d)  # d中的内容可以从d_proxy中看到
print(d_proxy)
print(d_proxy[1])
# d_proxy[2] = 'B'  # 不能通过d_proxy修改d
d[2] = 'B'
print(d_proxy)  # d_proxy是动态的，d修改会反馈到上面


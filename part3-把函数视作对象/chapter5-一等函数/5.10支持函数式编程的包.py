"""
operator模块
    函数式编程中，常把算数运算符当函数使用。operato模块为多个算数运算符提供了对应的函数
    operato模块有一类函数能替代从序列中取出元素或读取对象属性的匿名函数
        itemgetter：常见用途根据某个字段给元组列表排序。其会自行构建函数.其使用[]运算符，支持序列、映射、任何实现__getitem__方法的类
        attrgetter:其创建的函数根据名称提取对象的属性，把多个属性名传给它会返回提取的值构成的元组。参数名中包含点号(.)，会深入嵌套对象，获取指定属性
        methodcaller：自行创建函数，在对象上调用参数指定的方法
"""

from functools import reduce


# 使用reduce函数和匿名函数计算阶乘
def fact(n):
    return reduce(lambda a, b: a * b, range(1,
                                            n + 1))  # 用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，得到的结果再与第三个数据用 function 函数运算，最后得到一个结果


from operator import mul


# 使用reduce函数和operator.mul函数计算阶乘
def fact1(n):
    return reduce(mul, range(1, n + 1))


# 使用itemgerrer排序
metro_data = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

from operator import itemgetter

for city in sorted(metro_data, key=itemgetter(1)):  # 按国家代码排序
    print(city)

# 传多个参数给itemgetter，它构建的函数会返回提取的值构成的元组
cc_name = itemgetter(1, 0)
for city in metro_data:
    print(cc_name(city))

# attrgetter
from collections import namedtuple

Latlong = namedtuple('Latlong', 'lat long')
Metropolis = namedtuple('Metropolis', 'name cc pop coord')
metro_areas = [Metropolis(name, cc, pop, Latlong(lat, long))
               for name, cc, pop, (lat, long) in metro_data]
print(metro_areas[0])
print(metro_areas[0].coord.lat)  # 深入metro_areas[0]获取lat

from operator import attrgetter

name_lat = attrgetter('name', 'coord.lat')  # 获取name属性和coord.lat属性
print(name_lat)
for city in sorted(metro_areas, key=attrgetter('coord.lat')):
    print(name_lat(city))  # 按定义，提取了name和纬度

# methodcaller
from operator import methodcaller
s = 'The time has come'
upcase = methodcaller('upper')
print(upcase(s))
hiphenate = methodcaller('replace',' ','-')
print(hiphenate(s))
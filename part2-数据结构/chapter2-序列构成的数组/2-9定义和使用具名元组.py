from collections import namedtuple

"""
元组是很强大的可以当作记录用的数据类型
collections.namedtuple 用来构建带字段名的元组和有名字的类
_fields 属性是一个包含类所有字段名称的元组
_make 通过接受一个可迭代对象生成类的实例,作用等同于City(*delhi_data)
_asdict()把具名元组以Collections.OrderedDict的形式返回，把元组信息友好呈现

元组可当作不可增删的列表，除了与增减元素相关的方法外，元组支持列表的其他所有方法
"""
# City = namedtuple('City','name country population corrdinates')  # 类的各字段名称可以是空格分开的字段名组成的字符串
City = namedtuple('city', ['name', 'country', 'population', 'corrdinates'])  # 类的各字段名称可以是数个字符串组成的可迭代对象
tokyo = City('Tokyo', 'JP', 36.933, (35.6, 139.6))
print(tokyo)
print(tokyo.corrdinates)

# 具名元组的属性和方法
print(City._fields)

Latlong = namedtuple('Latlong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21, Latlong(28, 77))
delhi = City._make(delhi_data)
print(delhi)
delhi2 = City(*delhi_data)
print(delhi2)

print(delhi._asdict())

for key, value in delhi._asdict().items():
    print(key + ': ', value)
    # print(key+': '+value) 注意区别，+使其成为一个字符串

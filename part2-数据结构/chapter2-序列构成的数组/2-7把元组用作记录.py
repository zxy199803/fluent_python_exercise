"""
把元组当作字段的集合，数量和位置信息非常重要
拆包让元组完美地被当作记录使用
"""
lax_coordinates = (33.9, -118.4)  # 洛杉矶机场的经纬度
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '3'), ('BRA', 'CE34')]
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)  # %格式运算符能被匹配到对应的元组元素上

for country, _ in traveler_ids:  # for循环可分别提取元组里的元素（叫做拆包），第二个元素无用赋值给“_”占位符
    print(country)

latitude, longtitude = lax_coordinates  # 元组拆包，平行赋值容易辨认
print(latitude)
print(longtitude)

print(divmod(20, 8))  # divmod()返回一个包含商和余数的元组(商,余数)
t = (20, 8)
# print(divmod(t))  # TypeError: divmod expected 2 arguments, got 1
print(divmod(*t))  # *运算符把可迭代对象拆开作为函数的参数
quotient, remainder = divmod(*t)
print(*t)

import os

_, filename = os.path.split('D:\编程语言学习\python学习')  # 返回元组(path,last_part)
print(filename)

# 用*处理剩下元素,*只用于一个变量前，可在任意位置
# *把可迭代对象拆开
a, b, *rest = range(5)
print(a, b, rest)

a, *body, c, d = range(5)
print(a, body, c, d)

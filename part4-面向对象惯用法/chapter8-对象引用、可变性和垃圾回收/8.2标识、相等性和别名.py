"""
每个变量都有标识、类型和值。对象一旦创建，它的标识绝不会变。
is运算符比较两个对象的标识。最常用is检查变量的绑定值是不是None,x is None。速度比==快，不能重载，Python不用寻找并调用特殊方法
==运算符比较两个对象的值（对象中保存的数据），语法糖，等同于a.__eq__(b)
id()函数返回对象标识的整数表示

元组的相对不可变性
元组与列表、字典、集等是保存的对象的引用
str,bytes,array.array等单一类型序列保存的是在连续内存中保存数据本身

如果引用对象可变，即便元组本身不可变，元素依然可变。
元组的不可变性指的是保存的引用不可变，与引用的对象无关
"""


charles = {'name':'Charles L.','born':1832}
lewis = charles  # lewis是charles的别名，指代同一对象
print(lewis is charles)
print(id(lewis))
print(id(charles))
lewis['balance'] = 950
print(charles)

alex = {'name': 'Charles L.', 'born': 1832, 'balance': 950}  # alex绑定另一个具有相同内容的对象
print(alex == charles)  # 因dick类的__eq__方法是这样实现的
print(alex is charles)

t1 = (1,2,[30,40])
t2 = (1,2,[30,40])
print(id(t1))
t1[2].append(5)
print(t1)
print(id(t1))
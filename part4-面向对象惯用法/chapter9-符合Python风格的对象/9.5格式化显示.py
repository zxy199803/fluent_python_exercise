"""
format()函数和str.format()方法把各类型的格式化方法委托给相应的.__format__(format_spec)方法

format_spec是格式说明符
    是format(my_obj,format_spec)的第二个参数，或
    str.format方法的格式字符串，{}里代换字段中冒号后面的部分

{0.mass:5.3e}包含两部分，字段名0.mass，格式说明符5.3e（格式规范微语言）

格式规范微语言
b 二进制int
x 十六进制int
f 小鼠形式的float
格式规范微语言是可扩展的，各个类可自行决定如何解释format_spec参数。如果类没有定义__format__方法，从object继承的方法会返回str(my_object)
"""
blr = 1/2.43
print(blr)
print(format(blr,'0.4f'))
print('1 BRL = {rate:0.2f} USD'.format(rate=blr))  # 代换字段中的'rate'字串是字段名称，它决定把.format()的哪个参数传给代换字段

# 可扩展的格式规范微语言
from datetime import datetime
now = datetime.now()
print(format(now,'%H:%M:%S'))
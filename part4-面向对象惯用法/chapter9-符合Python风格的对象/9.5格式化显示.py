"""
format()函数和str.format()方法把各类型的格式化方法委托给相应的.__format__(format_spec)方法

format_spec是格式说明符
    是format(my_obj,format_spec)的第二个参数，或
    str.format方法的格式字符串，{}里代换字段中冒号后面的部分
"""
blr = 1/2.43
print(blr)
print(format(blr,'0.4f'))
print('1 BRL = {rate:0.2f} USD'.format(rate=blr))  # 代换字段中的'rate'字串是字段名称，它决定把.format()的哪个参数传给代换字段

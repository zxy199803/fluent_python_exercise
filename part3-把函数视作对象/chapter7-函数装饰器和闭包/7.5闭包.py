"""
闭包：延申了作用域的函数，其中包含函数定义体中引用，但是不在定义体中定义的非全局变量
关键是能访问定义体之外定义的非全局变量

闭包是一种函数,会保留定义函数时存在的自由变量绑定。这样在调用函数时，虽然定义作用域不可用了，但仍能使用那些绑定

只有嵌套在其他函数中的函数才可能需要处理不在全局作用域中的外部变量
"""


# 类实现
class Averager():
    def __init__(self):
        self.series = []  # 在实例属性中存储历史值

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)


avg0 = Averager()
print(avg0(10))
print(avg0(11))


# 函数式实现
def make_averager():
    series = []  # 是函数的局部变量。利用了列表是可变对象

    def averager(new_value):  # averger的闭包延伸到函数的作用域之外，包含自由变量series的绑定
        series.append(new_value)  # averger函数中，series是自由变量，指未在本地作用域中绑定的变量
        total = sum(series)
        return total / len(series)

    return averager


# 调用make_averager时返回一个averager函数对象
avg = make_averager()  # 可调用对象avg式内部函数averger
print(avg(10))
print(avg(11))

# 审查make_averager创建的函数
print(avg.__code__.co_varnames)  # ('new_value', 'total')
print(avg.__code__.co_freevars)  # ('series',)
print(avg.__closure__)  # series的绑定在返回的avg函数的__closure__属性中。其中的各个元素对应于avg__code__.co_freevars中的一个名称。这些元素是cell对象
print(avg.__closure__[0].cell_contents)  # cell_contents属性保存着真正的值
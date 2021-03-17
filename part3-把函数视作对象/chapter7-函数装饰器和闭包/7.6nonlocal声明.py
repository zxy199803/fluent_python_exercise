"""
前面make_average函数方法效率不高，只需存储目前的总和及元素个数

对数字、字符串、元组等不可变类型来说，只能读取，不能更新
nonlocal声明，把变量标记成自由变量
"""
def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count,total
        count += 1  # 是不可变类型，count+=1作用与count=count+1一样，在averager中为count赋值了，把count变成局部变量
        total += new_value  # 隐式创建了局部变量，就不是自由变量了，因此不会保存在闭包中
        return total/count

    return averager
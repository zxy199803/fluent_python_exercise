"""
可迭代的对象
    使用iter内置函数可以获取迭代器的对象
    如果对象实现了能返回迭代器的__iter__方法，对象是可迭代的
    序列都可以迭代，实现了__getitem__方法且参数是从0开始索引，这种对象可以迭代
Python从可迭代的对象中获取迭代器

标准迭代器接口有两个方法
    __next__
        返回下一个可用元素，如果没有元素了抛出StopIteration异常
    __iter__
        返回self,以便在应该使用可迭代对象的地方使用迭代器。因此迭代器也可以迭代
    没有办法检查是否还有遗留元素，也没有办法还原迭代器，

"""
s = 'ABC'  # 该字符串是可迭代的对象。背后是有迭代器的
for char in s:
    print(char)

# 使用while模拟循环
it = iter(s)  # 使用可迭代对象构造迭代器it
while True:
    try:
        print(next(it))  # 调用next函数获取下一个字符
    except StopIteration:  #
        del it  # 释放对it的引用
        break
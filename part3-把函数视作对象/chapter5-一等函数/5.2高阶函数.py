"""
接受函数作为参数，或把函数作为结果返回的函数是高阶函数

函数式语言常提供map,filter,reduce三个高阶函数。
列表推导或生成器表达式具有map,filter两个函数的功能，且更易于阅读
Python3中map,filter返回生成器
"""
# sorted函数，key参数用于提供一个函数，它应用到各个元素上进行排序
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits, key=len))


# 任何单参函数都能作为key参数的值
def reverse(word):
    return word[::-1]


print(reverse("testing"))
print(sorted(fruits, key=reverse))  # 根据反向拼写给单词列表排序


def factorial(n):
    """return n!"""
    return 1 if n < 2 else n * factorial(n - 1)


fact = factorial
print(list(map(fact, range(6))))
print([fact(n) for n in range(6)])
print(list(map(fact, filter(lambda n: n % 2, range(6)))))  # 奇数的阶乘
print([fact(n) for n in range(6) if n % 2])

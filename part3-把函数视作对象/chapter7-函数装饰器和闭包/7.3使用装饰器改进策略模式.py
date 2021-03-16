"""
使用装饰器将促销策略添加到promos列表中
优点：
促销策略函数不用特殊名称
便于禁用某个策略，只需将装饰器注释掉
策略可以在其他模块中定义，只要使用装饰器即可

多数装饰器会修改被装饰的函数。通常会定义一个内部函数，然后将其返回，替换被装饰的函数
"""
promos = []


def promotion(promo_func):
    promos.append(promo_func)
    return promo_func


@promotion
def fidelity(order):
    return 1


@promotion
def bult_item(order):
    return 2


@promotion
def large_order(order):
    return 3


print(promos)

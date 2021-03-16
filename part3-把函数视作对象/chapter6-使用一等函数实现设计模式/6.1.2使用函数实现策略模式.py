"""
原示例中每个策略都是一个类且都只定义了一个方法。策略实例没有状态。
把具体策略换成简单函数，且去掉了抽象类
普通函数也是可共享的对象，可以同时在多个上下文中使用

globals()
    返回一个字典，表示当前的全局符号表，始终针对当前模块

可内省单独的promotions模块
    inspect.getmembers函数获取对象的属性
    inspect.isfunction 获取模块中的函数
"""
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')  # fidelity忠诚度


class LineItem:  # 订单详情
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:  # 上下文，把一些计算委托给实现不同算法的可互换组件
    def __init__(self, customer, cart, promotion=None):  # cart 购物车
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total:{:.2f} due:{:.2f}>'
        return fmt.format(self.total(), self.due())


def fidelity_promo(order):
    return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0


def bulk_item_promo(order):
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * 0.1
    return discount


def large_order_promo(order):
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * 0.07
    return 0


promos = [fidelity_promo, bulk_item_promo, large_order_promo]  # 函数列表，函数是一等对象。有缺陷，构建新的促销策略要添加到列表中


def best_promo(order):
    return max(promo(order) for promo in promos)


joe = Customer('John', 0)
ann = Customer('Ann', 1100)
cart = [LineItem('banana', 4, 0.5),
        LineItem('apple', 10, 1.5),
        LineItem('water', 5, 5.0)]
print(Order(joe, cart, best_promo))  # 把促销函数作为参数传入，不用实例化新的促销对象

# 找出模块中的全部策略
promos_all = [globals()[name] for name in globals()
              if name.endswith('_promo')
              and name != 'best_promo']


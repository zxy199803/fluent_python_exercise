"""
“策略”模式：定义一系列算法，把它们一一封装起来，并使它们可以相互替换。本模式使得算法可以独立于使用它的客户而变化

电商领域，根据客户属性或订单中的商品计算折扣
"""
# 实现Order类，支持插入式折扣策略
from abc import ABC, abstractmethod
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
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total:{:.2f} due:{:.2f}>'
        return fmt.format(self.total(), self.due())


class Promotion(ABC):  # 策略：抽象基类。为了使用@abstractmethod装饰器，从而明确表明所用的模式
    @abstractmethod
    def discount(self, order):
        """返回折扣金额（正值）"""


class FidelityPromo(Promotion):  # 第一个具体策略
    """为积分1000或以上的顾客提供5%的折扣"""

    def discount(self, order):
        return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0


class BulkItemPromo(Promotion):  # 第二个具体策略
    """单个商品为20个或以上时提供10%折扣"""

    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * 0.1
        return discount


class LargeOrderPromo(Promotion):  # 第三个策略
    """订单中不同商品达到十个或以上时提供7%折扣"""

    def discount(self, order):
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * 0.07
        return 0


joe = Customer('John', 0)
ann = Customer('Ann', 1100)
cart = [LineItem('banana', 4, 0.5),
        LineItem('apple', 10, 1.5),
        LineItem('water', 5, 5.0)]
print(Order(joe, cart, FidelityPromo()))

import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])  # 只有属性没有方法的对象

'''
特殊方法使得自定义类型表现得和内置类型一样
通过实现特殊方法（data method又称magic method,dunder method）利用Python数据模型
    操作名称统一
    方便利用Python标准库，如random.choice()

不要自己调用特殊方法，最好使用内置函数使用特殊方法
'''


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


beer_card = Card('7', 'diamonds')
print(beer_card)

deck = FrenchDeck()
print(len(deck))  # 与python标准集一样可以用len()查看长度
print(deck[0])  # 由__getitem__方法提供
print(deck[-1])
print(choice(deck))  # 方便利用python标准库
print(deck[:5])  # 方便切片
# for card in deck:  # 可迭代
#     print(card)

suit_values = dict(spades=3, diamonds=2, clubs=1, hearts=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)  # 找到card值的序号
    return rank_value * len(suit_values) + suit_values[card.suit]


for card in sorted(deck, key=spades_high):  # 利用spades_high定义的规则对deck进行排序
    print(card)

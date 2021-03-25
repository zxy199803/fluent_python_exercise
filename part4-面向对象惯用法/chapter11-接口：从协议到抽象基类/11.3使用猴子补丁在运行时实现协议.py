"""
着重强调协议的动态本性

鸭子类型：对象的类型无关紧要，只要实现了特定的协议即可

如果遵守既定协议，很可能增加利用现有标准库和第三方代码的可能性

可变序列必须提供__setitem__方法

猴子补丁：在运行时修改类或模块，而不改动源码
协议是动态的，如random.shuffle不关心参数类型，只要对象实现了部分可变序列协议即可。
即便对象一开始没有所需方法也没关系，可以后来提供
不允许为内置类型打猴子补丁

了解现有协议可以充分利用Python的标准库
"""
from random import shuffle
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


# 打猴子补丁，让它变成可变的。突出协议的动态本性
def set_card(deck, position, card):
    deck._cards[position] = card

# 部分实现协议是有用的
FrenchDeck.__setitem__ = set_card
deck = FrenchDeck()
shuffle(deck)
print(deck[:5])

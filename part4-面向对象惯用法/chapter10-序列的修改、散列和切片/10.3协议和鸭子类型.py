"""
协议是非正式的接口，只在文档中定义，在代码中不定义，
如Python的序列协议只需要__len__和__getitem__两个方法，任何类只要使用标准的签名和语义实现了这两个方法，就能用在任何期待序列的地方

说它是序列是因为它的行为像序列

协议是非正式的，没有强制力。可以实现一个协议的部分
"""
import collections

Card = collections.namedtuple('Card',['rank','suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)+list('JQKA')]
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank,suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]
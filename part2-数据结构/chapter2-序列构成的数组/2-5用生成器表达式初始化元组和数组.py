symbols = '$¢£¥€¤'
t = tuple(ord(symbol) for symbol in symbols)  # 生成器表达式是唯一参数则不需要额外括号
print(t)

import array
a = array.array('I',((ord(symbol) for symbol in symbols)))  # array的构造方法需要两个参数，括号是必需的
print(a)
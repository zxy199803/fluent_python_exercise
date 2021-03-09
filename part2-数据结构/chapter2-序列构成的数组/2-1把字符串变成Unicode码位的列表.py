"""
列表推导
只用来创建新列表，并尽量简短（超过两行，考虑用for重写）
"""

symbols = 'abc'
symbol = 'd'
codes = [ord(symbol) for symbol in symbols]  # 表达式内部变量只在局部起作用，无变量泄露问题
print(codes)
print(symbol)



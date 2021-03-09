"""
序列支持+和*操作
通常+两侧序列由相同类型的数据所构成
拼接过程中两个被操作序列都不会被更改，Python会创建一个新序列
"""
l = [1, 2, 3]
print(l * 5)
print(5 * l)
print(5 * 'abcd')

board = [['_'] * 3 for i in range(3)]
print(board)
board[1][2] = 'x'
print(board)

# 含有3个指向同一对象的引用的列表是毫无用处的
weird_board = [['_'] * 3] * 3  # 列表内的引用指向同一个对象
print(weird_board)
weird_board[1][2] = '0'
print(weird_board)

# 错误本质上与上面相同
row = ['_']*3
weird_board_2 = []
for i in range(3):
    weird_board_2.append(row)
weird_board_2[1][2] = '2'
print(weird_board_2)

#与正确做法等同
fine_board = []
for i in range(3):
    row = ['_'] * 3 # 每次都新建了一个列表
    fine_board.append(row)
fine_board[1][2] = 'f'
print(fine_board)
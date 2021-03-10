import bisect
import sys

'''
bisect函数是bisect_right的别名
bisect_left 新元素放置于它相等元素的左边
'''

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]  # 干草垛
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d}   {2}{0:<2d}'


def demo(bisect_fn):
    for neddle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, neddle)  # 计算元素出现的位置
        offset = position * '  |'
        print(ROW_FMT.format(neddle, position, offset))


print(__name__)
if __name__ == '__main__':  # 当模块被直接执行时，__name__ == 'main' 结果为真
    if sys.argv[-1] == 'left':  # Sys.argv[ ]其实就是一个列表，里边的项为用户输入的参数，这参数是从程序外部输入的，要想看到它的效果就应该将程序保存了，从外部来运行程序并给出参数。
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect_right
    print('DEMO:', bisect_fn.__name__)
    print('haystack->', ' '.join('%2d' % n for n in HAYSTACK))
    demo(bisect_fn)

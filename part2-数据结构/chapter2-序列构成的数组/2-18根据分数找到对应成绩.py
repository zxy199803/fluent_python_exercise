import bisect

'''
利用bisect函数在很长的有序序列作为index的替代，更快查找元素位置
bisect需输入有序序列，即二分查找要求有序序列
'''


def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    print(i)
    return grades[i]


print([grade(score) for score in [60, 50, 99]])

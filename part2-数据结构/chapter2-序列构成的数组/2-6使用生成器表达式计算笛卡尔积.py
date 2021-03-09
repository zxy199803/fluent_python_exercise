colors = ['black', 'white']
sizes = ['s', 'm', 'l']
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)
'''
生成器表达式逐个产出元素，不会一次性产生列表，节省for循环开销
'''
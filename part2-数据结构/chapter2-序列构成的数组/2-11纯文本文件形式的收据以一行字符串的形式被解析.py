"""
切片和区间操作不包含区间范围的最后一个元素
以0作为起始下标
好处：
1.只有最后一个位置信息时，快速看出有几个元素，my_list[:3]有三个元素
2.起止都可见时，区间长度=stop-start
3.利用任一下标将序列分成两部分，my_list[:x],my_list[x:]
"""

# seq[start:stop:step]
s = 'bicycle'
print(s[::-2])

invoice = """
0.....6................................40........52...55........
1909  Pimoroni PiBrella                $17.50    3    $52.50
1489  6mm Tactile Switch x20           $4.95     2    $9.90
1510  Panavise Jr. - PV-201            $28.00    1    $28.00
1601  PiTFT Mini Kit 320x240           $34.95    1    $34.95
"""
# invoice 发票；发货单
SKU = slice(0, 6)
DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(39, 52)
QUANTITY = slice(52, 55)
ITEM_TOTAL = slice(55, None)
line_items = invoice.split('\n')[2:]
# slice() 函数实现切片对象，主要用在切片操作函数里的参数传递。增强可读性
for item in line_items:
    print(item[UNIT_PRICE], item[DESCRIPTION])

'''
切片可用来就地修改可变序列
把切片放在赋值语句的左边，可对序列进行嫁接、切除、就地修改
'''
l = list(range(10))
print(l)
l[2:5] = [20, 30]  # l[4]被删除
print(l)
del l[5:7]
print(l)
l[3::2] = [11, 22]
print(l)
# l[2:5] = 100 右侧必须是可迭代形式
l[2:5]=[100]
print(l)

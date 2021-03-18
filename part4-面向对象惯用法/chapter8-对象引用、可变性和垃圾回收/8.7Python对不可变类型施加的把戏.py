"""
使用另一个元组构建的元组，得到的是同一个元组

共享字符串的字面量是种优化措施，称为驻留(interning)
"""
t1 = (1,2,3)
t2 = tuple(t1)
print(t1 is t2)
t3 = t1[:]
print(t3 is t1)

s1 = 'ABC'
s2 = 'ABC'
print(s1 is s2)
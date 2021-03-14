"""
为使用高阶函数，创建一次性的小型函数。lamba关键字 创建匿名函数
lamba函数的定义体中不能赋值，不能使用while,try等语句
参数列表中最适合使用，lamba句法是句法糖，与def一样会创建函数对象
除了作为参数传给高阶函数外Python很少使用匿名函数
"""
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits,key=lambda word: word[::-1]))
"""
上下文管理器对象的存在目的是管理with语句
迭代器是为了管理for语句

with语句的目的是简化try/finally模式,用于保证一段代码运行完毕后执行某项操作，即便因为异常，return等终止也会执行
finally子句中的代码常用于释放重要资源或还原临时更改的状态

上下文管理器协议包含__enter__和__exit__方法
    with语句开始运行时，会在上下文管理器对象上调用__enter__方法
    结束运行时调用__exit__方法

最常见的例子是确保关闭文件对象
with块没有定义新的作用域

__exit__(self, exc_type, exc_val, exc_tb)
    exc_type 异常类
    exc_val 异常实例
    exc_tb traceback对象
"""


class LookingGlass:
    def __enter__(self):  # Python调用__enter__方法只传入self参数
        import sys
        self.original_write = sys.stdout.write  # 将其保存在一个实例属性中
        sys.stdout.write = self.reverse_write  # 打猴子补丁，替换成自己编写的方法
        return None  # 返回的内容存入目标变量what

    def reverse_write(self, text):
        self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_val, exc_tb):  # 异常数据
        import sys  # Python会缓存导入的模块，重复导入模块不会消耗很多资源
        sys.stdout.write = self.original_write  # 还原原来的方法
        if exc_type is ZeroDivisionError:
            print('Please DO not divide by Zero')
            return True  # 返回True告诉Python异常已经处理了

None
with LookingGlass() as what:
    print('abc')
    print(what)

print(what)
print('abc')

# with块之外使用LookingGlass类
manager = LookingGlass()
print(manager)
monster = manager.__enter__()
print(monster == None)
print(monster)
manager.__exit__(None,None,None)
print(monster)
"""
获取对象字符串表示形式的标准方式
    repr()以便于开发者理解的方式返回对象的字符串表示形式
    str()以便于用户理解的方式返回对象的字符串表示形式
    bytes()获取对象的字节序列表示形式
    __format__被内置的format()函数和str.format()调用，使用特殊的格式代码显示对象的字符串表示形式
要实现__repr__和__str__特殊方法，为repr()和str()提供支持

"""
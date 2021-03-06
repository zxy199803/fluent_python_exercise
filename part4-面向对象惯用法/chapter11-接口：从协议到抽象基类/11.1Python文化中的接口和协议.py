"""
抽象类表示接口

除了抽象基类，每个类都有接口：类实现或继承的公开属性

受保护的属性和私有属性不在接口中。受保护的属性是采用命名约定实现的，私有属性也可轻松访问

接口的补充定义：对象公开方法的子集，让对象在系统中扮演特定的角色。
接口是实现特定角色方法的集合。

协议是接口，但不是正式的，只由文档和约定定义。协议不能像正式接口那样施加限制。一个类可实现部分接口

对Python来说，X类对象，X协议，X接口都是一个意思
协议风格的接口与继承完全没有关系，实现同一个协议的各个类是相互独立的
"""
"""
else子句不仅能在if语句使用，还能在for,while,try语句使用

for
    仅当for循环运行完毕时（即没有被break语句中止）才运行else块
while
    仅当while循环因为条件为假值而退出时（即没有被break语句中止）才运行else块
try
    仅当try块没有异常抛出时才运行else块，else子句抛出的异常不会由前面的except子句处理

如果异常，return,break,continue语句导致控制权跳到了复合语句主块之外，else语句也会被跳过

循环中else语义：运行这个循环然后做那件事，类似（then）
"""
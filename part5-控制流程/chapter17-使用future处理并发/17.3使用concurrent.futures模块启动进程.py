"""
concurrent,futures模块实现的是真正的并行计算，使用ProcessPoolExecutor类把工作分配给多个Python进程处理。使用这个模块能绕开GIL利用所有CPU核心

ProcessPoolExecutor　和　ThreadPoolExecutor都实现了通用的Executor接口

ThreadPoolExecutor CPU密集型处理，数量不超过CPU数量的线程
ProcessPoolExecutor I/O密集型，可有多个线程，取决于做什么是及可用内存

使用Python处理ＣＰＵ密集工作，试试PyPy
"""
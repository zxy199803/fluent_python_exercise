"""
仿真时协程的经典应用
离散事件仿真
    把系统建模成一系列事件的仿真类型。仿真“钟”向前推进的量不是固定的，而是直接推进到下一个事件模型的模拟时间
    如模拟出租车运营，乘客上车、乘客下车，一旦乘客下车仿真钟就会更新，指向此次运营的结束时间
    如回合制游戏，游戏状态只在玩家操作时变化，一旦决定了仿真钟就会冻结
连续仿真
    仿真钟以固定量不断向前推进

协程暂停 ->主程序处理下一个事件，激活时(发送send()) ->协程继续

协程显式自主地把控制权让步给中央调度程序
多线程实现的是抢占式多任务，调度程序可以在任何时刻暂停线程，把控制权让给其他线程
"""
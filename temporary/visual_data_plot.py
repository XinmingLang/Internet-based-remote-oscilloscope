import matplotlib.pyplot as plt
import pandas as pd
import math
import itertools
import matplotlib.animation as animation
#模拟数据更新#####
import threading
import time
import random
received_data = []
def simulate_device():
    """模拟另一个设备每隔0.06秒发送一个数据"""
    while True:
        # 模拟设备发来的随机值
        value = random.uniform(-1, 1) 
        # 写入全局列表
        received_data.clear()  # 为了简单，只保留最新一个值
        received_data.append(value)
        time.sleep(0.06) # 和 animation 的 interval 保持一致

# 在 plt.show() 之前启动模拟设备线程
threading.Thread(target=simulate_device, daemon=True).start()
#################

# 创建一个示例数据框
fig, ax = plt.subplots()

data = {'Time': [0], 'Value': [0]}
df = pd.DataFrame(data)

# 绘制折线图
line  = ax.plot(df['Time'], df['Value'])[0]
ax.set(xlim=[data['Time'][0],data['Time'][0]+100], ylim=[-1, 1], xlabel='Time', ylabel='Value')
ax.legend()

def update(frame):
    
    # 模拟数据更新
    new_time = frame
    if len(received_data) > 0:
        # 假设 received_data 存储的是数值
        new_value = received_data[-1] # 取最新的值
        # 注意：取出来后，根据你的需求决定是否要清空列表或删除该元素
        # 如果是实时流，通常只保留最新一个，或者清空
    else:
        # 如果没有接收到数据，给一个默认值（防止报错）
        new_value = 0
    df.loc[len(df)] = [new_time, new_value]
    
    if len(df) > 100:
        df.drop(index=0, inplace=True)
        df.reset_index(drop=True, inplace=True)
    
    # 更新折线图数据
    line.set_xdata(df['Time'])
    line.set_ydata(df['Value'])
    x_min = max(0, frame - 100) 
    x_max = max(frame,100)
    ax.set(xlim=[x_min, x_max], ylim=[-1, 1], xlabel='Time', ylabel='Value')
    
    return line,

ani = animation.FuncAnimation(fig=fig, func=update, frames=itertools.count(0), interval=30)
plt.show()
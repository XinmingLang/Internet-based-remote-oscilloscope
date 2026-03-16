# main.py
import sys
import math
import itertools
import pandas as pd
from PySide6.QtWidgets import QApplication, QMainWindow
from matplotlib import animation
from sympy.plotting.intervalmath import interval
from pyreciever.reciever import reciever
import threading

# 1. 导入转换好的 UI 模块
from .pc_ui import Ui_MainWindow  # 假设你的 UI 是 MainWindow 类型

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.values = []
        self.ani_started = False

        # --- 2. 设置 UI ---
        # 这里直接调用 setupUi
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # 将 UI 设置到当前窗口
        self.ui.reciever.data_received.connect(self.handle_data)  # 连接信号和槽函数

        # --- 3. 获取绘图控件 ---
        # 这里的 'widget_plot' 必须和你在 Qt Designer 里给那个 Widget 设置的 objectName 保持一致
        self.plot_widget = self.ui.widget

        # --- 4. 初始化数据 ---
        self.df = pd.DataFrame({'Frame': [], 'Value': []})
        self.current_frame = 0

        # --- 5. 在控件上初始化图形 ---
        self.plot_widget.ax.clear()
        self.line, = self.plot_widget.ax.plot([], [])
        self.plot_widget.ax.set_xlim(0, 100)
        self.plot_widget.ax.set_ylim(-1, 1)
        self.plot_widget.ax.set_xlabel('Frame(30ms per frame)')
        self.plot_widget.ax.set_ylabel('Value')
        self.plot_widget.start_animation(self.update,interval=30)

    def flush_anime(self,ylim,ms_per_frame):
        self.plot_widget.ax.clear()
        self.line, = self.plot_widget.ax.plot([], [])
        self.plot_widget.ax.set_xlim(0, 100)
        self.plot_widget.ax.set_ylim(0-ylim, ylim)
        self.plot_widget.ax.set_xlabel('Frame({ms_per_frame} ms per frame)'.format(ms_per_frame=ms_per_frame))
        self.plot_widget.ax.set_ylabel('Value')
        self.plot_widget.start_animation(self.update,interval=ms_per_frame)    
        

    def handle_data(self, value):
        self.values.append(value)
        print(f"Recieved data: {value}")
        '''
        # --- 6. 启动动画 ---
        if not self.ani_started:
            self.plot_widget.start_animation(self.update,interval=30)
            self.ani_started = True
'''
    def update(self,frame):
        # --- 模拟数据 ---
        if len(self.values) > 0:
            new_value = self.values.pop(0)
        else:
            new_value = 0
        new_row = pd.DataFrame({'Frame': [self.current_frame], 'Value': [new_value]})
        # --- 更新数据 ---
        self.df = pd.concat([self.df,new_row], ignore_index=True)
        self.current_frame += 1
        if len(self.df) > 100:
            self.df=self.df.iloc[-100:].reset_index(drop=True)

        # --- 更新图形 ---
        if len(self.df) > 0:
            self.line.set_data(self.df['Frame'], self.df['Value'])

        # 动态移动 X 轴
        window_width = 100
        x_min = max(0, frame - window_width)
        x_max = x_min + window_width
        self.plot_widget.ax.set_autoscalex_on(False)
        self.plot_widget.ax.set_xlim(x_min, x_max)

        # 返回值用于 blit 优化
        return [self.line]


def start():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
# mplwidget.py
from PySide6.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib import animation


class MplWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # 1. 创建 Matplotlib 的 Figure 和 Canvas
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        # 2. 创建布局并将 Canvas 加入布局
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)

        # 3. 获取绘图轴对象，供后续绘图使用
        self.ax = self.figure.add_subplot(111)

        self.ani = None
        self._paused = False

    def start_animation(self, update_func, interval=60):
        """
        启动动画
        :param update_func: 更新函数
        :param interval: 刷新间隔
        """
        # 创建 FuncAnimation 对象
        # 注意：这里设置一个 frames，比如 itertools.count(0)
        import itertools
        self.ani = animation.FuncAnimation(
            self.figure,
            update_func,
            frames=itertools.count(0),
            interval=interval,
            #blit=True,
            cache_frame_data=False,
        )
        # 初始状态如果是暂停，则立即暂停
        if self._paused:
            self.ani.pause()

    def toggle_pause(self):
        """
        槽函数：用于切换暂停/继续
        你可以通过按钮点击或快捷键触发这个槽
        """
        if self.ani is None:
            return

        if self._paused:
            self.ani.resume()
            self._paused = False
            print("动画恢复")
        else:
            self.ani.pause()
            self._paused = True
            print("动画暂停")

    @property
    def paused(self):
        return self._paused
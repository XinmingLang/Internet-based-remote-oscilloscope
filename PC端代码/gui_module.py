import sys
from PyQt5.QtWidgets import *
import pyautogui as pg

def raise_messagebox(note,message):
        msg = QMessageBox()
        msg.setWindowTitle(note)
        msg.setText(message)
        msg.setIcon(QMessageBox.Information)
        msg.exec_()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        #获取当前屏幕大小
        screen_width, screen_height = pg.size()
        
        main_window_width = int(screen_width/4)
        main_window_height = int(screen_height/2)
        
        # 设置窗口标题和大小
        self.setWindowTitle("远程示波器")
        self.setGeometry(int(screen_width*3/8), int(screen_height/4), main_window_width, main_window_height)  # x, y, width, height
        
        button_width = int(main_window_width/3)
        button_height = int(main_window_height/6)
        
        # 创建按钮
        self.button = QPushButton("连接示波器", self)
        self.button.setGeometry(button_width, main_window_height-300, button_width, button_height)  # x, y, width, height
        self.button.clicked.connect(self.try_connect_oscilloscope)
        
    def try_connect_oscilloscope(self):
        raise_messagebox("提示","连接示波器功能尚未实现")

def run_app():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    print("This module is not intended to be run directly.Please import it as a module.")
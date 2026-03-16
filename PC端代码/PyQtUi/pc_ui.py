# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pc.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget,QMessageBox)
from PySide6.QtWidgets import QLabel,QLineEdit

from .mplwidget import MplWidget
import sys,re
from pyreciever import reciever
import threading

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 500)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = MplWidget(self.centralwidget)
        self.widget.setObjectName(u"波形窗口")
        self.widget.setGeometry(QRect(0, 0, 670, 450))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"退出键")
        self.pushButton.setGeometry(QRect(670, 0, 130, 60))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"切换播放状态按键")
        self.pushButton_3.setGeometry(QRect(670, 60, 130, 60))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"ip:端口提示文字")
        self.label.setGeometry(QRect(670, 120, 120, 30))
        self.label.setText("Enter Server's 'IP:PORT'")
        self.label.setWordWrap(True)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"用户输入ip和端口的位置")
        self.lineEdit.setGeometry(QRect(670, 150, 60, 30))
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"连接按钮")
        self.pushButton_4.setGeometry(QRect(730, 150, 70, 30))
        self.label1 = QLabel(self.centralwidget)
        self.label1.setObjectName(u"提示y轴范围")
        self.label1.setGeometry(QRect(670, 180, 120, 30))
        self.label1.setText("Set y limits(in abs):")
        self.label1.setWordWrap(True)
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"用户输入y轴范围的位置")
        self.lineEdit_2.setGeometry(QRect(670, 210, 60, 30))
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"设置y轴范围按钮")
        self.pushButton_5.setGeometry(QRect(730, 210, 70, 30))
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"用户输入刷新率的位置")
        self.lineEdit_3.setGeometry(QRect(670, 270, 60, 30))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"提示刷新率")
        self.label_3.setGeometry(QRect(670, 240, 120, 30))
        self.label_3.setText("Set millisecond per frame:")
        self.label_3.setWordWrap(True)
        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"设置刷新率按钮")
        self.pushButton_6.setGeometry(QRect(730, 270, 70, 30))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.close)
        self.pushButton_3.clicked.connect(self.flushtext)
        self.pushButton_3.clicked.connect(self.widget.toggle_pause)
        self.pushButton_4.clicked.connect(self.connect_server)

        
        self.reciever = reciever.reciever()
        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Oscilloscope", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        if self.widget.paused:
            self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"StartAnime", None))
        else:
            self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PauseAnime", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow",u"Connect",None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow",u"Set",None))
    # retranslateUi

    def flushtext(self):
        if not self.widget.paused:
            self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"StartAnime", None))
        else:
            self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PauseAnime", None))
            
    def connect_server(self):
        ip_port = re.split(':',self.lineEdit.text())
        self.lineEdit.clear()
        if len(ip_port) != 2:
            QMessageBox.critical(None, "Error", "Invalid input format. Please enter in 'IP:PORT' format.")
            print("Invalid input format. Please enter in 'IP:PORT' format.")
            return
        ip, port = ip_port
        if not re.match(r"^\d{1,3}(\.\d{1,3}){3}$", ip):
            QMessageBox.critical(None, "Error", "Invalid IP address format. Please enter a valid IP.")
            print("Invalid IP address format. Please enter a valid IP.")
            return
        if not port.isdigit() or not (0 < int(port) < 65536):
            QMessageBox.critical(None, "Error", "Invalid port number. Please enter a number between 1 and 65535.")
            print("Invalid port number. Please enter a number between 1 and 65535.")
            return
        print("Connecting to server at IP:PORT @", ip+':'+port)
        url = "http://"+ip+':'+port+"/value"
        thread = threading.Thread(target=self.reciever.recievefromurl, args=(url,), daemon=True)
        thread.start()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
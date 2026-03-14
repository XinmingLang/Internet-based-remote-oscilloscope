import requests
import time
from PySide6.QtCore import Signal,QObject
from PySide6.QtWidgets import QMessageBox


class reciever(QObject):
    data_received = Signal(float)  # 定义一个信号，传递接收到的数据
    connected = False

    def recievefromurl(self,url):
        while True:
            try:
                r = requests.get(url,timeout = 5)
                data = r.json()
                print("AIN0 = ",data["ain0"])
                self.data_received.emit(float(data["ain0"]))  # 发射信号，传递数据
            except Exception as e:
                QMessageBox.critical(None, "Error", f"Failed to connect to server:\n{e.__class__.__name__}\nPlease check the server and your network connection, or try again later.")
                print("Failed:",e.__class__.__name__,"\nPlease check the server and your network connection,or try again later.")
                return
            if not self.connected:
                self.connected = True
                #QMessageBox.information(None, "Success", "Successfully connected to server.")
                print("Successfully connected to server.")
            time.sleep(0.1)

'''
if __name__ == "__main__":
    while True:
        try:
            r = requests.get(url,timeout = 1)
            data = r.json()
            print("AIN0 = ",data["ain0"])
        except Exception as e:
            print("Failed:",e)
        time.sleep(0.2)

'''
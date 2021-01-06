# -*- coding: utf-8 -*-
# @Time    : 2021/1/6 16:06
# @Author  : Naruto
# @Email   : the-naruto@foxmail.com
# @Project : pyQT5-tutorial-code



import sys
from PyQt5.QtCore import Qt,pyqtSignal,QObject
from PyQt5.QtWidgets import QMainWindow,QApplication
'''
QObject实例能发送事件信号。下面的例子是发送自定义的信号。

'''

class Communicate(QObject):
    closeApp = pyqtSignal()



class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.c = Communicate()
        # 创建了一个叫closeApp的信号并与QMainWindow的close()方法绑定。
        self.c.closeApp.connect(self.close)


        self.setGeometry(300,300,200,150)
        self.setWindowTitle('信号发送')
        self.show()

    # 信号会在鼠标按下的时候触发
    def mousePressEvent(self, e):
        self.c.closeApp.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

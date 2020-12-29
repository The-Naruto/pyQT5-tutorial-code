# -*- coding: utf-8 -*-
# @Time    : 2020/12/29 15:02
# @Author  : Naruto
# @Email   : the-naruto@foxmail.com
# @Project : pyQT5-tutorial-code

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 调用QtGui.QMainWindow类的statusBar()方法，创建状态栏。
        # 第一次调用会创建一个状态栏，而再次调用会返回一个状态栏对象。
        # showMessage()方法在状态栏上显示一条信息。
        self.statusBar().showMessage('Ready')

        self.setGeometry(300,300,250,150)
        self.setWindowTitle('状态栏')
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())












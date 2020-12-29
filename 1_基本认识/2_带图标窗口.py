# -*- coding: utf-8 -*-
# @Time    : 2020/12/29 9:36
# @Author  : Naruto
# @Email   : the-naruto@foxmail.com
# @Project : pyQT5-Study

import sys

from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QIcon

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 同时设置大小和位置
        self.setGeometry(300,300,300,200)
        self.setWindowTitle('带图标窗口')
        # 定义并设置图标
        self.setWindowIcon(QIcon('web.jpg'))

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
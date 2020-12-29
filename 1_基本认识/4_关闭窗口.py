# -*- coding: utf-8 -*-
# @Time    : 2020/12/29 13:38
# @Author  : Naruto
# @Email   : the-naruto@foxmail.com
# @Project : pyQT5-Study

import sys

from PyQt5.QtWidgets import QApplication,QWidget,QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建一个继承自QPushButton的按钮。创建一个继承自QPushButton的按钮。
        qbtn = QPushButton('退出',self)
        # 退出事件的绑定
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        # sizeHint 表示默认尺寸
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50,50)
        self.setGeometry(300,300,300,200)
        self.setWindowTitle('关闭窗口')
        self.setWindowIcon(QIcon('web.jpg'))

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
# -*- coding: utf-8 -*-
# @Time    : 2020/12/29 9:36
# @Author  : Naruto
# @Email   : the-naruto@foxmail.com
# @Project : pyQT5-Study

import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication)
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QIcon

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置提示框字体
        QToolTip.setFont(QFont('SansSerif',10))
        # 为控件设置提示内容, 这里是为主窗体设置提示框
        self.setToolTip('这是一个<b>QWidget</b>')

        btn = QPushButton('Button',self)
        # 为按钮设置提示内容
        btn.setToolTip('这是一个<b>按钮</b>')
        btn.resize(btn.sizeHint())
        btn.move(50,50)

        self.setGeometry(300,300,300,200)
        self.setWindowTitle('提示框窗口')
        self.setWindowIcon(QIcon('web.jpg'))

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
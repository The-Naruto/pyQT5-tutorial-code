# -*- coding: utf-8 -*-
# @Time    : 2021/1/12 10:20
# @Author  : Naruto
# @Email   : the-naruto@foxmail.com
# @Project : pyQT5-tutorial-code

from PyQt5.QtWidgets import (QWidget, QHBoxLayout,
    QLabel, QApplication)
from PyQt5.QtGui import QPixmap
import sys
'''
QPixmap是处理图片的组件。本例中，
我们使用QPixmap在窗口里显示一张图片。

'''


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)
        # 创建一个QPixmap对象，接收一个文件作为参数。
        pixmap = QPixmap("web.jpg")

        lbl = QLabel(self)
        # 把QPixmap实例放到QLabel组件里。
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.move(300, 200)
        self.setWindowTitle('Red Rock')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
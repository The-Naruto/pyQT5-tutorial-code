# -*- coding: utf-8 -*-
# @Time    : 2021/1/6 13:49
# @Author  : Naruto
# @Email   : the-naruto@foxmail.com
# @Project : pyQT5-tutorial-code

import sys
from PyQt5.QtWidgets import QWidget,QLabel,QApplication

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        lbl1 = QLabel('ZerCode',self)
        # 这个元素的左上角就在这个程序的左上角开始的(15, 10)的位置
        lbl1.move(15,10)

        lbl2 = QLabel('Turorials',self)
        lbl2.move(35,40)

        lbl3 = QLabel('for programmers',self)
        lbl3.move(55,70)

        self.setGeometry(300,300,250,150)
        self.setWindowTitle('Absolute')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())







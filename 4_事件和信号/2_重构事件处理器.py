# -*- coding: utf-8 -*-
# @Time    : 2021/1/6 15:25
# @Author  : Naruto
# @Email   : the-naruto@foxmail.com
# @Project : pyQT5-tutorial-code

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget,QLCDNumber,QSlider,QVBoxLayout,QApplication

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setGeometry(300,300,200,150)
        self.setWindowTitle('Signal and slot')
        self.show()


    def keyPressEvent(self, e):

        # 点击esc键的时候退出程序
        if e.key() == Qt.Key_Escape:
            self.close()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

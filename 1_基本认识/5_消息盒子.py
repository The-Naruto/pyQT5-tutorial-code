# -*- coding: utf-8 -*-
# @Time    : 2020/12/29 9:36
# @Author  : Naruto
# @Email   : the-naruto@foxmail.com
# @Project : pyQT5-Study

import sys

from PyQt5.QtWidgets import QApplication,QWidget, QMessageBox
from PyQt5.QtGui import QIcon

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,300,200)
        self.setWindowTitle('带图标窗口')
        self.setWindowIcon(QIcon('web.jpg'))

        self.show()
    # 如果关闭QWidget，就会产生一个QCloseEvent，并且把它传入到closeEvent函数的event参数中。
    def closeEvent(self,event):
        reply = QMessageBox.question(self,'提示',
                "确认离开?",QMessageBox.Yes|QMessageBox.No,QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
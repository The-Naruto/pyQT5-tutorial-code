# -*- coding: utf-8 -*-
# @Time    : 2021/1/8 9:05
# @Author  : Naruto
# @Email   : the-naruto@foxmail.com
# @Project : pyQT5-tutorial-code

from PyQt5.QtWidgets import QWidget,QCheckBox,QApplication, QFrame,QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # 创建一个复选框
        cb = QCheckBox('Show title',self)
        cb.move(20,20)
        # 默认选中
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)




        self.setGeometry(300,300,250,150)
        self.setWindowTitle('QCheckBox')
        self.show()

    def changeTitle(self,state):
        if state == Qt.Checked:
            self.setWindowTitle('复选框被选中')
        else:
            self.setWindowTitle('复选框未被选中')


if __name__ =='__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


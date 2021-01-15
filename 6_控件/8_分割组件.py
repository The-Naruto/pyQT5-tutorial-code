# -*- coding: utf-8 -*-
# @Time    : 2021/1/12 11:16
# @Author  : Naruto
# @Email   : the-naruto@foxmail.com
# @Project : pyQT5-tutorial-code
'''
QSplitter组件能让用户通过拖拽分割线的方式改变子窗口大小的组件。
本例中我们展示用两个分割线隔开的三个QFrame组件。
'''

import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout,QFrame,QSplitter,\
                             QStyleFactory, QApplication)
from PyQt5.QtCore import Qt

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        hbox =QHBoxLayout(self)

        topleft = QFrame(self)
        # 为了更清楚的看到分割线，我们使用了设置好的子窗口样式。
        topleft.setFrameShape(QFrame.StyledPanel)

        topright = QFrame(self)
        topright.setFrameShape(QFrame.StyledPanel)

        bottom = QFrame(self)
        bottom.setFrameShape(QFrame.StyledPanel)

        # 创建一个QSplitter组件，并在里面添加了两个框架。
        spl1 = QSplitter(Qt.Horizontal)
        spl1.addWidget(topleft)
        spl1.addWidget(topright)

        # 也可以在分割线里面再进行分割。
        spl2 = QSplitter(Qt.Vertical)
        spl2.addWidget(spl1)
        spl2.addWidget(bottom)

        hbox.addWidget(spl2)
        self.setLayout(hbox)


        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QLineEdit')
        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
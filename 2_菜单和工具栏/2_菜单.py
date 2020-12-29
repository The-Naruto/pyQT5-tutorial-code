# -*- coding: utf-8 -*-
# @Time    : 2020/12/29 9:36
# @Author  : Naruto
# @Email   : the-naruto@foxmail.com
# @Project : pyQT5-Study

import sys

from PyQt5.QtWidgets import QApplication,QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAct = QAction(QIcon('web.jpg'),'&Exit',self)
        exitAct.setShortcut('Ctrl+D')
        exitAct.setStatusTip('Exit app')
        exitAct.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)


        # 同时设置大小和位置
        self.setGeometry(300,300,300,200)
        self.setWindowTitle('带图标窗口')


        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
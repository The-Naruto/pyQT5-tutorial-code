# -*- coding: utf-8 -*-
# @Time    : 2021/1/6 10:44
# @Author  : Naruto
# @Email   : the-naruto@foxmail.com
# @Project : pyQT5-tutorial-code


import sys

from PyQt5.QtWidgets import QApplication,QMainWindow, QAction, qApp,QMenu
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')


        impMenu = QMenu('Import',self)
        impAct = QAction('Import mail',self)
        # 添加动作会自动添加菜单
        impMenu.addAction(impAct)

        newAct = QAction('New',self)
        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)

        # 同时设置大小和位置
        self.setGeometry(300,300,300,200)
        self.setWindowTitle('带图标窗口')


        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
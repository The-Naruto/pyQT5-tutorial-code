# -*- coding: utf-8 -*-
# @Time    : 2021/1/6 13:26
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

        exitAct = QAction(QIcon('web.jpg'),'Exit',self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(qApp.quit)

        self.toolbar = self.addToolBar('Exit')
        # 用addToolBar()创建工具栏，并用addAction()将动作对象添加到工具栏。
        self.toolbar.addAction(exitAct)

        # 同时设置大小和位置
        self.setGeometry(300,300,300,200)
        self.setWindowTitle('右键菜单')
        self.show()







if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
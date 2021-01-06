# -*- coding: utf-8 -*-
# @Time    : 2021/1/6 13:35
# @Author  : Naruto
# @Email   : the-naruto@foxmail.com
# @Project : pyQT5-tutorial-code


import sys

from PyQt5.QtWidgets import QApplication,QMainWindow, QAction, qApp,QMenu,QTextEdit
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        textEdit = QTextEdit()
        # 创建了一个文本编辑区域，
        # 并把它放在QMainWindow的中间区域。这个组件会占满所有剩余的区域。
        self.setCentralWidget(textEdit)

        exitAct = QAction(QIcon('web.jpg'),'Exit',self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('退出应用程序')
        exitAct.triggered.connect(self.close)

        self.statusBar()

        menuabr = self.menuBar()
        fileMenu = menuabr.addMenu('&File')
        fileMenu.addAction(exitAct)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAct)


        # 同时设置大小和位置
        self.setGeometry(300,300,300,200)
        self.setWindowTitle('右键菜单')
        self.show()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
# -*- coding: utf-8 -*-
# @Time    : 2021/1/6 10:55
# @Author  : Naruto
# @Email   : the-naruto@foxmail.com
# @Project : pyQT5-tutorial-code




import sys

from PyQt5.QtWidgets import QApplication,QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):


        self.statusBar = self.statusBar()
        self.statusBar.showMessage('Ready')



        menubar = self.menuBar()
        viewMenu = menubar.addMenu('View')

        viewStatAct = QAction('View statubar',self,checkable=True)
        viewStatAct.setStatusTip('View statubar or not?')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.toggleMenu)

        viewMenu.addAction(viewStatAct)

        # 同时设置大小和位置
        self.setGeometry(300,300,300,200)
        self.setWindowTitle('带图标窗口')
        self.show()
    def toggleMenu(self,state):
        if state:
            self.statusBar.show()
        else:
            self.statusBar.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
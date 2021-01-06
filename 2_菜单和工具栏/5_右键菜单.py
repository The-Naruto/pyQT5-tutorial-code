# -*- coding: utf-8 -*-
# @Time    : 2021/1/6 13:19
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

        # 同时设置大小和位置
        self.setGeometry(300,300,300,200)
        self.setWindowTitle('右键菜单')
        self.show()

    def contextMenuEvent(self, event):
        cmenu = QMenu(self)

        newAct = cmenu.addAction('New')
        opnAct = cmenu.addAction('Open')
        quitAct = cmenu.addAction('Quit')

        # 使用exec_()方法显示菜单。从鼠标右键事件对象中获得当前坐标。
        # mapToGlobal()方法把当前组件的相对坐标转换为窗口（window）的绝对坐标。
        action = cmenu.exec_(self.mapToGlobal(event.pos()))

        if action ==quitAct:
            qApp.quit()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
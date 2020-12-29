# -*- coding: utf-8 -*-
# @Time    : 2020/12/29 9:36
# @Author  : Naruto
# @Email   : the-naruto@foxmail.com
# @Project : pyQT5-Study

import sys

# QtGui.QDesktopWidget提供了用户的桌面信息，包括屏幕的大小
from PyQt5.QtWidgets import QApplication,QWidget, QDesktopWidget
from PyQt5.QtGui import QIcon

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(250,150)
        self.center()

        self.setWindowTitle('带图标窗口')
        self.setWindowIcon(QIcon('web.jpg'))

        self.show()

    def center(self):
        # 获得主窗口所在的框架。
        qr = self.frameGeometry()
        # 获取显示器的分辨率，然后得到屏幕中间点的位置。
        cp = QDesktopWidget().availableGeometry().center()
        # 然后把主窗口框架的中心点放置到屏幕的中心位置。
        qr.moveCenter(cp)
        # 然后通过move函数把主窗口的左上角移动到其框架的左上角，这样就把窗口居中了。
        self.move(qr.topLeft())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
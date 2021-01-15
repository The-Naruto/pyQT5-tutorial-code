# -*- coding: utf-8 -*-
# @Time    : 2021/1/13 9:59
# @Author  : Naruto
# @Email   : the-naruto@foxmail.com
# @Project : pyQT5-tutorial-code
'''
这个例子展示怎么拖放一个button组件。
'''

from PyQt5.QtWidgets import QPushButton,QWidget,QApplication
from PyQt5.QtCore import Qt,QMimeData
from PyQt5.QtGui import QDrag
import sys

# 首先用QPushButton上构造一个按钮实例。
class Button(QPushButton):
    def __init__(self,title,parent):
        super().__init__(title,parent)

    # 拖拽开始的事件
    def mouseMoveEvent(self, e):
        # print(e.buttons())
        # 只劫持按钮的右键事件，左键的操作还是默认行为。
        if e.buttons() != Qt.LeftButton:
            return

        mimeData = QMimeData()
        # 创建一个QDrag对象，用来传输MIME - based数据。
        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(e.pos()-self.rect().topLeft())
        # 拖放事件开始时，用到的处理函数式start().
        dropAction = drag.exec_(Qt.MoveAction)

    def mousePressEvent(self, e):
        # 不写这个看不到按钮按下的效果
        super().mousePressEvent(e)
        # 左键点击按钮，控制台就会输出pres
        if e.button() == Qt.LeftButton:
            print('Press')

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setAcceptDrops(True)

        self.button = Button("Button",self)
        self.button.move(190,65)

        self.setWindowTitle(" 拖放按钮组件")
        self.setGeometry(300,300,280,150)

    def dragEnterEvent(self, e):
        e.accept()

    # 定义了按钮按下后和释放后的行为，
    # 获得鼠标移动的位置，然后把按钮放到这个地方。
    def dropEvent(self, e):
        position = e.pos()
        self.button.move(position)

        e.setDropAction(Qt.MoveAction)
        e.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()



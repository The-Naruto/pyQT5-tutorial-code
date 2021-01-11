# -*- coding: utf-8 -*-
# @Time    : 2021/1/8 9:31
# @Author  : Naruto
# @Email   : the-naruto@foxmail.com
# @Project : pyQT5-tutorial-code

# -*- coding: utf-8 -*-
# @Time    : 2021/1/8 9:05
# @Author  : Naruto
# @Email   : the-naruto@foxmail.com
# @Project : pyQT5-tutorial-code

from PyQt5.QtWidgets import QWidget,QCheckBox,QApplication, QFrame,QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
import sys
'''
切换按钮就是QPushButton的一种特殊模式。 
它只有两种状态：按下和未按下。
我们再点击的时候切换两种状态，
有很多场景会使用到这个功能。

'''
class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # 初始化一个颜色
        self.col = QColor(0,0,0)

        redb = QPushButton('Red',self)
        # 把这个按钮设定成切换按钮。
        redb.setCheckable(True)
        redb.move(10,10)
        # 把点击信号和我们定义好的函数关联起来，这里是把点击事件转换成布尔值。
        redb.clicked[bool].connect(self.setColor)

        grenb = QPushButton('Green',self)
        grenb.setCheckable(True)
        grenb.move(10,60)
        grenb.clicked[bool].connect(self.setColor)

        blueb = QPushButton('Blue',self)
        blueb.setCheckable(True)
        blueb.move(10,110)
        blueb.clicked[bool].connect(self.setColor)

        self.square = QFrame(self)
        self.square.setGeometry(150,20,100,100)
        self.square.setStyleSheet("QWidget { background-color: %s }"%self.col.name())



        self.setGeometry(300,300,250,150)
        self.setWindowTitle('QCheckBox')
        self.show()

    def setColor(self, pressed):
        # 可以获取被点击的按钮
        source = self.sender()

        if pressed:
            val = 255
        else: val = 0

        if source.text() == "Red":
            self.col.setRed(val)
        elif source.text() == "Green":
            self.col.setGreen(val)
        else:
            self.col.setBlue(val)
        # 可以根据设定,为目标制定颜色
        self.square.setStyleSheet("QFrame {background-color: %s }"%self.col.name())


if __name__ =='__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


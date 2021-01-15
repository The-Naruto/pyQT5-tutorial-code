# -*- coding: utf-8 -*-
# @Time    : 2021/1/8 16:21
# @Author  : Naruto
# @Email   : the-naruto@foxmail.com
# @Project : pyQT5-tutorial-code


from PyQt5.QtWidgets import QWidget,QSlider,QApplication, QFrame,\
    QVBoxLayout,QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
import sys
'''
QSlider是个有一个小滑块的组件，这个小滑块能拖着前后滑动，
这个经常用于修改一些具有范围的数值，
动态控制颜色变化
'''
class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # 初始化一个颜色
        self.col = QColor(0,0,0)
        self.vbox = QVBoxLayout()

        # 创建一个水平的QSlider。
        sldb = QSlider(Qt.Horizontal,self)
        sldb.setFocusPolicy(Qt.NoFocus)
        sldb.valueChanged[int].connect(self.changeValueb)
        self.vbox.addWidget(sldb)

        sldg = QSlider(Qt.Horizontal,self)
        sldg.setFocusPolicy(Qt.NoFocus)
        sldg.valueChanged[int].connect(self.changeValueg)
        self.vbox.addWidget(sldg)

        sldr = QSlider(Qt.Horizontal,self)
        sldr.setFocusPolicy(Qt.NoFocus)
        sldr.valueChanged[int].connect(self.changeValuer)
        self.vbox.addWidget(sldr)


        self.setLayout(self.vbox)

        self.square = QFrame(self)
        self.square.setGeometry(150,20,100,100)
        self.square.setStyleSheet("QWidget { background-color: %s }"%self.col.name())


        self.setGeometry(300,300,250,150)
        self.setWindowTitle('滑块测试')
        self.show()

    def changeValueb(self, value):
        self.col.setBlue(value)
        self.square.setStyleSheet("QFrame {background-color: %s }"%self.col.name())
    def changeValueg(self, value):
        self.col.setGreen(value)
        self.square.setStyleSheet("QFrame {background-color: %s }"%self.col.name())
    def changeValuer(self, value):
        self.col.setRed(value)
        self.square.setStyleSheet("QFrame {background-color: %s }"%self.col.name())


if __name__ =='__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())






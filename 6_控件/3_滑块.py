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

'''
class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # 初始化一个颜色
        self.col = QColor(0,0,0)
        self.vbox = QVBoxLayout()

        sldb = QSlider(Qt.Horizontal,self)
        sldb.setFocusPolicy(Qt.NoFocus)
        sldb.valueChanged[int].connect(self.changeValue)
        self.vbox.addWidget(sldb)

        sldg = QSlider(Qt.Horizontal,self)
        sldg.setFocusPolicy(Qt.NoFocus)
        sldg.valueChanged[int].connect(self.changeValue)
        self.vbox.addWidget(sldg)

        sldr = QSlider(Qt.Horizontal,self)
        sldr.setFocusPolicy(Qt.NoFocus)
        sldr.valueChanged[int].connect(self.changeValue)
        self.vbox.addWidget(sldr)

        self.le = QLineEdit(self)
        self.le.move(130, 22)

        self.setLayout(self.vbox)

        self.square = QFrame(self)
        self.square.setGeometry(150,20,100,100)
        self.square.setStyleSheet("QWidget { background-color: %s }"%self.col.name())


        self.setGeometry(300,300,250,150)
        self.setWindowTitle('滑块测试')
        self.show()

    def changeValue(self, value):
        # 可以获取被点击的按钮
        source = self.sender()



        # if pressed:
        #     val = 255
        # else: val = 0
        #
        # if source.text() == "Red":
        #     self.col.setRed(val)
        # elif source.text() == "Green":
        #     self.col.setGreen(val)
        # else:
        #     self.col.setBlue(val)
        # 可以根据设定,为目标制定颜色
        self.square.setStyleSheet("QFrame {background-color: %s }"%self.col.name())


if __name__ =='__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())






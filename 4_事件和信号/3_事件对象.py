# -*- coding: utf-8 -*-
# @Time    : 2021/1/6 15:35
# @Author  : Naruto
# @Email   : the-naruto@foxmail.com
# @Project : pyQT5-tutorial-code


import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget,QLabel,QGridLayout,QApplication
'''
这个示例中，我们在一个组件里显示鼠标的X和Y坐标

'''
class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        grid = QGridLayout()
        grid.setSpacing(10)

        x , y = 0,0
        # X Y坐标显示在QLabel组件里
        self.text = "x: {0}, y: {1}".format(x,y)
        self.label = QLabel(self.text,self)
        grid.addWidget(self.label,0,0,Qt.AlignTop)
        # 事件追踪默认没有开启，当开启后才会追踪鼠标的点击事件
        self.setMouseTracking(True)
        self.setLayout(grid)


        self.setGeometry(300,300,200,150)
        self.setWindowTitle('Signal and slot')
        self.show()

    def mouseMoveEvent(self, e):
        x = e.x()
        y = e.y()

        text = "x: {0}, y:{1}".format(x,y)
        self.label.setText(text)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

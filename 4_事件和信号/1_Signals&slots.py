# -*- coding: utf-8 -*-
# @Time    : 2021/1/6 14:47
# @Author  : Naruto
# @Email   : the-naruto@foxmail.com
# @Project : pyQT5-tutorial-code
'''
PyQt5处理事件方面有个signal and slot机制。Signals and slots用于对象间的通讯。事件触发的时候，发生一个signal，
slot是用来被Python调用的（相当于一个句柄？这个词也好恶心，就是相当于事件的绑定函数）slot只有在事件触发的时候才能调用。

案例:
拖动滑块让数字跟着发生改变。

sender是信号的发送者，receiver是信号的接收者，slot是对这个信号应该做出的反应。
'''
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget,QLCDNumber,QSlider,QVBoxLayout,QApplication

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal,self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)
        self.setLayout(vbox)
        # 这里是把滑块的变化和数字的变化绑定在一起。
        sld.valueChanged.connect(lcd.display)

        self.setGeometry(300,300,200,150)
        self.setWindowTitle('Signal and slot')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())






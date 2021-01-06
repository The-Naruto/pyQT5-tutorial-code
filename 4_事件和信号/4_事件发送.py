# -*- coding: utf-8 -*-
# @Time    : 2021/1/6 15:57
# @Author  : Naruto
# @Email   : the-naruto@foxmail.com
# @Project : pyQT5-tutorial-code


import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow,QPushButton,QGridLayout,QApplication
'''
有时候我们会想知道是哪个组件发出了一个信号，
PyQt5里的sender()方法能搞定这件事。

'''
class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        btn1 = QPushButton('按钮1',self)
        btn1.move(30,50)

        btn2 = QPushButton("按钮2",self)
        btn2.move(150,50)

        # 两个按钮都和同一个slot绑定。
        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        self.statusBar()


        self.setGeometry(300,300,200,150)
        self.setWindowTitle('Signal and slot')
        self.show()

    # 我们用调用sender()
    # 方法的方式决定了事件源。状态栏显示了被点击的按钮。
    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text()+' 被按下去了!')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-
# @Time    : 2021/1/6 13:49
# @Author  : Naruto
# @Email   : the-naruto@foxmail.com
# @Project : pyQT5-tutorial-code

import sys
from PyQt5.QtWidgets import QWidget,QLabel,QApplication,QPushButton,QHBoxLayout,QVBoxLayout

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # 创建按钮
        okButton = QPushButton('OK')
        cancelButton = QPushButton('Cancel')
        # 创建水平布局
        hbox = QHBoxLayout()
        # 在按钮前增加弹性空间
        hbox.addStretch(1)
        # 在布局里增加按钮
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        # 创建一个垂直布局
        vbox = QVBoxLayout()
        # 在布局里增加弹性空间
        vbox.addStretch(1)
        # 把水平布局放到这个垂直布局里
        vbox.addLayout(hbox)
        # 把垂直布局设定给当前界面
        self.setLayout(vbox)

        self.setGeometry(300,300,250,150)
        self.setWindowTitle('盒布局')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())







# -*- coding: utf-8 -*-
# @Time    : 2021/1/7 10:13
# @Author  : Naruto
# @Email   : the-naruto@foxmail.com
# @Project : pyQT5-tutorial-code


import sys
from PyQt5.QtWidgets import QWidget,QPushButton,QFrame,QColorDialog,QApplication
from PyQt5.QtGui import QColor

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.btn = QPushButton('对话框',self)
        self.btn.move(20,20)
        self.btn.clicked.connect(self.showDialog)

        # 初始化一个颜色
        col = QColor(100,0,0)
        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget {background-color: %s }"%col.name())
        self.frm.setGeometry(130,22,100,100)

        self.setGeometry(300,300,290,150)
        self.setWindowTitle('对话框测试')
        self.show()

    def showDialog(self):
        # 弹出一个QColorDialog对话框。
        col = QColorDialog.getColor()
        # 可以预览颜色，如果点击取消按钮，
        # 没有颜色值返回，如果颜色是我们想要的，就从取色框里选择这个颜色。
        if col.isValid():
            self.frm.setStyleSheet("QWidget {background-color: %s }"%col.name())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())




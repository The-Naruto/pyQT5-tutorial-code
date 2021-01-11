# -*- coding: utf-8 -*-
# @Time    : 2021/1/7 9:22
# @Author  : Naruto
# @Email   : the-naruto@foxmail.com
# @Project : pyQT5-tutorial-code

import sys
from PyQt5.QtWidgets import QWidget,QPushButton,QLineEdit,QInputDialog,QApplication

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.btn = QPushButton('输入对话框',self)
        self.btn.move(20,20)
        self.btn.clicked.connect(self.showInputDialog)

        self.le = QLineEdit(self)
        self.le.move(130,22)

        self.setGeometry(300,300,290,150)
        self.setWindowTitle('对话框测试')
        self.show()

    def showInputDialog(self):
        # 第一个参数是输入框的标题，
        # 第二个参数是输入框的占位符。
        # 对话框返回输入内容和一个布尔值，如果点击的是OK按钮，布尔值就返回True
        text,ok = QInputDialog.getText(self,'输入对话框','输入你的名字:')
        if ok:
            self.le.setText(str(text))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


















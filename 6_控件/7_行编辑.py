# -*- coding: utf-8 -*-
# @Time    : 2021/1/12 11:08
# @Author  : Naruto
# @Email   : the-naruto@foxmail.com
# @Project : pyQT5-tutorial-code

'''
QLineEdit组件提供了编辑文本的功能，
自带了撤销、重做、剪切、粘贴、拖拽等功能。

'''

import sys
from PyQt5.QtWidgets import (QWidget, QLabel,
                             QLineEdit, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.lbl = QLabel(self)
        # 创建一个QLineEdit对象。
        qle = QLineEdit(self)

        qle.move(60,100)
        self.lbl.move(60,40)

        # 如果输入框的值有变化，就调用onChanged()方法。
        qle.textChanged[str].connect(self.onChanged)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QLineEdit')
        self.show()

    def onChanged(self, text):
        self.lbl.setText(text)
        # 然后调用adjustSize()方法让标签自适应文本内容。
        self.lbl.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
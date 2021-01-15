# -*- coding: utf-8 -*-
# @Time    : 2021/1/12 14:24
# @Author  : Naruto
# @Email   : the-naruto@foxmail.com
# @Project : pyQT5-tutorial-code


import sys
from PyQt5.QtWidgets import (QWidget,QLabel,QComboBox,QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.lbl = QLabel("Ubantu",self)

        # 创建一个QComboBox组件和五个选项。
        combo = QComboBox(self)
        combo.addItem("Ubuntu")
        combo.addItem("Mandriva")
        combo.addItem("Fedora")
        combo.addItem("Arch")
        combo.addItem("Gentoo")
        combo.move(50,50)
        self.lbl.move(50,150)

        combo.activated[str].connect(self.onAvtivated)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QLineEdit')
        self.show()

    def onAvtivated(self,text):
        # 设置标签内容为选定的字符串，然后设置自适应文本大小。
        self.lbl.setText(text)
        self.lbl.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())







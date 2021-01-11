# -*- coding: utf-8 -*-
# @Time    : 2021/1/7 10:56
# @Author  : Naruto
# @Email   : the-naruto@foxmail.com
# @Project : pyQT5-tutorial-code


import sys
from PyQt5.QtWidgets import QWidget,QPushButton,QVBoxLayout,QApplication,\
    QSizePolicy,QLabel,QFontDialog


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        vbox = QVBoxLayout()

        btn = QPushButton('对话框',self)
        btn.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        btn.move(20,20)
        btn.clicked.connect(self.showDialog)

        vbox.addWidget(btn)

        self.lbl = QLabel('Knowledge only matters',self)
        self.lbl.move(130,20)

        vbox.addWidget(self.lbl)
        self.setLayout(vbox)

        self.setGeometry(300,300,290,150)
        self.setWindowTitle('对话框测试')
        self.show()

    def showDialog(self):
        # 弹出一个字体选择对话框。
        # getFont()方法返回一个字体名称和状态信息。状态信息有OK和其他两种。
        font, ok = QFontDialog.getFont()
        if ok:
            self.lbl.setFont(font)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

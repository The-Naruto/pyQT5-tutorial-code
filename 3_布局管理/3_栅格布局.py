# -*- coding: utf-8 -*-
# @Time    : 2021/1/6 13:49
# @Author  : Naruto
# @Email   : the-naruto@foxmail.com
# @Project : pyQT5-tutorial-code

import sys
from PyQt5.QtWidgets import QWidget,QLabel,QApplication,QPushButton,QGridLayout
'''
制作一个计算器的虚拟键盘
'''
class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 创建一个QGridLayout实例，并把它放到程序窗口里。
        grid = QGridLayout()
        self.setLayout(grid)

        # 按钮名称
        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                '4', '5', '6', '*',
                 '1', '2', '3', '-',
                '0', '.', '=', '+']
        # 创建按钮位置列表。
        positions = [(i,j) for i in range(5) for j in range(4)]

        # 创建按钮，并使用addWidget()方法把按钮放到布局里面。
        for position,name in zip(positions,names):
            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button,*position)



        self.setGeometry(300,300,250,150)
        self.setWindowTitle('网格布局')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())







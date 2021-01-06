# -*- coding: utf-8 -*-
# @Time    : 2021/1/6 13:49
# @Author  : Naruto
# @Email   : the-naruto@foxmail.com
# @Project : pyQT5-tutorial-code

import sys
from PyQt5.QtWidgets import QWidget,QLabel,\
    QApplication,QPushButton,QGridLayout,QLineEdit,QTextEdit

'''
组件能跨列和跨行展示

'''
class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QLineEdit()


        grid = QGridLayout()
        # 创建标签之间的空间。
        grid.setSpacing(10)

        grid.addWidget(title,1,0)
        grid.addWidget(titleEdit,1,1)

        grid.addWidget(author,2,0)
        grid.addWidget(authorEdit,2,1)

        grid.addWidget(review,3,0)
        # 我们可以指定组件的跨行和跨列的大小。这里我们指定这个元素跨5行跨1列显示。
        grid.addWidget(reviewEdit,3,1,5,1)

        self.setLayout(grid)

        self.setGeometry(300,300,250,150)
        self.setWindowTitle('网格布局')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())







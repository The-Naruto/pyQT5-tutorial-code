# -*- coding: utf-8 -*-
# @Time    : 2020/12/29 9:28
# @Author  : Naruto
# @Email   : the-naruto@foxmail.com
# @Project : pyQT5-Study


import sys
from PyQt5.QtWidgets import  QApplication,QWidget


if __name__ == '__main__':
    # 创建应用对象
    app = QApplication(sys.argv)
    # 创建一个基本用户界面
    w = QWidget()
    w.resize(250,150)
    w.move(300,300)
    w.setWindowTitle('HelloWorld')
    # 显示控件
    w.show()
    # 设置主循环,也就是事件处理器
    sys.exit(app.exec_())



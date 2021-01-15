# -*- coding: utf-8 -*-
# @Time    : 2021/1/12 10:11
# @Author  : Naruto
# @Email   : the-naruto@foxmail.com
# @Project : pyQT5-tutorial-code



from PyQt5.QtWidgets import (QWidget, QCalendarWidget,
    QLabel, QApplication, QVBoxLayout)
from PyQt5.QtCore import QDate
import sys
'''
QCalendarWidget提供了基于月份的日历插件，十分简易而且直观。

'''
class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        vbox = QVBoxLayout(self)

        # 初始化一个日期控件
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        # 将选择日期和显示日期绑定
        cal.clicked[QDate].connect(self.showDate)

        vbox.addWidget(cal)

        self.lbl = QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())

        vbox.addWidget(self.lbl)

        self.setLayout(vbox)

        self.setGeometry(300,300,280,170)
        self.setWindowTitle('进度条')
        self.show()

    # 使用selectedDate()
    # 方法获取选中的日期，然后把日期对象转成字符串，在标签里面显示出来。
    def showDate(self,date):
        self.lbl.setText(date.toString())



if __name__ =='__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())




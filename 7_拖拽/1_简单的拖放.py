# -*- coding: utf-8 -*-
# @Time    : 2021/1/13 9:32
# @Author  : Naruto
# @Email   : the-naruto@foxmail.com
# @Project : pyQT5-tutorial-code

'''
本例使用了QLineEdit和QPushButton。
把一个文本从编辑框里拖到按钮上，更新按钮上的标签（文字）。
只能拖动文本,可以从窗口外部拖动
'''
from PyQt5.QtWidgets import QPushButton,QWidget,QLineEdit,QApplication
import sys

# 首先用QPushButton上构造一个按钮实例。
class Button(QPushButton):
    def __init__(self,title,parent):
        super().__init__(title,parent)
        # 激活组件的拖拽事件。
        self.setAcceptDrops(True)

    # 我们重构了dragEnterEvent()
    # 方法。设定好接受拖拽的数据类型（plain text）。
    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()

    # 然后重构dropEvent()
    # 方法，更改按钮接受鼠标的释放事件的默认行为。
    def dropEvent(self, e):
        self.setText(e.mimeData().text())

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        edit = QLineEdit("",self)
        # QLineEdit默认支持拖拽操作，所以我们只要调用setDragEnabled()
        # 方法使用就行了。
        edit.setDragEnabled(True)
        edit.move(30,65)

        button = Button("Button",self)
        button.move(190,65)

        self.setWindowTitle(" 简单的拖放")
        self.setGeometry(300,300,300,150)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()












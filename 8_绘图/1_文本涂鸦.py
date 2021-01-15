# -*- coding: utf-8 -*-
# @Time    : 2021/1/13 10:35
# @Author  : Naruto
# @Email   : the-naruto@foxmail.com
# @Project : pyQT5-tutorial-code

'''
画一些Unicode文本

绘图由paintEvent()方法完成，
绘图的代码要放在QPainter对象的begin()和end()方法之间。是低级接口。
'''

from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter,QColor,QFont
import sys



class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.text = "Лев Николаевич Толстой\nАнна Каренина"

        self.setWindowTitle("绘制文本")
        self.setGeometry(300,300,280,150)

    # 在绘画事件内完成绘画动作。
    def paintEvent(self, e):
        qp = QPainter()
        # QPainter是低级的绘画类。所有的绘画动作都在这个类的begin()和end()
        # 方法之间完成，绘画动作都封装在drawText()内部了。
        qp.begin(self)
        self.drawText(e,qp)
        qp.end()

    def drawText(self,event,qp):
        # 文字绘画定义了笔和字体
        qp.setPen(QColor(168,34,3))
        qp.setFont(QFont('Decorative',20))

        # drawText()方法在窗口里绘制文本，
        # rect()方法返回要更新的矩形区域。
        qp.drawText(event.rect(),Qt.AlignCenter,self.text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()



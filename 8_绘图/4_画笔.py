# -*- coding: utf-8 -*-
# @Time    : 2021/1/13 11:19
# @Author  : Naruto
# @Email   : the-naruto@foxmail.com
# @Project : pyQT5-tutorial-code
'''
QPen是基本的绘画对象，能用来画直线、曲线、矩形框、椭圆、多边形和其他形状。
'''



from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtGui import QPainter,QPen
import sys
from PyQt5.QtCore import Qt



class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setWindowTitle("画笔练习")
        self.setGeometry(300,300,280,270)

    # 在绘画事件内完成绘画动作。
    def paintEvent(self, e):
        qp = QPainter()
        # QPainter是低级的绘画类。所有的绘画动作都在这个类的begin()和end()
        # 方法之间完成，绘画动作都封装在drawText()内部了。
        qp.begin(self)
        self.drawLines(qp)
        qp.end()

    def drawLines(self,qp):
        # 新建一个QPen对象，设置颜色黑色，宽2像素，这样就能看出来各个笔样式的区别。
        pen = QPen(Qt.black,2,Qt.SolidLine)

        qp.setPen(pen)
        qp.drawLine(20,40,250,40)
        # 使用预设的画笔样式
        pen.setStyle(Qt.DashLine)
        qp.setPen(pen)
        qp.drawLine(20,80,250,80)

        pen.setStyle(Qt.DashDotLine)
        qp.setPen(pen)
        qp.drawLine(20, 120, 250, 80)

        pen.setStyle(Qt.DotLine)
        qp.setPen(pen)
        qp.drawLine(20, 160, 250, 80)

        pen.setStyle(Qt.DashDotDotLine)
        qp.setPen(pen)
        qp.drawLine(20, 200, 250, 80)
        # 自定义了一个笔的样式
        # 数字列表是线的样式，要求必须是个数为奇数，奇数位定义的是空格，偶数位为线长，数字越大，空格或线长越大，比如本例的就是1像素线，4像素空格，5像素线，4像素空格
        pen.setStyle(Qt.CustomDashLine)
        pen.setDashPattern([1,4,5,4])
        qp.setPen(pen)
        qp.drawLine(20, 240, 250, 80)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()




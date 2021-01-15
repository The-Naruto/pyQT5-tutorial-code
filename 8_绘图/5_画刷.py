# -*- coding: utf-8 -*-
# @Time    : 2021/1/13 13:27
# @Author  : Naruto
# @Email   : the-naruto@foxmail.com
# @Project : pyQT5-tutorial-code
'''
QBrush也是图像的一个基本元素。
是用来填充一些物体的背景图用的，比如矩形，椭圆，多边形等。
有三种类型：预定义、渐变和纹理。
'''

from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtGui import QPainter,QBrush
import sys
from PyQt5.QtCore import Qt



class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setWindowTitle("画刷练习")
        self.setGeometry(300,300,355,270)

    # 在绘画事件内完成绘画动作。
    def paintEvent(self, e):
        qp = QPainter()
        # QPainter是低级的绘画类。所有的绘画动作都在这个类的begin()和end()
        # 方法之间完成，绘画动作都封装在drawText()内部了。
        qp.begin(self)
        self.drawBrushes(qp)
        qp.end()

    def drawBrushes(self,qp):
        # 创建了一个笔刷对象
        brush = QBrush(Qt.SolidPattern)
        # 添加笔刷样式
        qp.setBrush(brush)

        # 调用drawRect()方法画图
        qp.drawRect(10,15,90,60)

        brush.setStyle(Qt.Dense1Pattern)
        qp.setBrush(brush)
        qp.drawRect(130,15,90,60)

        brush.setStyle(Qt.Dense2Pattern)
        qp.setBrush(brush)
        qp.drawRect(250,15,90,60)

        brush.setStyle(Qt.DiagCrossPattern)
        qp.setBrush(brush)
        qp.drawRect(10,105,90,60)

        brush.setStyle(Qt.Dense5Pattern)
        qp.setBrush(brush)
        qp.drawRect(130, 105, 90, 60)

        brush.setStyle(Qt.Dense6Pattern)
        qp.setBrush(brush)
        qp.drawRect(250, 105, 90, 60)

        brush.setStyle(Qt.HorPattern)
        qp.setBrush(brush)
        qp.drawRect(10, 195, 90, 60)

        brush.setStyle(Qt.VerPattern)
        qp.setBrush(brush)
        qp.drawRect(130, 195, 90, 60)

        brush.setStyle(Qt.BDiagPattern)
        qp.setBrush(brush)
        qp.drawRect(250, 195, 90, 60)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()



# -*- coding: utf-8 -*-
# @Time    : 2021/1/13 13:36
# @Author  : Naruto
# @Email   : the-naruto@foxmail.com
# @Project : pyQT5-tutorial-code
'''
QPainterPath创建贝塞尔曲线。
绘画路径是由许多构建图形的对象，
具体表现就是一些线的形状，比如矩形，椭圆，线和曲线。
'''

from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtGui import QPainter,QPainterPath
import sys
from PyQt5.QtCore import Qt



class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setWindowTitle("贝塞尔曲线")
        self.setGeometry(300,300,355,270)

    # 在绘画事件内完成绘画动作。
    def paintEvent(self, e):
        qp = QPainter()
        # QPainter是低级的绘画类。所有的绘画动作都在这个类的begin()和end()
        # 方法之间完成，绘画动作都封装在drawText()内部了。
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        self.drawBezierCurve(qp)
        qp.end()

    def drawBezierCurve(self,qp):
        path = QPainterPath()
        path.moveTo(30,30)
        # 使用cubicTo()方法生成，分别需要三个点：起始点，控制点和终止点。
        path.cubicTo(30,30,200,350,350,30)
        # 绘制最后的图像。
        qp.drawPath(path)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()


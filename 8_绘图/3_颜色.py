# -*- coding: utf-8 -*-
# @Time    : 2021/1/13 10:54
# @Author  : Naruto
# @Email   : the-naruto@foxmail.com
# @Project : pyQT5-tutorial-code

'''
颜色是一个物体显示的RGB的混合色。
RBG值的范围是0255。
我们有很多方式去定义一个颜色，
最常见的方式就是RGB和16进制表示法，
也可以使用RGBA，增加了一个透明度的选项，
透明度值的范围是01，0代表完全透明。

我们画出了三个颜色的矩形
'''



from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtGui import QPainter,QColor,QBrush
import sys,random



class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setWindowTitle("绘制文本")
        self.setGeometry(300,300,280,150)

    # 在绘画事件内完成绘画动作。
    def paintEvent(self, e):
        qp = QPainter()
        # QPainter是低级的绘画类。所有的绘画动作都在这个类的begin()和end()
        # 方法之间完成，绘画动作都封装在drawText()内部了。
        qp.begin(self)
        self.drawRectangles(qp)
        qp.end()

    # 每次更改窗口大小，都会产生绘画事件，
    # 从size()方法里获得当前窗口的大小，然后把产生的点随机的分配到窗口的所有位置上。
    def drawRectangles(self,qp):
        col = QColor(0,0,0)
        # 使用16进制的方式定义一个颜色。
        col.setNamedColor('#d4d4d4')
        qp.setPen(col)
        # 定义了一个笔刷，并画出了一个矩形。笔刷是用来画一个物体的背景。
        qp.setBrush(QColor(200,0,0))
        # drawRect()有四个参数，分别是矩形的x、y、w、h。 然后用笔刷和矩形进行绘画。
        qp.drawRect(10,15,90,60)

        qp.setBrush(QColor(255,80,0,160))
        qp.drawRect(130,15,90,60)

        qp.setBrush(QColor(25,0,90,200))
        qp.drawRect(250,15,90,60)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()







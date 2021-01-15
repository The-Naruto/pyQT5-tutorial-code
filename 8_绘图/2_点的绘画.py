# -*- coding: utf-8 -*-
# @Time    : 2021/1/13 10:47
# @Author  : Naruto
# @Email   : the-naruto@foxmail.com
# @Project : pyQT5-tutorial-code


from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter,QColor,QFont
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
        self.drawPoints(qp)
        qp.end()

    # 每次更改窗口大小，都会产生绘画事件，
    # 从size()方法里获得当前窗口的大小，然后把产生的点随机的分配到窗口的所有位置上。
    def drawPoints(self,qp):
        # 文字绘画定义了笔和字体
        qp.setPen(QColor(168,34,3))
        # qp.setFont(QFont('Decorative', 20))
        size = self.size()
        for i  in range(1000):
            x = random.randint(1,size.width()-1)
            y = random.randint(1,size.height()-1)
            qp.drawPoint(x,y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()



# -*- coding: utf-8 -*-
# @Time    : 2021/1/12 9:58
# @Author  : Naruto
# @Email   : the-naruto@foxmail.com
# @Project : pyQT5-tutorial-code


from PyQt5.QtWidgets import QWidget,QSlider,QApplication, QProgressBar,\
    QPushButton
from PyQt5.QtCore import QBasicTimer
import sys
'''
进度条是用来展示任务进度
QProgressBar组件提供了水平和垂直两种进度条，
进度条可以设置最大值和最小值，默认情况是0~99。

'''
class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 新建一个QProgressBar构造器。
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30,40,200,25)

        self.btn = QPushButton('Start',self)
        self.btn.move(40,80)
        self.btn.clicked.connect(self.doAction)
        # 创建一个定时器
        self.timer = QBasicTimer()
        self.step = 0

        self.setGeometry(300,300,280,170)
        self.setWindowTitle('进度条')
        self.show()

    # 每个QObject和又它继承而来的对象都有一个timerEvent()
    # 事件处理函数
    def timerEvent(self,e):
        if self.step>=100:
            self.timer.stop()
            self.btn.setText('Finished')
            return
        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            # 调用start()方法加载一个时间事件。这个方法有两个参数
            # ：过期时间和事件接收者。
            self.timer.start(100,self)
            self.btn.setText('Stop')



if __name__ =='__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())




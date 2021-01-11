# -*- coding: utf-8 -*-
# @Time    : 2021/1/7 16:08
# @Author  : Naruto
# @Email   : the-naruto@foxmail.com
# @Project : pyQT5-tutorial-code


import sys
from PyQt5.QtWidgets import QMainWindow,QTextEdit,QApplication,\
    QAction,QFileDialog
from PyQt5.QtGui import QIcon

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon('web.jpg'),'Open',self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('打开新文件')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        self.setGeometry(300,300,290,150)
        self.setWindowTitle('对话框测试')
        self.show()

    def showDialog(self):
        #弹出QFileDialog窗口。
        # getOpenFileName()方法的第一个参数是说明文字，
        # 第二个参数是默认打开的文件夹路径。默认情况下显示所有类型的文件。
        fname = QFileDialog.getOpenFileName(self,'Open file','/')

        if fname[0]:
            f = open(fname[0],'r')

            with f:
                data = f.read()
                self.textEdit.setText(data)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())







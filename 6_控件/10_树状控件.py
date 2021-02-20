# -*- coding: utf-8 -*-
# @Time    : 2021/1/25 10:48
# @Author  : Naruto
# @Email   : the-naruto@foxmail.com
# @Project : pyQT5-tutorial-code
'''
QTreeWidget的使用方法

'''
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QTreeWidget,QMainWindow,QTreeWidgetItem
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.tree = QTreeWidget(self)
        self.tree.setColumnCount(2)
        self.tree.setHeaderLabels(["key","values"])

        root = QTreeWidgetItem()
        root.setText(0,"root")
        root.setCheckState(0, Qt.Checked)
        child1 = QTreeWidgetItem(root)
        child1.setText(0, 'child1')
        child1.setText(1, 'ios')
        child1.setCheckState(0, Qt.Checked)
        # root.addChild(child1)

        child2 = QTreeWidgetItem(root)
        child2.setText(0, 'child2')
        child2.setText(1, '')
        child2.setCheckState(0, Qt.Checked)


        child3 = QTreeWidgetItem(child2)
        child3.setText(0, 'child3')
        child3.setText(1, 'android')


        self.tree.addTopLevelItem(root)
        self.tree.expandAll()
        # self.setCentralWidget(self.tree)

        self.tree.clicked.connect(self.onClicked)


        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QTreeWidget')
        self.show()



    def onClicked(self, qmodeLindex):
        item = self.tree.currentItem()
        print('Key=%s,value=%s,parent=%s,index=%s' % (item.text(0), item.text(1),item.parent().text(0),item.parent().indexOfChild(item)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import sys
import os


class BLANK_Demand(QWidget):

    def __init__(self, Panel_ID, nodename, Destination):
        super(BLANK_Demand, self).__init__()

        self.resize(164, 577)
        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QLabel(self)
        self.horizontalLayout.setMargin(0)
        self.label.setStyleSheet("border-image: url(:/BLANK.png);" )
        self.setStyleSheet("border: 10px solid black;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        

        self.setAcceptDrops(True)


if __name__ == "__main__":

    app = QApplication([])
    window = BLANK_Demand(1,2,3)
    window.show()
    sys.exit(app.exec_())

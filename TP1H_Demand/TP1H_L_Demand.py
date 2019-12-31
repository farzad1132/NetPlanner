from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import sys
import os
from data import *


class TP1H_L_Demand(QWidget):
    def __init__(self, Panel_ID, nodename , Destination):
        super(TP1H_L_Demand, self).__init__()

        self.id = Panel_ID
        self.nodename = nodename
        self.Destination = Destination

        self.setFixedSize(112, 521)
        self.label_19 = QLabel(self)
        self.label_19.setGeometry(QRect(20, -20, 41, 81))
        self.label_19.setText("")
        self.label_19.setPixmap(QPixmap(os.path.join("TP1H_Demand","socket1.png")))
        self.label_19.setObjectName("label_19")
        self.label_22 = QLabel(self)
        self.label_22.setGeometry(QRect(20, 470, 55, 61))
        self.label_22.setText("")
        self.label_22.setPixmap(QPixmap(os.path.join("TP1H_Demand","socket2.png")))
        self.label_22.setObjectName("label_22")
        self.label = QLabel(self)
        self.label.setGeometry(QRect(80, 10, 51, 121))
        self.label.setObjectName("label")
        self.line = QLabel(self)
        self.line.setGeometry(QRect(30, 140, 55, 191))
        self.line.setText("")
        self.line.setPixmap(QPixmap("tp1h_line.png"))
        self.line.setObjectName("line")
        self.client = QLabel(self)
        self.client.setGeometry(QRect(30, 320, 55, 141))
        self.client.setText("")
        self.client.setPixmap(QPixmap("TP1H_CLIENT.png"))
        self.client.setObjectName("client")
        self.title = QLabel(self)
        self.title.setGeometry(QRect(60, 30, 55, 111))
        self.title.setText("")
        self.title.setPixmap(QPixmap("title.png"))
        self.title.setObjectName("title")

        self.retranslateUi()
        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))

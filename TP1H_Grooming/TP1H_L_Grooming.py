from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import sys
import os
from data import *


class TP1H_L_Grooming(QWidget):

    def __init__(self,Panel_ID,nodename):

        self.id = Panel_ID
        self.nodename = nodename

        super(TP1H_L_Grooming, self).__init__()
        self.setFixedSize(109, 810)

        self.title = QLabel(self)
        self.title.setGeometry(QRect(60, 60, 55, 131))
        self.title.setText("")
        self.title.setPixmap(QPixmap(os.path.join("TP1H_Grooming", "title.png")))
        self.title.setObjectName("title") 

        self.client = QLabel(self)
        self.client.setGeometry(QRect(30, 450, 55, 241))
        self.client.setText("")
        self.client.setPixmap(QPixmap(os.path.join("TP1H_Grooming", "TP1H_CLIENT.png")))
        self.client.setObjectName("client") 

        self.upper_socket = QLabel(self)
        self.upper_socket.setGeometry(QRect(10, -10, 55, 61))
        self.upper_socket.setText("")
        self.upper_socket.setPixmap(QPixmap(os.path.join("TP1H_Grooming", "socket1.png")))
        self.upper_socket.setObjectName("upper_socket") 

        self.line = QLabel(self)
        self.line.setGeometry(QRect(30, 220, 55, 231))
        self.line.setText("")
        self.line.setPixmap(QPixmap(os.path.join("TP1H_Grooming", "tp1h_line.png")))
        self.line.setObjectName("line") 

        self.socket = QLabel(self)
        self.socket.setGeometry(QRect(10, 760, 55, 61))
        self.socket.setText("")
        self.socket.setPixmap(QPixmap(os.path.join("TP1H_Grooming", "socket2.png")))
        self.socket.setObjectName("socket")

        self.retranslateUi()
        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
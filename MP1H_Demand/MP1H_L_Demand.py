from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import sys
import os

from data import *


class MP1H_L_Demand(QWidget):
    def __init__(self, Panel_ID, nodename):
        super(MP1H_L_Demand, self).__init__()

        self.id =Panel_ID
        self.nodename = nodename
        self.setFixedSize(112, 521) 

        
        self.client1 = QLabel(self)
        self.client1.setGeometry(QRect(40, 140, 31, 41))
        self.client1.setText("")
        self.client1.setPixmap(QPixmap(os.path.join("MP1H_Demand","client.png")))
        self.client1.setObjectName("client1") 

        self.client2 = QLabel(self)
        self.client2.setGeometry(QRect(60, 140, 31, 41))
        self.client2.setText("")
        self.client2.setPixmap(QPixmap(os.path.join("MP1H_Demand","client.png")))
        self.client2.setObjectName("client2")
        
        self.client3 = QLabel(self)
        self.client3.setGeometry(QRect(40, 180, 31, 41))
        self.client3.setText("")
        self.client3.setPixmap(QPixmap(os.path.join("MP1H_Demand","client.png")))
        self.client3.setObjectName("client3") 

        self.client4 = QLabel(self)
        self.client4.setGeometry(QRect(60, 180, 31, 41))
        self.client4.setText("")
        self.client4.setPixmap(QPixmap(os.path.join("MP1H_Demand","client.png")))
        self.client4.setObjectName("client4") 

        self.client5 = QLabel(self)
        self.client5.setGeometry(QRect(40, 220, 31, 41))
        self.client5.setText("")
        self.client5.setPixmap(QPixmap(os.path.join("MP1H_Demand","client.png")))
        self.client5.setObjectName("client5") 

        self.client6 = QLabel(self)
        self.client6.setGeometry(QRect(60, 220, 31, 41))
        self.client6.setText("")
        self.client6.setPixmap(QPixmap(os.path.join("MP1H_Demand","client.png")))
        self.client6.setObjectName("client6") 

        self.client7 = QLabel(self)
        self.client7.setGeometry(QRect(40, 260, 31, 41))
        self.client7.setText("")
        self.client7.setPixmap(QPixmap(os.path.join("MP1H_Demand","client.png")))
        self.client7.setObjectName("client7") 

        self.client8 = QLabel(self)
        self.client8.setGeometry(QRect(60, 260, 31, 41))
        self.client8.setText("")
        self.client8.setPixmap(QPixmap(os.path.join("MP1H_Demand","client.png")))
        self.client8.setObjectName("client8") 

        self.client9 = QLabel(self)
        self.client9.setGeometry(QRect(40, 300, 31, 41))
        self.client9.setText("")
        self.client9.setPixmap(QPixmap(os.path.join("MP1H_Demand","client.png")))
        self.client9.setObjectName("client9") 

        self.client10 = QLabel(self)
        self.client10.setGeometry(QRect(60, 300, 31, 41))
        self.client10.setText("")
        self.client10.setPixmap(QPixmap(os.path.join("MP1H_Demand","client.png")))
        self.client10.setObjectName("client10") 

        
        self.title = QLabel(self)
        self.title.setGeometry(QRect(70, 10, 41, 121))
        self.title.setText("")
        self.title.setPixmap(QPixmap(os.path.join("MP1H_Demand","title2.png")))
        self.title.setObjectName("title2") 

        self.clientx = QLabel(self)
        self.clientx.setGeometry(QRect(40, 350, 55, 101))
        self.clientx.setText("")
        self.clientx.setPixmap(QPixmap(os.path.join("MP1H_Demand","clientx.png")))
        self.clientx.setObjectName("clientx") 

        self.socket = QLabel(self)
        self.socket.setGeometry(QRect(20, 470, 55, 51))
        self.socket.setText("")
        self.socket.setPixmap(QPixmap(os.path.join("MP1H_Demand","socket2.png")))
        self.socket.setObjectName("socket") 

        self.upper_socket = QLabel(self)
        self.upper_socket.setGeometry(QRect(20, 0, 55, 41))
        self.upper_socket.setText("")
        self.upper_socket.setPixmap(QPixmap(os.path.join("MP1H_Demand","socket1.png")))
        self.upper_socket.setObjectName("upper_socket")

        self.retranslateUi(self)
        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))




from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import sys
import os
from data import *


class MP1H_L_Grooming(QWidget):

    def __init__(self,Panel_ID,nodename):

        self.id = Panel_ID
        self.nodename = nodename

        super(MP1H_L_Grooming, self).__init__()
        self.setFixedSize(109, 810)

        self.client1 = QLabel(self)
        self.client1.setGeometry(QRect(20, 150, 55, 71))
        self.client1.setText("")
        self.client1.setPixmap(QPixmap(os.path.join("MP1H_Grooming", "client_grooming.png")))
        self.client1.setObjectName("client1") 

        self.client2 = QLabel(self)
        self.client2.setGeometry(QRect(50, 150, 55, 71))
        self.client2.setText("")
        self.client2.setPixmap(QPixmap(os.path.join("MP1H_Grooming", "client_grooming.png")))
        self.client2.setObjectName("client2")  

        self.client3 = QLabel(self)
        self.client3.setGeometry(QRect(20, 220, 55, 71))
        self.client3.setText("")
        self.client3.setPixmap(QPixmap(os.path.join("MP1H_Grooming", "client_grooming.png")))
        self.client3.setObjectName("client3") 

        self.client4 = QLabel(self)
        self.client4.setGeometry(QRect(50, 220, 55, 71))
        self.client4.setText("")
        self.client4.setPixmap(QPixmap(os.path.join("MP1H_Grooming", "client_grooming.png")))
        self.client4.setObjectName("client4")
        
        self.client5 = QLabel(self)
        self.client5.setGeometry(QRect(20, 290, 55, 71))
        self.client5.setText("")
        self.client5.setPixmap(QPixmap(os.path.join("MP1H_Grooming", "client_grooming.png")))
        self.client5.setObjectName("client5") 

        self.client6 = QLabel(self)
        self.client6.setGeometry(QRect(50, 290, 55, 71))
        self.client6.setText("")
        self.client6.setPixmap(QPixmap(os.path.join("MP1H_Grooming", "client_grooming.png")))
        self.client6.setObjectName("client6") 

        self.client7 = QLabel(self)
        self.client7.setGeometry(QRect(20, 360, 55, 71))
        self.client7.setText("")
        self.client7.setPixmap(QPixmap(os.path.join("MP1H_Grooming", "client_grooming.png")))
        self.client7.setObjectName("client7") 

        self.client8 = QLabel(self)
        self.client8.setGeometry(QRect(50, 360, 55, 71))
        self.client8.setText("")
        self.client8.setPixmap(QPixmap(os.path.join("MP1H_Grooming", "client_grooming.png")))
        self.client8.setObjectName("client8") 

        self.client9 = QLabel(self)
        self.client9.setGeometry(QRect(20, 430, 55, 71))
        self.client9.setText("")
        self.client9.setPixmap(QPixmap(os.path.join("MP1H_Grooming", "client_grooming.png")))
        self.client9.setObjectName("client9") 

        self.client10 = QLabel(self)
        self.client10.setGeometry(QRect(50, 430, 55, 71))
        self.client10.setText("")
        self.client10.setPixmap(QPixmap(os.path.join("MP1H_Grooming", "client_grooming.png")))
        self.client10.setObjectName("client10") 

        self.line = QLabel(self)
        self.line.setGeometry(QRect(20, 500, 55, 201))
        self.line.setText("")
        self.line.setPixmap(QPixmap(os.path.join("MP1H_Grooming", "line.png")))
        self.line.setObjectName("line") 

        self.title = QLabel(self) 
        self.title.setGeometry(QRect(60, 40, 31, 121))
        self.title.setText("")
        self.title.setPixmap(QPixmap(os.path.join("MP1H_Grooming", "title.png")))
        self.title.setObjectName("title") 

        self.socket = QLabel(self)
        self.socket.setGeometry(QRect(10, 760, 55, 61))
        self.socket.setText("")
        self.socket.setPixmap(QPixmap(os.path.join("MP1H_Grooming", "socket2.png")))
        self.socket.setObjectName("socket") 

        self.upper_socket = QLabel(self)
        self.upper_socket.setGeometry(QRect(10, -10, 55, 61))
        self.upper_socket.setText("")
        self.upper_socket.setPixmap(QPixmap(os.path.join("MP1H_Grooming", "socket1.png")))
        self.upper_socket.setObjectName("upper_socket")

        self.retranslateUi()
        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))



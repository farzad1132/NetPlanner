from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import sys
import os

from data import *


class MP2X_L_Demand(QWidget):
    def __init__(self, Panel_ID, nodename):
        super(MP2X_L_Demand, self).__init__()

        self.id =Panel_ID
        self.nodename = nodename
        self.setFixedSize(112, 521)
        
        
        self.client1 = QLabel(self)
        self.client1.setGeometry(QRect(30, 120, 21, 71))
        self.client1.setText("")
        self.client1.setPixmap(QPixmap(os.path.join("MP2X_Demand","client.png")))
        self.client1.setObjectName("client1")  

        self.client2 = QLabel(self)
        self.client2.setGeometry(QRect(50, 120, 21, 71))
        self.client2.setText("")
        self.client2.setPixmap(QPixmap(os.path.join("MP2X_Demand","client.png")))
        self.client2.setObjectName("client2")  

        self.client3 = QLabel(self)
        self.client3.setGeometry(QRect(30, 160, 21, 71))
        self.client3.setText("")
        self.client3.setPixmap(QPixmap(os.path.join("MP2X_Demand","client.png")))
        self.client3.setObjectName("client3") 

        self.client4 = QLabel(self)
        self.client4.setGeometry(QRect(50, 160, 21, 71))
        self.client4.setText("")
        self.client4.setPixmap(QPixmap(os.path.join("MP2X_Demand","client.png")))
        self.client4.setObjectName("client4")
        
        
        self.client5 = QLabel(self)
        self.client5.setGeometry(QRect(30, 200, 21, 71))
        self.client5.setText("")
        self.client5.setPixmap(QPixmap(os.path.join("MP2X_Demand","client.png")))
        self.client5.setObjectName("client5") 

        self.client6 = QLabel(self)
        self.client6.setGeometry(QRect(50, 200, 21, 71))
        self.client6.setText("")
        self.client6.setPixmap(QPixmap(os.path.join("MP2X_Demand","client.png")))
        self.client6.setObjectName("client6") 

        self.client7 = QLabel(self)
        self.client7.setGeometry(QRect(30, 240, 21, 71))
        self.client7.setText("")
        self.client7.setPixmap(QPixmap(os.path.join("MP2X_Demand","client.png")))
        self.client7.setObjectName("client7") 

        self.client8 = QLabel(self)
        self.client8.setGeometry(QRect(50, 240, 21, 71))
        self.client8.setText("")
        self.client8.setPixmap(QPixmap(os.path.join("MP2X_Demand","client.png")))
        self.client8.setObjectName("client8")  

        self.client9 = QLabel(self)
        self.client9.setGeometry(QRect(30, 280, 21, 71))
        self.client9.setText("")
        self.client9.setPixmap(QPixmap(os.path.join("MP2X_Demand","client.png")))
        self.client9.setObjectName("client9") 

        self.client10 = QLabel(self)
        self.client10.setGeometry(QRect(50, 280, 21, 71))
        self.client10.setText("")
        self.client10.setPixmap(QPixmap(os.path.join("MP2X_Demand","client.png")))
        self.client10.setObjectName("client10") 

        self.client11 = QLabel(self)
        self.client11.setGeometry(QRect(30, 320, 21, 71))
        self.client11.setText("")
        self.client11.setPixmap(QPixmap(os.path.join("MP2X_Demand","client.png")))
        self.client11.setObjectName("client11") 

        self.client12 = QLabel(self)
        self.client12.setGeometry(QRect(50, 320, 21, 71))
        self.client12.setText("")
        self.client12.setPixmap(QPixmap(os.path.join("MP2X_Demand","client.png")))
        self.client12.setObjectName("client12") 

        self.client13 = QLabel(self)
        self.client13.setGeometry(QRect(30, 360, 21, 71))
        self.client13.setText("")
        self.client13.setPixmap(QPixmap(os.path.join("MP2X_Demand","client.png")))
        self.client13.setObjectName("client13") 

        self.client14 = QLabel(self)
        self.client14.setGeometry(QRect(50, 360, 21, 71))
        self.client14.setText("")
        self.client14.setPixmap(QPixmap(os.path.join("MP2X_Demand","client.png")))
        self.client14.setObjectName("client14")
        
        
        self.client15 = QLabel(self)
        self.client15.setGeometry(QRect(30, 400, 21, 71))
        self.client15.setText("")
        self.client15.setPixmap(QPixmap(os.path.join("MP2X_Demand","client.png")))
        self.client15.setObjectName("client15") 

        self.client16 = QLabel(self)
        self.client16.setGeometry(QRect(50, 400, 21, 71))
        self.client16.setText("")
        self.client16.setPixmap(QPixmap(os.path.join("MP2X_Demand","client.png")))
        self.client16.setObjectName("client16") 

        self.line1 = QLabel(self)
        self.line1.setGeometry(QRect(30, 100, 41, 31))
        self.line1.setText("")
        self.line1.setPixmap(QPixmap(os.path.join("MP2X_Demand","line2.png")))
        self.line1.setObjectName("line1") 

        self.line2 = QLabel(self)
        self.line2.setGeometry(QRect(50, 100, 51, 31))
        self.line2.setText("")
        self.line2.setPixmap(QPixmap(os.path.join("MP2X_Demand","line2.png")))
        self.line2.setObjectName("line2")
        
        self.upper_socket = QLabel(self)
        self.upper_socket.setGeometry(QRect(20, -20, 41, 81))
        self.upper_socket.setText("")
        self.upper_socket.setPixmap(QPixmap(os.path.join("MP2X_Demand","socket1.png")))
        self.upper_socket.setObjectName("upper_soclet") 

        self.socket = QLabel(self)
        self.socket.setGeometry(QRect(20, 470, 55, 61))
        self.socket.setText("")
        self.socket.setPixmap(QPixmap(os.path.join("MP2X_Demand","socket2.png")))
        self.socket.setObjectName("socket") 

        self.title = QLabel(self)
        self.title.setGeometry(QRect(70, 0, 55, 91))
        self.title.setText("")
        self.title.setPixmap(QPixmap(os.path.join("MP2X_Demand","title2.png")))
        self.title.setObjectName("title2")

        self.retranslateUi()
        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(_translate("self", "self"))
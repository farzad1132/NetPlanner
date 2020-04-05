from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import sys
import os
from data import *


class TP1H_R_Grooming(QWidget):

    def __init__(self,Panel_ID,nodename):

        self.id = Panel_ID
        self.nodename = nodename

        super(TP1H_R_Grooming, self).__init__()
        self.setFixedSize(109, 810)

        

        self.label_31 = QLabel(self)
        self.label_31.setGeometry(QRect(50, 130, 55, 16))
        self.label_31.setObjectName("label_31") 

        self.label_13 = QLabel(self)
        self.label_13.setGeometry(QRect(30, 540, 55, 16))
        self.label_13.setObjectName("label_13") 

        self.label_29 = QLabel(self)
        self.label_29.setGeometry(QRect(50, 120, 55, 16))
        self.label_29.setObjectName("label_29") 

        self.label_27 = QLabel(self)
        self.label_27.setGeometry(QRect(50, 110, 55, 16))
        self.label_27.setObjectName("label_27") 

        
        self.label_12 = QLabel(self)
        self.label_12.setGeometry(QRect(40, 280, 55, 16))
        self.label_12.setObjectName("label_12") 

        
        self.label_25 = QLabel(self)
        self.label_25.setGeometry(QRect(30, 460, 55, 16))
        self.label_25.setObjectName("label_25") 

        self.label_14 = QLabel(self)
        self.label_14.setGeometry(QRect(30, 560, 55, 16))
        self.label_14.setObjectName("label_14") 

        self.ch = QLabel(self)
        self.ch.setGeometry(QRect(50, 460, 55, 16))
        self.ch.setText("")
        self.ch.setPixmap(QPixmap(os.path.join("TP1H_Grooming", "CH.png")))
        self.ch.setObjectName("ch") 

        self.label_11 = QLabel(self)
        self.label_11.setGeometry(QRect(40, 260, 55, 16))
        self.label_11.setObjectName("label_11") 

       
        self.b1 = QLabel(self)
        self.b1.setGeometry(QRect(30, 110, 55, 16))
        self.b1.setText("")
        self.b1.setPixmap(QPixmap(os.path.join("TP1H_Grooming", "button.png")))
        self.b1.setObjectName("b1") 

        self.b2 = QLabel(self)
        self.b2.setGeometry(QRect(30, 120, 55, 16))
        self.b2.setText("")
        self.b2.setPixmap(QPixmap(os.path.join("TP1H_Grooming", "button.png")))
        self.b2.setObjectName("b2") 

        self.b3 = QLabel(self)
        self.b3.setGeometry(QRect(30, 130, 21, 20))
        self.b3.setText("")
        self.b3.setPixmap(QPixmap(os.path.join("TP1H_Grooming", "button.png")))
        self.b3.setObjectName("b3") 

        self.b4 = QLabel(self)
        self.b4.setGeometry(QRect(30, 260, 55, 16))
        self.b4.setText("")
        self.b4.setPixmap(QPixmap(os.path.join("TP1H_Grooming", "button.png")))
        self.b4.setObjectName("b4") 

        self.b5 = QLabel(self)
        self.b5.setGeometry(QRect(30, 280, 55, 16))
        self.b5.setText("")
        self.b5.setPixmap(QPixmap(os.path.join("TP1H_Grooming", "button.png")))
        self.b5.setObjectName("b5") 

        self.b6 = QLabel(self)
        self.b6.setGeometry(QRect(20, 540, 55, 16))
        self.b6.setText("")
        self.b6.setPixmap(QPixmap(os.path.join("TP1H_Grooming", "button.png")))
        self.b6.setObjectName("b6") 

        self.b7 = QLabel(self)
        self.b7.setGeometry(QRect(20, 560, 55, 16))
        self.b7.setText("")
        self.b7.setPixmap(QPixmap(os.path.join("TP1H_Grooming", "button.png")))
        self.b7.setObjectName("b7")

        self.retranslateUi()
        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.label_31.setText(_translate("self", "<html><head/><body><p><span style=\" font-size:6pt;\">W/P</span></p></body></html>"))
        self.label_13.setText(_translate("self", "<html><head/><body><p><span style=\" font-size:6pt;\">ACT</span></p></body></html>"))
        self.label_29.setText(_translate("self", "<html><head/><body><p><span style=\" font-size:6pt;\">FAIL</span></p></body></html>"))
        self.label_27.setText(_translate("self", "<html><head/><body><p><span style=\" font-size:6pt;\">ACT</span></p></body></html>"))
        self.label_12.setText(_translate("self", "<html><head/><body><p><span style=\" font-size:6pt;\">SF</span></p></body></html>"))
        self.label_25.setText(_translate("self", "CH"))
        self.label_14.setText(_translate("self", "<html><head/><body><p><span style=\" font-size:6pt;\">SF</span></p></body></html>"))
        self.label_11.setText(_translate("self", "<html><head/><body><p><span style=\" font-size:6pt;\">ACT</span></p></body></html>"))



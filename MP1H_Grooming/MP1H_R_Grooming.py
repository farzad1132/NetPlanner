from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import sys
import os
from data import *


class MP1H_R_Grooming(QWidget):

    def __init__(self,Panel_ID,nodename):

        self.id = Panel_ID
        self.nodename = nodename

        super(MP1H_R_Grooming, self).__init__()
        self.setFixedSize(109, 810) 

        self.label_25 = QLabel(self)
        self.label_25.setGeometry(QRect(10, 550, 55, 16))
        self.label_25.setObjectName("label_25") 

        self.button2 = QLabel(self)
        self.button2.setGeometry(QRect(40, 90, 31, 16))
        self.button2.setText("")
        self.button2.setPixmap(QPixmap(os.path.join("MP1H_Grooming", "button.png")))
        self.button2.setObjectName("button2") 

        self.button7 = QLabel(self)
        self.button7.setGeometry(QRect(10, 250, 31, 16))
        self.button7.setText("")
        self.button7.setPixmap(QPixmap(os.path.join("MP1H_Grooming", "button.png")))
        self.button7.setObjectName("button7") 

        self.button15 = QLabel(self)
        self.button15.setGeometry(QRect(10, 620, 31, 16))
        self.button15.setText("")
        self.button15.setPixmap(QPixmap(os.path.join("MP1H_Grooming", "button.png")))
        self.button15.setObjectName("button15") 

        self.label_17 = QLabel(self)
        self.label_17.setGeometry(QRect(20, 390, 55, 16))
        self.label_17.setObjectName("label_17") 

        self.button11 = QLabel(self)
        self.button11.setGeometry(QRect(10, 390, 31, 16))
        self.button11.setText("")
        self.button11.setPixmap(QPixmap(os.path.join("MP1H_Grooming", "button.png")))
        self.button11.setObjectName("button11") 

        self.button14 = QLabel(self)
        self.button14.setGeometry(QRect(10, 610, 31, 16))
        self.button14.setText("")
        self.button14.setPixmap(QPixmap(os.path.join("MP1H_Grooming", "button.png")))
        self.button14.setObjectName("button14") 

        self.label_20 = QLabel(self)
        self.label_20.setGeometry(QRect(20, 450, 55, 16))
        self.label_20.setObjectName("label_20") 

        self.label_24 = QLabel(self)
        self.label_24.setGeometry(QRect(20, 610, 55, 16))
        self.label_24.setObjectName("label_24") 

        self.label_29 = QLabel(self)
        self.label_29.setGeometry(QRect(50, 90, 55, 16))
        self.label_29.setObjectName("label_29") 

        self.label_15 = QLabel(self)
        self.label_15.setGeometry(QRect(20, 320, 55, 16))
        self.label_15.setObjectName("label_15") 

        self.ch = QLabel(self)
        self.ch.setGeometry(QRect(30, 550, 55, 16))
        self.ch.setText("")
        self.ch.setPixmap(QPixmap(os.path.join("MP1H_Grooming","CH.png")))
        self.ch.setObjectName("ch") 

        self.button5 = QLabel(self)
        self.button5.setGeometry(QRect(10, 180, 31, 21))
        self.button5.setText("")
        self.button5.setPixmap(QPixmap(os.path.join("MP1H_Grooming", "button.png")))
        self.button5.setObjectName("button5") 

        self.button13 = QLabel(self)
        self.button13.setGeometry(QRect(10, 460, 31, 16))
        self.button13.setText("")
        self.button13.setPixmap(QPixmap(os.path.join("MP1H_Grooming", "button.png")))
        self.button13.setObjectName("button13") 

        self.button9 = QLabel(self)
        self.button9.setGeometry(QRect(10, 320, 31, 16))
        self.button9.setText("")
        self.button9.setPixmap(QPixmap(os.path.join("MP1H_Grooming", "button.png")))
        self.button9.setObjectName("button9") 

        self.label_19 = QLabel(self)
        self.label_19.setGeometry(QRect(20, 460, 55, 16))
        self.label_19.setObjectName("label_19") 

        self.label_12 = QLabel(self)
        self.label_12.setGeometry(QRect(20, 180, 55, 16))
        self.label_12.setObjectName("label_12") 

        self.label_27 = QLabel(self)
        self.label_27.setGeometry(QRect(50, 80, 55, 16))
        self.label_27.setObjectName("label_27") 

        self.label_13 = QLabel(self)
        self.label_13.setGeometry(QRect(20, 250, 55, 16))
        self.label_13.setObjectName("label_13") 

        self.label_16 = QLabel(self)
        self.label_16.setGeometry(QRect(20, 310, 55, 16))
        self.label_16.setObjectName("label_16") 

        self.button1 = QLabel(self) 
        self.button1.setGeometry(QRect(40, 80, 31, 16))
        self.button1.setText("")
        self.button1.setPixmap(QPixmap(os.path.join("MP1H_Grooming", "button.png")))
        self.button1.setObjectName("button1") 

        self.label_11 = QLabel(self)
        self.label_11.setGeometry(QRect(20, 170, 55, 16))
        self.label_11.setObjectName("label_11")
        self.label_14 = QLabel(self)
        self.label_14.setGeometry(QRect(20, 240, 55, 16))
        self.label_14.setObjectName("label_14") 

        self.button3 = QLabel(self)
        self.button3.setGeometry(QRect(40, 100, 31, 16))
        self.button3.setText("")
        self.button3.setPixmap(QPixmap(os.path.join("MP1H_Grooming", "button.png")))
        self.button3.setObjectName("button3") 

        self.button12 = QLabel(self)
        self.button12.setGeometry(QRect(10, 450, 31, 16))
        self.button12.setText("")
        self.button12.setPixmap(QPixmap(os.path.join("MP1H_Grooming", "button.png")))
        self.button12.setObjectName("button12") 

        self.button4 = QLabel(self)
        self.button4.setGeometry(QRect(10, 170, 31, 16))
        self.button4.setText("")
        self.button4.setPixmap(QPixmap(os.path.join("MP1H_Grooming", "button.png")))
        self.button4.setObjectName("button4") 

        self.button10 = QLabel(self)
        self.button10.setGeometry(QRect(10, 380, 31, 16))
        self.button10.setText("")
        self.button10.setPixmap(QPixmap(os.path.join("MP1H_Grooming", "button.png")))
        self.button10.setObjectName("button10") 

        self.label_31 = QLabel(self)
        self.label_31.setGeometry(QRect(50, 100, 55, 16))
        self.label_31.setObjectName("label_31") 

        self.label_21 = QLabel(self)
        self.label_21.setGeometry(QRect(20, 620, 55, 16))
        self.label_21.setObjectName("label_21") 

        self.button8 = QLabel(self)
        self.button8.setGeometry(QRect(10, 310, 31, 16))
        self.button8.setText("")
        self.button8.setPixmap(QPixmap(os.path.join("MP1H_Grooming", "button.png")))
        self.button8.setObjectName("button8") 

        self.label_18 = QLabel(self)
        self.label_18.setGeometry(QRect(20, 380, 55, 16))
        self.label_18.setObjectName("label_18") 

        self.button6 = QLabel(self)
        self.button6.setGeometry(QRect(10, 240, 31, 16))
        self.button6.setText("")
        self.button6.setPixmap(QPixmap(os.path.join("MP1H_Grooming", "button.png")))
        self.button6.setObjectName("button6")

        self.retranslateUi(self)
        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.label_25.setText(_translate("self", "CH"))
        self.label_17.setText(_translate("self", "<html><head/><body><p><span style=\" font-size:6pt;\">SF</span></p></body></html>"))
        self.label_20.setText(_translate("self", "<html><head/><body><p><span style=\" font-size:6pt;\">ACT</span></p></body></html>"))
        self.label_24.setText(_translate("self", "<html><head/><body><p><span style=\" font-size:6pt;\">ACT</span></p></body></html>"))
        self.label_29.setText(_translate("self", "<html><head/><body><p><span style=\" font-size:6pt;\">FAIL</span></p></body></html>"))
        self.label_15.setText(_translate("self", "<html><head/><body><p><span style=\" font-size:6pt;\">SF</span></p></body></html>"))
        self.label_19.setText(_translate("self", "<html><head/><body><p><span style=\" font-size:6pt;\">SF</span></p></body></html>"))
        self.label_12.setText(_translate("self", "<html><head/><body><p><span style=\" font-size:6pt;\">SF</span></p></body></html>"))
        self.label_27.setText(_translate("self", "<html><head/><body><p><span style=\" font-size:6pt;\">ACT</span></p></body></html>"))
        self.label_13.setText(_translate("self", "<html><head/><body><p><span style=\" font-size:6pt;\">SF</span></p></body></html>"))
        self.label_16.setText(_translate("self", "<html><head/><body><p><span style=\" font-size:6pt;\">ACT</span></p></body></html>"))
        self.label_11.setText(_translate("self", "<html><head/><body><p><span style=\" font-size:6pt;\">ACT</span></p></body></html>"))
        self.label_14.setText(_translate("self", "<html><head/><body><p><span style=\" font-size:6pt;\">ACT</span></p></body></html>"))
        self.label_31.setText(_translate("self", "<html><head/><body><p><span style=\" font-size:6pt;\">W/P</span></p></body></html>"))
        self.label_21.setText(_translate("self", "<html><head/><body><p><span style=\" font-size:6pt;\">SF</span></p></body></html>"))
        self.label_18.setText(_translate("self", "<html><head/><body><p><span style=\" font-size:6pt;\">ACT</span></p></body></html>"))


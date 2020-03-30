<<<<<<< HEAD
=======
from PySide2 import QtWidgets, QtCore, QtGui
>>>>>>> 90860f6dace01a70861946f38b5327974962c8c8
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import sys
import os
<<<<<<< HEAD
from data import *


class TP1H_R_Demand(QWidget):
    def __init__(self, Panel_ID, nodename):
        super(TP1H_R_Demand, self).__init__()

        self.id =Panel_ID
        self.nodename = nodename

        self.setFixedSize(112, 521)
        self.label_12 = QLabel(self)
        self.label_12.setGeometry(QRect(20, 230, 55, 16))
=======

from data import *

class TP1H_R_Demand(QObject):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(112, 521)
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(20, 230, 55, 16))
>>>>>>> 90860f6dace01a70861946f38b5327974962c8c8
        self.label_12.setObjectName("label_12")
        self.label_2 = QLabel(self)
        self.label_2.setGeometry(QRect(10, 230, 31, 16))
        self.label_2.setText("")
        self.label_2.setPixmap(QPixmap(os.path.join("TP1H_Demand","button.png")))
        self.label_2.setObjectName("label_2")
        self.label = QLabel(self)
        self.label.setGeometry(QRect(10, 210, 31, 16))
        self.label.setText("")
        self.label.setPixmap(QPixmap(os.path.join("TP1H_Demand","button.png")))
        self.label.setObjectName("label")
        self.label_11 = QLabel(self)
        self.label_11.setGeometry(QRect(20, 210, 55, 16))
        self.label_11.setObjectName("label_11")
        self.label_3 = QLabel(self)
        self.label_3.setGeometry(QRect(10, 380, 31, 16))
        self.label_3.setText("")
        self.label_3.setPixmap(QPixmap(os.path.join("TP1H_Demand","button.png")))
        self.label_3.setObjectName("label_3")
        self.label_4 = QLabel(self)
        self.label_4.setGeometry(QRect(10, 360, 31, 16))
        self.label_4.setText("")
        self.label_4.setPixmap(QPixmap(os.path.join("TP1H_Demand","button.png")))
        self.label_4.setObjectName("label_4")
        self.label_13 = QLabel(self)
        self.label_13.setGeometry(QRect(20, 360, 55, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QLabel(self)
        self.label_14.setGeometry(QRect(20, 380, 55, 16))
        self.label_14.setObjectName("label_14")
        self.label_29 = QLabel(self)
        self.label_29.setGeometry(QRect(30, 70, 55, 16))
        self.label_29.setObjectName("label_29")
        self.label_30 = QLabel(self)
        self.label_30.setGeometry(QRect(20, 80, 31, 16))
        self.label_30.setText("")
        self.label_30.setPixmap(QPixmap(os.path.join("TP1H_Demand","button.png")))
        self.label_30.setObjectName("label_30")
        self.label_27 = QLabel(self)
        self.label_27.setGeometry(QRect(30, 60, 55, 16))
        self.label_27.setObjectName("label_27")
        self.label_26 = QLabel(self)
        self.label_26.setGeometry(QRect(20, 70, 31, 16))
        self.label_26.setText("")
        self.label_26.setPixmap(QPixmap(os.path.join("TP1H_Demand","button.png")))
        self.label_26.setObjectName("label_26")
        self.label_31 = QLabel(self)
        self.label_31.setGeometry(QRect(30, 80, 55, 16))
        self.label_31.setObjectName("label_31")
        self.label_28 = QLabel(self)
        self.label_28.setGeometry(QRect(20, 60, 31, 16))
        self.label_28.setText("")
        self.label_28.setPixmap(QPixmap(os.path.join("TP1H_Demand","button.png")))
        self.label_28.setObjectName("label_28")
        self.label_61 = QLabel(self)
        self.label_61.setGeometry(QRect(30, 330, 55, 16))
        self.label_61.setText("")
        self.label_61.setPixmap(QPixmap(os.path.join("TP1H_Demand","CH.png")))
        self.label_61.setObjectName("label_61")
        self.label_25 = QLabel(self)
        self.label_25.setGeometry(QRect(10, 330, 55, 16))
        self.label_25.setObjectName("label_25")

        self.retranslateUi()
        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.label_12.setText(_translate("self", "<html><head/><body><p><span style=\" font-size:6pt;\">SF</span></p></body></html>"))
        self.label_11.setText(_translate("self", "<html><head/><body><p><span style=\" font-size:6pt;\">ACT</span></p></body></html>"))
        self.label_13.setText(_translate("self", "<html><head/><body><p><span style=\" font-size:6pt;\">ACT</span></p></body></html>"))
        self.label_14.setText(_translate("self", "<html><head/><body><p><span style=\" font-size:6pt;\">SF</span></p></body></html>"))
        self.label_29.setText(_translate("self", "<html><head/><body><p><span style=\" font-size:6pt;\">FAIL</span></p></body></html>"))
        self.label_27.setText(_translate("self", "<html><head/><body><p><span style=\" font-size:6pt;\">ACT</span></p></body></html>"))
        self.label_31.setText(_translate("self", "<html><head/><body><p><span style=\" font-size:6pt;\">W/P</span></p></body></html>"))
        self.label_25.setText(_translate("self", "CH"))



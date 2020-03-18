# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TP1H_L.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(116, 521)
        self.line = QtWidgets.QLabel(Form)
        self.line.setGeometry(QtCore.QRect(30, 140, 55, 191))
        self.line.setText("")
        self.line.setPixmap(QPixmap(os.path.join("tp1h_line","TP1H_CLIENT.png")))
        self.line.setObjectName("line") 

        self.client = QtWidgets.QLabel(Form)
        self.client.setGeometry(QtCore.QRect(30, 320, 55, 141))
        self.client.setText("")
        self.client.setPixmap(QPixmap(os.path.join("TP1H_Demand","TP1H_CLIENT.png")))
        self.client.setObjectName("client") 

        self.title = QtWidgets.QLabel(Form)
        self.title.setGeometry(QtCore.QRect(60, 30, 55, 111))
        self.title.setText("")
        self.titlesetPixmap(QPixmap(os.path.join("TP1H_Demand","title2.png")))
        self.title.setObjectName("title2")  

        self.upper_socket = QLabel(self)
        self.upper_socket.setGeometry(QRect(20, -20, 41, 81))
        self.upper_socket.setText("")
        self.upper_socket.setPixmap(QPixmap(os.path.join("TP1H_Demand","socket1.png")))
        self.upper_socket.setObjectName("upper_soclet") 

        self.socket = QLabel(self)
        self.socket.setGeometry(QRect(20, 470, 55, 61))
        self.socket.setText("")
        self.socket.setPixmap(QPixmap(os.path.join("TP1H_Demand","socket2.png")))
        self.socket.setObjectName("socket") 

        self.retranslateUi(self)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'New_TP1H_L.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(94, 593)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.Line = QtWidgets.QLabel(Form)
        self.Line.setMinimumSize(QtCore.QSize(0, 25))
        self.Line.setMaximumSize(QtCore.QSize(100, 200))
        self.Line.setStyleSheet("image: url(:/Line/tp1h_line.png);")
        self.Line.setText("")
        self.Line.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Line.setObjectName("Line")
        self.gridLayout.addWidget(self.Line, 1, 0, 3, 1)
        self.not_used_1 = QtWidgets.QLabel(Form)
        self.not_used_1.setMaximumSize(QtCore.QSize(16777215, 20))
        self.not_used_1.setText("")
        self.not_used_1.setObjectName("not_used_1")
        self.gridLayout.addWidget(self.not_used_1, 4, 0, 1, 1)
        self.Top_Socket = QtWidgets.QLabel(Form)
        self.Top_Socket.setStyleSheet("image: url(:/Socket/socket1.png);")
        self.Top_Socket.setText("")
        self.Top_Socket.setObjectName("Top_Socket")
        self.gridLayout.addWidget(self.Top_Socket, 0, 0, 1, 1)
        self.Bottom_Socket = QtWidgets.QLabel(Form)
        self.Bottom_Socket.setStyleSheet("image: url(:/Socket_bottom/socket2.png);")
        self.Bottom_Socket.setText("")
        self.Bottom_Socket.setObjectName("Bottom_Socket")
        self.gridLayout.addWidget(self.Bottom_Socket, 7, 0, 1, 1)
        self.Client = QtWidgets.QLabel(Form)
        self.Client.setMinimumSize(QtCore.QSize(0, 25))
        self.Client.setStyleSheet("image: url(:/Client/TP1H_CLIENT.png);")
        self.Client.setText("")
        self.Client.setObjectName("Client")
        self.gridLayout.addWidget(self.Client, 5, 0, 2, 1)
        self.Line_Title = QtWidgets.QLabel(Form)
        self.Line_Title.setObjectName("Line_Title")
        self.gridLayout.addWidget(self.Line_Title, 2, 2, 1, 1)
        self.Client_Title = QtWidgets.QLabel(Form)
        self.Client_Title.setObjectName("Client_Title")
        self.gridLayout.addWidget(self.Client_Title, 5, 2, 2, 1)
        self.TP1H_Name = QtWidgets.QLabel(Form)
        self.TP1H_Name.setMaximumSize(QtCore.QSize(35, 16777215))
        self.TP1H_Name.setStyleSheet("image: url(:/title/title.png);")
        self.TP1H_Name.setText("")
        self.TP1H_Name.setObjectName("TP1H_Name")
        self.gridLayout.addWidget(self.TP1H_Name, 0, 2, 2, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Line_Title.setText(_translate("Form", "Line"))
        self.Client_Title.setText(_translate("Form", "Client"))
import Client
import Line
import Socket_bottom
import Socket
import TP1H_R
import title


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'New_TP1H_R.ui'
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
        self.TP1H_R = QtWidgets.QLabel(Form)
        self.TP1H_R.setMinimumSize(QtCore.QSize(0, 113))
        self.TP1H_R.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.TP1H_R.setStyleSheet("border-image: url(:/TP1H_R/TP1H_R.png);")
        self.TP1H_R.setText("")
        self.TP1H_R.setObjectName("TP1H_R")
        self.gridLayout.addWidget(self.TP1H_R, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
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

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Source_type_error.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_Source_type_error(object):
    def setupUi(self, Source_type_error):
        Source_type_error.setObjectName("Source_type_error")
        Source_type_error.resize(428, 199)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/error_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Source_type_error.setWindowIcon(icon)
        Source_type_error.setStyleSheet("background-color: rgb(255, 247, 248);")
        self.gridLayout = QtWidgets.QGridLayout(Source_type_error)
        self.gridLayout.setObjectName("gridLayout")
        self.textEdit = QtWidgets.QTextEdit(Source_type_error)
        self.textEdit.setStyleSheet("color:#2c3e50")
        self.textEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setTabChangesFocus(False)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Source_type_error)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"    font: 75 10pt \"Bahnschrift Condensed\";\n"
"    background-color:#FFFFFF;\n"
"    color: rgb(117, 117, 117);\n"
"    border: 2px solid #Eb8686; min-width: 80px;\n"
"    border-color: #Eb8686; \n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)
        self.pushButton.clicked.connect(Source_type_error.close)
        self.retranslateUi(Source_type_error)
        QtCore.QMetaObject.connectSlotsByName(Source_type_error)

    def retranslateUi(self, Source_type_error):
        _translate = QtCore.QCoreApplication.translate
        Source_type_error.setWindowTitle(_translate("Source_type_error", "Type Error"))
        self.textEdit.setHtml(_translate("Source_type_error", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">&quot;Source&quot; type is a </span><span style=\" font-size:11pt; text-decoration: underline;\">string</span><span style=\" font-size:11pt;\"> !  </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">please enter a string input(e.g. (Source , 1)=Tehran).</span></p></body></html>"))
        self.pushButton.setText(_translate("Source_type_error", "ok"))
from TrafficMatrixError import iconresources


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Source_type_error = QtWidgets.QWidget()
    ui = Ui_Source_type_error()
    ui.setupUi(Source_type_error)
    Source_type_error.show()
    sys.exit(app.exec_())

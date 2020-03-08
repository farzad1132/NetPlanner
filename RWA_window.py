from PySide2 import QtWidgets, QtGui, QtCore
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import sys
import os
from data import *
from Common_Object_def import Network
import pandas as pd 
bus = {}

class Ui_RWA_Window(object):
    def setupUi(self, RWA_Window):
        bus["RWA_Window"] = RWA_Window
        RWA_Window.setObjectName("RWA_Window")
        RWA_Window.resize(477, 363)
        self.gridLayout_2 = QtWidgets.QGridLayout(RWA_Window)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.mergindemands_gridlayout = QtWidgets.QGridLayout()
        self.mergindemands_gridlayout.setObjectName("mergindemands_gridlayout")
        self.mergingdemands_label = QtWidgets.QLabel(RWA_Window)
        font = QtGui.QFont()
        font.setFamily("IRANSans")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.mergingdemands_label.setFont(font)
        self.mergingdemands_label.setStyleSheet(" QLabel {\n"
"    border: 2px solid green;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}")
        self.mergingdemands_label.setAlignment(QtCore.Qt.AlignCenter)
        self.mergingdemands_label.setObjectName("mergingdemands_label")
        self.mergindemands_gridlayout.addWidget(self.mergingdemands_label, 0, 0, 1, 1)
        self.mergindemands_comboBox = QtWidgets.QComboBox(RWA_Window)
        self.mergindemands_comboBox.setStyleSheet("border-color: rgb(0, 85, 0);\n"
"border-color: rgb(85, 255, 0);")
        self.mergindemands_comboBox.setEditable(False)
        self.mergindemands_comboBox.setObjectName("mergindemands_comboBox")
        self.mergindemands_comboBox.addItem("")
        self.mergindemands_comboBox.addItem("")
        self.mergindemands_gridlayout.addWidget(self.mergindemands_comboBox, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.mergindemands_gridlayout, 0, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.mergingdemands_label_2 = QtWidgets.QLabel(RWA_Window)
        font = QtGui.QFont()
        font.setFamily("IRANSans")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.mergingdemands_label_2.setFont(font)
        self.mergingdemands_label_2.setStyleSheet(" QLabel {\n"
"    border: 2px solid green;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}")
        self.mergingdemands_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.mergingdemands_label_2.setObjectName("mergingdemands_label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.mergingdemands_label_2)
        self.alphalineEdit = QtWidgets.QLineEdit(RWA_Window)
        self.alphalineEdit.setStyleSheet("")
        self.alphalineEdit.setText("")
        self.alphalineEdit.setObjectName("alphalineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.alphalineEdit)
        self.gridLayout_2.addLayout(self.formLayout, 1, 0, 1, 1)
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setObjectName("formLayout_4")
        self.Iteration_label = QtWidgets.QLabel(RWA_Window)
        font = QtGui.QFont()
        font.setFamily("IRANSans")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.Iteration_label.setFont(font)
        self.Iteration_label.setStyleSheet(" QLabel {\n"
"    border: 2px solid green;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}")
        self.Iteration_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Iteration_label.setObjectName("Iteration_label")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Iteration_label)
        self.Iteration_lineedit = QtWidgets.QLineEdit(RWA_Window)
        self.Iteration_lineedit.setStyleSheet("\n"
"border-color: rgb(170, 0, 0);")
        self.Iteration_lineedit.setText("")
        self.Iteration_lineedit.setObjectName("Iteration_lineedit")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Iteration_lineedit)
        self.gridLayout_2.addLayout(self.formLayout_4, 1, 1, 1, 1)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.Margin_label = QtWidgets.QLabel(RWA_Window)
        font = QtGui.QFont()
        font.setFamily("IRANSans")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.Margin_label.setFont(font)
        self.Margin_label.setStyleSheet(" QLabel {\n"
"    border: 2px solid green;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}")
        self.Margin_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Margin_label.setObjectName("Margin_label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Margin_label)
        self.Margin_lineedit = QtWidgets.QLineEdit(RWA_Window)
        self.Margin_lineedit.setStyleSheet("\n"
"border-color: rgb(170, 0, 0);")
        self.Margin_lineedit.setText("")
        self.Margin_lineedit.setObjectName("Margin_lineedit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Margin_lineedit)
        self.gridLayout_2.addLayout(self.formLayout_2, 2, 0, 1, 1)
        self.formLayout_5 = QtWidgets.QFormLayout()
        self.formLayout_5.setObjectName("formLayout_5")
        self.Processors_label = QtWidgets.QLabel(RWA_Window)
        font = QtGui.QFont()
        font.setFamily("IRANSans")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.Processors_label.setFont(font)
        self.Processors_label.setStyleSheet(" QLabel {\n"
"    border: 2px solid green;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}")
        self.Processors_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Processors_label.setObjectName("Processors_label")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Processors_label)
        self.Processors_lineedit = QtWidgets.QLineEdit(RWA_Window)
        self.Processors_lineedit.setStyleSheet("\n"
"border-color: rgb(170, 0, 0);")
        self.Processors_lineedit.setText("")
        self.Processors_lineedit.setObjectName("Processors_lineedit")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Processors_lineedit)
        self.gridLayout_2.addLayout(self.formLayout_5, 2, 1, 1, 1)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.K_label = QtWidgets.QLabel(RWA_Window)
        font = QtGui.QFont()
        font.setFamily("IRANSans")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.K_label.setFont(font)
        self.K_label.setStyleSheet(" QLabel {\n"
"    border: 2px solid green;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}")
        self.K_label.setAlignment(QtCore.Qt.AlignCenter)
        self.K_label.setObjectName("K_label")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.K_label)
        self.K_lineedit = QtWidgets.QLineEdit(RWA_Window)
        self.K_lineedit.setStyleSheet("\n"
"border-color: rgb(170, 0, 0);")
        self.K_lineedit.setText("")
        self.K_lineedit.setObjectName("K_lineedit")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.K_lineedit)
        self.gridLayout_2.addLayout(self.formLayout_3, 3, 0, 1, 1)
        self.formLayout_6 = QtWidgets.QFormLayout()
        self.formLayout_6.setObjectName("formLayout_6")
        self.MNV_label = QtWidgets.QLabel(RWA_Window)
        font = QtGui.QFont()
        font.setFamily("IRANSans")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.MNV_label.setFont(font)
        self.MNV_label.setStyleSheet(" QLabel {\n"
"    border: 2px solid green;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}")
        self.MNV_label.setAlignment(QtCore.Qt.AlignCenter)
        self.MNV_label.setObjectName("MNV_label")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.MNV_label)
        self.MNV_lineedit = QtWidgets.QLineEdit(RWA_Window)
        self.MNV_lineedit.setStyleSheet("\n"
"border-color: rgb(170, 0, 0);")
        self.MNV_lineedit.setText("")
        self.MNV_lineedit.setObjectName("MNV_lineedit")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.MNV_lineedit)
        self.gridLayout_2.addLayout(self.formLayout_6, 3, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.ok_pushbutton = QtWidgets.QPushButton(RWA_Window)
        self.ok_pushbutton.setStyleSheet("QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: #8ADBB5;\n"
"    min-width: 80px;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: dark-orange;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"QPushButton::hover{\n"
"    background-color: #2EDB8A;\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"QPushButton:open { /* when the button has its menu open */\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton::menu-indicator {\n"
"    image: url(menu_indicator.png);\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: bottom right;\n"
"}\n"
"\n"
"QPushButton::menu-indicator:pressed, QPushButton::menu-indicator:open {\n"
"    position: relative;\n"
"    top: 2px; left: 2px; /* shift the arrow by 2 px */\n"
"}")
        self.ok_pushbutton.setAutoDefault(False)
        self.ok_pushbutton.setObjectName("ok_pushbutton")
        self.gridLayout.addWidget(self.ok_pushbutton, 0, 1, 1, 1)
        self.cancel_pushbutton = QtWidgets.QPushButton(RWA_Window)
        self.cancel_pushbutton.setStyleSheet("QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: #8ADBB5;\n"
"    min-width: 80px;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: dark-orange;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"QPushButton::hover{\n"
"    background-color: #2EDB8A;\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"QPushButton:open { /* when the button has its menu open */\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton::menu-indicator {\n"
"    image: url(menu_indicator.png);\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: bottom right;\n"
"}\n"
"\n"
"QPushButton::menu-indicator:pressed, QPushButton::menu-indicator:open {\n"
"    position: relative;\n"
"    top: 2px; left: 2px; /* shift the arrow by 2 px */\n"
"}")
        self.cancel_pushbutton.setObjectName("cancel_pushbutton")
        self.gridLayout.addWidget(self.cancel_pushbutton, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 4, 0, 1, 2)

        self.retranslateUi(RWA_Window)
        QtCore.QMetaObject.connectSlotsByName(RWA_Window)

        # NOTE: added 
        self.cancel_pushbutton.clicked.connect(RWA_Window.close)
        self.ok_pushbutton.clicked.connect(self.ok_button_fun)

    def retranslateUi(self, RWA_Window):
        _translate = QtCore.QCoreApplication.translate
        RWA_Window.setWindowTitle(_translate("RWA_Window", "RWA Window"))
        self.mergingdemands_label.setText(_translate("RWA_Window", "Merging demands"))
        self.mergindemands_comboBox.setItemText(0, _translate("RWA_Window", "True"))
        self.mergindemands_comboBox.setItemText(1, _translate("RWA_Window", "False"))
        self.mergingdemands_label_2.setText(_translate("RWA_Window", "      Alpha  "))
        self.Iteration_label.setText(_translate("RWA_Window", "  Iteration   "))
        self.Margin_label.setText(_translate("RWA_Window", "    Margin "))
        self.Processors_label.setText(_translate("RWA_Window", " Processors"))
        self.K_label.setText(_translate("RWA_Window", "        k     "))
        self.MNV_label.setText(_translate("RWA_Window", "Maximum Number of Wavelengths"))
        self.ok_pushbutton.setText(_translate("RWA_Window", "OK"))
        self.cancel_pushbutton.setText(_translate("RWA_Window", "Cancel"))

    
    def ok_button_fun(self):
        merge = self.mergindemands_comboBox.currentText()
        alpha = self.alphalineEdit.text()
        margin = self.Margin_lineedit.text()
        iterations = self.Iteration_lineedit.text()
        processors = self.Processors_lineedit.text()

        k = self.K_lineedit.text()
        maxNW = self.MNV_lineedit.text()

        if (alpha and margin and iterations and processors and k) != "":
            if merge == "False":
                merge = False
            elif merge == "True":
                merge = True
            else:
                print(f"merge error")
                assert False
            alpha = float(alpha)
            margin = int(margin)
            iterations = int(iterations)
            processors = int(processors)
            k = int(k)
            
            if maxNW == "":
                maxNW = None
            else:
                maxNW = int(maxNW)


            Data["ui"].RWA_procedure(merge, alpha, iterations, margin, processors, k, maxNW)
            bus["RWA_Window"].close()
        else:
            print("fill all boxes")

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RWA_Window = QtWidgets.QWidget()
    ui = Ui_RWA_Window()
    ui.setupUi(RWA_Window)
    RWA_Window.show()
    sys.exit(app.exec_())

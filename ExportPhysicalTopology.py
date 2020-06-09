from PySide2 import QtWidgets, QtGui, QtCore
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import sys
import os
from data import *
from Common_Object_def import Network
bus = {}


class Ui_Export_PT(object):
    def setupUi(self, Export_PT):

        bus["Export_PT"] = Export_PT

        Export_PT.setObjectName("Export_PT")
        Export_PT.resize(614, 244)
        self.gridLayout = QtWidgets.QGridLayout(Export_PT)
        self.gridLayout.setObjectName("gridLayout")
        self.ExportPhysicalTopology_PushButton = QtWidgets.QPushButton(Export_PT)
        self.ExportPhysicalTopology_PushButton.setMinimumSize(QtCore.QSize(84, 70))
        self.ExportPhysicalTopology_PushButton.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"    font: 75 10pt \"Bahnschrift Condensed\";\n"
"    \n"
"    border: 2px solid #8f8f91; min-width: 80px;\n"
"    border-color:  #4072B3; \n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed,hover {\n"
"    background-color:  #4072B3; \n"
"}\n"
"QPushButton:hover {\n"
"    background-color:  #4072B3; \n"
"}\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        self.ExportPhysicalTopology_PushButton.setObjectName("ExportPhysicalTopology_PushButton")
        self.gridLayout.addWidget(self.ExportPhysicalTopology_PushButton, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(Export_PT)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 2, 1)
        self.line = QtWidgets.QFrame(Export_PT)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 1, 2, 1)
        self.EnterTrafficMatrix_PushButton = QtWidgets.QPushButton(Export_PT)
        self.EnterTrafficMatrix_PushButton.setMinimumSize(QtCore.QSize(84, 50))
        self.EnterTrafficMatrix_PushButton.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"    font: 75 10pt \"Bahnschrift Condensed\";\n"
"    \n"
"    border: 2px solid #8f8f91; min-width: 80px;\n"
"    border-color: #EB8686; \n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed,hover {\n"
"    background-color: #EB8686; \n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #EB8686; \n"
"}\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        self.EnterTrafficMatrix_PushButton.setObjectName("EnterTrafficMatrix_PushButton")
        self.gridLayout.addWidget(self.EnterTrafficMatrix_PushButton, 1, 2, 1, 1)
        self.ImportTrafficMatrixExcel_pushButton = QtWidgets.QPushButton(Export_PT)
        self.ImportTrafficMatrixExcel_pushButton.setMinimumSize(QtCore.QSize(84, 50))
        self.ImportTrafficMatrixExcel_pushButton.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"    font: 75 10pt \"Bahnschrift Condensed\";\n"
"    \n"
"    border: 2px solid #8f8f91; min-width: 80px;\n"
"    border-color: #EB8686; \n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed,hover {\n"
"    background-color: #EB8686; \n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #EB8686; \n"
"}\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        self.ImportTrafficMatrixExcel_pushButton.setObjectName("ImportTrafficMatrixExcel_pushButton")
        self.gridLayout.addWidget(self.ImportTrafficMatrixExcel_pushButton, 2, 2, 1, 1)

        self.retranslateUi(Export_PT)
        QtCore.QMetaObject.connectSlotsByName(Export_PT)

        # NOTE: added
        self.ExportPhysicalTopology_PushButton.clicked.connect(self.Export_PT)
        self.ImportTrafficMatrixExcel_pushButton.clicked.connect(self.import_tm)
        self.EnterTrafficMatrix_PushButton.clicked.connect(self.enter_tm)

    def retranslateUi(self, Export_PT):
        _translate = QtCore.QCoreApplication.translate
        Export_PT.setWindowTitle(_translate("Export_PT", "Expot Physical Topology"))
        self.ExportPhysicalTopology_PushButton.setText(_translate("Export_PT", "Export Physical Topology"))
        self.label.setText(_translate("Export_PT", "Adding Traffic Matrix to Project"))
        self.EnterTrafficMatrix_PushButton.setText(_translate("Export_PT", "Enter Traffic Matrix"))
        self.ImportTrafficMatrixExcel_pushButton.setText(_translate("Export_PT", "Import Traffic Matrix Excel"))

    def Export_PT(self):
        Data["ui"].save_PT_excel()

    def import_tm(self):
        path, Success = Data["ui"].LoadTM_fun(bus["Export_PT"])

        if Success:
            Data["ui"].SaveChanges_button_fun()
            bus["Export_PT"].close()
        else:
            self.ImportTrafficMatrixExcel_pushButton.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"    font: 75 10pt \"Bahnschrift Condensed\";\n"
"    \n"
"    border: 2px solid #8f8f91; min-width: 80px;\n"
"    border-color: #EB8686; \n"
"    border-radius: 5px;\n"
"    background-color: red; \n"
"}\n"
"\n"
"QPushButton:pressed,hover {\n"
"    background-color: #EB8686; \n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #EB8686; \n"
"}\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")

    def enter_tm(self):
        Data["TabWidget"].setTabEnabled(1, True)
        Data["TabWidget"].setCurrentIndex(1)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Export_PT = QtWidgets.QWidget()
    ui = Ui_Export_PT()
    ui.setupUi(Export_PT)
    Export_PT.show()
    sys.exit(app.exec_())

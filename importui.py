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


class Ui_ImportMenuUI(object):
    def setupUi(self, ImportMenuUI):

        # NOTE: added
        bus["ImportMenuUI"] = ImportMenuUI

        ImportMenuUI.setObjectName("ImportMenuUI")
        ImportMenuUI.resize(459, 319)
        ImportMenuUI.setStyleSheet("background-color:rgb(226, 226, 226);")
        self.gridLayout = QtWidgets.QGridLayout(ImportMenuUI)
        self.gridLayout.setObjectName("gridLayout")
        self.PlanningLabel = QtWidgets.QLabel(ImportMenuUI)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.PlanningLabel.setFont(font)
        self.PlanningLabel.setStyleSheet("QLabel {\n"
"  \n"
"    \n"
"    font: 63 12pt \"Bahnschrift SemiBold Condensed\";\n"
"    background-color:  #6088C6;\n"
"}")
        self.PlanningLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.PlanningLabel.setObjectName("PlanningLabel")
        self.gridLayout.addWidget(self.PlanningLabel, 0, 0, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.PT_LineEdit = QtWidgets.QLineEdit(ImportMenuUI)
        self.PT_LineEdit.setStyleSheet("QLineEdit {\n"
" \n"
"    border: 2px solid rgb(226, 226, 226);\n"
"    border-bottom-color: rgb(86, 86, 86);\n"
"    padding: 0 8px;\n"
"    \n"
"    selection-background-color: darkgray; \n"
"    font: 8pt \"Bahnschrift\";\n"
"\n"
"}")
        self.PT_LineEdit.setObjectName("PT_LineEdit")
        self.horizontalLayout.addWidget(self.PT_LineEdit)
        self.PT_button = QtWidgets.QPushButton(ImportMenuUI)
        self.PT_button.setMaximumSize(QtCore.QSize(999, 999))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.PT_button.setFont(font)
        self.PT_button.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"    font: 75 10pt \"Bahnschrift Condensed\";\n"
"    \n"
"    color: rgb(117, 117, 117);\n"
"    border: 2px solid #8f8f91; min-width: 80px;\n"
"    border-color: #4072B3; \n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"} \n"
"\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        self.PT_button.setObjectName("PT_button")
        self.horizontalLayout.addWidget(self.PT_button)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 2)
        self.line_2 = QtWidgets.QFrame(ImportMenuUI)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 2, 0, 1, 2)
        self.line = QtWidgets.QFrame(ImportMenuUI)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 4, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.TrafficLineEdit = QtWidgets.QLineEdit(ImportMenuUI)
        self.TrafficLineEdit.setStyleSheet("QLineEdit {\n"
" \n"
"    border: 2px solid rgb(226, 226, 226);\n"
"    border-bottom-color: rgb(86, 86, 86);\n"
"    padding: 0 8px;\n"
"    \n"
"    selection-background-color: darkgray; \n"
"    font: 8pt \"Bahnschrift\";\n"
"\n"
"}")
        self.TrafficLineEdit.setObjectName("TrafficLineEdit")
        self.horizontalLayout_2.addWidget(self.TrafficLineEdit)
        self.TrafficButton = QtWidgets.QPushButton(ImportMenuUI)
        self.TrafficButton.setMaximumSize(QtCore.QSize(999, 999))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.TrafficButton.setFont(font)
        self.TrafficButton.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"    font: 75 10pt \"Bahnschrift Condensed\";\n"
"    \n"
"    color: rgb(117, 117, 117);\n"
"    border: 2px solid #8f8f91; min-width: 80px;\n"
"    border-color: #4072B3; \n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"} \n"
"\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        self.TrafficButton.setObjectName("TrafficButton")
        self.horizontalLayout_2.addWidget(self.TrafficButton)
        self.gridLayout.addLayout(self.horizontalLayout_2, 5, 0, 1, 2)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.SaveChangesBitton = QtWidgets.QPushButton(ImportMenuUI)
        self.SaveChangesBitton.setMaximumSize(QtCore.QSize(165, 100))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.SaveChangesBitton.setFont(font)
        self.SaveChangesBitton.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"     \n"
"    font: 75 10pt \"Bahnschrift Condensed\";\n"
"    \n"
"    \n"
"    border:2px solid black; min-width: 80px;\n"
"    border-color: dark gray; \n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed,hover {\n"
"    background-color: #EB8686; \n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #Eb8686; \n"
"}\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        self.SaveChangesBitton.setObjectName("SaveChangesBitton")
        self.gridLayout_2.addWidget(self.SaveChangesBitton, 0, 1, 1, 1)
        self.DrawButton = QtWidgets.QPushButton(ImportMenuUI)
        self.DrawButton.setMaximumSize(QtCore.QSize(165, 100))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.DrawButton.setFont(font)
        self.DrawButton.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"     \n"
"    font: 75 10pt \"Bahnschrift Condensed\";\n"
"    \n"
"    \n"
"    border:2px solid black; min-width: 80px;\n"
"    border-color: dark gray; \n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed,hover {\n"
"    background-color: #EB8686; \n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #AEC4E5; \n"
"}\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        self.DrawButton.setObjectName("DrawButton")
        self.gridLayout_2.addWidget(self.DrawButton, 0, 2, 1, 1)
        self.CloseButton = QtWidgets.QPushButton(ImportMenuUI)
        self.CloseButton.setMaximumSize(QtCore.QSize(165, 100))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.CloseButton.setFont(font)
        self.CloseButton.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"     \n"
"    font: 75 10pt \"Bahnschrift Condensed\";\n"
"    \n"
"    \n"
"    border:2px solid black; min-width: 80px;\n"
"    border-color: dark gray; \n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed,hover {\n"
"    background-color: #EB8686; \n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #c0c0c0; \n"
"}\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        self.CloseButton.setObjectName("CloseButton")
        self.gridLayout_2.addWidget(self.CloseButton, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 6, 0, 1, 2)
        self.label = QtWidgets.QLabel(ImportMenuUI)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label.setFont(font)
        self.label.setStyleSheet("  QLabel {\n"
"    \n"
"    font: 63 12pt \"Bahnschrift SemiBold Condensed\";\n"
"   \n"
"  \n"
"    background-color: rgb(235, 134, 134);\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 2)

        self.retranslateUi(ImportMenuUI)
        QtCore.QMetaObject.connectSlotsByName(ImportMenuUI)

        # NOTE: added
        self.CloseButton.clicked.connect(ImportMenuUI.close)
        self.PT_button.clicked.connect(self.PT_import_procedure)
        self.TrafficButton.clicked.connect(self.import_TM_procedure)
        self.SaveChangesBitton.clicked.connect(self.call_savechange)
        self.DrawButton.clicked.connect(self.call_insert_links)

        self.DrawButton.setEnabled(False)
        self.SaveChangesBitton.setEnabled(False)
        self.TrafficButton.setEnabled(False)

    def retranslateUi(self, ImportMenuUI):
        _translate = QtCore.QCoreApplication.translate
        ImportMenuUI.setWindowTitle(_translate("ImportMenuUI", "ImportMenuUI"))
        self.PlanningLabel.setText(_translate("ImportMenuUI", "Import Physical Topology"))
        self.PT_button.setText(_translate("ImportMenuUI", "Physical Topology"))
        self.TrafficButton.setText(_translate("ImportMenuUI", "Traffic Matrix"))
        self.SaveChangesBitton.setText(_translate("ImportMenuUI", "Save Changes"))
        self.DrawButton.setText(_translate("ImportMenuUI", "Draw"))
        self.CloseButton.setText(_translate("ImportMenuUI", "Close"))
        self.label.setText(_translate("ImportMenuUI", "Import Traffic Matrix "))

    def call_savechange(self):
        Data["ui"].SaveChanges_button_fun()

        self.DrawButton.setEnabled(True)
        self.TrafficButton.setEnabled(False)
        self.PT_button.setEnabled(False)
    
    def call_insert_links(self):
        Data["ui"].insert_link_fun()
        Data["ui"].Grouping_groupbox.setEnabled(True)
        Data["ui"].ShowSubNodes.setEnabled(False)
        Data["ui"].Demand_combo_notifications_flag = False
        bus["ImportMenuUI"].close()


    def PT_import_procedure(self):
        PT_path, PT_Success = self.import_PT_fun()
        self.PT_LineEdit.setText(PT_path[0])
        if PT_Success is True:
            self.TrafficButton.setEnabled(True)
            self.PT_button.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"    font: 75 10pt \"Bahnschrift Condensed\";\n"
"    \n"
"    color: rgb(117, 117, 117);\n"
"    border: 2px solid #8f8f91; min-width: 80px;\n"
"    border-color: #4072B3; \n"
"    border-radius: 15px;\n"
"    background-color: green;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: green;\n"

"} \n"
"\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")

    def import_PT_fun(self):
        name = QFileDialog.getOpenFileName(bus["ImportMenuUI"], "Open Physical Topology")

        if name[0] != 0 and name[0] != "":
            Data["Nodes"].clear()
            Data["Links"].clear()
            try:
                xls = pd.ExcelFile(name[0])
                Temp_data = pd.read_excel(xls, 'Nodes')
                temp_dic ={}
                headers = ['ID','Node','Location','ROADM_Type'] 

                for pointer in headers:
                    temp_dic[pointer] = {}
                    temp_dic[pointer].update(Temp_data[pointer])
                
                ProperDict = {}
                for Row in temp_dic["ID"].keys():
                    Node = temp_dic["Node"][Row]
                    Location = str(temp_dic["Location"][Row]).split(',')
                    Location = list(map(lambda x : float(x), Location))

                    ROADM_Type = temp_dic["ROADM_Type"][Row]

                    ProperDict[Node] = {"Location": Location, "ROADM_Type":ROADM_Type}

                Data["Nodes"].update(ProperDict)

                Temp_data = pd.read_excel(xls, 'Links')
                temp_dic ={}
                headers = ["ID", "Source", "Destination", "Distance", "Fiber Type", "Loss Coefficient", "Beta", "Gamma", "Dispersion"]
                
                for pointer in headers:
                    temp_dic[pointer] = {}
                    temp_dic[pointer].update(Temp_data[pointer])
                
                ProperDict = {}
                for Row in temp_dic["ID"].keys():
                    Source = temp_dic["Source"][Row]
                    Destination = temp_dic["Destination"][Row]
                    Distance = str(temp_dic["Distance"][Row]).split("+")
                    Distance = list(map(lambda x : float(x.strip()), Distance))

                    Fiber_Type = str(temp_dic["Fiber Type"][Row]).split("+")

                    Loss = str(temp_dic["Loss Coefficient"][Row]).split("+")
                    Loss = list(map(lambda x : float(x.strip()), Loss))

                    Beta = str(temp_dic["Beta"][Row]).split('+')
                    Beta = list(map(lambda x : float(x.strip()), Beta))

                    Gamma = str(temp_dic["Gamma"][Row]).split('+')
                    Gamma = list(map(lambda x : float(x.strip()), Gamma))

                    Dispersion = str(temp_dic["Dispersion"][Row]).split('+')
                    Dispersion = list(map(lambda x : float(x.strip()), Dispersion))

                    
                    # TODO: Some Data doesn't exist in Link Dictionary
                    ProperDict[(Source, Destination)] = {"NumSpan": len(Distance), "Length": Distance, "Loss":Loss, "Type":Fiber_Type, "Beta":Beta, "Gamma": Gamma,
                    "Dispersion": Dispersion}

                Data["Links"].update(ProperDict)

                PT_success = True
            except:
                PT_success = False
        
        else:
            PT_success = False

        return name, PT_success

    def import_TM_procedure(self):
        TMpath, TM_Success = Data["ui"].LoadTM_fun(bus["ImportMenuUI"])
        self.TrafficLineEdit.setText(TMpath[0])
        if TM_Success is True:
            self.SaveChangesBitton.setEnabled(True)
            self.TrafficButton.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"    font: 75 10pt \"Bahnschrift Condensed\";\n"
"    \n"
"    color: rgb(117, 117, 117);\n"
"    border: 2px solid #8f8f91; min-width: 80px;\n"
"    border-color: #4072B3; \n"
"    border-radius: 15px;\n"
"    background-color: green;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: green;\n"
"} \n"
"\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ImportMenuUI = QtWidgets.QWidget()
    ui = Ui_ImportMenuUI()
    ui.setupUi(ImportMenuUI)
    ImportMenuUI.show()
    sys.exit(app.exec_())

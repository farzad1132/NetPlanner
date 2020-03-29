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
        bus["ImportMenuUI"] = ImportMenuUI
        ImportMenuUI.setObjectName("ImportMenuUI")
        ImportMenuUI.resize(459, 319)
        self.gridLayout = QtWidgets.QGridLayout(ImportMenuUI)
        self.gridLayout.setObjectName("gridLayout")
        self.PlanningLabel = QtWidgets.QLabel(ImportMenuUI)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.PlanningLabel.setFont(font)
        self.PlanningLabel.setStyleSheet(" QLabel {\n"
"    border: 2px solid green;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}")
        self.PlanningLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.PlanningLabel.setObjectName("PlanningLabel")
        self.gridLayout.addWidget(self.PlanningLabel, 0, 0, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.NodeLineEdit = QtWidgets.QLineEdit(ImportMenuUI)
        self.NodeLineEdit.setObjectName("NodeLineEdit")
        self.horizontalLayout.addWidget(self.NodeLineEdit)
        self.NodeButton = QtWidgets.QPushButton(ImportMenuUI)
        self.NodeButton.setMaximumSize(QtCore.QSize(999, 999))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.NodeButton.setFont(font)
        self.NodeButton.setStyleSheet("QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    min-width: 80px;\n"
"    border-color: dark-orange;\n"
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
        self.NodeButton.setObjectName("NodeButton")
        self.horizontalLayout.addWidget(self.NodeButton)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.LinkLineEdit = QtWidgets.QLineEdit(ImportMenuUI)
        self.LinkLineEdit.setObjectName("LinkLineEdit")
        self.horizontalLayout_3.addWidget(self.LinkLineEdit)
        self.LinkButton = QtWidgets.QPushButton(ImportMenuUI)
        self.LinkButton.setMaximumSize(QtCore.QSize(999, 999))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.LinkButton.setFont(font)
        self.LinkButton.setStyleSheet("QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    min-width: 80px;\n"
"    border-color: dark-orange;\n"
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
        self.LinkButton.setObjectName("LinkButton")
        self.horizontalLayout_3.addWidget(self.LinkButton)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 2)
        self.line_2 = QtWidgets.QFrame(ImportMenuUI)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 3, 0, 1, 2)
        self.label = QtWidgets.QLabel(ImportMenuUI)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(" QLabel {\n"
"    border: 2px solid green;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 4, 0, 2, 2)
        self.line = QtWidgets.QFrame(ImportMenuUI)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 5, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.TrafficLineEdit = QtWidgets.QLineEdit(ImportMenuUI)
        self.TrafficLineEdit.setObjectName("TrafficLineEdit")
        self.horizontalLayout_2.addWidget(self.TrafficLineEdit)
        self.TrafficButton = QtWidgets.QPushButton(ImportMenuUI)
        self.TrafficButton.setMaximumSize(QtCore.QSize(999, 999))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.TrafficButton.setFont(font)
        self.TrafficButton.setStyleSheet("QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    min-width: 80px;\n"
"    border-color: dark-orange;\n"
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
        self.TrafficButton.setObjectName("TrafficButton")
        self.horizontalLayout_2.addWidget(self.TrafficButton)
        self.gridLayout.addLayout(self.horizontalLayout_2, 6, 0, 1, 2)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.SaveChangesBitton = QtWidgets.QPushButton(ImportMenuUI)
        self.SaveChangesBitton.setMaximumSize(QtCore.QSize(165, 100))
        font = QtGui.QFont()
        #font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.SaveChangesBitton.setFont(font)
        self.SaveChangesBitton.setStyleSheet("QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: #8ADBB5;\n"
"    min-width: 80px;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: dark-orange;\n"
"    font: bold 14px;\n"
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
        self.SaveChangesBitton.setObjectName("SaveChangesBitton")
        self.gridLayout_2.addWidget(self.SaveChangesBitton, 0, 1, 1, 1)
        self.DrawButton = QtWidgets.QPushButton(ImportMenuUI)
        self.DrawButton.setMaximumSize(QtCore.QSize(165, 100))
        font = QtGui.QFont()
        #font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.DrawButton.setFont(font)
        self.DrawButton.setStyleSheet("QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: #8ADBB5;\n"
"    min-width: 80px;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: dark-orange;\n"
"    font: bold 14px;\n"
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
        self.DrawButton.setObjectName("DrawButton")
        self.gridLayout_2.addWidget(self.DrawButton, 0, 2, 1, 1)
        self.CloseButton = QtWidgets.QPushButton(ImportMenuUI)
        self.CloseButton.setMaximumSize(QtCore.QSize(165, 100))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.CloseButton.setFont(font)
        self.CloseButton.setStyleSheet("QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    min-width: 80px;\n"
"    border-color: dark-orange;\n"
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
        self.CloseButton.setObjectName("CloseButton")
        self.gridLayout_2.addWidget(self.CloseButton, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 7, 0, 1, 2)

        self.retranslateUi(ImportMenuUI)
        QtCore.QMetaObject.connectSlotsByName(ImportMenuUI)

        # NOTE: added
        self.CloseButton.clicked.connect(ImportMenuUI.close)
        self.NodeButton.clicked.connect(self.node_import_procedure)
        self.LinkButton.clicked.connect(self.link_import_procedure)
        self.TrafficButton.clicked.connect(self.import_TM_procedure)
        self.SaveChangesBitton.clicked.connect(self.call_savechange)
        self.DrawButton.clicked.connect(self.call_insert_links)

    def retranslateUi(self, ImportMenuUI):
        _translate = QtCore.QCoreApplication.translate
        ImportMenuUI.setWindowTitle(_translate("ImportMenuUI", "ImportMenuUI"))
        self.PlanningLabel.setText(_translate("ImportMenuUI", "Import Physical Topology"))
        self.NodeButton.setText(_translate("ImportMenuUI", "Nodes"))
        self.LinkButton.setText(_translate("ImportMenuUI", "Links"))
        self.label.setText(_translate("ImportMenuUI", "Import Traffic Matrix "))
        self.TrafficButton.setText(_translate("ImportMenuUI", "Traffic Matrix"))
        self.SaveChangesBitton.setText(_translate("ImportMenuUI", "Save Changes"))
        self.DrawButton.setText(_translate("ImportMenuUI", "Draw"))
        self.CloseButton.setText(_translate("ImportMenuUI", "Close"))

    
    def call_savechange(self):
        Data["ui"].SaveChanges_button_fun()
    
    def call_insert_links(self):
        Data["ui"].insert_link_fun()
        bus["ImportMenuUI"].close()
    
    def node_import_procedure(self):

        nodepath, Node_Success = self.import_nodes_fun()
        self.NodeLineEdit.setText(nodepath[0])
        if Node_Success is True:
            self.NodeButton.setStyleSheet("QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: green;\n"
"    min-width: 80px;\n"
"    border-color: dark-orange;\n"
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

    def link_import_procedure(self):
        linkpath, Link_Success = self.import_links_fun()
        self.LinkLineEdit.setText(linkpath[0])
        if Link_Success is True:
            self.LinkButton.setStyleSheet("QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: green;\n"
"    min-width: 80px;\n"
"    border-color: dark-orange;\n"
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

    def import_TM_procedure(self):
        TMpath, TM_Success = self.LoadTM_fun()
        self.TrafficLineEdit.setText(TMpath[0])
        if TM_Success is True:
            self.TrafficButton.setStyleSheet("QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: green;\n"
"    min-width: 80px;\n"
"    border-color: dark-orange;\n"
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


    def import_nodes_fun(self):
        # this method imports Nodes Information
        name = QFileDialog.getOpenFileName(bus["ImportMenuUI"], "Open Topology")

        if name[0] != 0 and name[0] != "":
            with pd.ExcelFile(name[0]) as handle:
                Temp_data = handle.parse(header=0, skipfooter=0)
            temp_dic ={}
            handle.close() 
            headers = ['ID','Node','Location','ROADM_Type'] 

            for pointer in headers:
                temp_dic[pointer] = {}
                temp_dic[pointer].update(Temp_data[pointer])
            
            ProperDict = {}
            for Row in temp_dic["ID"].keys():
                Id = temp_dic["ID"][Row]
                Node = temp_dic["Node"][Row]
                Location = str(temp_dic["Location"][Row]).split(',')
                Location = list(map(lambda x : float(x), Location))

                ROADM_Type = temp_dic["ROADM_Type"][Row]

                ProperDict[Id] = {"Node": Node, "Location": Location, "ROADM_Type":ROADM_Type}

            Data["Nodes"].update(ProperDict)
            Node_success = True
        
        else:
            Node_success = False

        return name, Node_success
    
    def import_links_fun(self):
        name = QFileDialog.getOpenFileName(bus["ImportMenuUI"], "Open Topology")
        

        if name[0] != 0 and name[0] != "":
            with pd.ExcelFile(name[0]) as handle:
                Temp_data = handle.parse(header=0, skipfooter=0)
            temp_dic ={}
            handle.close()
            headers = ["ID", "Source", "Destination", "Distance", "Fiber Type", "Loss Coefficient", "Beta", "Gamma", "Dispersion"]
            
            for pointer in headers:
                temp_dic[pointer] = {}
                temp_dic[pointer].update(Temp_data[pointer])
            
            ProperDict = {}
            for Row in temp_dic["ID"].keys():
                id = temp_dic["ID"][Row]
                Source = temp_dic["Source"][Row]
                Destination = temp_dic["Destination"][Row]
                Distance = str(temp_dic["Distance"][Row]).split("+")
                Distance = list(map(lambda x : float(x), Distance))

                Fiber_Type = str(temp_dic["Fiber Type"][Row]).split("+")

                Loss = str(temp_dic["Loss Coefficient"][Row]).split("+")
                Loss = list(map(lambda x : float(x), Loss))

                Beta = str(temp_dic["Beta"][Row]).split('+')
                Beta = list(map(lambda x : float(x), Beta))

                Gamma = str(temp_dic["Gamma"][Row]).split('+')
                Gamma = list(map(lambda x : float(x), Gamma))

                Dispersion = str(temp_dic["Dispersion"][Row]).split('+')
                Dispersion = list(map(lambda x : float(x), Dispersion))

                
                # TODO: Some Data doesn't exist in Link Dictionary
                ProperDict[(Source, Destination)] = {"NumSpan": len(Distance), "Length": Distance, "Loss":Loss, "Type":Fiber_Type, "Beta":Beta, "Gamma": Gamma,
                "Dispersion": Dispersion}

            Data["Links"].update(ProperDict)
            Link_Success = True
        
        else:
            Link_Success = False

        return name, Link_Success
    
    def LoadTM_fun(self):
        name = QFileDialog.getOpenFileName(bus["ImportMenuUI"], "Load Traffic Matrix")

        if name[0] != 0 and name[0] != "":
            with pd.ExcelFile(name[0]) as handle:
                Temp_data = handle.parse(header=1, skipfooter=0)

            handle.close()
            header_list = ['ID', 'Source', 'Destination', 'Old\nCable\nType', 'Cable\nType', 'Distance\nReal\n(Km)',
                           'Att. (dB/km)\nfor Network Plan\n(Option 1 or 2)', 'Status',"Degree"]

            j = -1
            for i in header_list:
                dict1 = {}
                j += 1
                dict1.update(Temp_data[i])
                Data["General"]["DataSection"][str(j)].update(dict1)
                #print(Data["General"]["DataSection"][str(j)])
                for keys in list(Data["General"]["DataSection"][str(j)].keys()):
                    text = str(Data["General"]["DataSection"][str(j)][keys])
                    if text == "nan":
                        Data["General"]["DataSection"][str(j)].pop(keys)
                    else:
                        Data["General"]["DataSection"][str(j)][keys] = text
            Data["ui"].update_cells()
            header_list2 = [['Quantity_E1', 'SLA_E1'], ['Quantity_STM1_E', 'SLA_STM1_E'],
                            ['Quantity_STM1_O', 'λ_STM1_O(nm)', 'SLA_STM1_O'],
                            ['Quantity_STM4', 'λ_STM4(nm)', 'Concat._STM4', 'SLA_STM4'],
                            ['Quantity_STM16', 'λ_STM16(nm)', 'Concat._STM16', 'SLA_STM16'],
                            ['Quantity_STM64', 'λ_STM64(nm)', 'Concat._STM64', 'SLA_STM64'],
                            ['Quantity_FE', "GranularityxVC12", "GranularityxVC4", 'λ_FE(nm)', 'SLA_FE'],
                            ['Quantity_GE', 'Granularity_GE', 'λ_GE(nm)', 'SLA_GE'],
                            ['Quantity_10GE', 'Granularity_10GE', 'λ_10GE(nm)', 'SLA_10GE'],
                            ['Quantity_40GE', 'Granularity_40GE', 'λ_40GE(nm)', 'SLA_40GE'],
                            ['Quantity_100GE', 'Granularity_100GE', 'λ_100GE(nm)', 'SLA_100GE']]
            self.all_headers = ["E1", "STM_1_Electrical", "STM_1_Optical", "STM_4", "STM_16", "STM_64", "FE", "1GE", "10GE",
                           "40GE", "100GE"]
            l1 = [["Quantity", "SLA"], ["Quantity", "SLA"], ["Quantity", "λ", "SLA"],
                  ["Quantity", "λ", "concat.", "SLA"], ["Quantity", "λ", "concat.", "SLA"],
                  ["Quantity", "λ", "concat.", "SLA"],
                  ["Quantity", "Granularity_xVC12", "Granularity_xVC4", "λ", "SLA"],
                  ["Quantity", "Granularity", "λ", "SLA"], ["Quantity", "Granularity", "λ", "SLA"],
                  ["Quantity", "Granularity", "λ", "SLA"], ["Quantity", "Granularity", "λ", "SLA"]]
            k = -1
            for m in self.all_headers:
                k += 1
                for j in range(len(header_list2[k])):
                    dict1 = {}
                    dict1.update(Temp_data[header_list2[k][j]])
                    Data[m]["DataSection"][l1[k][j]].update(dict1)
                    #print(Data[m]["DataSection"][l1[k][j]])
                    for keys in list(Data[m]["DataSection"][l1[k][j]].keys()):
                        text = str(Data[m]["DataSection"][l1[k][j]][keys])
                        if  text == "nan":
                            Data[m]["DataSection"][l1[k][j]].pop(keys)
                        else:
                            Data[m]["DataSection"][l1[k][j]][keys] = text
            
            TM_Success = True
        
        else:
            TM_Success = False

        return name, TM_Success


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ImportMenuUI = QtWidgets.QWidget()
    ui = Ui_ImportMenuUI()
    ui.setupUi(ImportMenuUI)
    ImportMenuUI.show()
    sys.exit(app.exec_())

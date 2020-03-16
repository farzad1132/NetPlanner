from PySide2 import QtWidgets, QtGui, QtCore
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import sys
import os
from data import *
from Common_Object_def import Network
bus = {}


class Ui_RWA_Window(object):
    def setupUi(self, RWA_Window):
        RWA_Window.setObjectName("RWA_Window")

        # NOTE: added
        bus["RWA_Window"] = RWA_Window

        RWA_Window.resize(493, 462)
        self.gridLayout = QtWidgets.QGridLayout(RWA_Window)
        self.gridLayout.setObjectName("gridLayout")
        self.RW_toolBox = QtWidgets.QToolBox(RWA_Window)
        self.RW_toolBox.setStyleSheet("QToolBox::tab {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"    border-radius: 5px;\n"
"    color: gray;\n"
"}\n"
"\n"
"QToolBox::tab:selected {\n"
"    font: 75 8pt \"MS Shell Dlg 2\";\n"
"    color: red;\n"
"    background-color: rgb(170, 255, 127);\n"
"}\n"
"\n"
"QToolBox::tab:only-one{\n"
"}")
        self.RW_toolBox.setObjectName("RW_toolBox")
        self.Greedy = QtWidgets.QWidget()
        self.Greedy.setGeometry(QtCore.QRect(0, 0, 471, 305))
        self.Greedy.setObjectName("Greedy")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.Greedy)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.mergindemands_gridlayout_3 = QtWidgets.QGridLayout()
        self.mergindemands_gridlayout_3.setObjectName("mergindemands_gridlayout_3")
        self.Mergin_DemandRe_Label = QtWidgets.QLabel(self.Greedy)
        font = QtGui.QFont()
        font.setFamily("IRANSans")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.Mergin_DemandRe_Label.setFont(font)
        self.Mergin_DemandRe_Label.setStyleSheet(" QLabel {\n"
"    border: 2px solid green;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}")
        self.Mergin_DemandRe_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Mergin_DemandRe_Label.setObjectName("Mergin_DemandRe_Label")
        self.mergindemands_gridlayout_3.addWidget(self.Mergin_DemandRe_Label, 0, 0, 1, 1)
        self.Mergin_DemandRe_LineEdit = QtWidgets.QComboBox(self.Greedy)
        self.Mergin_DemandRe_LineEdit.setStyleSheet("")
        self.Mergin_DemandRe_LineEdit.setEditable(False)
        self.Mergin_DemandRe_LineEdit.setObjectName("Mergin_DemandRe_LineEdit")
        self.Mergin_DemandRe_LineEdit.addItem("")
        self.Mergin_DemandRe_LineEdit.addItem("")
        self.mergindemands_gridlayout_3.addWidget(self.Mergin_DemandRe_LineEdit, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.mergindemands_gridlayout_3, 0, 0, 1, 1)
        self.RWA_WindowLayout_13 = QtWidgets.QRWA_WindowLayout()
        self.RWA_WindowLayout_13.setObjectName("RWA_WindowLayout_13")
        self.Greedy_Alpha_Label = QtWidgets.QLabel(self.Greedy)
        font = QtGui.QFont()
        font.setFamily("IRANSans")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.Greedy_Alpha_Label.setFont(font)
        self.Greedy_Alpha_Label.setStyleSheet(" QLabel {\n"
"    border: 2px solid green;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}")
        self.Greedy_Alpha_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Greedy_Alpha_Label.setObjectName("Greedy_Alpha_Label")
        self.RWA_WindowLayout_13.setWidget(0, QtWidgets.QRWA_WindowLayout.LabelRole, self.Greedy_Alpha_Label)
        self.Greedy_Alpha_LineEdit = QtWidgets.QLineEdit(self.Greedy)
        self.Greedy_Alpha_LineEdit.setStyleSheet(" QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.Greedy_Alpha_LineEdit.setText("")
        self.Greedy_Alpha_LineEdit.setObjectName("Greedy_Alpha_LineEdit")
        self.RWA_WindowLayout_13.setWidget(1, QtWidgets.QRWA_WindowLayout.LabelRole, self.Greedy_Alpha_LineEdit)
        self.gridLayout_4.addLayout(self.RWA_WindowLayout_13, 1, 0, 1, 1)
        self.RWA_WindowLayout_14 = QtWidgets.QRWA_WindowLayout()
        self.RWA_WindowLayout_14.setObjectName("RWA_WindowLayout_14")
        self.Greedy_Iteration_Label = QtWidgets.QLabel(self.Greedy)
        font = QtGui.QFont()
        font.setFamily("IRANSans")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.Greedy_Iteration_Label.setFont(font)
        self.Greedy_Iteration_Label.setStyleSheet(" QLabel {\n"
"    border: 2px solid green;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}")
        self.Greedy_Iteration_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Greedy_Iteration_Label.setObjectName("Greedy_Iteration_Label")
        self.RWA_WindowLayout_14.setWidget(0, QtWidgets.QRWA_WindowLayout.LabelRole, self.Greedy_Iteration_Label)
        self.Greedy_Iteration_LineEdit = QtWidgets.QLineEdit(self.Greedy)
        self.Greedy_Iteration_LineEdit.setStyleSheet("\n"
" QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.Greedy_Iteration_LineEdit.setText("")
        self.Greedy_Iteration_LineEdit.setObjectName("Greedy_Iteration_LineEdit")
        self.RWA_WindowLayout_14.setWidget(1, QtWidgets.QRWA_WindowLayout.LabelRole, self.Greedy_Iteration_LineEdit)
        self.gridLayout_4.addLayout(self.RWA_WindowLayout_14, 1, 1, 1, 1)
        self.RWA_WindowLayout_15 = QtWidgets.QRWA_WindowLayout()
        self.RWA_WindowLayout_15.setObjectName("RWA_WindowLayout_15")
        self.Greedy_Margin_Label = QtWidgets.QLabel(self.Greedy)
        font = QtGui.QFont()
        font.setFamily("IRANSans")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.Greedy_Margin_Label.setFont(font)
        self.Greedy_Margin_Label.setStyleSheet(" QLabel {\n"
"    border: 2px solid green;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}")
        self.Greedy_Margin_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Greedy_Margin_Label.setObjectName("Greedy_Margin_Label")
        self.RWA_WindowLayout_15.setWidget(0, QtWidgets.QRWA_WindowLayout.LabelRole, self.Greedy_Margin_Label)
        self.Greedy_Margin_LineEdit = QtWidgets.QLineEdit(self.Greedy)
        self.Greedy_Margin_LineEdit.setStyleSheet("\n"
" QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.Greedy_Margin_LineEdit.setText("")
        self.Greedy_Margin_LineEdit.setObjectName("Greedy_Margin_LineEdit")
        self.RWA_WindowLayout_15.setWidget(1, QtWidgets.QRWA_WindowLayout.LabelRole, self.Greedy_Margin_LineEdit)
        self.gridLayout_4.addLayout(self.RWA_WindowLayout_15, 2, 0, 1, 1)
        self.RWA_WindowLayout_16 = QtWidgets.QRWA_WindowLayout()
        self.RWA_WindowLayout_16.setObjectName("RWA_WindowLayout_16")
        self.Greedy_Processors_Label = QtWidgets.QLabel(self.Greedy)
        font = QtGui.QFont()
        font.setFamily("IRANSans")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.Greedy_Processors_Label.setFont(font)
        self.Greedy_Processors_Label.setStyleSheet(" QLabel {\n"
"    border: 2px solid green;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}")
        self.Greedy_Processors_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Greedy_Processors_Label.setObjectName("Greedy_Processors_Label")
        self.RWA_WindowLayout_16.setWidget(0, QtWidgets.QRWA_WindowLayout.LabelRole, self.Greedy_Processors_Label)
        self.Greedy_Processors_LineEdit = QtWidgets.QLineEdit(self.Greedy)
        self.Greedy_Processors_LineEdit.setStyleSheet("\n"
" QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.Greedy_Processors_LineEdit.setText("")
        self.Greedy_Processors_LineEdit.setObjectName("Greedy_Processors_LineEdit")
        self.RWA_WindowLayout_16.setWidget(1, QtWidgets.QRWA_WindowLayout.LabelRole, self.Greedy_Processors_LineEdit)
        self.gridLayout_4.addLayout(self.RWA_WindowLayout_16, 2, 1, 1, 1)
        self.RWA_WindowLayout_17 = QtWidgets.QRWA_WindowLayout()
        self.RWA_WindowLayout_17.setObjectName("RWA_WindowLayout_17")
        self.Greedy_K_Label = QtWidgets.QLabel(self.Greedy)
        font = QtGui.QFont()
        font.setFamily("IRANSans")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.Greedy_K_Label.setFont(font)
        self.Greedy_K_Label.setStyleSheet(" QLabel {\n"
"    border: 2px solid green;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}")
        self.Greedy_K_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Greedy_K_Label.setObjectName("Greedy_K_Label")
        self.RWA_WindowLayout_17.setWidget(0, QtWidgets.QRWA_WindowLayout.LabelRole, self.Greedy_K_Label)
        self.Greedy_K_LineEdit = QtWidgets.QLineEdit(self.Greedy)
        self.Greedy_K_LineEdit.setStyleSheet("\n"
" QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.Greedy_K_LineEdit.setText("")
        self.Greedy_K_LineEdit.setObjectName("Greedy_K_LineEdit")
        self.RWA_WindowLayout_17.setWidget(1, QtWidgets.QRWA_WindowLayout.LabelRole, self.Greedy_K_LineEdit)
        self.gridLayout_4.addLayout(self.RWA_WindowLayout_17, 3, 0, 1, 1)
        self.RWA_WindowLayout_18 = QtWidgets.QRWA_WindowLayout()
        self.RWA_WindowLayout_18.setObjectName("RWA_WindowLayout_18")
        self.Greedy_MaxNW_LineEdit = QtWidgets.QLineEdit(self.Greedy)
        self.Greedy_MaxNW_LineEdit.setStyleSheet(" QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.Greedy_MaxNW_LineEdit.setText("")
        self.Greedy_MaxNW_LineEdit.setObjectName("Greedy_MaxNW_LineEdit")
        self.RWA_WindowLayout_18.setWidget(1, QtWidgets.QRWA_WindowLayout.LabelRole, self.Greedy_MaxNW_LineEdit)
        self.Greedy_MaxNW_Label = QtWidgets.QLabel(self.Greedy)
        font = QtGui.QFont()
        font.setFamily("IRANSans")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.Greedy_MaxNW_Label.setFont(font)
        self.Greedy_MaxNW_Label.setStyleSheet(" QLabel {\n"
"    border: 2px solid green;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}")
        self.Greedy_MaxNW_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Greedy_MaxNW_Label.setObjectName("Greedy_MaxNW_Label")
        self.RWA_WindowLayout_18.setWidget(0, QtWidgets.QRWA_WindowLayout.LabelRole, self.Greedy_MaxNW_Label)
        self.gridLayout_4.addLayout(self.RWA_WindowLayout_18, 3, 1, 1, 1)
        self.RW_toolBox.addItem(self.Greedy, "")
        self.Group_ILP = QtWidgets.QWidget()
        self.Group_ILP.setGeometry(QtCore.QRect(0, 0, 471, 305))
        self.Group_ILP.setObjectName("Group_ILP")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Group_ILP)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.RWA_WindowLayout_19 = QtWidgets.QRWA_WindowLayout()
        self.RWA_WindowLayout_19.setObjectName("RWA_WindowLayout_19")
        self.GroupILP_Alpha_Label = QtWidgets.QLabel(self.Group_ILP)
        font = QtGui.QFont()
        font.setFamily("IRANSans")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.GroupILP_Alpha_Label.setFont(font)
        self.GroupILP_Alpha_Label.setStyleSheet(" QLabel {\n"
"    border: 2px solid green;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}")
        self.GroupILP_Alpha_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.GroupILP_Alpha_Label.setObjectName("GroupILP_Alpha_Label")
        self.RWA_WindowLayout_19.setWidget(0, QtWidgets.QRWA_WindowLayout.LabelRole, self.GroupILP_Alpha_Label)
        self.GroupILP_Alpha_LineEdit = QtWidgets.QLineEdit(self.Group_ILP)
        self.GroupILP_Alpha_LineEdit.setStyleSheet(" QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.GroupILP_Alpha_LineEdit.setText("")
        self.GroupILP_Alpha_LineEdit.setObjectName("GroupILP_Alpha_LineEdit")
        self.RWA_WindowLayout_19.setWidget(1, QtWidgets.QRWA_WindowLayout.LabelRole, self.GroupILP_Alpha_LineEdit)
        self.gridLayout_2.addLayout(self.RWA_WindowLayout_19, 0, 0, 1, 1)
        self.RWA_WindowLayout_20 = QtWidgets.QRWA_WindowLayout()
        self.RWA_WindowLayout_20.setObjectName("RWA_WindowLayout_20")
        self.GroupILP_Iteration_Label = QtWidgets.QLabel(self.Group_ILP)
        font = QtGui.QFont()
        font.setFamily("IRANSans")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.GroupILP_Iteration_Label.setFont(font)
        self.GroupILP_Iteration_Label.setStyleSheet(" QLabel {\n"
"    border: 2px solid green;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}")
        self.GroupILP_Iteration_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.GroupILP_Iteration_Label.setObjectName("GroupILP_Iteration_Label")
        self.RWA_WindowLayout_20.setWidget(0, QtWidgets.QRWA_WindowLayout.LabelRole, self.GroupILP_Iteration_Label)
        self.GroupILP_Iteration_LineEdit = QtWidgets.QLineEdit(self.Group_ILP)
        self.GroupILP_Iteration_LineEdit.setStyleSheet(" QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.GroupILP_Iteration_LineEdit.setText("")
        self.GroupILP_Iteration_LineEdit.setObjectName("GroupILP_Iteration_LineEdit")
        self.RWA_WindowLayout_20.setWidget(1, QtWidgets.QRWA_WindowLayout.LabelRole, self.GroupILP_Iteration_LineEdit)
        self.gridLayout_2.addLayout(self.RWA_WindowLayout_20, 0, 1, 1, 1)
        self.RWA_WindowLayout_21 = QtWidgets.QRWA_WindowLayout()
        self.RWA_WindowLayout_21.setObjectName("RWA_WindowLayout_21")
        self.GroupILP_Margin_Label = QtWidgets.QLabel(self.Group_ILP)
        font = QtGui.QFont()
        font.setFamily("IRANSans")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.GroupILP_Margin_Label.setFont(font)
        self.GroupILP_Margin_Label.setStyleSheet(" QLabel {\n"
"    border: 2px solid green;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}")
        self.GroupILP_Margin_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.GroupILP_Margin_Label.setObjectName("GroupILP_Margin_Label")
        self.RWA_WindowLayout_21.setWidget(0, QtWidgets.QRWA_WindowLayout.LabelRole, self.GroupILP_Margin_Label)
        self.GroupILP_Margin_LineEdit = QtWidgets.QLineEdit(self.Group_ILP)
        self.GroupILP_Margin_LineEdit.setStyleSheet(" QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.GroupILP_Margin_LineEdit.setText("")
        self.GroupILP_Margin_LineEdit.setObjectName("GroupILP_Margin_LineEdit")
        self.RWA_WindowLayout_21.setWidget(1, QtWidgets.QRWA_WindowLayout.LabelRole, self.GroupILP_Margin_LineEdit)
        self.gridLayout_2.addLayout(self.RWA_WindowLayout_21, 1, 0, 1, 1)
        self.RWA_WindowLayout_22 = QtWidgets.QRWA_WindowLayout()
        self.RWA_WindowLayout_22.setObjectName("RWA_WindowLayout_22")
        self.GroupILP_Processors_Label = QtWidgets.QLabel(self.Group_ILP)
        font = QtGui.QFont()
        font.setFamily("IRANSans")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.GroupILP_Processors_Label.setFont(font)
        self.GroupILP_Processors_Label.setStyleSheet(" QLabel {\n"
"    border: 2px solid green;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}")
        self.GroupILP_Processors_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.GroupILP_Processors_Label.setObjectName("GroupILP_Processors_Label")
        self.RWA_WindowLayout_22.setWidget(0, QtWidgets.QRWA_WindowLayout.LabelRole, self.GroupILP_Processors_Label)
        self.GroupILP_Processors_LineEdit = QtWidgets.QLineEdit(self.Group_ILP)
        self.GroupILP_Processors_LineEdit.setStyleSheet(" QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.GroupILP_Processors_LineEdit.setText("")
        self.GroupILP_Processors_LineEdit.setObjectName("GroupILP_Processors_LineEdit")
        self.RWA_WindowLayout_22.setWidget(1, QtWidgets.QRWA_WindowLayout.LabelRole, self.GroupILP_Processors_LineEdit)
        self.gridLayout_2.addLayout(self.RWA_WindowLayout_22, 1, 1, 1, 1)
        self.RWA_WindowLayout_23 = QtWidgets.QRWA_WindowLayout()
        self.RWA_WindowLayout_23.setObjectName("RWA_WindowLayout_23")
        self.GroupILP_K_Label = QtWidgets.QLabel(self.Group_ILP)
        font = QtGui.QFont()
        font.setFamily("IRANSans")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.GroupILP_K_Label.setFont(font)
        self.GroupILP_K_Label.setStyleSheet(" QLabel {\n"
"    border: 2px solid green;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}")
        self.GroupILP_K_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.GroupILP_K_Label.setObjectName("GroupILP_K_Label")
        self.RWA_WindowLayout_23.setWidget(0, QtWidgets.QRWA_WindowLayout.LabelRole, self.GroupILP_K_Label)
        self.GroupILP_K_LineEdit = QtWidgets.QLineEdit(self.Group_ILP)
        self.GroupILP_K_LineEdit.setStyleSheet(" QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.GroupILP_K_LineEdit.setText("")
        self.GroupILP_K_LineEdit.setObjectName("GroupILP_K_LineEdit")
        self.RWA_WindowLayout_23.setWidget(1, QtWidgets.QRWA_WindowLayout.LabelRole, self.GroupILP_K_LineEdit)
        self.gridLayout_2.addLayout(self.RWA_WindowLayout_23, 2, 0, 1, 1)
        self.RWA_WindowLayout_24 = QtWidgets.QRWA_WindowLayout()
        self.RWA_WindowLayout_24.setObjectName("RWA_WindowLayout_24")
        self.GroupILP_MaxNW_Label = QtWidgets.QLabel(self.Group_ILP)
        font = QtGui.QFont()
        font.setFamily("IRANSans")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.GroupILP_MaxNW_Label.setFont(font)
        self.GroupILP_MaxNW_Label.setStyleSheet(" QLabel {\n"
"    border: 2px solid green;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}")
        self.GroupILP_MaxNW_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.GroupILP_MaxNW_Label.setObjectName("GroupILP_MaxNW_Label")
        self.RWA_WindowLayout_24.setWidget(0, QtWidgets.QRWA_WindowLayout.LabelRole, self.GroupILP_MaxNW_Label)
        self.GroupILP_MaxNW_LineEdit = QtWidgets.QLineEdit(self.Group_ILP)
        self.GroupILP_MaxNW_LineEdit.setStyleSheet(" QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.GroupILP_MaxNW_LineEdit.setText("")
        self.GroupILP_MaxNW_LineEdit.setObjectName("GroupILP_MaxNW_LineEdit")
        self.RWA_WindowLayout_24.setWidget(1, QtWidgets.QRWA_WindowLayout.LabelRole, self.GroupILP_MaxNW_LineEdit)
        self.gridLayout_2.addLayout(self.RWA_WindowLayout_24, 2, 1, 1, 1)
        self.RWA_WindowLayout_25 = QtWidgets.QRWA_WindowLayout()
        self.RWA_WindowLayout_25.setObjectName("RWA_WindowLayout_25")
        self.GroupILP_Groupsize_Label = QtWidgets.QLabel(self.Group_ILP)
        font = QtGui.QFont()
        font.setFamily("IRANSans")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.GroupILP_Groupsize_Label.setFont(font)
        self.GroupILP_Groupsize_Label.setStyleSheet(" QLabel {\n"
"    border: 2px solid green;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}")
        self.GroupILP_Groupsize_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.GroupILP_Groupsize_Label.setObjectName("GroupILP_Groupsize_Label")
        self.RWA_WindowLayout_25.setWidget(0, QtWidgets.QRWA_WindowLayout.LabelRole, self.GroupILP_Groupsize_Label)
        self.GroupILP_Groupsize_LineEdit = QtWidgets.QLineEdit(self.Group_ILP)
        self.GroupILP_Groupsize_LineEdit.setStyleSheet(" QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.GroupILP_Groupsize_LineEdit.setText("")
        self.GroupILP_Groupsize_LineEdit.setObjectName("GroupILP_Groupsize_LineEdit")
        self.RWA_WindowLayout_25.setWidget(1, QtWidgets.QRWA_WindowLayout.LabelRole, self.GroupILP_Groupsize_LineEdit)
        self.gridLayout_2.addLayout(self.RWA_WindowLayout_25, 3, 0, 1, 1)
        self.RWA_WindowLayout_26 = QtWidgets.QRWA_WindowLayout()
        self.RWA_WindowLayout_26.setObjectName("RWA_WindowLayout_26")
        self.GroupILP_History_LineEdit = QtWidgets.QLineEdit(self.Group_ILP)
        self.GroupILP_History_LineEdit.setStyleSheet(" QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.GroupILP_History_LineEdit.setText("")
        self.GroupILP_History_LineEdit.setObjectName("GroupILP_History_LineEdit")
        self.RWA_WindowLayout_26.setWidget(1, QtWidgets.QRWA_WindowLayout.LabelRole, self.GroupILP_History_LineEdit)
        self.GroupILP_History_Label = QtWidgets.QLabel(self.Group_ILP)
        font = QtGui.QFont()
        font.setFamily("IRANSans")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.GroupILP_History_Label.setFont(font)
        self.GroupILP_History_Label.setStyleSheet(" QLabel {\n"
"    border: 2px solid green;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}")
        self.GroupILP_History_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.GroupILP_History_Label.setObjectName("GroupILP_History_Label")
        self.RWA_WindowLayout_26.setWidget(0, QtWidgets.QRWA_WindowLayout.LabelRole, self.GroupILP_History_Label)
        self.gridLayout_2.addLayout(self.RWA_WindowLayout_26, 3, 1, 1, 1)
        self.RW_toolBox.addItem(self.Group_ILP, "")
        self.ILP = QtWidgets.QWidget()
        self.ILP.setGeometry(QtCore.QRect(0, 0, 471, 305))
        self.ILP.setObjectName("ILP")
        self.RWA_WindowLayout = QtWidgets.QRWA_WindowLayout(self.ILP)
        self.RWA_WindowLayout.setObjectName("RWA_WindowLayout")
        self.RWA_WindowLayout_28 = QtWidgets.QRWA_WindowLayout()
        self.RWA_WindowLayout_28.setObjectName("RWA_WindowLayout_28")
        self.ILP_Margin_Label = QtWidgets.QLabel(self.ILP)
        font = QtGui.QFont()
        font.setFamily("IRANSans")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.ILP_Margin_Label.setFont(font)
        self.ILP_Margin_Label.setStyleSheet(" QLabel {\n"
"    border: 2px solid green;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}")
        self.ILP_Margin_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.ILP_Margin_Label.setObjectName("ILP_Margin_Label")
        self.RWA_WindowLayout_28.setWidget(0, QtWidgets.QRWA_WindowLayout.LabelRole, self.ILP_Margin_Label)
        self.ILP_Margin_LineEdit = QtWidgets.QLineEdit(self.ILP)
        self.ILP_Margin_LineEdit.setStyleSheet(" QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.ILP_Margin_LineEdit.setText("")
        self.ILP_Margin_LineEdit.setObjectName("ILP_Margin_LineEdit")
        self.RWA_WindowLayout_28.setWidget(1, QtWidgets.QRWA_WindowLayout.LabelRole, self.ILP_Margin_LineEdit)
        self.RWA_WindowLayout.setLayout(0, QtWidgets.QRWA_WindowLayout.LabelRole, self.RWA_WindowLayout_28)
        self.RWA_WindowLayout_29 = QtWidgets.QRWA_WindowLayout()
        self.RWA_WindowLayout_29.setObjectName("RWA_WindowLayout_29")
        self.ILP_Processors_Label = QtWidgets.QLabel(self.ILP)
        font = QtGui.QFont()
        font.setFamily("IRANSans")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.ILP_Processors_Label.setFont(font)
        self.ILP_Processors_Label.setStyleSheet(" QLabel {\n"
"    border: 2px solid green;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}")
        self.ILP_Processors_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.ILP_Processors_Label.setObjectName("ILP_Processors_Label")
        self.RWA_WindowLayout_29.setWidget(0, QtWidgets.QRWA_WindowLayout.LabelRole, self.ILP_Processors_Label)
        self.ILP_Processors_LineEdit = QtWidgets.QLineEdit(self.ILP)
        self.ILP_Processors_LineEdit.setStyleSheet(" QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.ILP_Processors_LineEdit.setText("")
        self.ILP_Processors_LineEdit.setObjectName("ILP_Processors_LineEdit")
        self.RWA_WindowLayout_29.setWidget(1, QtWidgets.QRWA_WindowLayout.LabelRole, self.ILP_Processors_LineEdit)
        self.RWA_WindowLayout.setLayout(0, QtWidgets.QRWA_WindowLayout.FieldRole, self.RWA_WindowLayout_29)
        self.RWA_WindowLayout_30 = QtWidgets.QRWA_WindowLayout()
        self.RWA_WindowLayout_30.setObjectName("RWA_WindowLayout_30")
        self.ILP_K_Label = QtWidgets.QLabel(self.ILP)
        font = QtGui.QFont()
        font.setFamily("IRANSans")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.ILP_K_Label.setFont(font)
        self.ILP_K_Label.setStyleSheet(" QLabel {\n"
"    border: 2px solid green;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}")
        self.ILP_K_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.ILP_K_Label.setObjectName("ILP_K_Label")
        self.RWA_WindowLayout_30.setWidget(0, QtWidgets.QRWA_WindowLayout.LabelRole, self.ILP_K_Label)
        self.ILP_K_LineEdit = QtWidgets.QLineEdit(self.ILP)
        self.ILP_K_LineEdit.setStyleSheet(" QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.ILP_K_LineEdit.setText("")
        self.ILP_K_LineEdit.setObjectName("ILP_K_LineEdit")
        self.RWA_WindowLayout_30.setWidget(1, QtWidgets.QRWA_WindowLayout.LabelRole, self.ILP_K_LineEdit)
        self.RWA_WindowLayout.setLayout(1, QtWidgets.QRWA_WindowLayout.LabelRole, self.RWA_WindowLayout_30)
        self.RWA_WindowLayout_31 = QtWidgets.QRWA_WindowLayout()
        self.RWA_WindowLayout_31.setObjectName("RWA_WindowLayout_31")
        self.ILP_MaxNW_Label = QtWidgets.QLabel(self.ILP)
        font = QtGui.QFont()
        font.setFamily("IRANSans")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.ILP_MaxNW_Label.setFont(font)
        self.ILP_MaxNW_Label.setStyleSheet(" QLabel {\n"
"    border: 2px solid green;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}")
        self.ILP_MaxNW_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.ILP_MaxNW_Label.setObjectName("ILP_MaxNW_Label")
        self.RWA_WindowLayout_31.setWidget(0, QtWidgets.QRWA_WindowLayout.LabelRole, self.ILP_MaxNW_Label)
        self.ILP_MaxNW_LineEdit = QtWidgets.QLineEdit(self.ILP)
        self.ILP_MaxNW_LineEdit.setStyleSheet(" QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.ILP_MaxNW_LineEdit.setText("")
        self.ILP_MaxNW_LineEdit.setObjectName("ILP_MaxNW_LineEdit")
        self.RWA_WindowLayout_31.setWidget(1, QtWidgets.QRWA_WindowLayout.LabelRole, self.ILP_MaxNW_LineEdit)
        self.RWA_WindowLayout.setLayout(1, QtWidgets.QRWA_WindowLayout.FieldRole, self.RWA_WindowLayout_31)
        self.RWA_WindowLayout_27 = QtWidgets.QRWA_WindowLayout()
        self.RWA_WindowLayout_27.setObjectName("RWA_WindowLayout_27")
        self.ILP_Alpha_Label = QtWidgets.QLabel(self.ILP)
        font = QtGui.QFont()
        font.setFamily("IRANSans")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.ILP_Alpha_Label.setFont(font)
        self.ILP_Alpha_Label.setStyleSheet(" QLabel {\n"
"    border: 2px solid green;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}")
        self.ILP_Alpha_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.ILP_Alpha_Label.setObjectName("ILP_Alpha_Label")
        self.RWA_WindowLayout_27.setWidget(0, QtWidgets.QRWA_WindowLayout.LabelRole, self.ILP_Alpha_Label)
        self.ILP_Alpha_LineEdit = QtWidgets.QLineEdit(self.ILP)
        self.ILP_Alpha_LineEdit.setStyleSheet(" QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.ILP_Alpha_LineEdit.setText("")
        self.ILP_Alpha_LineEdit.setObjectName("ILP_Alpha_LineEdit")
        self.RWA_WindowLayout_27.setWidget(1, QtWidgets.QRWA_WindowLayout.LabelRole, self.ILP_Alpha_LineEdit)
        self.RWA_WindowLayout.setLayout(2, QtWidgets.QRWA_WindowLayout.LabelRole, self.RWA_WindowLayout_27)
        self.RW_toolBox.addItem(self.ILP, "")
        self.gridLayout.addWidget(self.RW_toolBox, 0, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
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
        self.gridLayout_3.addWidget(self.ok_pushbutton, 0, 2, 1, 1)
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
        self.gridLayout_3.addWidget(self.cancel_pushbutton, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 1, 0, 1, 1)

        self.retranslateUi(RWA_Window)
        self.RW_toolBox.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(RWA_Window)

        # NOTE: added 
        self.cancel_pushbutton.clicked.connect(RWA_Window.close)
        self.ok_pushbutton.clicked.connect(self.ok_button_fun)

    def retranslateUi(self, RWA_Window):
        _translate = QtCore.QCoreApplication.translate
        RWA_Window.setWindowTitle(_translate("RWA_Window", "RWA_Window"))
        self.Mergin_DemandRe_Label.setText(_translate("RWA_Window", "Merging demands"))
        self.Mergin_DemandRe_LineEdit.setItemText(0, _translate("RWA_Window", "Yes"))
        self.Mergin_DemandRe_LineEdit.setItemText(1, _translate("RWA_Window", "No"))
        self.Greedy_Alpha_Label.setText(_translate("RWA_Window", "      Alpha  "))
        self.Greedy_Iteration_Label.setText(_translate("RWA_Window", "  Iteration   "))
        self.Greedy_Margin_Label.setText(_translate("RWA_Window", "    Margin "))
        self.Greedy_Processors_Label.setText(_translate("RWA_Window", " Processors"))
        self.Greedy_K_Label.setText(_translate("RWA_Window", "        k     "))
        self.Greedy_MaxNW_Label.setText(_translate("RWA_Window", "Maximum Number of Wavelengths"))
        self.RW_toolBox.setItemText(self.RW_toolBox.indexOf(self.Greedy), _translate("RWA_Window", "Greedy"))
        self.GroupILP_Alpha_Label.setText(_translate("RWA_Window", "      Alpha  "))
        self.GroupILP_Iteration_Label.setText(_translate("RWA_Window", "  Iteration   "))
        self.GroupILP_Margin_Label.setText(_translate("RWA_Window", "    Margin "))
        self.GroupILP_Processors_Label.setText(_translate("RWA_Window", " Processors"))
        self.GroupILP_K_Label.setText(_translate("RWA_Window", "        k     "))
        self.GroupILP_MaxNW_Label.setText(_translate("RWA_Window", "Maximum Number of Wavelengths"))
        self.GroupILP_Groupsize_Label.setText(_translate("RWA_Window", "Group Size"))
        self.GroupILP_History_Label.setText(_translate("RWA_Window", "      History   "))
        self.RW_toolBox.setItemText(self.RW_toolBox.indexOf(self.Group_ILP), _translate("RWA_Window", "Group ILP"))
        self.ILP_Margin_Label.setText(_translate("RWA_Window", "    Margin "))
        self.ILP_Processors_Label.setText(_translate("RWA_Window", " Processors"))
        self.ILP_K_Label.setText(_translate("RWA_Window", "        k     "))
        self.ILP_MaxNW_Label.setText(_translate("RWA_Window", "Maximum Number of Wavelengths"))
        self.ILP_Alpha_Label.setText(_translate("RWA_Window", "      Alpha  "))
        self.RW_toolBox.setItemText(self.RW_toolBox.indexOf(self.ILP), _translate("RWA_Window", "ILP"))
        self.ok_pushbutton.setText(_translate("RWA_Window", "OK"))
        self.cancel_pushbutton.setText(_translate("RWA_Window", "Cancel"))

    
    def ok_button_fun(self):

        index = self.RW_toolBox.currentIndex()

        if index == 0:
            merge = self.mergindemands_comboBox.currentText()
            alpha = self.Greedy_Alpha_LineEdit.text()
            margin = self.Greedy_Margin_LineEdit.text()
            iterations = self.Greedy_Iteration_LineEdit.text()
            processors = self.Greedy_Processors_LineEdit.text()
            k = self.Greedy_K_LineEdit.text()
            maxNW = self.Greedy_MaxNW_LineEdit.text()
            Algorithm = "Greedy"

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
        
        elif index == 1:
            alpha = self.GroupILP_Alpha_LineEdit.text()
            margin = self.GroupILP_Margin_LineEdit.text()
            iterations = self.GroupILP_Iteration_LineEdit.text()
            processors = self.GroupILP_Processors_LineEdit.text()
            k = self.GroupILP_K_LineEdit.text()
            maxNW = self.GroupILP_MaxNW_LineEdit.text()
            groupsize = GroupILP_Groupsize_LineEdit.text()
            history = GroupILP_History_LineEdit.text()
            Algorithm = "GroupILP"

            alpha = float(alpha)
            margin = int(margin)
            iterations = int(iterations)
            processors = int(processors)
            k = int(k)
            groupsize = int(groupsize)
            history = int(history)
        
        elif index == 2:
            alpha = self.ILP_Alpha_LineEdit.text()
            margin = self.ILP_Margin_LineEdit.text()
            processors = self.ILP_Processors_LineEdit.text()
            k = self.ILP_K_LineEdit.text()
            maxNW = self.ILP_MaxNW_LineEdit.text()
            Algorithm = "ILP"





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RWA_Window = QtWidgets.QWidget()
    ui = Ui_RWA_Window()
    ui.setupUi(RWA_Window)
    RWA_Window.show()
    sys.exit(app.exec_())

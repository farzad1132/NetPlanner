from PySide2 import QtWidgets, QtGui, QtCore
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import sys
import os
from data import *
from Common_Object_def import Network
bus = {}
from Ui_files.new_ui import iconresources


class Ui_RWA_Window(object):
    def setupUi(self, RWA_Window):

        # NOTE: added
        bus["RWA_Window"] = RWA_Window

        RWA_Window.setObjectName("RWA_Window")
        RWA_Window.resize(493, 462)
        self.gridLayout = QtWidgets.QGridLayout(RWA_Window)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.ok_pushbutton = QtWidgets.QPushButton(RWA_Window)
        self.ok_pushbutton.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"     \n"
"    font: 75 10pt \"Bahnschrift Condensed\";\n"
"    \n"
"    \n"
"    border:2px solid black; min-width: 80px;\n"
"    border-color: dark gray; \n"
"    border-radius: 25px;\n"
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
        self.ok_pushbutton.setAutoDefault(False)
        self.ok_pushbutton.setObjectName("ok_pushbutton")
        self.gridLayout_3.addWidget(self.ok_pushbutton, 0, 2, 1, 1)
        self.cancel_pushbutton = QtWidgets.QPushButton(RWA_Window)
        self.cancel_pushbutton.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"     \n"
"    font: 75 10pt \"Bahnschrift Condensed\";\n"
"    \n"
"    \n"
"    border:2px solid black; min-width: 80px;\n"
"    border-color: dark gray; \n"
"    border-radius: 25px;\n"
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
        self.cancel_pushbutton.setObjectName("cancel_pushbutton")
        self.gridLayout_3.addWidget(self.cancel_pushbutton, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 1, 0, 1, 1)
        self.RW_toolBox = QtWidgets.QToolBox(RWA_Window)
        self.RW_toolBox.setStyleSheet("QToolBox::tab {\n"
"    background-color: rgb(192, 192, 192);\n"
"     border: 2px solid gray; \n"
"     \n"
"     border-bottom-color: Ea8686; /* same as the pane color */\n"
"     border-top-left-radius: 7px;\n"
"     border-top-right-radius: 7px;\n"
"     min-width: 28ex;\n"
"     padding: 2px; \n"
"     \n"
"    \n"
"    font: 25 9pt \"Bahnschrift condensed\";\n"
"}\n"
"\n"
"QToolBox::tab:selected {\n"
"    background-color:#Eb8686; /* same as pane color */ \n"
"     margin-left: -4px;\n"
"     margin-right: -4px;\n"
"    font: 63 9pt \"Bahnschrift SemiBold\";\n"
"}\n"
"\n"
"")
        self.RW_toolBox.setObjectName("RW_toolBox")
        self.Greedy = QtWidgets.QWidget()
        self.Greedy.setGeometry(QtCore.QRect(0, 0, 471, 313))
        self.Greedy.setObjectName("Greedy")
        self.formLayout_10 = QtWidgets.QFormLayout(self.Greedy)
        self.formLayout_10.setObjectName("formLayout_10")
        self.mergindemands_gridlayout_3 = QtWidgets.QGridLayout()
        self.mergindemands_gridlayout_3.setObjectName("mergindemands_gridlayout_3")
        self.Mergin_DemandRe_Label = QtWidgets.QLabel(self.Greedy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.Mergin_DemandRe_Label.setFont(font)
        self.Mergin_DemandRe_Label.setStyleSheet("")
        self.Mergin_DemandRe_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Mergin_DemandRe_Label.setObjectName("Mergin_DemandRe_Label")
        self.mergindemands_gridlayout_3.addWidget(self.Mergin_DemandRe_Label, 0, 0, 1, 1)
        self.Mergin_DemandRe_LineEdit = QtWidgets.QComboBox(self.Greedy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(9)
        self.Mergin_DemandRe_LineEdit.setFont(font)
        self.Mergin_DemandRe_LineEdit.setStyleSheet("QComboBox {\n"
"    \n"
"    border-radius: 0px;\n"
"    padding: 1px 18px 1px 5px;\n"
"    min-width: 6em; \n"
"    \n"
"    border:1px solid rgb(0, 139, 208);\n"
"    \n"
"   \n"
"    \n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    \n"
"    \n"
"    border-left-width: 2px;\n"
"    border-left-color: darkblue;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 0px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"   \n"
"    image: url(:/newPrefix/dropdown.png); \n"
"    \n"
"    \n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    \n"
"    \n"
"    image: url(:/newPrefix/dropup.png);\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    \n"
"    border-color:2px solid blue;\n"
"   }")
        self.Mergin_DemandRe_LineEdit.setEditable(False)
        self.Mergin_DemandRe_LineEdit.setObjectName("Mergin_DemandRe_LineEdit")
        self.Mergin_DemandRe_LineEdit.addItem("")
        self.Mergin_DemandRe_LineEdit.addItem("")
        self.mergindemands_gridlayout_3.addWidget(self.Mergin_DemandRe_LineEdit, 0, 1, 1, 1)
        self.formLayout_10.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.mergindemands_gridlayout_3)
        self.formLayout_9 = QtWidgets.QFormLayout()
        self.formLayout_9.setObjectName("formLayout_9")
        self.Greedy_Alpha_Label = QtWidgets.QLabel(self.Greedy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Greedy_Alpha_Label.setFont(font)
        self.Greedy_Alpha_Label.setStyleSheet(" QLabel {\n"
"    \n"
"    border-radius: 10px;\n"
"    \n"
"    \n"
"    font: 75 10pt \"Bahnschrift Condensed\";\n"
"    \n"
"    border: 2px solid #8f8f91; min-width: 80px;\n"
"    border-color: #4072B3; \n"
"}")
        self.Greedy_Alpha_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Greedy_Alpha_Label.setObjectName("Greedy_Alpha_Label")
        self.formLayout_9.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Greedy_Alpha_Label)
        self.Greedy_Alpha_LineEdit = QtWidgets.QLineEdit(self.Greedy)
        self.Greedy_Alpha_LineEdit.setStyleSheet(" QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.Greedy_Alpha_LineEdit.setText("")
        self.Greedy_Alpha_LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.Greedy_Alpha_LineEdit.setClearButtonEnabled(True)
        self.Greedy_Alpha_LineEdit.setObjectName("Greedy_Alpha_LineEdit")
        self.formLayout_9.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Greedy_Alpha_LineEdit)
        self.formLayout_10.setLayout(1, QtWidgets.QFormLayout.LabelRole, self.formLayout_9)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.Greedy_Iteration_Label = QtWidgets.QLabel(self.Greedy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Greedy_Iteration_Label.setFont(font)
        self.Greedy_Iteration_Label.setStyleSheet(" QLabel {\n"
"    \n"
"    border-radius: 10px;\n"
"    \n"
"    \n"
"    font: 75 10pt \"Bahnschrift Condensed\";\n"
"    \n"
"    border: 2px solid #8f8f91; min-width: 80px;\n"
"    border-color: #4072B3; \n"
"}")
        self.Greedy_Iteration_Label.setMidLineWidth(7)
        self.Greedy_Iteration_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Greedy_Iteration_Label.setObjectName("Greedy_Iteration_Label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Greedy_Iteration_Label)
        self.Greedy_Iteration_LineEdit = QtWidgets.QLineEdit(self.Greedy)
        self.Greedy_Iteration_LineEdit.setStyleSheet("\n"
" QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.Greedy_Iteration_LineEdit.setText("")
        self.Greedy_Iteration_LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.Greedy_Iteration_LineEdit.setClearButtonEnabled(True)
        self.Greedy_Iteration_LineEdit.setObjectName("Greedy_Iteration_LineEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Greedy_Iteration_LineEdit)
        self.formLayout_10.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.formLayout_2)
        self.formLayout_8 = QtWidgets.QFormLayout()
        self.formLayout_8.setObjectName("formLayout_8")
        self.Greedy_Margin_Label = QtWidgets.QLabel(self.Greedy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Greedy_Margin_Label.setFont(font)
        self.Greedy_Margin_Label.setStyleSheet(" QLabel {\n"
"    \n"
"    border-radius: 10px;\n"
"    \n"
"    \n"
"    font: 75 10pt \"Bahnschrift Condensed\";\n"
"    \n"
"    border: 2px solid #8f8f91; min-width: 80px;\n"
"    border-color: #4072B3; \n"
"}")
        self.Greedy_Margin_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Greedy_Margin_Label.setObjectName("Greedy_Margin_Label")
        self.formLayout_8.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Greedy_Margin_Label)
        self.Greedy_Margin_LineEdit = QtWidgets.QLineEdit(self.Greedy)
        self.Greedy_Margin_LineEdit.setStyleSheet("\n"
" QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.Greedy_Margin_LineEdit.setText("")
        self.Greedy_Margin_LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.Greedy_Margin_LineEdit.setClearButtonEnabled(True)
        self.Greedy_Margin_LineEdit.setObjectName("Greedy_Margin_LineEdit")
        self.formLayout_8.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Greedy_Margin_LineEdit)
        self.formLayout_10.setLayout(2, QtWidgets.QFormLayout.LabelRole, self.formLayout_8)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.Greedy_Processors_Label = QtWidgets.QLabel(self.Greedy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Greedy_Processors_Label.setFont(font)
        self.Greedy_Processors_Label.setStyleSheet("  QLabel {\n"
"    \n"
"    border-radius: 10px;\n"
"    \n"
"    \n"
"    font: 75 10pt \"Bahnschrift Condensed\";\n"
"    \n"
"    border: 2px solid #8f8f91; min-width: 80px;\n"
"    border-color: #4072B3; \n"
"}")
        self.Greedy_Processors_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Greedy_Processors_Label.setObjectName("Greedy_Processors_Label")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Greedy_Processors_Label)
        self.Greedy_Processors_LineEdit = QtWidgets.QLineEdit(self.Greedy)
        self.Greedy_Processors_LineEdit.setStyleSheet("\n"
" QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.Greedy_Processors_LineEdit.setText("")
        self.Greedy_Processors_LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.Greedy_Processors_LineEdit.setClearButtonEnabled(True)
        self.Greedy_Processors_LineEdit.setObjectName("Greedy_Processors_LineEdit")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Greedy_Processors_LineEdit)
        self.formLayout_10.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.formLayout_3)
        self.formLayout_7 = QtWidgets.QFormLayout()
        self.formLayout_7.setObjectName("formLayout_7")
        self.Greedy_K_Label = QtWidgets.QLabel(self.Greedy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Greedy_K_Label.setFont(font)
        self.Greedy_K_Label.setStyleSheet("  QLabel {\n"
"    \n"
"    border-radius: 10px;\n"
"    \n"
"    \n"
"    font: 75 10pt \"Bahnschrift Condensed\";\n"
"    \n"
"    border: 2px solid #8f8f91; min-width: 80px;\n"
"    border-color: #4072B3; \n"
"}")
        self.Greedy_K_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Greedy_K_Label.setObjectName("Greedy_K_Label")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Greedy_K_Label)
        self.Greedy_K_LineEdit = QtWidgets.QLineEdit(self.Greedy)
        self.Greedy_K_LineEdit.setStyleSheet("\n"
" QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.Greedy_K_LineEdit.setText("")
        self.Greedy_K_LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.Greedy_K_LineEdit.setClearButtonEnabled(True)
        self.Greedy_K_LineEdit.setObjectName("Greedy_K_LineEdit")
        self.formLayout_7.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Greedy_K_LineEdit)
        self.formLayout_10.setLayout(3, QtWidgets.QFormLayout.LabelRole, self.formLayout_7)
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setObjectName("formLayout_4")
        self.Greedy_MaxNW_Label = QtWidgets.QLabel(self.Greedy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Greedy_MaxNW_Label.setFont(font)
        self.Greedy_MaxNW_Label.setStyleSheet("  QLabel {\n"
"    \n"
"    border-radius: 10px;\n"
"    \n"
"    \n"
"    font: 75 9pt \"Bahnschrift Condensed\";\n"
"    \n"
"    border: 2px solid #8f8f91; min-width: 80px;\n"
"    border-color: #4072B3; \n"
"}")
        self.Greedy_MaxNW_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Greedy_MaxNW_Label.setObjectName("Greedy_MaxNW_Label")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Greedy_MaxNW_Label)
        self.Greedy_MaxNW_LineEdit = QtWidgets.QLineEdit(self.Greedy)
        self.Greedy_MaxNW_LineEdit.setStyleSheet(" QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.Greedy_MaxNW_LineEdit.setText("")
        self.Greedy_MaxNW_LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.Greedy_MaxNW_LineEdit.setClearButtonEnabled(True)
        self.Greedy_MaxNW_LineEdit.setObjectName("Greedy_MaxNW_LineEdit")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Greedy_MaxNW_LineEdit)
        self.formLayout_10.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.formLayout_4)
        self.formLayout_6 = QtWidgets.QFormLayout()
        self.formLayout_6.setObjectName("formLayout_6")
        self.Greedy_K_Restoration_Label = QtWidgets.QLabel(self.Greedy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Greedy_K_Restoration_Label.setFont(font)
        self.Greedy_K_Restoration_Label.setStyleSheet("  QLabel {\n"
"    \n"
"    border-radius: 10px;\n"
"    \n"
"    \n"
"    font: 75 10pt \"Bahnschrift Condensed\";\n"
"    \n"
"    border: 2px solid #8f8f91; min-width: 80px;\n"
"    border-color: #4072B3; \n"
"}")
        self.Greedy_K_Restoration_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Greedy_K_Restoration_Label.setObjectName("Greedy_K_Restoration_Label")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Greedy_K_Restoration_Label)
        self.Greedy_K_Restoration_LineEdit = QtWidgets.QLineEdit(self.Greedy)
        self.Greedy_K_Restoration_LineEdit.setStyleSheet("\n"
" QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.Greedy_K_Restoration_LineEdit.setText("")
        self.Greedy_K_Restoration_LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.Greedy_K_Restoration_LineEdit.setClearButtonEnabled(True)
        self.Greedy_K_Restoration_LineEdit.setObjectName("Greedy_K_Restoration_LineEdit")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Greedy_K_Restoration_LineEdit)
        self.formLayout_10.setLayout(4, QtWidgets.QFormLayout.LabelRole, self.formLayout_6)
        self.formLayout_5 = QtWidgets.QFormLayout()
        self.formLayout_5.setObjectName("formLayout_5")
        self.Greedy_numRandomChoices_LineEdit = QtWidgets.QLineEdit(self.Greedy)
        self.Greedy_numRandomChoices_LineEdit.setStyleSheet(" QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.Greedy_numRandomChoices_LineEdit.setText("")
        self.Greedy_numRandomChoices_LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.Greedy_numRandomChoices_LineEdit.setClearButtonEnabled(True)
        self.Greedy_numRandomChoices_LineEdit.setObjectName("Greedy_numRandomChoices_LineEdit")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Greedy_numRandomChoices_LineEdit)
        self.Greedy_numRandomChoices_Label = QtWidgets.QLabel(self.Greedy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Greedy_numRandomChoices_Label.setFont(font)
        self.Greedy_numRandomChoices_Label.setStyleSheet("  QLabel {\n"
"    \n"
"    border-radius: 10px;\n"
"    \n"
"    \n"
"    font: 75 9pt \"Bahnschrift Condensed\";\n"
"    \n"
"    border: 2px solid #8f8f91; min-width: 80px;\n"
"    border-color: #4072B3; \n"
"}")
        self.Greedy_numRandomChoices_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Greedy_numRandomChoices_Label.setObjectName("Greedy_numRandomChoices_Label")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.Greedy_numRandomChoices_Label)
        self.formLayout_10.setLayout(4, QtWidgets.QFormLayout.FieldRole, self.formLayout_5)
        self.RW_toolBox.addItem(self.Greedy, "")
        self.Group_ILP = QtWidgets.QWidget()
        self.Group_ILP.setGeometry(QtCore.QRect(0, 0, 471, 313))
        self.Group_ILP.setObjectName("Group_ILP")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Group_ILP)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.formLayout_19 = QtWidgets.QFormLayout()
        self.formLayout_19.setObjectName("formLayout_19")
        self.GroupILP_Alpha_Label = QtWidgets.QLabel(self.Group_ILP)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.GroupILP_Alpha_Label.setFont(font)
        self.GroupILP_Alpha_Label.setStyleSheet(" QLabel {\n"
"    \n"
"    border-radius: 10px;\n"
"    \n"
"    \n"
"    font: 75 10pt \"Bahnschrift Condensed\";\n"
"    \n"
"    border: 2px solid #8f8f91; min-width: 80px;\n"
"    border-color: #4072B3; \n"
"}")
        self.GroupILP_Alpha_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.GroupILP_Alpha_Label.setObjectName("GroupILP_Alpha_Label")
        self.formLayout_19.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.GroupILP_Alpha_Label)
        self.GroupILP_Alpha_LineEdit = QtWidgets.QLineEdit(self.Group_ILP)
        self.GroupILP_Alpha_LineEdit.setStyleSheet(" QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.GroupILP_Alpha_LineEdit.setText("")
        self.GroupILP_Alpha_LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.GroupILP_Alpha_LineEdit.setClearButtonEnabled(True)
        self.GroupILP_Alpha_LineEdit.setObjectName("GroupILP_Alpha_LineEdit")
        self.formLayout_19.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.GroupILP_Alpha_LineEdit)
        self.gridLayout_2.addLayout(self.formLayout_19, 0, 0, 1, 1)
        self.formLayout_20 = QtWidgets.QFormLayout()
        self.formLayout_20.setObjectName("formLayout_20")
        self.GroupILP_Iteration_Label = QtWidgets.QLabel(self.Group_ILP)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.GroupILP_Iteration_Label.setFont(font)
        self.GroupILP_Iteration_Label.setStyleSheet(" QLabel {\n"
"    \n"
"    border-radius: 10px;\n"
"    \n"
"    \n"
"    font: 75 10pt \"Bahnschrift Condensed\";\n"
"    \n"
"    border: 2px solid #8f8f91; min-width: 80px;\n"
"    border-color: #4072B3; \n"
"}")
        self.GroupILP_Iteration_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.GroupILP_Iteration_Label.setObjectName("GroupILP_Iteration_Label")
        self.formLayout_20.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.GroupILP_Iteration_Label)
        self.GroupILP_Iteration_LineEdit = QtWidgets.QLineEdit(self.Group_ILP)
        self.GroupILP_Iteration_LineEdit.setStyleSheet(" QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.GroupILP_Iteration_LineEdit.setText("")
        self.GroupILP_Iteration_LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.GroupILP_Iteration_LineEdit.setClearButtonEnabled(True)
        self.GroupILP_Iteration_LineEdit.setObjectName("GroupILP_Iteration_LineEdit")
        self.formLayout_20.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.GroupILP_Iteration_LineEdit)
        self.gridLayout_2.addLayout(self.formLayout_20, 0, 1, 1, 1)
        self.formLayout_21 = QtWidgets.QFormLayout()
        self.formLayout_21.setObjectName("formLayout_21")
        self.GroupILP_Margin_Label = QtWidgets.QLabel(self.Group_ILP)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.GroupILP_Margin_Label.setFont(font)
        self.GroupILP_Margin_Label.setStyleSheet("  QLabel {\n"
"    \n"
"    border-radius: 10px;\n"
"    \n"
"    \n"
"    font: 75 10pt \"Bahnschrift Condensed\";\n"
"    \n"
"    border: 2px solid #8f8f91; min-width: 80px;\n"
"    border-color: #4072B3; \n"
"}")
        self.GroupILP_Margin_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.GroupILP_Margin_Label.setObjectName("GroupILP_Margin_Label")
        self.formLayout_21.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.GroupILP_Margin_Label)
        self.GroupILP_Margin_LineEdit = QtWidgets.QLineEdit(self.Group_ILP)
        self.GroupILP_Margin_LineEdit.setStyleSheet(" QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.GroupILP_Margin_LineEdit.setText("")
        self.GroupILP_Margin_LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.GroupILP_Margin_LineEdit.setClearButtonEnabled(True)
        self.GroupILP_Margin_LineEdit.setObjectName("GroupILP_Margin_LineEdit")
        self.formLayout_21.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.GroupILP_Margin_LineEdit)
        self.gridLayout_2.addLayout(self.formLayout_21, 1, 0, 1, 1)
        self.formLayout_22 = QtWidgets.QFormLayout()
        self.formLayout_22.setObjectName("formLayout_22")
        self.GroupILP_Processors_Label = QtWidgets.QLabel(self.Group_ILP)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.GroupILP_Processors_Label.setFont(font)
        self.GroupILP_Processors_Label.setStyleSheet(" QLabel {\n"
"    \n"
"    border-radius: 10px;\n"
"    \n"
"    \n"
"    font: 75 10pt \"Bahnschrift Condensed\";\n"
"    \n"
"    border: 2px solid #8f8f91; min-width: 80px;\n"
"    border-color: #4072B3; \n"
"}")
        self.GroupILP_Processors_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.GroupILP_Processors_Label.setObjectName("GroupILP_Processors_Label")
        self.formLayout_22.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.GroupILP_Processors_Label)
        self.GroupILP_Processors_LineEdit = QtWidgets.QLineEdit(self.Group_ILP)
        self.GroupILP_Processors_LineEdit.setStyleSheet(" QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.GroupILP_Processors_LineEdit.setText("")
        self.GroupILP_Processors_LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.GroupILP_Processors_LineEdit.setClearButtonEnabled(True)
        self.GroupILP_Processors_LineEdit.setObjectName("GroupILP_Processors_LineEdit")
        self.formLayout_22.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.GroupILP_Processors_LineEdit)
        self.gridLayout_2.addLayout(self.formLayout_22, 1, 1, 1, 1)
        self.formLayout_23 = QtWidgets.QFormLayout()
        self.formLayout_23.setObjectName("formLayout_23")
        self.GroupILP_K_Label = QtWidgets.QLabel(self.Group_ILP)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.GroupILP_K_Label.setFont(font)
        self.GroupILP_K_Label.setStyleSheet("  QLabel {\n"
"    \n"
"    border-radius: 10px;\n"
"    \n"
"    \n"
"    font: 75 10pt \"Bahnschrift Condensed\";\n"
"    \n"
"    border: 2px solid #8f8f91; min-width: 80px;\n"
"    border-color: #4072B3; \n"
"}")
        self.GroupILP_K_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.GroupILP_K_Label.setObjectName("GroupILP_K_Label")
        self.formLayout_23.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.GroupILP_K_Label)
        self.GroupILP_K_LineEdit = QtWidgets.QLineEdit(self.Group_ILP)
        self.GroupILP_K_LineEdit.setStyleSheet(" QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.GroupILP_K_LineEdit.setText("")
        self.GroupILP_K_LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.GroupILP_K_LineEdit.setClearButtonEnabled(True)
        self.GroupILP_K_LineEdit.setObjectName("GroupILP_K_LineEdit")
        self.formLayout_23.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.GroupILP_K_LineEdit)
        self.gridLayout_2.addLayout(self.formLayout_23, 2, 0, 1, 1)
        self.formLayout_24 = QtWidgets.QFormLayout()
        self.formLayout_24.setObjectName("formLayout_24")
        self.GroupILP_MaxNW_Label = QtWidgets.QLabel(self.Group_ILP)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.GroupILP_MaxNW_Label.setFont(font)
        self.GroupILP_MaxNW_Label.setStyleSheet(" QLabel {\n"
"    \n"
"    border-radius: 10px;\n"
"    \n"
"    \n"
"    font: 75 10pt \"Bahnschrift Condensed\";\n"
"    \n"
"    border: 2px solid #8f8f91; min-width: 80px;\n"
"    border-color: #4072B3; \n"
"}")
        self.GroupILP_MaxNW_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.GroupILP_MaxNW_Label.setObjectName("GroupILP_MaxNW_Label")
        self.formLayout_24.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.GroupILP_MaxNW_Label)
        self.GroupILP_MaxNW_LineEdit = QtWidgets.QLineEdit(self.Group_ILP)
        self.GroupILP_MaxNW_LineEdit.setStyleSheet(" QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.GroupILP_MaxNW_LineEdit.setText("")
        self.GroupILP_MaxNW_LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.GroupILP_MaxNW_LineEdit.setClearButtonEnabled(True)
        self.GroupILP_MaxNW_LineEdit.setObjectName("GroupILP_MaxNW_LineEdit")
        self.formLayout_24.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.GroupILP_MaxNW_LineEdit)
        self.gridLayout_2.addLayout(self.formLayout_24, 2, 1, 1, 1)
        self.formLayout_25 = QtWidgets.QFormLayout()
        self.formLayout_25.setObjectName("formLayout_25")
        self.GroupILP_Groupsize_Label = QtWidgets.QLabel(self.Group_ILP)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.GroupILP_Groupsize_Label.setFont(font)
        self.GroupILP_Groupsize_Label.setStyleSheet("  QLabel {\n"
"    \n"
"    border-radius: 10px;\n"
"    \n"
"    \n"
"    font: 75 10pt \"Bahnschrift Condensed\";\n"
"    \n"
"    border: 2px solid #8f8f91; min-width: 80px;\n"
"    border-color: #4072B3; \n"
"}")
        self.GroupILP_Groupsize_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.GroupILP_Groupsize_Label.setObjectName("GroupILP_Groupsize_Label")
        self.formLayout_25.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.GroupILP_Groupsize_Label)
        self.GroupILP_Groupsize_LineEdit = QtWidgets.QLineEdit(self.Group_ILP)
        self.GroupILP_Groupsize_LineEdit.setStyleSheet(" QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.GroupILP_Groupsize_LineEdit.setText("")
        self.GroupILP_Groupsize_LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.GroupILP_Groupsize_LineEdit.setClearButtonEnabled(True)
        self.GroupILP_Groupsize_LineEdit.setObjectName("GroupILP_Groupsize_LineEdit")
        self.formLayout_25.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.GroupILP_Groupsize_LineEdit)
        self.gridLayout_2.addLayout(self.formLayout_25, 3, 0, 1, 1)
        self.formLayout_26 = QtWidgets.QFormLayout()
        self.formLayout_26.setObjectName("formLayout_26")
        self.GroupILP_History_LineEdit = QtWidgets.QLineEdit(self.Group_ILP)
        self.GroupILP_History_LineEdit.setStyleSheet(" QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.GroupILP_History_LineEdit.setText("")
        self.GroupILP_History_LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.GroupILP_History_LineEdit.setClearButtonEnabled(True)
        self.GroupILP_History_LineEdit.setObjectName("GroupILP_History_LineEdit")
        self.formLayout_26.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.GroupILP_History_LineEdit)
        self.GroupILP_History_Label = QtWidgets.QLabel(self.Group_ILP)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.GroupILP_History_Label.setFont(font)
        self.GroupILP_History_Label.setStyleSheet("  QLabel {\n"
"    \n"
"    border-radius: 10px;\n"
"    \n"
"    \n"
"    font: 75 10pt \"Bahnschrift Condensed\";\n"
"    \n"
"    border: 2px solid #8f8f91; min-width: 80px;\n"
"    border-color: #4072B3; \n"
"}")
        self.GroupILP_History_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.GroupILP_History_Label.setObjectName("GroupILP_History_Label")
        self.formLayout_26.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.GroupILP_History_Label)
        self.gridLayout_2.addLayout(self.formLayout_26, 3, 1, 1, 1)
        self.RW_toolBox.addItem(self.Group_ILP, "")
        self.ILP = QtWidgets.QWidget()
        self.ILP.setGeometry(QtCore.QRect(0, 0, 471, 313))
        self.ILP.setObjectName("ILP")
        self.formLayout = QtWidgets.QFormLayout(self.ILP)
        self.formLayout.setObjectName("formLayout")
        self.formLayout_28 = QtWidgets.QFormLayout()
        self.formLayout_28.setObjectName("formLayout_28")
        self.ILP_Margin_Label = QtWidgets.QLabel(self.ILP)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.ILP_Margin_Label.setFont(font)
        self.ILP_Margin_Label.setStyleSheet(" QLabel {\n"
"    \n"
"    border-radius: 10px;\n"
"    \n"
"    \n"
"    font: 75 10pt \"Bahnschrift Condensed\";\n"
"    \n"
"    border: 2px solid #8f8f91; min-width: 80px;\n"
"    border-color: #4072B3; \n"
"}")
        self.ILP_Margin_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.ILP_Margin_Label.setObjectName("ILP_Margin_Label")
        self.formLayout_28.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.ILP_Margin_Label)
        self.ILP_Margin_LineEdit = QtWidgets.QLineEdit(self.ILP)
        self.ILP_Margin_LineEdit.setStyleSheet(" QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.ILP_Margin_LineEdit.setText("")
        self.ILP_Margin_LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.ILP_Margin_LineEdit.setClearButtonEnabled(True)
        self.ILP_Margin_LineEdit.setObjectName("ILP_Margin_LineEdit")
        self.formLayout_28.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.ILP_Margin_LineEdit)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.formLayout_28)
        self.formLayout_29 = QtWidgets.QFormLayout()
        self.formLayout_29.setObjectName("formLayout_29")
        self.ILP_Processors_Label = QtWidgets.QLabel(self.ILP)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.ILP_Processors_Label.setFont(font)
        self.ILP_Processors_Label.setStyleSheet(" QLabel {\n"
"    \n"
"    border-radius: 10px;\n"
"    \n"
"    \n"
"    font: 75 10pt \"Bahnschrift Condensed\";\n"
"    \n"
"    border: 2px solid #8f8f91; min-width: 80px;\n"
"    border-color: #4072B3; \n"
"}")
        self.ILP_Processors_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.ILP_Processors_Label.setObjectName("ILP_Processors_Label")
        self.formLayout_29.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.ILP_Processors_Label)
        self.ILP_Processors_LineEdit = QtWidgets.QLineEdit(self.ILP)
        self.ILP_Processors_LineEdit.setStyleSheet(" QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.ILP_Processors_LineEdit.setText("")
        self.ILP_Processors_LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.ILP_Processors_LineEdit.setClearButtonEnabled(True)
        self.ILP_Processors_LineEdit.setObjectName("ILP_Processors_LineEdit")
        self.formLayout_29.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.ILP_Processors_LineEdit)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.formLayout_29)
        self.formLayout_30 = QtWidgets.QFormLayout()
        self.formLayout_30.setObjectName("formLayout_30")
        self.ILP_K_Label = QtWidgets.QLabel(self.ILP)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.ILP_K_Label.setFont(font)
        self.ILP_K_Label.setStyleSheet("  QLabel {\n"
"    \n"
"    border-radius: 10px;\n"
"    \n"
"    \n"
"    font: 75 10pt \"Bahnschrift Condensed\";\n"
"    \n"
"    border: 2px solid #8f8f91; min-width: 80px;\n"
"    border-color: #4072B3; \n"
"}")
        self.ILP_K_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.ILP_K_Label.setObjectName("ILP_K_Label")
        self.formLayout_30.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.ILP_K_Label)
        self.ILP_K_LineEdit = QtWidgets.QLineEdit(self.ILP)
        self.ILP_K_LineEdit.setStyleSheet(" QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.ILP_K_LineEdit.setText("")
        self.ILP_K_LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.ILP_K_LineEdit.setClearButtonEnabled(True)
        self.ILP_K_LineEdit.setObjectName("ILP_K_LineEdit")
        self.formLayout_30.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.ILP_K_LineEdit)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.LabelRole, self.formLayout_30)
        self.formLayout_31 = QtWidgets.QFormLayout()
        self.formLayout_31.setObjectName("formLayout_31")
        self.ILP_MaxNW_Label = QtWidgets.QLabel(self.ILP)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.ILP_MaxNW_Label.setFont(font)
        self.ILP_MaxNW_Label.setStyleSheet("  QLabel {\n"
"    \n"
"    border-radius: 10px;\n"
"    \n"
"    \n"
"    font: 75 9pt \"Bahnschrift Condensed\";\n"
"    \n"
"    border: 2px solid #8f8f91; min-width: 80px;\n"
"    border-color: #4072B3; \n"
"}")
        self.ILP_MaxNW_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.ILP_MaxNW_Label.setObjectName("ILP_MaxNW_Label")
        self.formLayout_31.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.ILP_MaxNW_Label)
        self.ILP_MaxNW_LineEdit = QtWidgets.QLineEdit(self.ILP)
        self.ILP_MaxNW_LineEdit.setStyleSheet(" QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.ILP_MaxNW_LineEdit.setText("")
        self.ILP_MaxNW_LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.ILP_MaxNW_LineEdit.setClearButtonEnabled(True)
        self.ILP_MaxNW_LineEdit.setObjectName("ILP_MaxNW_LineEdit")
        self.formLayout_31.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.ILP_MaxNW_LineEdit)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.formLayout_31)
        self.formLayout_27 = QtWidgets.QFormLayout()
        self.formLayout_27.setObjectName("formLayout_27")
        self.ILP_Alpha_Label = QtWidgets.QLabel(self.ILP)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.ILP_Alpha_Label.setFont(font)
        self.ILP_Alpha_Label.setStyleSheet("  QLabel {\n"
"    \n"
"    border-radius: 10px;\n"
"    \n"
"    \n"
"    font: 75 10pt \"Bahnschrift Condensed\";\n"
"    \n"
"    border: 2px solid #8f8f91; min-width: 80px;\n"
"    border-color: #4072B3; \n"
"}")
        self.ILP_Alpha_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.ILP_Alpha_Label.setObjectName("ILP_Alpha_Label")
        self.formLayout_27.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.ILP_Alpha_Label)
        self.ILP_Alpha_LineEdit = QtWidgets.QLineEdit(self.ILP)
        self.ILP_Alpha_LineEdit.setStyleSheet(" QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.ILP_Alpha_LineEdit.setText("")
        self.ILP_Alpha_LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.ILP_Alpha_LineEdit.setClearButtonEnabled(True)
        self.ILP_Alpha_LineEdit.setObjectName("ILP_Alpha_LineEdit")
        self.formLayout_27.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.ILP_Alpha_LineEdit)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.LabelRole, self.formLayout_27)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label = QtWidgets.QLabel(self.ILP)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.gridLayout_5)
        self.RW_toolBox.addItem(self.ILP, "")
        self.gridLayout.addWidget(self.RW_toolBox, 0, 0, 1, 1)

        self.retranslateUi(RWA_Window)
        self.RW_toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(RWA_Window)

        # NOTE: added 
        self.cancel_pushbutton.clicked.connect(RWA_Window.close)
        self.ok_pushbutton.clicked.connect(self.ok_button_fun)

    def retranslateUi(self, RWA_Window):
        _translate = QtCore.QCoreApplication.translate
        RWA_Window.setWindowTitle(_translate("RWA_Window", "RWA_Window"))
        self.ok_pushbutton.setText(_translate("RWA_Window", "OK"))
        self.cancel_pushbutton.setText(_translate("RWA_Window", "Cancel"))
        self.Mergin_DemandRe_Label.setText(_translate("RWA_Window", "Merging demands"))
        self.Mergin_DemandRe_LineEdit.setCurrentText(_translate("RWA_Window", "True"))
        self.Mergin_DemandRe_LineEdit.setItemText(0, _translate("RWA_Window", "True"))
        self.Mergin_DemandRe_LineEdit.setItemText(1, _translate("RWA_Window", "False"))
        self.Greedy_Alpha_Label.setText(_translate("RWA_Window", "      Alpha  "))
        self.Greedy_Alpha_LineEdit.setPlaceholderText(_translate("RWA_Window", "0.2"))
        self.Greedy_Iteration_Label.setText(_translate("RWA_Window", "  Iteration   "))
        self.Greedy_Iteration_LineEdit.setPlaceholderText(_translate("RWA_Window", "4"))
        self.Greedy_Margin_Label.setText(_translate("RWA_Window", "    Margin "))
        self.Greedy_Margin_LineEdit.setPlaceholderText(_translate("RWA_Window", "3-7"))
        self.Greedy_Processors_Label.setText(_translate("RWA_Window", " Processors"))
        self.Greedy_Processors_LineEdit.setPlaceholderText(_translate("RWA_Window", "4"))
        self.Greedy_K_Label.setText(_translate("RWA_Window", "     k     "))
        self.Greedy_K_LineEdit.setPlaceholderText(_translate("RWA_Window", "3"))
        self.Greedy_MaxNW_Label.setText(_translate("RWA_Window", "Maximum Number of Wavelengths"))
        self.Greedy_MaxNW_LineEdit.setPlaceholderText(_translate("RWA_Window", "80"))
        self.Greedy_K_Restoration_Label.setText(_translate("RWA_Window", "     K Restoration      "))
        self.Greedy_K_Restoration_LineEdit.setPlaceholderText(_translate("RWA_Window", "2"))
        self.Greedy_numRandomChoices_LineEdit.setPlaceholderText(_translate("RWA_Window", "10"))
        self.Greedy_numRandomChoices_Label.setText(_translate("RWA_Window", "Number of Random Choices"))
        self.RW_toolBox.setItemText(self.RW_toolBox.indexOf(self.Greedy), _translate("RWA_Window", "Greedy"))
        self.GroupILP_Alpha_Label.setText(_translate("RWA_Window", "      Alpha  "))
        self.GroupILP_Alpha_LineEdit.setPlaceholderText(_translate("RWA_Window", "0.2"))
        self.GroupILP_Iteration_Label.setText(_translate("RWA_Window", "  Iteration   "))
        self.GroupILP_Iteration_LineEdit.setPlaceholderText(_translate("RWA_Window", "4"))
        self.GroupILP_Margin_Label.setText(_translate("RWA_Window", "    Margin "))
        self.GroupILP_Margin_LineEdit.setPlaceholderText(_translate("RWA_Window", "3-7"))
        self.GroupILP_Processors_Label.setText(_translate("RWA_Window", " Processors"))
        self.GroupILP_Processors_LineEdit.setPlaceholderText(_translate("RWA_Window", "4"))
        self.GroupILP_K_Label.setText(_translate("RWA_Window", "        k     "))
        self.GroupILP_K_LineEdit.setPlaceholderText(_translate("RWA_Window", "3"))
        self.GroupILP_MaxNW_Label.setText(_translate("RWA_Window", "Maximum Number of Wavelengths"))
        self.GroupILP_MaxNW_LineEdit.setPlaceholderText(_translate("RWA_Window", "80"))
        self.GroupILP_Groupsize_Label.setText(_translate("RWA_Window", "Group Size"))
        self.GroupILP_Groupsize_LineEdit.setPlaceholderText(_translate("RWA_Window", "2-3"))
        self.GroupILP_History_LineEdit.setPlaceholderText(_translate("RWA_Window", "20-30"))
        self.GroupILP_History_Label.setText(_translate("RWA_Window", "      History   "))
        self.RW_toolBox.setItemText(self.RW_toolBox.indexOf(self.Group_ILP), _translate("RWA_Window", "Group ILP"))
        self.ILP_Margin_Label.setText(_translate("RWA_Window", "    Margin "))
        self.ILP_Margin_LineEdit.setPlaceholderText(_translate("RWA_Window", "3-7"))
        self.ILP_Processors_Label.setText(_translate("RWA_Window", " Processors"))
        self.ILP_Processors_LineEdit.setPlaceholderText(_translate("RWA_Window", "4"))
        self.ILP_K_Label.setText(_translate("RWA_Window", "        k     "))
        self.ILP_K_LineEdit.setPlaceholderText(_translate("RWA_Window", "3"))
        self.ILP_MaxNW_Label.setText(_translate("RWA_Window", "Maximum Number of Wavelengths"))
        self.ILP_MaxNW_LineEdit.setPlaceholderText(_translate("RWA_Window", "80"))
        self.ILP_Alpha_Label.setText(_translate("RWA_Window", "      Alpha  "))
        self.ILP_Alpha_LineEdit.setPlaceholderText(_translate("RWA_Window", "0.2"))
        self.RW_toolBox.setItemText(self.RW_toolBox.indexOf(self.ILP), _translate("RWA_Window", "ILP"))

    
    def ok_button_fun(self):
        index = self.RW_toolBox.currentIndex()
        if index == 0:
            merge = self.Mergin_DemandRe_LineEdit.currentText()
            alpha = self.Greedy_Alpha_LineEdit.text()
            margin = self.Greedy_Margin_LineEdit.text()
            iterations = self.Greedy_Iteration_LineEdit.text()
            processors = self.Greedy_Processors_LineEdit.text()
            k = self.Greedy_K_LineEdit.text()
            maxNW = self.Greedy_MaxNW_LineEdit.text()
            Algorithm = "Greedy"
            K_Restoration = self.Greedy_K_Restoration_LineEdit.text()
            numRandomChoices = self.Greedy_numRandomChoices_LineEdit.text()
            
            if (alpha and margin and iterations and processors and k and K_Restoration and numRandomChoices) != "":
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
                K_Restoration = int(K_Restoration)
                numRandomChoices = int(numRandomChoices)
                
                if maxNW == "":
                    maxNW = None
                else:
                    maxNW = int(maxNW)


                Data["ui"].RWA_procedure(merge, alpha, iterations, margin, processors, k, maxNW, None, None, Algorithm, K_Restoration, numRandomChoices)
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
            groupsize = self.GroupILP_Groupsize_LineEdit.text()
            history = self.GroupILP_History_LineEdit.text()
            Algorithm = "GroupILP"

            alpha = float(alpha)
            margin = int(margin)
            iterations = int(iterations)
            processors = int(processors)
            k = int(k)
            groupsize = int(groupsize)
            history = int(history)

            Data["ui"].RWA_procedure(None, alpha, iterations, margin, processors, k, maxNW, groupsize, history, Algorithm)
            bus["RWA_Window"].close()
        
        elif index == 2:
            alpha = self.ILP_Alpha_LineEdit.text()
            margin = self.ILP_Margin_LineEdit.text()
            processors = self.ILP_Processors_LineEdit.text()
            k = self.ILP_K_LineEdit.text()
            maxNW = self.ILP_MaxNW_LineEdit.text()
            Algorithm = "ILP"

            Data["ui"].RWA_procedure(None, alpha, None, margin, processors, k, maxNW, None, None, Algorithm)
            bus["RWA_Window"].close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RWA_Window = QtWidgets.QWidget()
    ui = Ui_RWA_Window()
    ui.setupUi(RWA_Window)
    RWA_Window.show()
    sys.exit(app.exec_())

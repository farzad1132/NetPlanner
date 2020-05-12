from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QApplication,QTableWidget,QTableWidgetItem,QFileDialog,QMdiSubWindow,QWidget,QLabel,QAbstractItemView,QListWidgetItem,QMenu,QFontComboBox
from PySide2.QtCore import SIGNAL,QObject,Slot
from PySide2.QtGui import QPixmap, QBrush, QColor
import pickle
import sys, os
import pandas as pd
from PySide2 import QtWebEngineWidgets
from PySide2.QtWebEngineWidgets import QWebEnginePage
import folium,random
from PySide2.QtCore import QUrl,Qt,QModelIndex
from PySide2.QtGui import QStandardItemModel
import re
from PySide2.QtWebChannel import QWebChannel
import branca
from branca.element import Element
import xlrd
import xlsxwriter
from pandas import ExcelWriter
from pandas import ExcelFile
from Common_Object_def import Network
import math
from math import ceil
import requests
import json
import socketio  
import time
import copy , warnings

from add_node import Ui_add_node_window
from grooming_window import Ui_grooming_window
from importui import Ui_ImportMenuUI
from RWA_window import Ui_RWA_Window
from Ui_files.new_ui import iconresources

from data import *
from grooming_algorithm import grooming_fun


from BLANK_Demand.BLANK_Demand import BLANK_Demand
from MP2X_Demand.MP2X_L_Demand import MP2X_L_Demand
from MP2X_Demand.MP2X_R_Demand import MP2X_R_Demand
from MP1H_Demand.MP1H_L_Demand import MP1H_L_Demand
from MP1H_Demand.MP1H_R_Demand import MP1H_R_Demand
from TP1H_Demand.TP1H_L_Demand import TP1H_L_Demand
from TP1H_Demand.TP1H_R_Demand import TP1H_R_Demand

from TrafficMatrixError.Source_type_error import Ui_Source_type_error
from TrafficMatrixError.ID_type_error import Ui_ID_type_error
from TrafficMatrixError.Destination_type_error import Ui_Destination_type_error
from TrafficMatrixError.Quantity_type_error import Ui_Quantity_type_error
from TrafficMatrixError.SLA_type_error import Ui_SLA_type_error

#from mapwidget import MapWidget
from mapwidget import MapWidget
import matplotlib as mpl
from  matplotlib.backends.backend_qt5agg  import  FigureCanvas
from  matplotlib.figure  import  Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
#from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import networkx as nx
import utm
import numpy

class Backend_map(QObject):

    @Slot(str)
    def Create_DataBase(self,text):
        print("last GateWay: ",text)
        self.LastGateWay = text

        # creating grouping database
        print("we are grouping")
        Data["Clustering"][text] = {}
        Data["Clustering"][text]["Color"] = ui.lastgroup_color
        Data["Clustering"][text]["Type"] = ui.lastgroup_type
        Data["Clustering"][text]["SubNodes"] = []


    
    @Slot(str,str)
    def SetNode_flag_fun(self,text,color = ""):
        print("SetNode_flag: ",text)
        self.SetNode_flag = text
        ui.SetNode_flag_javascript(text)
        ui.ColorTo_javascript(color)

        self.lastgroup_color = color
    
    @Slot(str)
    def SubNodeSelect_flag_fun(self,text):
        print("SunNodeSelect flag: ",text)
        self.SubNodeSelect_flag = text
        ui.SelectSubNode_flag_javascript(text)
    
    @Slot(str)
    def AddNode_DataBase(self,node):
        Data["Clustering"][self.LastGateWay]["SubNodes"].append(node)

    @Slot()
    def TurnSubNodeSelect_off(self):
        ui.SelectSubNode_button.toggle()


    @Slot(str)
    def change_tab_to4(self,degreename):
        degreename = degreename.strip()
        print(">>>>>>",degreename)

        if Data["Stage_flag"] == "Demand":
            Data["Clicked_Node"] = degreename

            if degreename in DemandTabDataBase["Source_Destination"]:
                Data["ui"].clicked_Node_flag = True
                Data["ui"].update_Demand_lightpath_list_flag = False
                Data["TabWidget"].setCurrentIndex(2)
                Data["ui"].update_Demand_lightpath_list_flag = True
                
                
                rep_source = DemandTabDataBase["Source_Destination"][degreename]["Source"]
                if rep_source == Data["Demand_Source_combo"].currentText():
                    Data["Demand_Source_combo"].setCurrentText(rep_source)
                    Data["ui"].Demand_Source_combobox_Change()
                else:
                    Data["Demand_Source_combo"].setCurrentText(rep_source)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")

        # NOTE: commented
        #MainWindow.resize(1198, 841)

        self.gridLayout = QtWidgets.QGridLayout(MainWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.tabWidget = QtWidgets.QTabWidget(MainWindow)
        self.tabWidget.setMinimumSize(QtCore.QSize(1125, 817))
        font = QtGui.QFont()
        font.setFamily("IRANSans")
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("QTabWidget::pane { /* The tab widget frame */\n"
"     border-top: 2px  #C0C0C0;\n"
" }\n"
"\n"
" \n"
"QTabWidget::tab-bar {\n"
"     alignment: left;\n"
" }\n"
" /* Style the tab using the tab sub-control. Note that\n"
"     it reads QTabBar _not_ QTabWidget */\n"
" QTabBar::tab {\n"
"     \n"
"    \n"
"     border: 2px solid gray;\n"
"     border-bottom-color: none; /* same as the pane color */\n"
"     border-top-left-radius: 0px;\n"
"     border-top-right-radius: 0px;\n"
"     min-width: 20ex;\n"
"     padding: 2px; \n"
"     \n"
"    \n"
"    font: 25 9pt \"Bahnschrift\";\n"
" }\n"
"\n"
"\n"
"\n"
" QTabBar::tab:selected {\n"
"    \n"
"    \n"
"    background-color:#AEC4E5; /* same as pane color */ \n"
"     \n"
"    font: 63 9pt \"Bahnschrift SemiBold\";\n"
" }\n"
"\n"
" QTabBar::tab:!selected {\n"
"     margin-top: -2px; /* make non-selected tabs look smaller */ \n"
"     \n"
" }\n"
"\n"
" /* make use of negative margins for overlapping tabs */\n"
" QTabBar::tab:selected {\n"
"     /* expand/overlap to the left and right by 4px */\n"
"     margin-left: -4px;\n"
"     margin-right: -4px;\n"
" }\n"
"\n"
" QTabBar::tab:first:selected {\n"
"     margin-left: 0; /* the first selected tab has nothing to overlap with on the left */\n"
" }\n"
"\n"
" QTabBar::tab:last:selected {\n"
"     margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
" }\n"
"\n"
" QTabBar::tab:only-one {\n"
"     margin: 0; /* if there is only one tab, we don\'t want overlapping margins */\n"
" }r")
        self.tabWidget.setObjectName("tabWidget")
        self.TopologyTab = QtWidgets.QWidget()
        self.TopologyTab.setObjectName("TopologyTab")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.TopologyTab)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.pushButton_6 = QtWidgets.QPushButton(self.TopologyTab)
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"    color: rgb(117, 117, 117);\n"
"    \n"
"    \n"
"    font: 75 9pt \"Bahnschrift Condensed\";\n"
"    \n"
"    border: 2px solid #8f8f91; min-width: 80px;\n"
"    border-color: #4072B3; \n"
"    border-radius: 15px;\n"
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
"}\n"
"")
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_11.addWidget(self.pushButton_6, 1, 1, 1, 1)
        self.webengine = QtWebEngineWidgets.QWebEngineView(self.TopologyTab)
        self.webengine.setMinimumSize(QtCore.QSize(1570, 840))
        self.webengine.setObjectName("webengine")
        self.gridLayout_11.addWidget(self.webengine, 2, 0, 1, 1)
        self.T_groupbox = QtWidgets.QGroupBox(self.TopologyTab)
        self.T_groupbox.setEnabled(True)
        self.T_groupbox.setMaximumSize(QtCore.QSize(300, 16777215))
        self.T_groupbox.setStyleSheet("QGroupBox {linea\n"
"    background-color: #C0C0C0;\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF0ECE, stop: 1 #FFFFFF);\n"
"}")
        self.T_groupbox.setTitle("")
        self.T_groupbox.setObjectName("T_groupbox")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.T_groupbox)
        self.gridLayout_14.setObjectName("gridLayout_14")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_14.addItem(spacerItem, 2, 0, 1, 1)
        self.ViewGroupbox = QtWidgets.QGroupBox(self.T_groupbox)
        self.ViewGroupbox.setStyleSheet("QGroupBox {\n"
"    \n"
"    background-color: #C0C0C0;\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin; \n"
"    font: 63 8pt \"Bahnschrift SemiBold\";\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #C0C0C0, stop: 1 #FFFFFF);\n"
"}")
        self.ViewGroupbox.setObjectName("ViewGroupbox")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.ViewGroupbox)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.Max_available_radiobutton = QtWidgets.QRadioButton(self.ViewGroupbox)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiCondensed")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Max_available_radiobutton.setFont(font)
        self.Max_available_radiobutton.setObjectName("Max_available_radiobutton")
        self.gridLayout_18.addWidget(self.Max_available_radiobutton, 0, 0, 1, 1)
        self.Max_Used_radiobutton = QtWidgets.QRadioButton(self.ViewGroupbox)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiCondensed")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.Max_Used_radiobutton.setFont(font)
        self.Max_Used_radiobutton.setObjectName("Max_Used_radiobutton")
        self.gridLayout_18.addWidget(self.Max_Used_radiobutton, 1, 0, 1, 1)
        self.Enable_google_view_checkbox = QtWidgets.QCheckBox(self.ViewGroupbox)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.Enable_google_view_checkbox.setFont(font)
        self.Enable_google_view_checkbox.setStyleSheet("")
        self.Enable_google_view_checkbox.setObjectName("Enable_google_view_checkbox")
        self.gridLayout_18.addWidget(self.Enable_google_view_checkbox, 2, 0, 1, 1)
        self.gridLayout_14.addWidget(self.ViewGroupbox, 1, 0, 1, 1)
        self.Grouping_groupbox = QtWidgets.QGroupBox(self.T_groupbox)
        self.Grouping_groupbox.setStyleSheet("QGroupBox {\n"
"    \n"
"    border: 2px solid #C0C0C0;\n"
"    border-radius: 5px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */ \n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin; \n"
"    font: 63 8pt \"Bahnschrift SemiBold\";\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #C0C0C0, stop: 1 #FFFFFF);\n"
"}")
        self.Grouping_groupbox.setObjectName("Grouping_groupbox")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.Grouping_groupbox)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.gridLayout_16 = QtWidgets.QGridLayout()
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.Cancel_button = QtWidgets.QPushButton(self.Grouping_groupbox)
        self.Cancel_button.setMinimumSize(QtCore.QSize(84, 20))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Cancel_button.setFont(font)
        self.Cancel_button.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"    font: 75 10pt \"Bahnschrift Condensed\";\n"
"    \n"
"    \n"
"    border:2px solid black; min-width: 80px;\n"
"    border-color: dark gray; \n"
"    border-radius: 25px;\n"
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
        self.Cancel_button.setObjectName("Cancel_button")
        self.gridLayout_16.addWidget(self.Cancel_button, 10, 0, 1, 1)
        self.SetGatewayNode_button = QtWidgets.QPushButton(self.Grouping_groupbox)
        self.SetGatewayNode_button.setMinimumSize(QtCore.QSize(84, 30))
        self.SetGatewayNode_button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.SetGatewayNode_button.setFont(font)
        self.SetGatewayNode_button.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"    font: 75 10pt \"Bahnschrift Condensed\";\n"
"    \n"
"    border: 2px solid #8f8f91; min-width: 80px;\n"
"    border-color: #EB8686; \n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FFFFFF, stop: 1 #EB8686);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"} \n"
"QPushButton:hover{ \n"
"    background-color: #EB8686 \n"
"\n"
"}")
        self.SetGatewayNode_button.setObjectName("SetGatewayNode_button")
        self.gridLayout_16.addWidget(self.SetGatewayNode_button, 5, 0, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_16.addItem(spacerItem1, 2, 0, 1, 1)
        self.select_Sub_Nodes_labe = QtWidgets.QLabel(self.Grouping_groupbox)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(10)
        self.select_Sub_Nodes_labe.setFont(font)
        self.select_Sub_Nodes_labe.setObjectName("select_Sub_Nodes_labe")
        self.gridLayout_16.addWidget(self.select_Sub_Nodes_labe, 7, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_16.addItem(spacerItem2, 6, 0, 1, 2)
        self.SelectSubNode_button = QtWidgets.QPushButton(self.Grouping_groupbox)
        self.SelectSubNode_button.setMinimumSize(QtCore.QSize(84, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.SelectSubNode_button.setFont(font)
        self.SelectSubNode_button.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"    font: 75 9pt \"Bahnschrift Condensed\";\n"
"    \n"
"    \n"
"    border: 2px solid #8f8f91; min-width: 80px;\n"
"    border-color: #c0c0c0; \n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    \n"
"    border-color:#Eb8686 ;\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        self.SelectSubNode_button.setCheckable(True)
        self.SelectSubNode_button.setObjectName("SelectSubNode_button")
        self.gridLayout_16.addWidget(self.SelectSubNode_button, 7, 1, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_16.addItem(spacerItem3, 9, 0, 1, 1)
        self.OK_button = QtWidgets.QPushButton(self.Grouping_groupbox)
        self.OK_button.setMinimumSize(QtCore.QSize(84, 20))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.OK_button.setFont(font)
        self.OK_button.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"    font: 75 10pt \"Bahnschrift Condensed\";\n"
"    \n"
"    \n"
"    border:2px solid black; min-width: 80px;\n"
"    border-color: dark gray; \n"
"    border-radius: 25px;\n"
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
        self.OK_button.setObjectName("OK_button")
        self.gridLayout_16.addWidget(self.OK_button, 10, 1, 1, 2)
        self.ShowSubNodes = QtWidgets.QCheckBox(self.Grouping_groupbox)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        font.setItalic(True)
        self.ShowSubNodes.setFont(font)
        self.ShowSubNodes.setStyleSheet("")
        self.ShowSubNodes.setObjectName("ShowSubNodes")
        self.gridLayout_16.addWidget(self.ShowSubNodes, 11, 0, 1, 2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_16.addItem(spacerItem4, 4, 0, 1, 1)
        self.GroupColor = QtWidgets.QLabel(self.Grouping_groupbox)
        self.GroupColor.setStyleSheet("  QLabel {\n"
"    \n"
"    \n"
"    \n"
"    font: 75 10pt \"Bahnschrift Condensed\";\n"
"    \n"
"   \n"
"}")
        self.GroupColor.setObjectName("GroupColor")
        self.gridLayout_16.addWidget(self.GroupColor, 3, 0, 1, 1)
        self.GroupID = QtWidgets.QLabel(self.Grouping_groupbox)
        self.GroupID.setStyleSheet(" QLabel {\n"
"    \n"
"  \n"
"    \n"
"    font: 75 10pt \"Bahnschrift Condensed\";\n"
"    \n"
"    \n"
"}")
        self.GroupID.setObjectName("GroupID")
        self.gridLayout_16.addWidget(self.GroupID, 1, 0, 1, 1)
        self.cluster_type_combobox = QtWidgets.QComboBox(self.Grouping_groupbox)
        self.cluster_type_combobox.setStyleSheet("QComboBox {\n"
"    \n"
"    border-radius: 0px;\n"
"    padding: 1px 18px 1px 5px;\n"
"    min-width: 6em; \n"
"    \n"
"    border:1px solid rgb(0, 139, 208);\n"
"    \n"
"    font: 9pt \"Bahnschrift\";\n"
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
"   \n"
"}")
        self.cluster_type_combobox.setEditable(True)
        self.cluster_type_combobox.setObjectName("cluster_type_combobox")
        self.gridLayout_16.addWidget(self.cluster_type_combobox, 1, 1, 1, 2)
        self.ClusterColor_combobox = QtWidgets.QComboBox(self.Grouping_groupbox)
        self.ClusterColor_combobox.setStyleSheet("QComboBox {\n"
"    \n"
"    border-radius: 0px;\n"
"    padding: 1px 18px 1px 5px;\n"
"    min-width: 6em; \n"
"    \n"
"    border:1px solid rgb(0, 139, 208);\n"
"    \n"
"    font: 9pt \"Bahnschrift\";\n"
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
"   \n"
"}")
        self.ClusterColor_combobox.setEditable(True)
        self.ClusterColor_combobox.setObjectName("ClusterColor_combobox")
        self.gridLayout_16.addWidget(self.ClusterColor_combobox, 3, 1, 1, 2)
        self.gridLayout_17.addLayout(self.gridLayout_16, 0, 0, 1, 1)
        self.gridLayout_14.addWidget(self.Grouping_groupbox, 0, 0, 1, 1)
        self.gridLayout_11.addWidget(self.T_groupbox, 2, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.import_button = QtWidgets.QPushButton(self.TopologyTab)
        self.import_button.setMaximumSize(QtCore.QSize(81, 50))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.import_button.setFont(font)
        self.import_button.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"    font: 75 10pt \"Bahnschrift Condensed\";\n"
"    \n"
"    color: rgb(117, 117, 117);\n"
"    border: 2px solid #8f8f91; min-width: 80px;\n"
"    border-color: #4072B3; \n"
"    border-radius: 25px;\n"
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
        self.import_button.setObjectName("import_button")
        self.horizontalLayout_3.addWidget(self.import_button)
        self.export_result_button = QtWidgets.QPushButton(self.TopologyTab)
        self.export_result_button.setMaximumSize(QtCore.QSize(81, 50))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.export_result_button.setFont(font)
        self.export_result_button.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"    font: 75 10pt \"Bahnschrift Condensed\";\n"
"    \n"
"    color: rgb(117, 117, 117);\n"
"    border: 2px solid #8f8f91; min-width: 80px;\n"
"    border-color: #4072B3; \n"
"    border-radius: 25px;\n"
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
        self.export_result_button.setObjectName("export_result_button")
        self.horizontalLayout_3.addWidget(self.export_result_button)
        self.add_node_button = QtWidgets.QPushButton(self.TopologyTab)
        self.add_node_button.setMaximumSize(QtCore.QSize(81, 50))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.add_node_button.setFont(font)
        self.add_node_button.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"    font: 75 10pt \"Bahnschrift Condensed\";\n"
"    \n"
"    color: rgb(117, 117, 117);\n"
"    border: 2px solid #8f8f91; min-width: 80px;\n"
"    border-color: #4072B3; \n"
"    border-radius: 25px;\n"
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
        self.add_node_button.setObjectName("add_node_button")
        self.horizontalLayout_3.addWidget(self.add_node_button)
        self.groupBox = QtWidgets.QGroupBox(self.TopologyTab)
        self.groupBox.setEnabled(True)
        self.groupBox.setMinimumSize(QtCore.QSize(294, 81))
        self.groupBox.setMaximumSize(QtCore.QSize(294, 81))
        self.groupBox.setStyleSheet("QGroupBox {\n"
"    \n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin; \n"
"    font: 63 8pt \"Bahnschrift SemiBold\";\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #C0C0C0, stop: 1 #FFFFFF);\n"
"}")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Grooming_pushbutton = QtWidgets.QPushButton(self.groupBox)
        self.Grooming_pushbutton.setMinimumSize(QtCore.QSize(84, 0))
        self.Grooming_pushbutton.setMaximumSize(QtCore.QSize(81, 50))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Grooming_pushbutton.setFont(font)
        self.Grooming_pushbutton.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"    font: 75 10pt \"Bahnschrift Condensed\";\n"
"    \n"
"    border: 2px solid #8f8f91; min-width: 80px;\n"
"    border-color: #EB8686; \n"
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
        self.Grooming_pushbutton.setCheckable(False)
        self.Grooming_pushbutton.setObjectName("Grooming_pushbutton")
        self.horizontalLayout_2.addWidget(self.Grooming_pushbutton)
        self.RWA_pushbutton = QtWidgets.QPushButton(self.groupBox)
        self.RWA_pushbutton.setMinimumSize(QtCore.QSize(84, 0))
        self.RWA_pushbutton.setMaximumSize(QtCore.QSize(81, 50))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.RWA_pushbutton.setFont(font)
        self.RWA_pushbutton.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"    font: 75 10pt \"Bahnschrift Condensed\";\n"
"    \n"
"    border: 2px solid #8f8f91; min-width: 80px;\n"
"    border-color: #EB8686; \n"
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
        self.RWA_pushbutton.setObjectName("RWA_pushbutton")
        self.horizontalLayout_2.addWidget(self.RWA_pushbutton)
        self.FinalPlan_pushbutton = QtWidgets.QPushButton(self.groupBox)
        self.FinalPlan_pushbutton.setEnabled(True)
        self.FinalPlan_pushbutton.setMaximumSize(QtCore.QSize(81, 50))
        palette = QtGui.QPalette()
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(246, 247, 250))
        gradient.setColorAt(1.0, QtGui.QColor(218, 219, 222))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(246, 247, 250))
        gradient.setColorAt(1.0, QtGui.QColor(218, 219, 222))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(246, 247, 250))
        gradient.setColorAt(1.0, QtGui.QColor(218, 219, 222))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(246, 247, 250))
        gradient.setColorAt(1.0, QtGui.QColor(218, 219, 222))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(246, 247, 250))
        gradient.setColorAt(1.0, QtGui.QColor(218, 219, 222))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(246, 247, 250))
        gradient.setColorAt(1.0, QtGui.QColor(218, 219, 222))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(246, 247, 250))
        gradient.setColorAt(1.0, QtGui.QColor(218, 219, 222))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(246, 247, 250))
        gradient.setColorAt(1.0, QtGui.QColor(218, 219, 222))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(246, 247, 250))
        gradient.setColorAt(1.0, QtGui.QColor(218, 219, 222))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.FinalPlan_pushbutton.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.FinalPlan_pushbutton.setFont(font)
        self.FinalPlan_pushbutton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.FinalPlan_pushbutton.setMouseTracking(False)
        self.FinalPlan_pushbutton.setTabletTracking(False)
        self.FinalPlan_pushbutton.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.FinalPlan_pushbutton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.FinalPlan_pushbutton.setAutoFillBackground(False)
        self.FinalPlan_pushbutton.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"    font: 75 10pt \"Bahnschrift Condensed\";\n"
"    \n"
"    border: 2px solid #8f8f91; min-width: 80px;\n"
"    border-color: #EB8686; \n"
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
        self.FinalPlan_pushbutton.setIconSize(QtCore.QSize(20, 20))
        self.FinalPlan_pushbutton.setAutoRepeatDelay(295)
        self.FinalPlan_pushbutton.setObjectName("FinalPlan_pushbutton")
        self.horizontalLayout_2.addWidget(self.FinalPlan_pushbutton)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.groupBox)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.gridLayout_11.addLayout(self.horizontalLayout_3, 0, 0, 2, 1)
        self.tabWidget.addTab(self.TopologyTab, "")
        self.TrafficMatrixTab = QtWidgets.QWidget()
        self.TrafficMatrixTab.setObjectName("TrafficMatrixTab")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.TrafficMatrixTab)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.splitter_2 = QtWidgets.QSplitter(self.TrafficMatrixTab)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.General_TM = QtWidgets.QTableWidget(self.splitter_2)
        self.General_TM.setStyleSheet("QTableWidget {\n"
"    \n"
"    \n"
"    selection-background-color: #C0C0C0\n"
"}\n"
"QTableWidget QTableCornerButton::section {\n"
"    background: #EB8686;\n"
"  }")
        self.General_TM.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.General_TM.setLineWidth(1)
        self.General_TM.setDragDropOverwriteMode(True)
        self.General_TM.setAlternatingRowColors(False)
        self.General_TM.setRowCount(20)
        self.General_TM.setColumnCount(9)
        self.General_TM.setObjectName("General_TM")
        item = QtWidgets.QTableWidgetItem()
        self.General_TM.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.General_TM.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.General_TM.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.General_TM.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.General_TM.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.General_TM.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.General_TM.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.General_TM.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.General_TM.setHorizontalHeaderItem(8, item)
        self.Traffic_matrix = QtWidgets.QTableWidget(self.splitter_2)
        self.Traffic_matrix.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Traffic_matrix.setStyleSheet("QTableWidget {\n"
"    \n"
"    \n"
"    selection-background-color: #C0C0C0 ;\n"
"  \n"
"    \n"
"}\n"
"QTableWidget QTableCornerButton::section {\n"
"    background: #EB8686;\n"
"  }")
        self.Traffic_matrix.setAlternatingRowColors(False)
        self.Traffic_matrix.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.Traffic_matrix.setShowGrid(True)
        self.Traffic_matrix.setGridStyle(QtCore.Qt.SolidLine)
        self.Traffic_matrix.setRowCount(20)
        self.Traffic_matrix.setColumnCount(10)
        self.Traffic_matrix.setObjectName("Traffic_matrix")
        self.Traffic_matrix.horizontalHeader().setCascadingSectionResizes(True)
        self.Traffic_matrix.horizontalHeader().setDefaultSectionSize(125)
        self.Traffic_matrix.horizontalHeader().setSortIndicatorShown(False)
        self.Traffic_matrix.verticalHeader().setSortIndicatorShown(True)
        self.Traffic_matrix.verticalHeader().setStretchLastSection(False)
        self.gridLayout_12.addWidget(self.splitter_2, 0, 0, 1, 1)
        self.TM_groupbox = QtWidgets.QGroupBox(self.TrafficMatrixTab)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        font.setItalic(True)
        self.TM_groupbox.setFont(font)
        self.TM_groupbox.setMouseTracking(False)
        self.TM_groupbox.setAccessibleDescription("")
        self.TM_groupbox.setFlat(True)
        self.TM_groupbox.setCheckable(True)
        self.TM_groupbox.setChecked(True)
        self.TM_groupbox.setObjectName("TM_groupbox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.TM_groupbox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_7 = QtWidgets.QLabel(self.TM_groupbox)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("QLabel {\n"
"  \n"
"    \n"
"    font: 63 12pt \"Bahnschrift SemiBold Condensed\";\n"
"    background-color:  #6088C6;\n"
"}")
        self.label_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 0, 0, 1, 1)
        self.listWidget = QtWidgets.QListWidget(self.TM_groupbox)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("QListWidget {\n"
"    alternate-background-color: yellow;\n"
"    border:2px double;\n"
"    border-color: #6088C6;\n"
"    border-radius: 5px; \n"
"    \n"
"}\n"
"QListWidget {\n"
"    show-decoration-selected: 1; /* make the selection span the entire width of the view */\n"
"}\n"
"\n"
"QListWidget::item:alternate {\n"
"    background: #EEEEEE;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    border: 1px solid #6a6ea9;\n"
"}\n"
"\n"
"QListWidget::item:selected:!active {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #ABAFE5, stop: 1 #8588B2);\n"
"}\n"
"\n"
"QListWidget::item:selected:active {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #6a6ea9, stop: 1 #888dd9);\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #FAFBFE, stop: 1 #DCDEF1);\n"
"}")
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.gridLayout_5.addWidget(self.listWidget, 1, 0, 1, 2)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem6, 4, 0, 1, 1)
        self.SaveChanges_button = QtWidgets.QPushButton(self.TM_groupbox)
        self.SaveChanges_button.setMinimumSize(QtCore.QSize(84, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.SaveChanges_button.setFont(font)
        self.SaveChanges_button.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"    font: 75 11pt \"Bahnschrift Condensed\";\n"
"    \n"
"    border: 2px solid #8f8f91; min-width: 80px;\n"
"    border-color: #EB8686; \n"
"    border-radius: 15px;\n"
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
        self.SaveChanges_button.setObjectName("SaveChanges_button")
        self.gridLayout_5.addWidget(self.SaveChanges_button, 2, 0, 2, 2)
        self.gridLayout_12.addWidget(self.TM_groupbox, 0, 1, 1, 1)
        self.tabWidget.addTab(self.TrafficMatrixTab, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.splitter = QtWidgets.QSplitter(self.tab)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setHandleWidth(6)
        self.splitter.setObjectName("splitter")
        self.Demand_tab = QtWidgets.QTabWidget(self.splitter)
        self.Demand_tab.setEnabled(True)
        self.Demand_tab.setMinimumSize(QtCore.QSize(0, 100))
        self.Demand_tab.setObjectName("Demand_tab")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tab_8)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.DemandPanel_1 = QtWidgets.QWidget(self.tab_8)
        self.DemandPanel_1.setObjectName("DemandPanel_1")
        self.horizontalLayout_4.addWidget(self.DemandPanel_1)
        self.DemandPanel_2 = QtWidgets.QWidget(self.tab_8)
        self.DemandPanel_2.setObjectName("DemandPanel_2")
        self.horizontalLayout_4.addWidget(self.DemandPanel_2)
        self.DemandPanel_3 = QtWidgets.QWidget(self.tab_8)
        self.DemandPanel_3.setObjectName("DemandPanel_3")
        self.horizontalLayout_4.addWidget(self.DemandPanel_3)
        self.DemandPanel_4 = QtWidgets.QWidget(self.tab_8)
        self.DemandPanel_4.setObjectName("DemandPanel_4")
        self.horizontalLayout_4.addWidget(self.DemandPanel_4)
        self.DemandPanel_5 = QtWidgets.QWidget(self.tab_8)
        self.DemandPanel_5.setObjectName("DemandPanel_5")
        self.horizontalLayout_4.addWidget(self.DemandPanel_5)
        self.DemandPanel_6 = QtWidgets.QWidget(self.tab_8)
        self.DemandPanel_6.setObjectName("DemandPanel_6")
        self.horizontalLayout_4.addWidget(self.DemandPanel_6)
        self.DemandPanel_7 = QtWidgets.QWidget(self.tab_8)
        self.DemandPanel_7.setObjectName("DemandPanel_7")
        self.horizontalLayout_4.addWidget(self.DemandPanel_7)
        self.DemandPanel_8 = QtWidgets.QWidget(self.tab_8)
        self.DemandPanel_8.setObjectName("DemandPanel_8")
        self.horizontalLayout_4.addWidget(self.DemandPanel_8)
        self.DemandPanel_9 = QtWidgets.QWidget(self.tab_8)
        self.DemandPanel_9.setObjectName("DemandPanel_9")
        self.horizontalLayout_4.addWidget(self.DemandPanel_9)
        self.DemandPanel_10 = QtWidgets.QWidget(self.tab_8)
        self.DemandPanel_10.setObjectName("DemandPanel_10")
        self.horizontalLayout_4.addWidget(self.DemandPanel_10)
        self.DemandPanel_11 = QtWidgets.QWidget(self.tab_8)
        self.DemandPanel_11.setObjectName("DemandPanel_11")
        self.horizontalLayout_4.addWidget(self.DemandPanel_11)
        self.DemandPanel_12 = QtWidgets.QWidget(self.tab_8)
        self.DemandPanel_12.setObjectName("DemandPanel_12")
        self.horizontalLayout_4.addWidget(self.DemandPanel_12)
        self.DemandPanel_13 = QtWidgets.QWidget(self.tab_8)
        self.DemandPanel_13.setObjectName("DemandPanel_13")
        self.horizontalLayout_4.addWidget(self.DemandPanel_13)
        self.DemandPanel_14 = QtWidgets.QWidget(self.tab_8)
        self.DemandPanel_14.setObjectName("DemandPanel_14")
        self.horizontalLayout_4.addWidget(self.DemandPanel_14)
        self.Demand_tab.addTab(self.tab_8, "")
        self.MapWidget = MapWidget(self.splitter)
        self.MapWidget.setMinimumSize(QtCore.QSize(821, 259))
        self.MapWidget.setObjectName("MapWidget")
        self.line = QtWidgets.QFrame(self.MapWidget)
        self.line.setGeometry(QtCore.QRect(-340, -10, 2341, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.gridLayout_4.addWidget(self.splitter, 1, 1, 1, 3)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setMinimumSize(QtCore.QSize(120, 0))
        self.label_8.setMaximumSize(QtCore.QSize(62, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("QLabel {\n"
"    border: 2px solid gray;\n"
"    border-color: rgb(64, 114, 179);\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}")
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.Demand_Destination_combobox = QtWidgets.QComboBox(self.tab)
        self.Demand_Destination_combobox.setMinimumSize(QtCore.QSize(121, 30))
        self.Demand_Destination_combobox.setStyleSheet("QComboBox {\n"
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
"   \n"
"}")
        self.Demand_Destination_combobox.setEditable(True)
        self.Demand_Destination_combobox.setObjectName("Demand_Destination_combobox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Demand_Destination_combobox)
        self.gridLayout_4.addLayout(self.formLayout, 0, 3, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Demand_LineList = QtWidgets.QListWidget(self.tab)
        self.Demand_LineList.setMinimumSize(QtCore.QSize(256, 133))
        self.Demand_LineList.setMaximumSize(QtCore.QSize(256, 133))
        self.Demand_LineList.setStyleSheet("QListWidget {\n"
"    alternate-background-color: yellow;\n"
"    border:2px double;\n"
"    border-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #6a6ea9, stop: 1 #Eb8686);\n"
"\n"
"    border-radius: 5px; \n"
"    \n"
"}\n"
"QListWidget {\n"
"    show-decoration-selected: 1; /* make the selection span the entire width of the view */\n"
"}\n"
"\n"
"QListWidget::item:alternate {\n"
"    background: rgb(170, 170, 170);\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    border: 1px solid #6a6ea9;\n"
"}\n"
"\n"
"QListWidget::item:selected:!active {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #ABAFE5, stop: 1 #EE817B);\n"
"}\n"
"\n"
"QListWidget::item:selected:active {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #6a6ea9, stop: 1 #Eb8686);\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #FAFBFE, stop: 1 #FFB2AE);\n"
"}")
        self.Demand_LineList.setObjectName("Demand_LineList")
        self.gridLayout_2.addWidget(self.Demand_LineList, 3, 0, 1, 1)
        self.ClientLabel_20 = QtWidgets.QLabel(self.tab)
        self.ClientLabel_20.setMinimumSize(QtCore.QSize(256, 30))
        self.ClientLabel_20.setMaximumSize(QtCore.QSize(256, 16))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.ClientLabel_20.setFont(font)
        self.ClientLabel_20.setStyleSheet("  QLabel {\n"
"    \n"
"    font: 63 12pt \"Bahnschrift SemiBold Condensed\";\n"
"   \n"
"  \n"
"    background-color: rgb(235, 134, 134);\n"
"}")
        self.ClientLabel_20.setObjectName("ClientLabel_20")
        self.gridLayout_2.addWidget(self.ClientLabel_20, 6, 0, 1, 1)
        self.ClientLabel_23 = QtWidgets.QLabel(self.tab)
        self.ClientLabel_23.setMinimumSize(QtCore.QSize(256, 30))
        self.ClientLabel_23.setMaximumSize(QtCore.QSize(256, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.ClientLabel_23.setFont(font)
        self.ClientLabel_23.setStyleSheet(" QLabel {\n"
"  \n"
"    \n"
"    font: 63 12pt \"Bahnschrift SemiBold Condensed\";\n"
"    background-color:  #6088C6;\n"
"}")
        self.ClientLabel_23.setObjectName("ClientLabel_23")
        self.gridLayout_2.addWidget(self.ClientLabel_23, 4, 0, 1, 1)
        self.groomout10_list = QtWidgets.QListWidget(self.tab)
        self.groomout10_list.setMinimumSize(QtCore.QSize(256, 135))
        self.groomout10_list.setMaximumSize(QtCore.QSize(256, 135))
        self.groomout10_list.setStyleSheet("QListWidget {\n"
"    alternate-background-color: yellow;\n"
"    border:2px double;\n"
"    border-color:#EB8686;\n"
"    border-radius: 5px; \n"
"    \n"
"}\n"
"QListWidget {\n"
"    show-decoration-selected: 1; /* make the selection span the entire width of the view */\n"
"}\n"
"\n"
"QListWidget::item:alternate {\n"
"    background: rgb(170, 170, 170);\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    border: 1px solid #6a6ea9;\n"
"}\n"
"\n"
"QListWidget::item:selected:!active {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #ABAFE5, stop: 1 #EE817B);\n"
"}\n"
"\n"
"QListWidget::item:selected:active {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #FFB2AE, stop: 1 #B22222);\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #FAFBFE, stop: 1 #FFB2AE);\n"
"}")
        self.groomout10_list.setObjectName("groomout10_list")
        self.gridLayout_2.addWidget(self.groomout10_list, 7, 0, 1, 1)
        self.Demand_ServiceList = QtWidgets.QListWidget(self.tab)
        self.Demand_ServiceList.setMinimumSize(QtCore.QSize(256, 133))
        self.Demand_ServiceList.setMaximumSize(QtCore.QSize(256, 133))
        self.Demand_ServiceList.setStyleSheet("QListWidget {\n"
"    alternate-background-color: yellow;\n"
"    border:2px double;\n"
"    border-color: #6088C6;\n"
"    border-radius: 5px; \n"
"    \n"
"}\n"
"QListWidget {\n"
"    show-decoration-selected: 1; /* make the selection span the entire width of the view */\n"
"}\n"
"\n"
"QListWidget::item:alternate {\n"
"    background: #EEEEEE;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    border: 1px solid #6a6ea9;\n"
"}\n"
"\n"
"QListWidget::item:selected:!active {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #ABAFE5, stop: 1 #8588B2);\n"
"}\n"
"\n"
"QListWidget::item:selected:active {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #6a6ea9, stop: 1 #888dd9);\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"    border: 2px solid #6a6ea9; \n"
"    background : #C0C0C0\n"
"}")
        self.Demand_ServiceList.setObjectName("Demand_ServiceList")
        self.gridLayout_2.addWidget(self.Demand_ServiceList, 5, 0, 1, 1)
        self.ClientLabel_21 = QtWidgets.QLabel(self.tab)
        self.ClientLabel_21.setMinimumSize(QtCore.QSize(256, 30))
        self.ClientLabel_21.setMaximumSize(QtCore.QSize(256, 16))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.ClientLabel_21.setFont(font)
        self.ClientLabel_21.setStyleSheet(" QLabel {\n"
"    \n"
"    font: 63 12pt \"Bahnschrift SemiBold Condensed\";\n"
"   \n"
"  \n"
"    \n"
"    background-color:#D0D0D0;\n"
"}")
        self.ClientLabel_21.setObjectName("ClientLabel_21")
        self.gridLayout_2.addWidget(self.ClientLabel_21, 0, 0, 1, 1)
        self.Demand_PanelList = QtWidgets.QListWidget(self.tab)
        self.Demand_PanelList.setMinimumSize(QtCore.QSize(256, 130))
        self.Demand_PanelList.setMaximumSize(QtCore.QSize(256, 130))
        self.Demand_PanelList.setStyleSheet("QListWidget {\n"
"    alternate-background-color: yellow;\n"
"    border:2px double;\n"
"    border-color: #c0c0c0;\n"
"    border-radius: 5px; \n"
"    \n"
"}\n"
"QListWidget {\n"
"    show-decoration-selected: 1; /* make the selection span the entire width of the view */\n"
"}\n"
"\n"
"QListWidget::item:alternate {\n"
"    background:rgb(170, 170, 170)\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    border: 1px solid #6a6ea9;\n"
"}\n"
"\n"
"\n"
"\n"
"QListWidget::item:selected:active {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #DCDCDC, stop: 1 #A9A9A9);\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #F8F8F8, stop: 1 #F5F5F5);\n"
"}")
        self.Demand_PanelList.setObjectName("Demand_PanelList")
        self.gridLayout_2.addWidget(self.Demand_PanelList, 1, 0, 1, 1)
        self.ClientLabel_22 = QtWidgets.QLabel(self.tab)
        self.ClientLabel_22.setMinimumSize(QtCore.QSize(256, 30))
        self.ClientLabel_22.setMaximumSize(QtCore.QSize(256, 16))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.ClientLabel_22.setFont(font)
        self.ClientLabel_22.setStyleSheet("QLabel {\n"
"    \n"
"    font: 63 12pt \"Bahnschrift SemiBold Condensed\";\n"
"   \n"
"  \n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #6a6ea9, stop: 1 #Eb8686);\n"
"}\n"
"")
        self.ClientLabel_22.setObjectName("ClientLabel_22")
        self.gridLayout_2.addWidget(self.ClientLabel_22, 2, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setObjectName("formLayout_4")
        self.SelectNode_Label_13 = QtWidgets.QLabel(self.tab)
        self.SelectNode_Label_13.setMinimumSize(QtCore.QSize(80, 0))
        self.SelectNode_Label_13.setMaximumSize(QtCore.QSize(43, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.SelectNode_Label_13.setFont(font)
        self.SelectNode_Label_13.setStyleSheet(" QLabel {\n"
"    border: 2px solid gray;\n"
"    border-color: rgb(64, 114, 179);\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}")
        self.SelectNode_Label_13.setObjectName("SelectNode_Label_13")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.SelectNode_Label_13)
        self.Demand_Source_combobox = QtWidgets.QComboBox(self.tab)
        self.Demand_Source_combobox.setMinimumSize(QtCore.QSize(121, 30))
        self.Demand_Source_combobox.setStyleSheet("QComboBox {\n"
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
"   \n"
"}")
        self.Demand_Source_combobox.setEditable(True)
        self.Demand_Source_combobox.setObjectName("Demand_Source_combobox")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Demand_Source_combobox)
        self.gridLayout_4.addLayout(self.formLayout_4, 0, 0, 1, 1)
        self.SplitterEventLabel = QtWidgets.QLabel(self.tab)
        self.SplitterEventLabel.setText("")
        self.SplitterEventLabel.setObjectName("SplitterEventLabel")
        self.gridLayout_4.addWidget(self.SplitterEventLabel, 0, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem7, 0, 2, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.gridLayout_10.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_10, 0, 0, 1, 1)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.Demand_tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        # NOTE: added

        self.Demand_Source_combobox.clear()
        self.Demand_Destination_combobox.clear()
        self.cluster_type_combobox.clear()
        self.ClusterColor_combobox.clear()
        
        ClusterColors = ["green", "blue", "purple", "orange", "yellow", "red"]
        self.ClusterColor_combobox.addItems(ClusterColors)

        ClusterTypes = ["100GE", "10GE", "100GE and 10GE"]
        self.cluster_type_combobox.addItems(ClusterTypes)

        DemandPanels = ["MP2X" , "MP1H", "TP1H"]


        DemandTabPanels = ["MP2X", "PS6X", "MP1H", "TP1H"]
        self.Demand_PanelList.addItems(DemandTabPanels)
        self.Demand_PanelList.setDragEnabled(True)

        self.tabWidget.setCurrentIndex(0)

        self.add_node_button.clicked.connect(self.add_node_button_fun)
        self.m = folium.Map(location=[35.6892,51.3890],zoom_start=6)
        self.m.save("map.html")
        Data["Map_Var"] = self.m
        Data["Web_Engine"] = self.webengine
        self.webengine.load(QUrl.fromLocalFile(os.path.abspath('map.html')))
        self.webengine.show()

        # NOTE: uncomment bellow if you want use console.log

        """ class WebEnginePage(QWebEnginePage):
            def javaScriptConsoleMessage(self, level, message, lineNumber, sourceID):
                print("javaScriptConsoleMessage: ", level, message, lineNumber, sourceID)

        self.webengine.setPage(WebEnginePage(self.webengine)) """
        backend_map = Backend_map(MainWindow)
        self.backend_map = backend_map
        channel = QWebChannel(MainWindow)
        channel.registerObject('backend_map', backend_map)
        self.webengine.page().setWebChannel(channel)

        self.Traffic_matrix.cellChanged.connect(self.TM_CellChange_fun)

        self.General_TM.cellChanged.connect(self.GTM_CellChange_fun)

        #.LoadTM_button.clicked.connect(self.LoadTM_fun)


        self.panels_name = ["BAF3","BLANK","LAF3","MP1H","MP2D","MP2X","OS5","PAF3","SC","SM2","TP1H","TP2X","TPAX","WS4"]

        self.SaveChanges_button.clicked.connect(self.SaveChanges_button_fun)

        self.tabWidget.currentChanged["int"].connect(self.main_tab_clicked)

        

        MainWindow.showMaximized()

        self.TMSliderBar = self.Traffic_matrix.verticalScrollBar()
		
        self.GMTSliderBar = self.General_TM.verticalScrollBar()
        QObject.connect(self.TMSliderBar,SIGNAL("actionTriggered(int)"),self.SyncScroll_1)
        QObject.connect(self.GMTSliderBar,SIGNAL("actionTriggered(int)"),self.SyncScroll_2)

        self.export_result_button.clicked.connect(self.export_excel_fun)

        #self.OpenTopology_button.clicked.connect(self.OpenTopology_fun)

        #self.ShelfTab.setStyleSheet("QTabBar::tab:selected {background-color: #4FA600}")

        Data["TabWidget"] = self.tabWidget

        self.network = Network()


        self.listWidget.clicked['QModelIndex'].connect(self.list_click)

        self.SelectSubNode_button.setChecked(True)
        #self.SelectSubNode_button.setText("Off")

        self.SetGatewayNode_button.clicked.connect(self.SetNode_gateway_fun)

        self.SelectSubNode_button.toggled["bool"].connect(self.SelectSubNode_button_fun)
        self.CurrentDegreename = None

        self.Demand_Source_combobox.currentTextChanged.connect(self.Demand_Source_combobox_Change)
        self.Demand_Destination_combobox.currentTextChanged.connect(self.Demand_Destination_combobox_change)

        #Data["Demand_mdi"] = self.Demand_mdi

        #self.OpenLinks_pushbutton.clicked.connect(self.open_links_fun)

        self.OK_button.clicked.connect(self.OK_button_fun)

        Data["Stage_flag"] = "Demand"
        Data["Demand_Source_combo"] = self.Demand_Source_combobox

        Data["Demand_LightPath_list"] = self.Demand_LineList
        Data["Demand_Service_list"] = self.Demand_ServiceList

        

        self.Demand_ServiceList.setDragEnabled(True)
        self.Demand_LineList.setDragEnabled(True)

        self.Grooming_pushbutton.clicked.connect(self.grooming_button_fun)
        self.RWA_pushbutton.clicked.connect(self.open_RWA_window_fun)
        self.FinalPlan_pushbutton.clicked.connect(self.create_obj)

        self.window = MainWindow

        Data["NetworkObj"] = self.network

        #self.Demand_LineList.clicked['QModelIndex'].connect(self.Demand_LineList_fun)
        self.Demand_LineList.currentItemChanged['QListWidgetItem*','QListWidgetItem*'].connect(self.Demand_LineList_fun)

        self.groomout10_list.currentItemChanged['QListWidgetItem*','QListWidgetItem*'].connect(self.groomout10_list_fun)

        self.import_button.clicked.connect(self.open_ImportUI_fun)

        #self.Demand_Shelf_set()

        self.Enable_google_view_checkbox.stateChanged["int"].connect(self.google_map_view)

        self.Max_Used_radiobutton.toggled["bool"].connect(self.change_radiobuttons_state)
        self.Max_available_radiobutton.toggled["bool"].connect(self.change_radiobuttons_state)

        Data["Service_item_num"] = 0
        Data["LightPath_item_num"] = 0

        Data["GroomOu10_list"] = self.groomout10_list

        self.groomout10_list.setDragEnabled(True)

        self.ShowSubNodes.stateChanged["int"].connect(self.show_subnodes_fun)

        self.Cancel_button.clicked.connect(self.cancel_button_fun)

        self.tabWidget.setTabEnabled(1, False)
        self.tabWidget.setTabEnabled(2, False)

        self.Max_Used_radiobutton.setChecked(True)
        self.ViewGroupbox.setEnabled(False)

        self.Grouping_groupbox.setEnabled(False)

        #self.setStyleSheet("QToolTip { background-color: black; color: white; border: black solid 1px; }")
        # NOTE ADDED
        self.splitter.splitterMoved["int", "int"].connect(self.SplitterCommandFun)

        self.New_Demand_Shelf_Num = 2

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Form"))
        self.tabWidget.setAccessibleName(_translate("MainWindow", "maintab"))
        self.pushButton_6.setText(_translate("MainWindow", "Help\n"
" Ctrl + H"))
        self.ViewGroupbox.setTitle(_translate("MainWindow", "Google View Modes"))
        self.Max_available_radiobutton.setText(_translate("MainWindow", "Use Max Available as Reference"))
        self.Max_Used_radiobutton.setText(_translate("MainWindow", "Use Max used Wavelength in a Link\n"
" as Reference"))
        self.Enable_google_view_checkbox.setText(_translate("MainWindow", "Enable"))
        self.Grouping_groupbox.setTitle(_translate("MainWindow", "Clustering"))
        self.Cancel_button.setText(_translate("MainWindow", "Cancel"))
        self.SetGatewayNode_button.setText(_translate("MainWindow", "Set Node as Gateway"))
        self.select_Sub_Nodes_labe.setText(_translate("MainWindow", " select Sub Nodes"))
        self.SelectSubNode_button.setText(_translate("MainWindow", "off"))
        self.OK_button.setText(_translate("MainWindow", "Ok"))
        self.ShowSubNodes.setText(_translate("MainWindow", "Show Sub Nodes"))
        self.GroupColor.setText(_translate("MainWindow", "        Cluster Color"))
        self.GroupID.setText(_translate("MainWindow", "        Cluster Type "))
        self.import_button.setText(_translate("MainWindow", "Imports"))
        self.export_result_button.setText(_translate("MainWindow", "Export \n"
"Result"))
        self.add_node_button.setText(_translate("MainWindow", "Add\n"
" Node"))
        self.groupBox.setTitle(_translate("MainWindow", "Planning"))
        self.Grooming_pushbutton.setText(_translate("MainWindow", "Grooming"))
        self.RWA_pushbutton.setText(_translate("MainWindow", "RWA"))
        self.FinalPlan_pushbutton.setText(_translate("MainWindow", "Final Plan"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TopologyTab), _translate("MainWindow", "Topology Tab"))
        item = self.General_TM.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.General_TM.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Source"))
        item = self.General_TM.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Destination"))
        item = self.General_TM.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Old\n"
"Cable Type"))
        item = self.General_TM.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Cable\n"
"Type"))
        item = self.General_TM.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Distance\n"
"Real (Km)"))
        item = self.General_TM.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Att. (dB/ Km )\n"
"for Network Plan "))
        item = self.General_TM.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Status"))
        item = self.General_TM.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Degree"))
        self.Traffic_matrix.setSortingEnabled(False)
        self.TM_groupbox.setTitle(_translate("MainWindow", "Tools"))
        self.label_7.setText(_translate("MainWindow", "       services"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "E1"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "STM_1_Electrical"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "STM_1_Optical"))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "STM_4"))
        item = self.listWidget.item(4)
        item.setText(_translate("MainWindow", "STM_16"))
        item = self.listWidget.item(5)
        item.setText(_translate("MainWindow", "STM_64"))
        item = self.listWidget.item(6)
        item.setText(_translate("MainWindow", "FE"))
        item = self.listWidget.item(7)
        item.setText(_translate("MainWindow", "1GE"))
        item = self.listWidget.item(8)
        item.setText(_translate("MainWindow", "10GE"))
        item = self.listWidget.item(9)
        item.setText(_translate("MainWindow", "40GE"))
        item = self.listWidget.item(10)
        item.setText(_translate("MainWindow", "100GE"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.SaveChanges_button.setText(_translate("MainWindow", "Export New Traffic Matrix"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TrafficMatrixTab), _translate("MainWindow", "Traffic Matrix Tab"))
        self.Demand_tab.setTabText(self.Demand_tab.indexOf(self.tab_8), _translate("MainWindow", "Shelf"))
        self.label_8.setText(_translate("MainWindow", "     Destination"))
        self.ClientLabel_20.setText(_translate("MainWindow", " Groom Out 10"))
        self.ClientLabel_23.setText(_translate("MainWindow", " Client Side Services:"))
        self.ClientLabel_21.setText(_translate("MainWindow", " Network Panels"))
        self.ClientLabel_22.setText(_translate("MainWindow", " LightPathes "))
        self.SelectNode_Label_13.setText(_translate("MainWindow", "   Source"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Demand tab"))

    
    # NOTE:ADDED
        
        if self.splitter.moveSplitter(0, 0):
            self.Demand_tab.setEnabled(False)
        else:
            self.Demand_tab.setEnabled(True)

    def SplitterCommandFun(self, pos):
        if pos == 0:
            self.SplitterEventLabel.setText("\t\t\t\t \31 Pull down The Splitter to see The Shelf !")
        elif pos == 727 or pos == 889:
            self.SplitterEventLabel.setText("\t\t\t\t \30 Pull up The Splitter to see The Map !")
        else :
            self.SplitterEventLabel.setText("")



    def create_obj(self):
        with open("NetworkObj.obj", 'wb') as handle:
            pickle.dump(self.network, handle, protocol=pickle.HIGHEST_PROTOCOL)
        handle.close()
        pass

    def show_subnodes_fun(self, state):

        if state == 2:
            self.webengine.page().runJavaScript('hide_subnodes()')
            
        elif state == 0:
            self.webengine.page().runJavaScript('show_subnodes()')


    def change_radiobuttons_state(self):
        if self.Max_available_radiobutton.isChecked():
            self.Max_Used_radiobutton.setChecked(False)
            return 2
        if self.Max_Used_radiobutton.isChecked():
            self.Max_available_radiobutton.setChecked(False)
            return 1

    def google_map_view(self, state):

        radio_state = self.change_radiobuttons_state()

        if state == 2:
            if radio_state == 1:
                green = ceil(self.Max_LinkState/4)
                yellow = ceil(self.Max_LinkState/2)
                orange = ceil(self.Max_LinkState * (3/4))
                
            else:
                self.MaxNW = int(self.MaxNW)
                green = ceil(self.MaxNW/4)
                yellow = ceil(self.MaxNW/2)
                orange = ceil(self.MaxNW * (3/4))
        
            self.webengine.page().runJavaScript('google_map_view_set(\'%s\', \'%s\', \'%s\')' %(green, yellow, orange))
        
        if state == 0:
            self.webengine.page().runJavaScript('google_map_view_reset()')


    

    def DemandMap_Change(self, Working = None, Protection = None, 
        WorkingRegeneratorsList = None, ProtectionRegenaratorsList = None, WorkingSNR = None, ProtectionSNR = None, WorkingLambdaList = None,
        ProtectionLambdaList= None):
        #mpl.rcParams["figure.figsize"] = [18.4, 7.8]
        self.MapWidget.canvas.figure.subplots_adjust(left = -0.001, right = 1, top = 1, bottom = -0.005)
        self.MapWidget.canvas.axes.cla()
        Source = self.Demand_Source_combobox.currentText()
        Destination = self.Demand_Destination_combobox.currentText()

        for node in Data["Nodes"].values():


            NodeName = node["Node"]
            id = self.NodeIdMap[NodeName]
            x, y = self.IdLocationMap[id]

            if NodeName == Source or NodeName == Destination:
                self.MapWidget.canvas.axes.plot(x, y, marker ="o", ms=13, color = 'gold')
            else:
                self.MapWidget.canvas.axes.plot(x, y, marker ="o", ms=13, color = 'black')

            self.MapWidget.canvas.axes.annotate(NodeName, xy = (x, y), xytext = (x, y),
             color='purple', rotation = 30, 
             horizontalalignment='left', verticalalignment='center_baseline')

        for key in Data["Links"].keys():
            InNodeName = key[0]
            OutNodeName = key[1]

            InNodeId = self.NodeIdMap[InNodeName]
            OutNodeId = self.NodeIdMap[OutNodeName]

            xIn , yIn = self.IdLocationMap[InNodeId]
            xOut, yOut = self.IdLocationMap[OutNodeId]

            xl = [xIn, xOut]
            yl = [yIn, yOut]
            self.MapWidget.canvas.axes.plot(xl,yl, c='black')

        #self.MapWidget.canvas.axes.plot(G)
        self.MapWidget.canvas.axes.get_xaxis().set_visible(False)
        self.MapWidget.canvas.axes.get_yaxis().set_visible(False)
        self.MapWidget.canvas.axes.set_frame_on(False)
        

        x_list_W = []
        y_list_W = []
        if Working != None:
            for key in Working:

                x1, y1 = self.IdLocationMap[key]


                x_list_W.append(x1)
                y_list_W.append(y1)

            if WorkingSNR != None:
                SNRList = str(WorkingSNR)
                WavelengthNumber = str(WorkingLambdaList)
                snr_label = "Working SNR = " + SNRList + '\n' + "Wavelength Number = " + WavelengthNumber
                self.MapWidget.canvas.axes.plot(x_list_W, y_list_W, c='blue', alpha = 0.5, linewidth=5, label=snr_label)
            else:
                self.MapWidget.canvas.axes.plot(x_list_W, y_list_W, c='blue', alpha = 0.5, linewidth=5, label="Working")
            self.MapWidget.canvas.axes.legend(loc = 'best')


        x_list_P = []
        y_list_P = []
        if Protection != None:
            for key in Protection:

                x1, y1 = self.IdLocationMap[key]


                x_list_P.append(x1)
                y_list_P.append(y1)

            if ProtectionSNR != None:
                SNRList = str(ProtectionSNR)
                WavelengthNumber = str(ProtectionLambdaList)
                snr_label1 = "Protection SNR = " + SNRList + '\n' + "Wavelength Number = " + WavelengthNumber          
                self.MapWidget.canvas.axes.plot(x_list_P, y_list_P, c='red', alpha = 0.5, linewidth=5, label=snr_label1)
            else:
                self.MapWidget.canvas.axes.plot(x_list_P, y_list_P, c='red', alpha = 0.5, linewidth=5, label="Protection")
            self.MapWidget.canvas.axes.legend(loc = 'best')

            
        if WorkingRegeneratorsList != None:
            for key in WorkingRegeneratorsList:

                x, y = self.IdLocationMap[key]

                self.MapWidget.canvas.axes.plot(x, y, marker ="o", ms=13, color = 'green')

        if ProtectionRegenaratorsList != None:
            for key in ProtectionRegenaratorsList:

                x, y = self.IdLocationMap[key]
                self.MapWidget.canvas.axes.plot(x, y, marker ="o", ms=13, color = 'green')

        self.MapWidget.canvas.draw()
    
    def cancel_button_fun(self):
        if hasattr(self.backend_map, "LastGateWay"):
            self.webengine.page().runJavaScript('cancel_clustering(\'%s\')' %(self.backend_map.LastGateWay))

            for node in Data["Clustering"][self.backend_map.LastGateWay]["SubNodes"]:
                self.webengine.page().runJavaScript('cancel_clustering(\'%s\')' %(node))

            Data["Clustering"].pop(self.backend_map.LastGateWay)

        self.SelectSubNode_button.toggle()

        self.Grooming_pushbutton.setEnabled(True)
    
    def OK_button_fun(self):
        SubNodes = []
        for node in Data["Clustering"][self.backend_map.LastGateWay]["SubNodes"]:
            SubNodes.append(self.NodeIdMap[node])
            self.webengine.page().runJavaScript('update_cluster_info(\'%s\', \'%s\', \'%s\')' %(node, Data["Clustering"][self.backend_map.LastGateWay]["Color"], 1))
        
        self.network.PhysicalTopology.add_cluster(self.NodeIdMap[self.backend_map.LastGateWay], SubNodes, Data["Clustering"][self.backend_map.LastGateWay]["Color"])
        self.webengine.page().runJavaScript('update_cluster_info(\'%s\', \'%s\', \'%s\')' %(self.backend_map.LastGateWay, Data["Clustering"][self.backend_map.LastGateWay]["Color"], 0))
        
        self.SelectSubNode_button.toggle()

        self.Grooming_pushbutton.setEnabled(True)

    #TODO: complete this method
    def working_view_fun(self):
        for key in Data["Links"].keys():
            InNodeName = key[0]
            OutNodeName = key[1]
            InNodeId = self.NodeIdMap[key[0]]
            OutNodeId = self.NodeIdMap[key[1]]
            

    
    def SetNode_flag_javascript(self,text):
        self.webengine.page().runJavaScript('SetNode_flag_fun(\'%s\')' %text)
    
    
    def SelectSubNode_flag_javascript(self,text):
        self.webengine.page().runJavaScript('SelectSubNode_flag_fun(\'%s\')' %text)

    def ColorTo_javascript(self,text):
        self.webengine.page().runJavaScript('setcolor(\'%s\')' %text)


    def SelectSubNode_button_fun(self):
        state = self.SelectSubNode_button.isChecked()

        if state is False:
            self.SelectSubNode_button.setText("On")
            self.backend_map.SubNodeSelect_flag_fun("True")
            self.SelectSubNode_flag_javascript("True")
        else:
            self.SelectSubNode_button.setText("off")
            self.backend_map.SubNodeSelect_flag_fun("False")
            self.SelectSubNode_flag_javascript("False")

        self.Grooming_pushbutton.setEnabled(False)


    def SetNode_gateway_fun(self):
        self.backend_map.SetNode_flag_fun("False")
        self.SetNode_flag_javascript("False")
        self.lastgroup_type = self.cluster_type_combobox.currentText()
        self.lastgroup_color = self.ClusterColor_combobox.currentText()
        
        self.backend_map.SetNode_flag_fun("True",self.lastgroup_color)
        self.SetNode_flag_javascript("True")
        
        self.Grooming_pushbutton.setEnabled(False)
        

    def set_demand_panels(self):


        Source = self.Demand_Source_combobox.currentText()
        Local_Destination = self.Demand_Destination_combobox.currentText()
        for i in range(1, (((self.New_Demand_Shelf_Num - 2) * 14) + 15)):
            # removing old panel
            panel_widget = Data["DemandPanel_" + str(i)].takeAt(0).widget()
            Data["DemandPanel_" + str(i)].removeWidget(panel_widget)
            panel_widget.deleteLater()

            #print(f"count: {Data['DemandPanel_' + str(i)].count()}")
            
            if str(i) in DemandTabDataBase["Panels"][Source]:
                panel = DemandTabDataBase["Panels"][Source][str(i)]
                
                Destination = panel.Destination

                DualPanelsId = panel.DualPanelsId

                if isinstance(panel , MP2X_L):
                    Data["DemandPanel_" + str(i)].addWidget(MP2X_L_Demand(str(i), Source, Destination, DualPanelsId))

                    GroomOutId_1, GroomOutId_2 = panel.LineIdList
                    

                    # finding panel widget
                    widget = Data["DemandPanel_" + str(i)].itemAt(0).widget()

                    for i in range(len(panel.ClientsCapacity)):
                        if panel.ClientsCapacity[i] != 0:

                            # finding object of client customlabel
                            text = "CLIENT" + str( i + 1 )
                            clientvar = getattr(widget, text)

                            if clientvar.ClientNum % 2 == 0:
                                clientvar.setStyleSheet("image: url(:/CLIENT_L_Selected_SOURCE/CLIENT_L_Selected.png);")
                            else:
                                clientvar.setStyleSheet("image: url(:/CLIENT_R_Selected_SOURCE/CLIENT_R_Selected.png);")
                            
                            clientvar.setToolTip(DemandTabDataBase["Services_static"][Source][(panel.DemandIdList[i],panel.ServiceIdList[i])].toolTip())

                            clientvar.servicetype = panel.ClientsCapacity[i]
                            clientvar.nodename = Source
                            clientvar.Destination = Destination
                            clientvar.ids = [panel.DemandIdList[i], panel.ServiceIdList[i]]
                            clientvar.setAcceptDrops(False)

                            # adding tooltip to line port
                            linevar_1 = getattr(widget, "LINE1")
                            linevar_1.setToolTip(DemandTabDataBase["GroomOut10"][(Source, Destination)][GroomOutId_1].toolTip())

                            linevar_1.setStyleSheet("QLabel{ image: url(:/Line_L_Selected_SOURCE/Line_L_Selected.png); }")

                            if GroomOutId_2 is not None:
                                linevar_2 = getattr(widget, "LINE2")
                                linevar_2.setToolTip(DemandTabDataBase["GroomOut10"][(Source, Destination)][GroomOutId_2].toolTip())

                                linevar_2.setStyleSheet("QLabel{ image: url(:/Line_R_Selected_SOURCE/Line_R_Selected.png); }")
                            
                elif isinstance(panel, MP2X_R):
                    Data["DemandPanel_" + str(i)].addWidget(MP2X_R_Demand(str(i), Source, Destination, DualPanelsId))
                
                elif isinstance(panel, MP1H_L):
                    LightPathId = panel.LightPathId
                    Data["DemandPanel_" + str(i)].addWidget(MP1H_L_Demand(str(i), Source, Destination, DualPanelsId))

                    # finding panel widget
                    widget = Data["DemandPanel_" + str(i)].itemAt(0).widget()
                        
                    for i in range(len(panel.ClientsCapacity)):
                        if panel.ClientsCapacity[i] != 0:

                            # finding object of client customlabel
                            text = "Client" + str( i + 1 )
                            clientvar = getattr(widget, text)

                            if clientvar.ClientNum % 2 == 0:
                                clientvar.setStyleSheet("image: url(:/CLIENT_L_Selected_SOURCE/CLIENT_L_Selected.png);")
                            else:
                                clientvar.setStyleSheet("image: url(:/CLIENT_R_Selected_SOURCE/CLIENT_R_Selected.png);")
                            # checking its GroomOut10 or not
                            if (panel.DemandIdList[i],panel.ServiceIdList[i]) in DemandTabDataBase["Services_static"][Source]:
                                clientvar.setToolTip(DemandTabDataBase["Services_static"][Source][(panel.DemandIdList[i],panel.ServiceIdList[i])].toolTip())
                            else:
                                clientvar.setToolTip(DemandTabDataBase["GroomOut10"][(Source, Destination)][panel.ServiceIdList[i]].toolTip())
                            clientvar.servicetype = panel.ClientsCapacity[i]
                            clientvar.nodename = Source
                            clientvar.Destination = Destination
                            clientvar.ids = [panel.DemandIdList[i], panel.ServiceIdList[i]]

                            if panel.ClientsCapacity[i] == "GroomOut10":
                                UserData = DemandTabDataBase["GroomOut10"][(Source, Destination)][panel.ServiceIdList[i]].data(Qt.UserRole)
                                clientvar.GroomOut_Capacity = UserData["Capacity"]

                            clientvar.setAcceptDrops(False)

                            # adding tooltip to line port
                            linevar = getattr(widget, "Line")
                            linevar.setToolTip(DemandTabDataBase["Lightpathes"][(Source, Destination)][LightPathId].toolTip())

                            linevar.setStyleSheet("QLabel{ image: url(:/Line_Selected_SOURCE/Line_Selected.png); }")

                elif isinstance(panel, MP1H_R):
                    Data["DemandPanel_" + str(i)].addWidget(MP1H_R_Demand(str(i), Source, Destination, DualPanelsId))
                
                elif isinstance(panel, TP1H_L):
                    LightPathId = panel.LightPathId
                    Data["DemandPanel_" + str(i)].addWidget(TP1H_L_Demand(str(i), Source, Destination, DualPanelsId))

                    # finding panel widget
                    widget = Data["DemandPanel_" + str(i)].itemAt(0).widget()

                    if panel.Line == "100GE":

                        # finding object of client customlabel
                        clientvar = getattr(widget, "Client")

                        # filling customlabel attributes 
                        clientvar.setToolTip(DemandTabDataBase["Services_static"][Source][(panel.DemandId, panel.ServiceId)].toolTip())
                        clientvar.servicetype = "100GE"
                        clientvar.nodename = Source
                        clientvar.Destination = Destination
                        clientvar.ids = [panel.DemandId, panel.ServiceId]
                        clientvar.setAcceptDrops(False)

                        clientvar.setStyleSheet("image: url(:/TP1H_CLIENT_Selected_SOURCE/TP1H_CLIENT_Selected.png);")

                        LineVar = getattr(widget, "Line")
                        LineVar.setToolTip(DemandTabDataBase["Lightpathes"][(Source, Destination)][LightPathId].toolTip())

                        LineVar.setStyleSheet("QLabel{ image: url(:/Line_Selected_SOURCE/Line_Selected.png); }")
                elif isinstance(panel, TP1H_R):
                    Data["DemandPanel_" + str(i)].addWidget(TP1H_R_Demand(str(i), Source, Destination, DualPanelsId))
            
            else:
                Data["DemandPanel_" + str(i)].addWidget(BLANK_Demand(str(i), Source, Local_Destination))

        self.show_hide_shelf(Source)
    
    def show_hide_shelf(self, Source):
        if Source != "":

            count = self.Demand_tab.count()

            if count < DemandTabDataBase["Shelf_Count"][Source]:
                for i in range(count, DemandTabDataBase["Shelf_Count"][Source]):
                    self.Demand_tab.addTab(getattr(self, "Shelf_" + str(i + 1)), "shelf " + str(i + 1))
            
            elif count > DemandTabDataBase["Shelf_Count"][Source]:
                for i in range(DemandTabDataBase["Shelf_Count"][Source] , count):
                    self.Demand_tab.removeTab(i)

    def export_excel_fun(self):
        

        def export_excel(filename, network, cluster_view = True):
            """
            filename: example.xlsx
            NOTE: if filename is open executing this function will cause an error
            network: an instance of Common_Object_def
            """
            sources = []
            destinations = []
            wavelengths = []
            routed_types = []
            worst_working_snrs = []
            worst_protection_snrs = []
            working_path = []
            protection_path = []
            working_regens = []
            protection_regens = []
            unprotected_indices = []
            # Building required lists for different fields
            for lightpath in network.LightPathDict.values():
                sources.append(self.IdNodeMap[lightpath.Source])
                destinations.append(self.IdNodeMap[lightpath.Destination])
                wavelengths.append(lightpath.WaveLength)
                routed_types.append(lightpath.Type)

                working_path.append(lightpath.WorkingPath)
                working_regens.append(lightpath.RegeneratorNode_w)
                snr = lightpath.SNR_w[0]
                for snr_temp in lightpath.SNR_w:
                    if snr>snr_temp:
                        snr = snr_temp
                worst_working_snrs.append(snr)
                try:
                    snr = lightpath.SNR_p[0]
                    for snr_temp in lightpath.SNR_p:
                        if snr>snr_temp:
                            snr = snr_temp
                    worst_protection_snrs.append(snr)
                    protection_path.append(lightpath.ProtectionPath)
                    protection_regens.append(lightpath.RegeneratorNode_p)
                except:
                    worst_protection_snrs.append(None)
                    protection_path.append([])
                    protection_regens.append([])
                    unprotected_indices.append(len(worst_protection_snrs))

            dictionary = {
            'Source Site' : sources,
            'Destination Site' : destinations,
            'Demand Type': routed_types,
            'Wavelength': wavelengths,
            'Working SNR': worst_working_snrs,
            'Protection SNR': worst_protection_snrs,
            'Working Path': working_path,
            'Working Regenerators': working_regens,
            'Protection Path': protection_path,
            'Protection Regenerators': protection_regens}

            df = pd.DataFrame(dictionary)
            writer = pd.ExcelWriter(filename, engine='xlsxwriter')
            df.to_excel(writer, sheet_name='Routed Demands')
            workbook  = writer.book
            worksheet = writer.sheets['Routed Demands']

            

            # Set column size (begininng, end, size)
            center_format = workbook.add_format({'align': 'center', 'valign': 'vcenter'})
            snr_format = workbook.add_format({'num_format': '0.00', 'align': 'center'})
            worksheet.set_column(1, 2 , 17,center_format)
            worksheet.set_column(3, 4 , 15,center_format)
            worksheet.set_column(5, 6, 17,snr_format)
            worksheet.set_column(7, 7, 40)
            worksheet.set_column(8, 8, 20)
            worksheet.set_column(9, 9, 45)
            worksheet.set_column(10, 10, 20)

            for index in unprotected_indices:
                color = "#D1D1D1"
                fmt = workbook.add_format()
                fmt = workbook.add_format({'bg_color': color})
                worksheet.set_row(index, cell_format = fmt)
                fmt = workbook.add_format()
                fmt = workbook.add_format({'align': 'center', 'bg_color': color})
                worksheet.write('B'+str(index+1), dictionary['Source Site'][index-1], fmt)
                worksheet.write('C'+str(index+1), dictionary['Destination Site'][index-1], fmt)
                worksheet.write('D'+str(index+1), dictionary['Demand Type'][index-1], fmt)
                worksheet.write('E'+str(index+1), dictionary['Wavelength'][index-1], fmt)
            
            # 3-color formatting for snrs
            lightpath_number = len(network.LightPathDict.keys())
            worksheet.conditional_format('F2:F' + str(lightpath_number+1), {'type': '3_color_scale'})
            worksheet.conditional_format('G2:G' + str(lightpath_number+1), {'type': '3_color_scale'})
            
            # Set example specific text and color for some headers
            color = "#FFC000"
            fmt = workbook.add_format()
            fmt = workbook.add_format({'align': 'center', 'bold': True, 'border': 1, 'bg_color': color})
            worksheet.write('B1', 'Source Site', fmt)
            worksheet.write('C1', 'Destination Site', fmt)
            
            color = "#FFFF64"
            fmt = workbook.add_format()
            fmt = workbook.add_format({'align': 'center', 'bold': True, 'border': 1, 'bg_color': color})
            worksheet.write('H1', 'Working Path', fmt)
            
            color = "#64FF00"
            fmt = workbook.add_format()
            fmt = workbook.add_format({'align': 'center', 'bold': True, 'border': 1, 'bg_color': color})
            worksheet.write('E1', 'Wavelength', fmt)

            #### Link Stats #######
            wavelength_number_on_links = []
            all_link_states = []
            for link in list(network.PhysicalTopology.LinkDict.keys()):
                wavelength_number_on_links.append(len(network.PhysicalTopology.LinkDict[link].LinkState))
                all_link_states.append(network.PhysicalTopology.LinkDict[link].LinkState)
            dictionary2 = {
            'Links' : list(map(lambda x : (self.IdNodeMap[x[0]], self.IdNodeMap[x[1]]), list(network.PhysicalTopology.LinkDict.keys()))),
            'Used Wavelengths' : all_link_states,
            'Wavelength Number': wavelength_number_on_links
            }
            link_number = len(list(network.PhysicalTopology.LinkDict.keys()))
            df2 = pd.DataFrame(dictionary2)
            df2.to_excel(writer, sheet_name='Link State')
            worksheet2 = writer.sheets['Link State']
            worksheet2.conditional_format('D2:D'+ str(link_number+1),  {'type': '3_color_scale',
                                                'min_color': "green",
                                                'mid_color': "yellow",
                                                'max_color': "red"})
            worksheet2.set_column(1, 1 , 12,center_format)
            worksheet2.set_column(2, 2, 52)
            worksheet2.set_column(3, 3, 18,center_format)

            #### Node Stats #######
            wavelength_number_on_nodes = []
            all_node_states = []
            for node in list(network.PhysicalTopology.NodeDict.keys()):
                wavelength_number_on_nodes.append(len(network.PhysicalTopology.NodeDict[node].NodeState))
                all_node_states.append(network.PhysicalTopology.NodeDict[node].NodeState)
            dictionary3 = {
            'Nodes' : list(map(lambda x : self.IdNodeMap[x], list(network.PhysicalTopology.NodeDict.keys()))),
            'Used Wavelengths' : all_node_states,
            'Wavelength Number': wavelength_number_on_nodes
            }
            node_number = len(list(network.PhysicalTopology.NodeDict.keys()))
            df3 = pd.DataFrame(dictionary3)
            df3.to_excel(writer, sheet_name='Node State')
            worksheet3 = writer.sheets['Node State']
            worksheet3.conditional_format('D2:D'+ str(node_number+1),  {'type': '3_color_scale',
                                                'min_color': "green",
                                                'mid_color': "yellow",
                                                'max_color': "red"})
            worksheet3.set_column(1, 1 , 12,center_format)
            worksheet3.set_column(2, 2, 52)
            worksheet3.set_column(3, 3, 18,center_format)
            

            if cluster_view:
                for cluster_id in network.PhysicalTopology.ClusterDict.keys():
                    sources = []
                    destinations = []
                    wavelengths = []
                    routed_types = []
                    worst_working_snrs = []
                    worst_protection_snrs = []
                    working_path = []
                    protection_path = []
                    working_regens = []
                    protection_regens = []
                    # Building required lists for different fields
                    for lightpath in network.LightPathDict.values():
                        if lightpath.ClusterNum == int(cluster_id):
                            sources.append(self.IdNodeMap[lightpath.Source])
                            destinations.append(self.IdNodeMap[lightpath.Destination])
                            wavelengths.append(lightpath.WaveLength)
                            routed_types.append(lightpath.Type)

                            working_path.append(lightpath.WorkingPath)
                            working_regens.append(lightpath.RegeneratorNode_w)
                            snr = lightpath.SNR_w[0]
                            for snr_temp in lightpath.SNR_w:
                                if snr>snr_temp:
                                    snr = snr_temp
                            worst_working_snrs.append(snr)
                            try:
                                snr = lightpath.SNR_p[0]
                                for snr_temp in lightpath.SNR_p:
                                    if snr>snr_temp:
                                        snr = snr_temp
                                worst_protection_snrs.append(snr)
                                protection_path.append(lightpath.ProtectionPath)
                                protection_regens.append(lightpath.RegeneratorNode_p)
                            except:
                                worst_protection_snrs.append([])
                                protection_path.append([])
                                protection_regens.append([])
                if sources:
                    dictionary4 = {
                    'Source Site' : sources,
                    'Destination Site' : destinations,
                    'Demand Type': routed_types,
                    'Wavelength': wavelengths,
                    'Working SNR': worst_working_snrs,
                    'Protection SNR': worst_protection_snrs,
                    'Working Path': working_path,
                    'Working Regenerators': working_regens,
                    'Protection Path': protection_path,
                    'Protection Regenerators': protection_regens}

                    df4 = pd.DataFrame(dictionary4)
                    df4.to_excel(writer, sheet_name='Cluster '+str(cluster_id))
                    worksheet = writer.sheets['Cluster '+str(cluster_id)]
                    # Set column size (begininng, end, size)
                    center_format = workbook.add_format({'align': 'center', 'valign': 'vcenter'})
                    snr_format = workbook.add_format({'num_format': '0.00', 'align': 'center'})
                    worksheet.set_column(1, 2 , 17,center_format)
                    worksheet.set_column(3, 4 , 15,center_format)
                    worksheet.set_column(5, 6, 17,snr_format)
                    worksheet.set_column(7, 7, 40)
                    worksheet.set_column(8, 8, 20)
                    worksheet.set_column(9, 9, 45)
                    worksheet.set_column(10, 10, 20)

                    # 3-color formatting for snrs
                    lightpath_number = len(sources)
                    worksheet.conditional_format('F2:F' + str(lightpath_number+1), {'type': '3_color_scale'})
                    worksheet.conditional_format('G2:G' + str(lightpath_number+1), {'type': '3_color_scale'})
                    
                    # Set example specific text and color for some headers
                    color = "#FFC000"
                    fmt = workbook.add_format()
                    fmt = workbook.add_format({'align': 'center', 'bold': True, 'border': 1, 'bg_color': color})
                    worksheet.write('B1', 'Source Site', fmt)
                    worksheet.write('C1', 'Destination Site', fmt)
                    
                    color = "#FFFF64"
                    fmt = workbook.add_format()
                    fmt = workbook.add_format({'align': 'center', 'bold': True, 'border': 1, 'bg_color': color})
                    worksheet.write('H1', 'Working Path', fmt)
                    
                    color = "#64FF00"
                    fmt = workbook.add_format()
                    fmt = workbook.add_format({'align': 'center', 'bold': True, 'border': 1, 'bg_color': color})
                    worksheet.write('E1', 'Wavelength', fmt)
            writer.save()

        if hasattr(self, "RWA_Success"):
            if self.RWA_Success is True:
                name = QFileDialog.getSaveFileName(MainWindow, "Save Topology", filter = "(*.xlsx)")
                if name[0] != 0:
                    try:
                        if not Data["Clustering"]:
                            export_excel(name[0], self.decoded_network, True)
                        else:
                            export_excel(name[0], self.decoded_network)
                    except:
                        pass        




    def SaveTopology_fun(self):
        TSD = {}    # TSD: Topology Save Dictionary
        TSD["Nodes"] = Data["Nodes"]
        TSD["Links"] = Data["Links"]
        name = QFileDialog.getSaveFileName(MainWindow, "Save Topology")

        if name[0] != 0:
            with open(name[0], 'wb') as handle:
                pickle.dump(TSD, handle, protocol=pickle.HIGHEST_PROTOCOL)
            handle.close()
        

    
    

    def SyncScroll_1(self):
        sliderValue = self.TMSliderBar.value()
        self.GMTSliderBar.setValue(sliderValue - 3)
    
    def SyncScroll_2(self):
        sliderValue = self.GMTSliderBar.value()
        self.TMSliderBar.setValue(sliderValue + 3)

    def main_tab_clicked(self,index):
        if index == 2:
            if Data["DemandTab_firststart_flag"] == False:
                Source = self.Demand_Source_combobox.currentText()
                self.Demand_Shelf_set()
                if self.clicked_Node_flag == False:
                    self.Demand_Destination_combobox.addItems(list(set(DemandTabDataBase["Source_Destination"][Source]["DestinationList"])))
                Data["DemandTab_firststart_flag"] = True
            if self.update_demand_service_flag is True:
                self.UpdateDemand_ServiceList()
            

            # TODO: run shelf set function for Demand Tab and turn its relevant flag on
                    

    
    def list_click(self):


        self.Traffic_matrix.clear()
    
        item = self.listWidget.currentItem()
        item = str(item.text())
    
        self.Traffic_matrix.setColumnCount(Data[item]["ColumnCount"])
        self.Traffic_matrix.setRowCount(Data["RowCount"])
        self.Traffic_matrix.setHorizontalHeaderLabels(Data[item]["Headers"])
    
        for i in range(Data[item]["ColumnCount"]):
            column_name = Data[item]["Headers"][i].strip()
            keys = Data[item]["DataSection"][column_name].keys()
            for row in list(keys):
                cell_data = Data[item]["DataSection"][column_name][row]
                self.Traffic_matrix.setCurrentCell(int(row),i)
                self.Traffic_matrix.setItem(int(row),i,QTableWidgetItem(cell_data))
    
    def Demand_LineList_fun(self, CurItem, PreItem):
        if self.update_Demand_lightpath_list_flag is True:
            if CurItem is not None:
                UserData = CurItem.data(Qt.UserRole)
                Source = UserData["Source"]
                Destination = UserData["Destination"]
                LightpathId = UserData["LightPathId"]

                # adding border to current panel
                LeftPanelId = UserData["PanelId"]
                left_widget = Data["DemandPanel_" + str(LeftPanelId)].itemAt(0).widget()
                linevar = left_widget.Line
                linevar.setStyleSheet(" QLabel{ image: url(:/line/line.png); border: 5px solid blue; }")
                
                if PreItem is not None:
                    pre_UserData = PreItem.data(Qt.UserRole)
                    pre_LeftPanelId = pre_UserData["PanelId"]
                    pre_left_widget = Data["DemandPanel_" + str(pre_LeftPanelId)].itemAt(0).widget()
                    pre_linevar = pre_left_widget.Line
                    pre_linevar.setStyleSheet(" QLabel{ image: url(:/line/line.png); }")

                if self.RWA_Success is True:

                    WorkingPath = GroomingTabDataBase["LightPathes"][(Source, Destination)][LightpathId]["Working"]
                    ProtectionPath = GroomingTabDataBase["LightPathes"][(Source, Destination)][LightpathId]["Protection"]
                    RG_w = GroomingTabDataBase["LightPathes"][(Source, Destination)][LightpathId]["RG_w"]
                    RG_p = GroomingTabDataBase["LightPathes"][(Source, Destination)][LightpathId]["RG_p"]
                    SNR_w = GroomingTabDataBase["LightPathes"][(Source, Destination)][LightpathId]["SNR_w"]
                    SNR_p = GroomingTabDataBase["LightPathes"][(Source, Destination)][LightpathId]["SNR_p"]
                    WorkingLambdaList = GroomingTabDataBase["LightPathes"][(Source, Destination)][LightpathId]["WorkingLambdaList"]
                    ProtectionLambdaList = GroomingTabDataBase["LightPathes"][(Source, Destination)][LightpathId]["ProtectionLambdaList"]
                    #print(f"here for calling demand change function <before> ")

                    # calling Demand map change function
                    self.DemandMap_Change(WorkingPath, ProtectionPath, WorkingRegeneratorsList = RG_w, ProtectionRegenaratorsList = RG_p
                                            ,WorkingSNR = SNR_w , ProtectionSNR = SNR_p, WorkingLambdaList= WorkingLambdaList,
                                            ProtectionLambdaList= ProtectionLambdaList)
    
    def groomout10_list_fun(self, CurItem, PreItem):
        if CurItem is not None:
            UserData = CurItem.data(Qt.UserRole)
            Source = UserData["Source"]
            Destination = UserData["Destination"]
            GroomOut10Id = UserData["GroomOut10Id"]

            PanelId = UserData["PanelId"]
            DemandId = UserData["DemandId"]
            widget = Data["DemandPanel_" + str(PanelId)].itemAt(0).widget()

            index = DemandTabDataBase["Panels"][Source][PanelId].LineIdList.index(GroomOut10Id)

            if index == 0:
                widget.LINE1.setStyleSheet(" QLabel{ image: url(:/Line_L_SOURCE/LINE_L.png); border: 5px solid red; }")
                
            else:
                widget.LINE2.setStyleSheet(" QLabel { image: url(:/Line_R_SOURCE/LINE_R.png); border: 5px solid red; }")
                
            
            if "MP1H_Client_Id" in UserData:
                MP1H_Id , Client_Id = UserData["MP1H_Client_Id"]
                MP1H_widget = Data["DemandPanel_" + str(MP1H_Id)].itemAt(0).widget()

                clientvar = getattr(MP1H_widget, "Client" + Client_Id )

                if ( int(Client_Id) - 1 ) % 2 == 1:
                    clientvar.setStyleSheet(" QLabel{ image: url(:/CLIENT_L_Selected_SOURCE/CLIENT_L_Selected.png); border: 5px solid red; }")
                    
                else:
                    clientvar.setStyleSheet(" QLabel{ image: url(:/CLIENT_R_Selected_SOURCE/CLIENT_R_Selected.png); border: 5px solid red; }")
                    


            if PreItem is not None:
                UserData = PreItem.data(Qt.UserRole)

                GroomOut10Id = UserData["GroomOut10Id"]

                PanelId = UserData["PanelId"]
                widget = Data["DemandPanel_" + str(PanelId)].itemAt(0).widget()

                index = DemandTabDataBase["Panels"][Source][PanelId].LineIdList.index(GroomOut10Id)

                if index == 0:
                    widget.LINE1.setStyleSheet(" QLabel{ image: url(:/Line_L_SOURCE/LINE_L.png); }")
                    
                else:
                    widget.LINE2.setStyleSheet(" QLabel{ image: url(:/Line_R_SOURCE/LINE_R.png); }")
                    
                
                if "MP1H_Client_Id" in UserData:
                    MP1H_Id , Client_Id = UserData["MP1H_Client_Id"]
                    MP1H_widget = Data["DemandPanel_" + str(MP1H_Id)].itemAt(0).widget()

                    clientvar = getattr(MP1H_widget, "Client" + Client_Id )

                    if ( int(Client_Id) - 1 ) % 2 == 1:
                        clientvar.setStyleSheet(" QLabel{ image: url(:/CLIENT_L_Selected_SOURCE/CLIENT_L_Selected.png); }")
                        
                    else:
                        clientvar.setStyleSheet(" QLabel{ image: url(:/CLIENT_R_Selected_SOURCE/CLIENT_R_Selected.png); }")
                        


    # MHA EDITION:
    def SaveTM_fun(self):
        header_list = ['ID', 'Source', 'Destination', 'Old\nCable\nType', 'Cable\nType', 'Distance\nReal\n(Km)',
                         'Att. (dB/km)\nfor Network Plan\n(Option 1 or 2)', 'Status']
        name = QFileDialog.getSaveFileName(MainWindow, "Save Traffic Matrix")
        if name[0] != 0:
            workbook = xlsxwriter.Workbook(name[0])
            worksheet = workbook.add_worksheet() 
            #data_format = workbook.add_format({'bg_color': '#D21F3C'})
            column = 0
            for i in range(8):
                row = 2
                worksheet.write(1, i,header_list[i])
                for item in list(Data["General"]["DataSection"][str(i)].values()):
                        worksheet.write(row, column, item)   
                        row += 1
                column += 1          

            header_list2 = {"E1":["Quantity", "SLA"], "STM_1_Electrical":["Quantity", "SLA"], "STM_1_Optical":
                            ["Quantity", "λ", "SLA"], "STM_4":
                            ["Quantity", "λ", "concat.", "SLA"],"STM_16":
                            ["Quantity", "λ", "concat.", "SLA"],"STM_64":
                            ["Quantity", "λ", "concat.", "SLA"],"FE":
                            ["Quantity", "Granularity_xVC12", "Granularity_xVC4", "λ", "SLA"],"1GE":
                            ["Quantity", "Granularity", "λ", "SLA"],"10GE":
                            ["Quantity", "Granularity", "λ", "SLA"],"40GE":
                            ["Quantity", "Granularity", "λ", "SLA"],"100GE":
                            ["Quantity", "Granularity", "λ", "SLA"]}
                            
            header_list3 = ['Quantity_E1', 'SLA_E1', 'Quantity_STM1_E', 'SLA_STM1_E',
                            'Quantity_STM1_O', 'λ_STM1_O(nm)', 'SLA_STM1_O',
                            'Quantity_STM4', 'λ_STM4(nm)', 'Concat._STM4', 'SLA_STM4',
                            'Quantity_STM16', 'λ_STM16(nm)', 'Concat._STM16', 'SLA_STM16',
                            'Quantity_STM64', 'λ_STM64(nm)', 'Concat._STM64', 'SLA_STM64',
                            'Quantity_FE', "GranularityxVC12", "GranularityxVC4", 'λ_FE(nm)', 'SLA_FE',
                            'Quantity_GE', 'Granularity_GE', 'λ_GE(nm)', 'SLA_GE',
                            'Quantity_10GE', 'Granularity_10GE', 'λ_10GE(nm)', 'SLA_10GE',
                            'Quantity_40GE', 'Granularity_40GE', 'λ_40GE(nm)', 'SLA_40GE',
                            'Quantity_100GE', 'Granularity_100GE', 'λ_100GE(nm)', 'SLA_100GE']

            worksheet.set_column('J:AW', 12)
            worksheet.set_row(0, 50)
            merge_format = workbook.add_format({
            'bold': 1,
            'border': 1,
            'align': 'center',
            'valign': 'vcenter'})
            

            #worksheet.set_row(6, 50) 

            worksheet.merge_range('I1:J1', 'E1',merge_format)
            worksheet.merge_range('K1:L1', "STM_1_Electrical",merge_format)
            worksheet.merge_range('M1:O1', "STM_1_Optical",merge_format)
            worksheet.merge_range('P1:S1', "STM_4",merge_format)
            worksheet.merge_range('T1:W1', "STM_16",merge_format)
            worksheet.merge_range('X1:AA1', "STM_64",merge_format)
            worksheet.merge_range('AB1:AF1', "FE",merge_format)
            worksheet.merge_range('AG1:AJ1', "1GE",merge_format)
            worksheet.merge_range('AK1:AN1', "10GE",merge_format)
            worksheet.merge_range('AO1:AR1', "40GE",merge_format)
            worksheet.merge_range('AS1:AV1', "100GE",merge_format)
        

            for item2 in header_list3:
                i+=1
                worksheet.write(1, i, item2)
            for key in header_list2.keys():
                for value in header_list2[key]:
                    row = 2
                    for item3 in list(Data[key]["DataSection"][value].values()):
                        if item3 == 'nan':
                            worksheet.write(row, column, None)   
                            row += 1
                        else:
                            worksheet.write(row, column, item3)
                            row += 1
                    column +=1

            workbook.close()

        
        #print(dict1["Destination"])
        
        #print(Data["General"]["DataSection"]["4"].values())

        #df.to_excel(writer, sheet_name='Sheet1')

        #Close the Pandas Excel writer and output the Excel file.
        #writer.save()   

    


            #Data.update(Temp_data)
    
    def TrafficMatrixToObject(self):
        RowsNumber = list(Data["General"]["DataSection"]["0"].keys())
        RowsNumber = list(filter(lambda x : isinstance(x,int),RowsNumber))
        ServiceTypes = ["E1", "STM_1_Electrical", "STM_1_Optical", "STM_4", "STM_16", "STM_64", "FE", "1GE", "10GE",
                           "40GE", "100GE"]

        SubHeaders = [["Quantity", "SLA"], ["Quantity", "SLA"], ["Quantity", "λ", "SLA"],
                  ["Quantity", "λ", "concat.", "SLA"], ["Quantity", "λ", "concat.", "SLA"],
                  ["Quantity", "λ", "concat.", "SLA"],
                  ["Quantity", "Granularity_xVC12", "Granularity_xVC4", "λ", "SLA"],
                  ["Quantity", "Granularity", "λ", "SLA"], ["Quantity", "Granularity", "λ", "SLA"],
                  ["Quantity", "Granularity", "λ", "SLA"], ["Quantity", "Granularity", "λ", "SLA"]]

        for Row in RowsNumber:
            #id = Data["General"]["DataSection"]["0"][Row]
            
            Source = Data["General"]["DataSection"]["1"][Row]
            Destination = Data["General"]["DataSection"]["2"][Row]
            SourceId = int(self.NodeIdMap[Source])
            DestinationId = int(self.NodeIdMap[Destination])

            # TODO: find Type in Traffic Matrix
            Type = None
            i = 0
            ServiceDict = {}
            for service in ServiceTypes:
                PropertyDict = {}
                ServiceCount = 0
                for PropNum in range(0,len(SubHeaders[i])):
                    Prop = SubHeaders[i][PropNum]
                    if PropNum == 0:
                        ServiceCount += int(Data[service]["DataSection"][Prop].get(Row, 0))
                        PropertyDict[Prop] = ServiceCount
                    else:
                        PropertyDict[Prop] = Data[service]["DataSection"][Prop].get(Row, None)
                i += 1
                ServiceDict[service] = PropertyDict
            self.network.TrafficMatrix.add_demand(SourceId,DestinationId,Type)

            
            id = self.network.Traffic.Demand.DemandReferenceId - 1 
            for service in list(ServiceDict.keys()):

                Sla = ServiceDict[service]["SLA"]

                if "λ" in ServiceDict[service]:
                    Wavelength = ServiceDict[service]["λ"]
                else:
                    Wavelength = None
                
                if "Granularity_xVC12" in ServiceDict[service]:
                    Granularity_xVC12 = ServiceDict[service]["Granularity_xVC12"]
                else:
                    Granularity_xVC12 = None
                
                if "Granularity_xVC4" in ServiceDict[service]:
                    Granularity_xVC4 = ServiceDict[service]["Granularity_xVC4"]
                else:
                    Granularity_xVC4 = None
                
                if "Granularity" in ServiceDict[service]:
                    Granularity = ServiceDict[service]["Granularity"]
                else:
                    Granularity = None
                
                IgnoringNodes = None

                for i in range(ServiceDict[service]["Quantity"]):

                    ServiceId = self.network.TrafficMatrix.DemandDict[0].GenerateId()

                    self.network.TrafficMatrix.DemandDict[id].add_service(ServiceId, service, Sla, IgnoringNodes, Wavelength, Granularity, Granularity_xVC12, Granularity_xVC4)
            
            # initializing DataBases 
            self.initialize_DemandTabDataBase(Source, Destination)
            self.FillDemandTabDataBase_Services(id ,Source, Destination, ServiceDict)
            self.initialize_GroomingTabDataBase(Source, Destination)

        #print(f"demandtabdatabase Services: {DemandTabDataBase['Services']}")
            
    def initialize_DemandTabDataBase(self, Source, Destination):
        DemandTabDataBase["Lightpathes"][(Source, Destination)] = {}
        DemandTabDataBase["Lightpathes"][(Destination, Source)] = {}

        DemandTabDataBase["GroomOut10"][(Source, Destination)] = {}
        DemandTabDataBase["GroomOut10"][(Destination, Source)] = {}

        DemandTabDataBase["Panels"][Source] = {}
        DemandTabDataBase["Panels"][Destination] = {}

        DemandTabDataBase["Shelf_Count"][Source] = 1
        DemandTabDataBase["Shelf_Count"][Destination] = 1

    def initialize_GroomingTabDataBase(self, Source, Destination):
        GroomingTabDataBase["LightPathes"][(Source, Destination)] = {}
        GroomingTabDataBase["LightPathes"][(Destination, Source)] = {}

        GroomingTabDataBase["Panels"][Source] = {}
        GroomingTabDataBase["Panels"][Destination] = {}
        
        #GroomingTabDataBase["LinkState"][(Source, Destination)] = []
        
    


    def FillDemandTabDataBase_Services(self, id, Source, Destination, ServiceDict):
        
        ServiceDict_static = {}
        ServiceDict_dynamic = {}

        # ** Dual **
        ServiceDict_static_d = {}
        ServiceDict_dynamic_d = {}
        """ for Service in ServiceDict.keys():
            Quantity = ServiceDict[Service]["Quantity"]
            for i in range(Quantity):
                item = "["+ str(id) + " - " + str ( Serviceid ) + "]" + "    " + str(Service)
                ServiceList.append(item)
        DemandTabDataBase["Services"][(Source,Destination)] = ServiceList """
        Servicedict = self.network.TrafficMatrix.DemandDict[id].ServiceDict
        #for servic
        # check wheather ServiceId is int or str
        for serviceId, service in Servicedict.items():

            serviceId = int(serviceId)
            setattr(self, "Service_item_" + str(Data["Service_item_num"]), QListWidgetItem(service.Type, self.Demand_ServiceList))
            item = getattr(self, "Service_item_" + str(Data["Service_item_num"]))
            Data["Service_item_num"] += 1
            item.setTextAlignment(Qt.AlignCenter)
            item.setToolTip(f"Type: {service.Type}\nSource: {Source}\nDestination: {Destination}")
            data = {"DemandId": id, "ServiceId": serviceId}
            item.setData(Qt.UserRole, data)
            item.setBackground(QBrush(QColor('#6088C6'), Qt.SolidPattern))

            ServiceDict_static[(id, serviceId)] = item
            ServiceDict_dynamic[(id, serviceId)] = 0
            

            # ** Dual **
            setattr(self, "Service_item_" + str(Data["Service_item_num"]), QListWidgetItem(service.Type, self.Demand_ServiceList))
            item = getattr(self, "Service_item_" + str(Data["Service_item_num"]))
            Data["Service_item_num"] += 1
            item.setTextAlignment(Qt.AlignCenter)
            item.setToolTip(f"Type: {service.Type}\nSource: {Destination}\nDestination: {Source}")
            data = {"DemandId": id, "ServiceId": serviceId}
            item.setData(Qt.UserRole, data)
            item.setBackground(QBrush(QColor('#6088C6'), Qt.SolidPattern))

            ServiceDict_static_d[(id, serviceId)] = item
            ServiceDict_dynamic_d[(id, serviceId)] = 0
            

        DemandTabDataBase["Services"][(Source, Destination)] = ServiceDict_dynamic

        # ** Dual **
        DemandTabDataBase["Services"][(Destination, Source)] = ServiceDict_dynamic_d

        if (Source in DemandTabDataBase["Services_static"]) is False:
            DemandTabDataBase["Services_static"][Source] = {}

        # ** Dual **
        if (Destination in DemandTabDataBase["Services_static"]) is False:
            DemandTabDataBase["Services_static"][Destination] = {}
            
        DemandTabDataBase["Services_static"][Source].update(ServiceDict_static)

        # ** Dual **
        DemandTabDataBase["Services_static"][Destination].update(ServiceDict_static_d)
    
        

    
    def Fill_Demand_SourceandDestination_combobox(self):

        SourceList = list(Data["General"]["DataSection"]["1"].values())
        DestinationList = list(Data["General"]["DataSection"]["2"].values())
        Original_Source_list = []
        for Source in SourceList :
            if (Source in DemandTabDataBase["Source_Destination"] ) == False:
                DemandTabDataBase["Source_Destination"][Source] = {"Source": Source, "DestinationList": []}
                Original_Source_list.append(Source)

        for Destination in DestinationList:
            if ( Destination in DemandTabDataBase["Source_Destination"] ) is False:
                DemandTabDataBase["Source_Destination"][Destination] = {"Source": Destination, "DestinationList": []}
                Original_Source_list.append(Destination)
        
        for i in range(len(SourceList)):
            Destination = DestinationList[i]
            Source = SourceList[i]
            DemandTabDataBase["Source_Destination"][Source]["DestinationList"].append(Destination)
            DemandTabDataBase["Source_Destination"][Destination]["DestinationList"].append(Source)

        


        self.Demand_Source_combobox.clear()
        self.Demand_Source_combobox.addItems(Original_Source_list)
    
    def UpdateDemand_ServiceList(self):

        Source = self.Demand_Source_combobox.currentText()
        Destination = self.Demand_Destination_combobox.currentText()
    
        while self.Demand_ServiceList.count() > 0:
            self.Demand_ServiceList.takeItem(0)
        for id, value in DemandTabDataBase["Services"][(Source,Destination)].items():
            item = DemandTabDataBase["Services_static"][Source][id]

            if value == 1:
                self.Demand_ServiceList.addItem(item)
            
            else:
                self.Demand_ServiceList.insertItem(0, item)
                
        self.update_demand_service_flag = False
    
    def Demand_Source_combobox_Change(self):
        Source = self.Demand_Source_combobox.currentText()
        if self.Demand_Source_flag is True:
            
            self.from_Source_to_Destination_flag = True

            if Source != '':                
                
                self.Demand_Destination_combobox.clear()
                
                
                if self.clicked_Node_flag is True:
                    
                    if Source != Data["Clicked_Node"]:
                        self.update_demand_service_flag = False
                        self.Demand_Destination_combobox.addItems(list(set(DemandTabDataBase["Source_Destination"][Source]["DestinationList"])))
                        self.update_demand_service_flag = True
                        self.Demand_Destination_combobox.setCurrentText(Data["Clicked_Node"])
                        if self.update_demand_service_flag is True:
                            self.Demand_Destination_combobox_change()
                    else:
                        self.update_demand_service_flag = True
                        self.Demand_Destination_combobox.addItems(list(set(DemandTabDataBase["Source_Destination"][Source]["DestinationList"])))
                        
                        
                else:
                    self.update_demand_service_flag = True
                    self.Demand_Destination_combobox.addItems(list(set(DemandTabDataBase["Source_Destination"][Source]["DestinationList"])))
        else:
            #self.Demand_Destination_combobox.addItems(list(set(DemandTabDataBase["Source_Destination"][Source]["DestinationList"])))
            self.Demand_Source_flag = True
            

        
    
    def Demand_Destination_combobox_change(self):
        Source = self.Demand_Source_combobox.currentText()
        Destination = self.Demand_Destination_combobox.currentText()


        if self.update_demand_service_flag is True and Destination != '' and self.Demand_combo_notifications_flag is False:

            if self.Failed_Nodes_flag is True:
                self.Demand_combobox_highlight_on_off(Source= Source,
                                                mode= "on")

            if self.clicked_Node_flag is True:
                self.clicked_Node_flag = False
            
            if self.from_Source_to_Destination_flag is True:
                self.from_Source_to_Destination_flag = False


            self.UpdateDemand_ServiceList()
            self.update_Demand_lightpath_list()
            self.update_Demand_groomout10_list()
            self.set_demand_panels()        
            self.DemandMap_Change()
        
        elif self.from_Source_to_Destination_flag is False and Destination != '' and self.Demand_combo_notifications_flag is False:
            
            if self.Failed_Nodes_flag is True:
                self.Demand_combobox_highlight_on_off(Source= Source,
                                                mode= "on")


            self.UpdateDemand_ServiceList()
            self.update_Demand_lightpath_list()
            self.update_Demand_groomout10_list()
            self.set_demand_panels()        
            self.DemandMap_Change()
    
    def Demand_combobox_highlight_on_off(self, Source, mode = "on", Target = None):
        self.Demand_combo_notifications_flag = True
        if mode == "on":
            Highlight_Font = QtGui.QFont()
            Highlight_Font.setBold(True)

            if Target is None:
                if Source in DemandTabDataBase["Failed_Demands"]:
                    for Destination in DemandTabDataBase["Failed_Demands"][Source]:
                        index = self.Demand_Destination_combobox.findText(Destination)
                        if index != -1 :
                            model = self.Demand_Destination_combobox.model().item(index)
                            model.setBackground(Qt.red)
                            model.setFont(Highlight_Font)

            elif Target is not None:
                index = self.Demand_Destination_combobox.findText(Target)
                if index != -1:
                    model = self.Demand_Destination_combobox.model().item(index)
                    model.setBackground(Qt.red)
                    model.setFont(Highlight_Font)
        
        elif mode == "off" and Target is not None:
            Highlight_Font = QtGui.QFont()
            Highlight_Font.setBold(False)
            index = self.Demand_Destination_combobox.findText(Target)
            if index != -1:
                model = self.Demand_Destination_combobox.model().item(index)
                model.setBackground(Qt.white)
                model.setFont(Highlight_Font)
        
        self.Demand_combo_notifications_flag = False
        

    def PhysicalTopologyToObject(self):

        def scale_calculation(lat, lon):
            u = utm.from_latlon(lat, lon)
            x = u[0]
            y = u[1]

            return [x,y]


        self.NodeIdMap = {}        # { name: id }
        self.IdNodeMap = {}        # {id : name}
        self.IdLocationMap = {}     # {id : [x , y]}

        for NodeData in Data["Nodes"].values():
            
            self.NodeIdMap[NodeData["Node"]] = self.network.Topology.Node.ReferenceId
            self.IdNodeMap[self.network.Topology.Node.ReferenceId] = NodeData["Node"]
            self.IdLocationMap[self.network.Topology.Node.ReferenceId] = scale_calculation(NodeData["Location"][0], NodeData["Location"][1])
            self.network.PhysicalTopology.add_node(NodeData["Location"], NodeData["ROADM_Type"])
        
        for LinkId , LinkData in Data["Links"].items():
            self.network.PhysicalTopology.add_link(self.NodeIdMap[LinkId[0]], self.NodeIdMap[LinkId[1]], LinkData["NumSpan"])
            
            # NOTE : here we are initializing link part of GroomingTabDataBase
            #GroomingTabDataBase["LinkState"][(LinkId[0], LinkId[1])] = []

            for i in range(LinkData["NumSpan"]):
                self.network.PhysicalTopology.LinkDict[(self.NodeIdMap[LinkId[0]], self.NodeIdMap[LinkId[1]])].put_fiber_Type(LinkData["Length"][i],
                 LinkData["Loss"][i], LinkData["Dispersion"][i], LinkData["Beta"][i], LinkData["Gamma"][i], i)
        
        # for using in panels widget
        Data["NodeIdMap"] = self.NodeIdMap
    
    def update_Demand_lightpath_list(self):
        #if Data["Stage_flag"] == "Grooming":
        Source = self.Demand_Source_combobox.currentText()
        Destination = self.Demand_Destination_combobox.currentText()
        #lightpath_list = list(DemandTabDataBase["Lightpathes"][(Source, Destination)].values())
        """ for i in range(self.Demand_LineList.count()):
            self.Demand_LineList.takeItem(i) """
        self.update_Demand_lightpath_list_flag = False

        while self.Demand_LineList.count() > 0:
            self.Demand_LineList.takeItem(0)
        for value in DemandTabDataBase["Lightpathes"][(Source, Destination)].values():
            self.Demand_LineList.addItem(value)

        self.update_Demand_lightpath_list_flag = True

    
    def update_Demand_groomout10_list(self):

        Source = self.Demand_Source_combobox.currentText()
        Destination = self.Demand_Destination_combobox.currentText()

        while self.groomout10_list.count() > 0:
            self.groomout10_list.takeItem(0)
        for value in DemandTabDataBase["GroomOut10"][(Source, Destination)].values():
            self.groomout10_list.addItem(value)

        
                

# NOTE: EDDITED



    def TM_CellChange_fun(self):
        row = self.Traffic_matrix.currentRow()
        if row == (Data["RowCount"] - 1):
            Data["RowCount"] += 1
            self.Traffic_matrix.setRowCount(Data["RowCount"])
            self.General_TM.setRowCount(Data["RowCount"])
        column = self.Traffic_matrix.currentColumn()
        value = self.Traffic_matrix.item(row,column)
        value = value.text()
        header = str(self.listWidget.currentItem().text())
        column_name = Data[header]["Headers"][column].strip()
        if value == "":
            if (str(row) in Data[header]["DataSection"][column_name]):
                Data[header]["DataSection"][column_name].pop(str(row))
        else:
            if column_name=='Quantity':
                if str(value).isdigit():
                    Data[header]["DataSection"][column_name][str(row)] = value
                else:
                    # error for wrong data type
                    self.TMErrorWrongDataType(column_name)
            elif column_name=='SLA' :
                if str(value).isalpha():
                    Data[header]["DataSection"][column_name][str(row)] = value
                else:
                    # error for wrong data type
                    self.TMErrorWrongDataType(column_name)
            else:
                Data[header]["DataSection"][column_name][str(row)] = value


    def GTM_CellChange_fun(self):
        row = self.General_TM.currentRow()
        if row == (Data["RowCount"] - 1):
            Data["RowCount"] += 1
            self.General_TM.setRowCount(Data["RowCount"])
            self.Traffic_matrix.setRowCount(Data["RowCount"])
        column = self.General_TM.currentColumn()
        value = self.General_TM.item(row,column)
        value = value.text()      
        if value == "":
            if (str(row) in Data["General"]["DataSection"][str(column)]):
                Data["General"]["DataSection"][str(column)].pop(str(row))
        else:
            if column == 0 and str(value).isdigit():
                Data["General"]["DataSection"][str(column)][str(row)] = value
        
            elif column==1 or column==2 or column==3 or column==4 or column==7:
                if str(value).isalpha():
                    Data["General"]["DataSection"][str(column)][str(row)] = value
                else:
                    self.GTMErrorWrongDataType(column)        
            
            elif column== 5 and type(value)==float :
                Data["General"]["DataSection"][str(column)][str(row)] = value
            elif column== 6 and type(value)==float and value <= 0.3 :
                Data["General"]["DataSection"][str(column)][str(row)] = value               
            else:
                # error for wrong data type
                self.GTMErrorWrongDataType(column)


    def GTMErrorWrongDataType(self, column):

        """ if column == 0 :
            self.ID_type_error_widget = QtWidgets.QWidget()
            self.ID_type_error = Ui_ID_type_error()
            self.ID_type_error.setupUi(self.ID_type_error_widget)
            self.ID_type_error_widget.show()
        if column == 1 :
            self.Source_type_error_widget = QtWidgets.QWidget()
            self.Source_type_error = Ui_Source_type_error()
            self.Source_type_error.setupUi(self.Source_type_error_widget)
            self.Source_type_error_widget.show()
        if column == 2 :
            self.Destination_type_error_widget = QtWidgets.QWidget()
            self.Destination_type_error = Ui_Destination_type_error()
            self.Destination_type_error.setupUi(self.Destination_type_error_widget)
            self.Destination_type_error_widget.show() """ 
        '''if column == 3 :
            self.OldCableType_type_error_widget = QtWidgets.QWidget()
            self.OldCableType_type_error = Ui_OldCableType_type_error()
            self.OldCableType_type_error.setupUi(self.OldCableType_type_error_widget)
            self.OldCableType_type_error_widget.show() 
        if column == 4 :
            self.CableType_type_error_widget = QtWidgets.QWidget()
            self.CableType_type_error = Ui_CableType_type_error()
            self.CableType_type_error.setupUi(self.CableType_type_error_widget)
            self.CableType_type_error_widget.show() 
        if column == 5 :
            self.DistanceReal_type_error_widget = QtWidgets.QWidget()
            self.DistanceReal_type_error = Ui_DistanceReal_type_error()
            self.DistanceReal_type_error.setupUi(self.DistanceReal_type_error_widget)
            self.DistanceReal_type_error_widget.show() 
        if column == 6 :
            self.Att_type_error_widget = QtWidgets.QWidget()
            self.Att_type_error = Ui_Att_type_error()
            self.Att_type_error.setupUi(self.Att_type_error_widget)
            self.Att_type_error_widget.show() 
        if column == 7 :
            self.Status_type_error_widget = QtWidgets.QWidget()
            self.Status_type_error = Ui_Status_type_error()
            self.Status_type_error.setupUi(self.Status_type_error_widget)
            self.Status_type_error_widget.show() '''
        pass

    def TMErrorWrongDataType(self, column_name):

        """ if column_name == 'Quantity' :
            self.Quantity_type_error_widget = QtWidgets.QWidget()
            self.Quantity_type_error = Ui_Quantity_type_error()
            self.Quantity_type_error.setupUi(self.Quantity_type_error_widget)
            self.Quantity_type_error_widget.show()
        if column_name=='SLA' :
            self.SLA_type_error_widget = QtWidgets.QWidget()
            self.SLA_type_error = Ui_SLA_type_error()
            self.SLA_type_error.setupUi(self.SLA_type_error_widget)
            self.SLA_type_error_widget.show() """
        pass


    def update_cells(self):
    
        '''item = self.listWidget.currentItem()
        item = str(item.text())'''
    
        for j in range(Data["General"]["ColumnCount"]):
            keys = Data["General"]["DataSection"][str(j)].keys()
            for row in list(keys):
                cell_data = Data["General"]["DataSection"][str(j)][row]
                self.General_TM.setCurrentCell(int(row),j)
                self.General_TM.setItem(int(row),j,QTableWidgetItem(cell_data))
    
    
    def add_node_button_fun(self):
        self.addnode_dialog = QtWidgets.QDialog()
        self.ui = Ui_add_node_window()
        self.ui.setupUi(self.addnode_dialog)
        self.addnode_dialog.show()
    
    def insert_link_fun(self):
        NodeCorDict = {}
        """ for id in list(Data["Links"].keys()):
            source = id[0]
            destination = id[1]
            source_cor = Data["Nodes"][source]["Coordinate"]
            destination_cor = Data["Nodes"][destination]["Coordinate"]
            loc = [source_cor,destination_cor]

            # drawing nodes and links on map
            folium.Marker(source_cor,icon=folium.Icon(color="red"), popup=  "<h2>%s</h2>" %source).add_to(self.m)
            added.append(source)
            folium.Marker(destination_cor,icon=folium.Icon(color="red"),popup= "<h2>%s</h2>" %destination).add_to(self.m)
            added.append(destination)
            folium.PolyLine(loc ,weight = 3,popup = "Link ID: %s"%(id),color = "black",opacity = 0.8).add_to(self.m) """
        for Node, data in Data["Nodes"].items():
            NodeName = data["Node"]
            Node_cor = data["Location"]
            NodeCorDict[NodeName] = Node_cor
            Icon = folium.features.CustomIcon('Icons\\blue\\server_blue.png',icon_size=(30, 30),icon_anchor=(20,30))
            folium.Marker(Node_cor ,icon = Icon, tooltip =  "<h2>%s</h2>" %NodeName).add_to(self.m)
        
        for link in Data["Links"].keys():
            Source_cor = NodeCorDict[link[0]]
            DesTination_cor = NodeCorDict[link[1]]
            loc = [Source_cor, DesTination_cor]
            folium.PolyLine(loc ,weight = 3,tooltip = "<h2>%s - %s</h2>"%(link[0], link[1]),color = "black",opacity = 0.8).add_to(self.m)

        self.m.save("map.html")

        # adding js events and settings on map

        Fig = self.m.get_root()
        Figtext = Fig.render()
        MapVar = re.findall("var( map_.*)=", Figtext)[0].strip()
        channel = "qrc:///qtwebchannel/qwebchannel.js"
        Fig.header.add_child(Element("<script src=%s></script>" %channel))
        Fig.header.add_child(Element("<link rel=\"stylesheet\" href=\"MainMap_style.css\" />"))
        '''Fig.script.add_child(Element("""window.onload = function() {
        new QWebChannel(qt.webChannelTransport, function (channel) {
        window.backend = channel.objects.backend;
        });"""))'''
        Fig.script.add_child(Element("""
        var  SetNodeGateWay_flag = null;
        var SelectSubNode_flag = null;
        var groupcolor = null;
        var marker_num = 0;
        var failed_nodes = new Object();
        var failed_nodes_list = [];
        var clusters_info = new Object();
        var clusters_info_list = [];
        var lambdas = new Object();
        var wrapper = document.createElement("div");
        var canvas = document.createElement("canvas");
        canvas.setAttribute("class", "focusArea");
        var displayArea = document.createElement('div');
        // displayArea.textContent = " ";
        displayArea.setAttribute("id", "displayArea");
        displayArea.innerHTML = "Wavelength Number: ";
        canvas.height = 50;
        canvas.width = 420
        wrapper.appendChild(canvas);
        wrapper.appendChild(displayArea);
        var Num_WL = null;
        var Num_RG = null;
        var Algorithm = null;
        var Worst_SNR = null;
        //handleMouseOverLines();
        function setcolor(text){
            groupcolor = text;
        }
        function SetNode_flag_fun(text){
            SetNodeGateWay_flag = text;
        }
        function SelectSubNode_flag_fun(text){
            SelectSubNode_flag = text;
        }
        function receive_failed_nodes(NodeName, Color, SubNode){
            failed_nodes[NodeName] = {"Color":Color, "SubNode":parseInt(SubNode)};
            failed_nodes_list.push(NodeName);
        }
        function change_failed_nodes_icon(){
            
            // loop on nodes group feature and notify their icon
            myFeatureGroup.eachLayer(function (layer) {
                var x = layer["_tooltip"]["_content"];
                var doc = new DOMParser().parseFromString(x, "text/xml");
                var z = doc.documentElement.textContent;
                NodeName = z.replace(/\s/g, '');
                if (failed_nodes_list.includes(NodeName)){
                    value = failed_nodes[NodeName]
                    Color = value["Color"]
                    SubNode = value["SubNode"]
                    index = failed_nodes_list.indexOf(NodeName);
                    failed_nodes_list.splice(index, 1);
                    
                    myFeatureGroup.removeLayer(layer);
                    latlng = layer.getLatLng()
                    %s.removeLayer(layer);
                    layer.remove();
                    if (SubNode == 0){
                        change_icon(NodeName, latlng, Color, 1, "notified")
                    } else{
                        change_icon(NodeName, latlng, Color, 0.6, "notified")
                    }
                    
                }
        });
        }
        function set_failed_node_default(Source){
            var value = failed_nodes[Source];
            var color = value["Color"];
            var subnode = value["SubNode"];
            var flag = 0;
            
            myFeatureGroup.eachLayer(function (layer) {
                var x = layer["_tooltip"]["_content"];
                var doc = new DOMParser().parseFromString(x, "text/xml");
                var z = doc.documentElement.textContent;
                NodeName = z.replace(/\s/g, '');
                if (NodeName == Source){
                    if (flag == 0){
                    var latlng = layer.getLatLng()
                    
                    %s.removeLayer(layer);
                    layer.remove();
                    if (subnode == 0){
                        
                        change_icon(NodeName, latlng, color, 1, "normal")
                    } else{
                        ("yes sub node is 1")
                        change_icon(NodeName, latlng, color, 0.6, "normal")
                    }
                }
                flag = 1;
                }
            });
        }

        function cancel_clustering(nodename){
            myFeatureGroup.eachLayer(function (layer) {

                var x = layer["_tooltip"]["_content"];
                var doc = new DOMParser().parseFromString(x, "text/xml");
                var z = doc.documentElement.textContent;
                NodeName = z.replace(/\s/g, '');

                if ( NodeName == nodename ){
                    var latlng = layer.getLatLng()

                    %s.removeLayer(layer);
                    layer.remove();

                    change_icon(NodeName, latlng, "blue", 1, "normal")

                }
            });
        }

        function update_cluster_info(nodename, color, subnode_state){
            clusters_info[nodename] = {"Color":color, "SubNode":parseInt(subnode_state)};
            clusters_info_list.push(nodename);
        }

        function hide_subnodes(){
            myFeatureGroup.eachLayer(function (layer) {
                var x = layer["_tooltip"]["_content"];
                var doc = new DOMParser().parseFromString(x, "text/xml");
                var z = doc.documentElement.textContent;
                NodeName = z.replace(/\s/g, '');

                if (clusters_info_list.includes(NodeName)){
                    SubNode_state = clusters_info[NodeName]["SubNode"];

                    if (SubNode_state == 1) {
                        layer.setOpacity(0);
                    }
                }
            });
        }

        function show_subnodes(){
            myFeatureGroup.eachLayer(function (layer) {
                var x = layer["_tooltip"]["_content"];
                var doc = new DOMParser().parseFromString(x, "text/xml");
                var z = doc.documentElement.textContent;
                NodeName = z.replace(/\s/g, '');

                if ( clusters_info_list.includes(NodeName) ){
                    SubNode_state = clusters_info[NodeName]["SubNode"];

                    if (SubNode_state == 1) {
                        layer.setOpacity(0.6);
                    }
                }
            });
        }
        function receive_lambdas(Source, Destination, value){
            a_value = JSON.parse(value)
            lambdas[[Source, Destination]] = a_value
        }
        var links_groupfeature = L.featureGroup().addTo(%s).on(\"click\", links_click_event);
        %s.eachLayer(function (layer) {
               if (layer instanceof L.Polyline){
                  layer.addTo(links_groupfeature);
               }
               
            });
        
        function google_map_view_set(green, yellow, orange){
            links_groupfeature.eachLayer(function (layer){
                var x = layer["_tooltip"]["_content"];
                var doc = new DOMParser().parseFromString(x, "text/xml");
                var z = doc.documentElement.textContent;
                link_key = z.replace(/\s/g, '');
                link_key = link_key.split("-");
                lambda_list = lambdas[link_key];
                Len = lambda_list.length;
                if ( Len <= green ){
                    layer.setStyle({
                        color: 'green'
                    });
                } else if ( Len <= yellow ){
                    layer.setStyle({
                        color: 'yellow'
                    });
                } else if ( Len <= orange ){
                    layer.setStyle({
                        color: 'orange'
                    });
                } else{
                    layer.setStyle({
                        color: 'red'
                    });
                }
            });
        }
        function google_map_view_reset(){
            links_groupfeature.eachLayer(function(layer){
                layer.setStyle({
                    color: 'black'
                });
            });
        }
        
        
        
        function links_click_event(event){
            var x = event.layer["_tooltip"]["_content"];
            var doc = new DOMParser().parseFromString(x, "text/xml");
            var z = doc.documentElement.textContent;
            link_key = z.replace(/\s/g, '');
            link_key = link_key.split("-")
            lambda_list = lambdas[link_key]
            
            drawLines(event.layer, lambda_list, handleMouseOverLines);
            
        }
        function drawLines(layer, lambdaList, callback) {
            popupOptions = {
                maxWidth: "auto"
            };
            layer.bindPopup(drawDetailBox(lambdaList), popupOptions)
            
            callback(lambdaList)
        }
        function drawDetailBox(lambdaList) {
            canvas.height = 90;
            canvas.width = 806;
            var h = canvas.height;
            const lineYStart = 15;
            const lineYEnd = h - 20;
            var ctx = canvas.getContext("2d");
            for (var i = 1; i <= 100; i++) {
                const lineX = (i * 8) - 4
                ctx.beginPath();
                ctx.moveTo(lineX, lineYStart);
                ctx.lineTo(lineX, lineYEnd);
                ctx.lineWidth = 2;
                if (lambdaList.includes(i)) {
                    ctx.strokeStyle = "black";
                } else {
                    ctx.strokeStyle = "gray";
                }
                ctx.stroke();
                ctx.save();
                var textX = lineX - 4;
                var textY = h - lineYStart;
                if (i %% 5 == 0) {
                    textY = 12;
                    ctx.translate(textX, textY);
                    ctx.rotate(-Math.PI / 5);
                    ctx.translate(-textX, -textY);
                    ctx.fillText(i, textX, lineYStart);
                }
                ctx.restore();
            }
            return wrapper;
        }
        function handleMouseOverLines(lambdaList) {
            canvas.addEventListener("mousemove", e => showLineNumberInBox(e, lambdaList));
            canvas.addEventListener("mouseleave", unshowLineNumberInBox);
        }
        function showLineNumberInBox(e, lambdaList) {
            console.log(e.offsetX);
            x = e.clientX;
            y = e.clientY;
            var lineNum = 0;
            const xOff = e.offsetX;
            if (xOff %% 8 >= 2 && xOff %% 8 <= 4) {
                cursor = " ";
                lineNum = 1 + parseInt(xOff / 8);
                if (lambdaList.includes(lineNum)) {
                    cursor = lineNum;
                }
            } else {
                cursor = " ";
            }
            document.getElementById("displayArea").style.display = 'block';
            document.getElementById("displayArea").innerHTML = 'Wavelength Number: ' + cursor;
            document.getElementById("displayArea").style.right = x + 'px';
            document.getElementById("displayArea").style.top = y + 'px';
        }
        
        function unshowLineNumberInBox() {
                document.getElementById("displayArea").innerHTML = "Wavelength Number: ";
            }
        function createLegend(num_WL, num_RG, algorithm , worst_SNR, RWA_Runtime) {
            Num_WL = num_WL;
            Num_RG = num_RG;
            Algorithm = algorithm;
            Worst_SNR = worst_SNR;
            var legend = L.control({ position: 'bottomleft' });
            legend.onAdd = function (map) {
                var div = L.DomUtil.create("div", "legend");
                div.style.backgroundColor = 'WHITE';
                div.innerHTML += '<h5>Total number of used wavelengths<b>: ' + Num_WL + '</b></h5>';
                div.innerHTML += '<h5>Total number of regenerators<b>: ' + Num_RG + '</b></h5>';
                div.innerHTML += '<h5>Used algorithm and its runtime<b>: ' + Algorithm + '  ,  ' + RWA_Runtime + ' s' + '</b></h5>';
                div.innerHTML += '<h5>Worst SNR on all links<b>: ' + Worst_SNR + '</b></h5>';
                return div;
            };
            legend.addTo(%s);
        }
        function change_icon(NodeName, latlng, Color, Opacity, mode){
                if ( mode == "normal" ){
                    var url = "Icons/" + Color + "/server_" + Color + ".png"
                } else {
                    var url = "Icons/" + Color + "/server_n" + Color + ".png"
                }
                //alert(url)
                var myIcon = L.icon({
                                        iconUrl: url,
                                        iconSize: [30, 30],
                                        iconAnchor: [20, 30],
                                    });
                var mark = L.marker(latlng,{opacity:Opacity}).setIcon(myIcon).addTo(%s);
                //var pop = L.popup({"maxWidth": "100%%"});
                //var htm = $(`<div id="htm" style="width: 100.0%%; height: 100.0%%;"><h2>${NodeName}</h2></div>`)[0];
                //pop.setContent(htm);
                mark.bindTooltip(
                `<div>
                     <h2>${NodeName}</h2>
                 </div>`,
                {"sticky": true}
            );
                mark.addTo(myFeatureGroup);
        }
        var backend_map = null;
        new QWebChannel(qt.webChannelTransport, function (channel) {
        window.backend_map = channel.objects.backend_map;
        });""" %(MapVar, MapVar, MapVar, MapVar, MapVar, MapVar, MapVar)))
        Fig.script.add_child(Element("var myFeatureGroup = L.featureGroup().addTo(%s).on(\"click\", groupClick);" %MapVar))

        Fig.script.add_child(Element("""%s.eachLayer(function (layer) {
               if (layer instanceof L.Marker){

                    
                    layer.addTo(myFeatureGroup);
               }
               
            });""" %MapVar))

        Fig.script.add_child(Element("""function groupClick(event) {
            //var degreename = event.layer.getPopup().getContent().textContent
            // TODO: change popup to tooltip
            //var degreename = event.layer.getTooltip().getContent()
            //alert(degreename)

            var x = event.layer["_tooltip"]["_content"];
            var doc = new DOMParser().parseFromString(x, "text/xml");
            var z = doc.documentElement.textContent;
            degreename = z.replace(/\s/g, '');

            //alert(groupcolor)
            

            if (SetNodeGateWay_flag == "True") {

                backend_map.Create_DataBase(degreename)

                var latlng = event.layer.getLatLng();
                
                myFeatureGroup.removeLayer(event.layer);
                %s.removeLayer(event.layer);
                event.layer.remove();
                
                
                change_icon(degreename, latlng, groupcolor, 1, "normal");


                backend_map.SetNode_flag_fun("False",groupcolor)

            } else if ( SelectSubNode_flag == "True") {

                backend_map.AddNode_DataBase(degreename)

                var latlng = event.layer.getLatLng();
                
                myFeatureGroup.removeLayer(event.layer);
                %s.removeLayer(event.layer);
                event.layer.remove();
                
                change_icon(degreename, latlng, groupcolor, 0.6, "normal");

                


            } else{
                backend_map.change_tab_to4(degreename);
            }

            
            }
            """ %(MapVar, MapVar) ))
        
        Fig.save("map.html")

        self.webengine.load(QUrl.fromLocalFile(os.path.abspath('map.html')))
        self.webengine.show()


    def SaveChanges_button_fun(self):
        # filling Network Object
        self.RWA_Success = False
        self.set_flags()
        self.PhysicalTopologyToObject()
        self.TrafficMatrixToObject()
        self.DemandTabDataBase_Setup()
        self.Demand_Shelf_set()
        self.Fill_Demand_SourceandDestination_combobox()

        self.tabWidget.setTabEnabled(1, True)
        self.tabWidget.setTabEnabled(2, True)

    def set_flags(self):
        self.from_Source_to_Destination_flag = False
        self.clicked_Node_flag = False
        self.Demand_Source_flag = False
        self.update_demand_service_flag = False
        self.Demand_first_run = False
        Data["DemandTab_firststart_flag"] = False
        Data["demand_first_run_flag"] = False
        Data["first_run_flag"] = False
        self.Data_file_Flag = False
        self.update_Demand_lightpath_list_flag = True
        self.Demand_shelf_init_flag = False
        self.Failed_Nodes_flag = False
        
    
    def DemandTabDataBase_Setup(self):
        for node in Data["Nodes"].values():
            nodename = node["Node"]
            DemandTabDataBase["Panels"][nodename] = {}
        
    
    def Demand_Shelf_set(self):
        # TODO: add this method to Demand tab initializer
        if self.Demand_shelf_init_flag is False: 
            Source = self.Demand_Source_combobox.currentText()
            Destination = self.Demand_Destination_combobox.currentText()
            for i in range(1,15):
                Data["DemandPanel_" + str(i)] = QtWidgets.QGridLayout(getattr(self, "DemandPanel_" + str(i)))
                #setattr(self, "DemandPanel_" + str(i),QMdiSubWindow())
                #Data["DemandPanel_" + str(i)] = getattr(ui, "DemandPanel_" + str(i))
                #Data["DemandPanel_" + str(i)].setWindowFlag(Qt.FramelessWindowHint)
                Data["DemandPanel_" + str(i)].setMargin(0)
                Data["DemandPanel_" + str(i)].addWidget(BLANK_Demand(str(i), Source, Destination))

                #self.Demand_mdi.addSubWindow(Data["DemandPanel_" + str(i)])
                #Data["DemandPanel_" + str(i)].show()
                self.Demand_shelf_init_flag = True
    
    def add_demand_shelf(self):

        Source = self.Demand_Source_combobox.currentText()
        Destination = self.Demand_Destination_combobox.currentText()

        setattr(self, "shelf_" + str(self.New_Demand_Shelf_Num), QWidget())
        setattr(self, "shelf_" + str(self.New_Demand_Shelf_Num) + "_layout", QtWidgets.QHBoxLayout(getattr(self, "shelf_" + str(self.New_Demand_Shelf_Num))))
        
        getattr(self, "shelf_" + str(self.New_Demand_Shelf_Num) + "_layout").setContentsMargins(0, 0, 0, 0)
        getattr(self, "shelf_" + str(self.New_Demand_Shelf_Num) + "_layout").setSpacing(0)

        for i in range(((self.New_Demand_Shelf_Num - 1) * 14) + 1, ((self.New_Demand_Shelf_Num - 1) * 14) + 15):
            setattr(self, "DemandPanel_" + str(i), QWidget(getattr(self, "shelf_" + str(self.New_Demand_Shelf_Num))))
            getattr(self, "shelf_" + str(self.New_Demand_Shelf_Num) + "_layout").addWidget(getattr(self, "DemandPanel_" + str(i)))
            Data["DemandPanel_" + str(i)] = QtWidgets.QGridLayout(getattr(self, "DemandPanel_" + str(i)))
            Data["DemandPanel_" + str(i)].setMargin(0)
            Data["DemandPanel_" + str(i)].addWidget(BLANK_Demand(str(i), Source, Destination))
        
        self.Demand_tab.addTab(getattr(self, "shelf_" + str(self.New_Demand_Shelf_Num)), "Shelf " + str(self.New_Demand_Shelf_Num))
        
        self.New_Demand_Shelf_Num += 1


    def get_panel_num(self, Source):
            IdList = list(DemandTabDataBase["Panels"][Source].keys())
            
            # if shelf is empty this method must return 1 in ## string ##
            if not IdList:
                return "1"
            IdList = list(map(lambda x : int(x), IdList))
            MaxId = max(IdList)

            if (MaxId + 1) // 15 >= self.New_Demand_Shelf_Num - 1:
                self.add_demand_shelf()
            
            if ((MaxId + 1) // 15 ) + 1 > DemandTabDataBase["Shelf_Count"][Source]:
                DemandTabDataBase["Shelf_Count"][Source] = ((MaxId + 1) // 15 ) + 1

            return str(MaxId + 1)

    def create_ClientsCapacityList(self, DemandId, ServiceIdList, netobj):
            OutputList = []
            LineCapacity = 0
            for ServiceId in ServiceIdList:
                # if its normal service
                if ServiceId in netobj.TrafficMatrix.DemandDict[DemandId].ServiceDict:
                    ServiceObj = netobj.TrafficMatrix.DemandDict[DemandId].ServiceDict[ServiceId]
                    LineCapacity += ServiceObj.BW
                else:
                    # if its GroomOut10
                    ServiceObj = netobj.TrafficMatrix.GroomOut10Dict[(DemandId, ServiceId)]
                    LineCapacity += ServiceObj.Capacity

                OutputList.append(ServiceObj.Type)
                
            
            return OutputList, LineCapacity
    
    # NOTE: this method just handles MP1H and TP1H
    def fill_DemandTabDataBase(self, netobj):
        
        # lightpath and panel part ( part 1 )
        for id, lightpath in netobj.LightPathDict.items():
            
            
            Source = self.IdNodeMap[lightpath.Source]
            Destination = self.IdNodeMap[lightpath.Destination]

            DualPanelsId = self.generate_dual_panel_num(Destination)

            type = lightpath.Type
            DemandId = lightpath.DemandId
            Capacity = lightpath.Capacity
            
            

            """ ## debug section
            print("Source: ", Source)
            print("Destination:" , Destination)
            print("DemandId :", DemandId)
            print("serviceIdList :", lightpath.ServiceIdList)

            ## end of debug section """
            
            # checking wheather lightpath is created by tp1h or not
            if len(lightpath.ServiceIdList) == 1:
                panelid = self.get_panel_num(Source)
                #DemandTabDataBase["Panels"][Source][panelid] = TP1H_L(DemandId, lightpath.ServiceIdList[0], "100GE", id)
                DemandTabDataBase["Panels"][Source][panelid] = TP1H_L(  DemandId= DemandId,
                                                                        ServiceId= lightpath.ServiceIdList[0],
                                                                        Line= "100GE",
                                                                        LightPathId= id,
                                                                        Destination= Destination,
                                                                        DualPanelsId= DualPanelsId)

                # ** Dual **
                DemandTabDataBase["Panels"][Destination][DualPanelsId[0]] = TP1H_L(  DemandId= DemandId,
                                                                        ServiceId= lightpath.ServiceIdList[0],
                                                                        Line= "100GE",
                                                                        LightPathId= id,
                                                                        Destination= Source,
                                                                        DualPanelsId= (panelid, (str(int(panelid) + 1))))

                """ ## debug section
                print(DemandTabDataBase["Panels"][Source][panelid].__dict__)

                ## end of debug section """
                DemandTabDataBase["Panels"][Source][str(int(panelid) + 1)] = TP1H_R(    LeftId= panelid,
                                                                                        Destination= Destination,
                                                                                        DualPanelsId= DualPanelsId)

                # ** Dual **
                DemandTabDataBase["Panels"][Destination][DualPanelsId[1]] = TP1H_R(    LeftId= DualPanelsId[0],
                                                                                        Destination= Source,
                                                                                        DualPanelsId = (panelid, (str(int(panelid) + 1))))


            else:
                panelid = self.get_panel_num(Source)
                ClientCapacity, LineCapacity = self.create_ClientsCapacityList(DemandId, lightpath.ServiceIdList, netobj)
                #LineCapacity = len(ClientCapacity) * 10
                
                ClientLen = len(ClientCapacity) 
                if ClientLen != 10:
                    for i in range(10 - ClientLen):
                        ClientCapacity.append(0)
                
                
                #DemandTabDataBase["Panels"][Source][panelid] = MP1H_L(ClientCapacity, LineCapacity, lightpath.ServiceIdList, [DemandId for i in range(10)], id, LightPath_flag= 1)
                DemandTabDataBase["Panels"][Source][panelid] = MP1H_L(  ClientsCapacity= ClientCapacity,
                                                                        LineCapacity= LineCapacity,
                                                                        ServiceIdList= list(lightpath.ServiceIdList),
                                                                        DemandIdList= [DemandId for i in range(10)],
                                                                        LightPathId= id,
                                                                        LightPath_flag= 1,
                                                                        Destination= Destination,
                                                                        DualPanelsId= DualPanelsId)

                # ** Dual **
                DemandTabDataBase["Panels"][Destination][DualPanelsId[0]] = MP1H_L(  ClientsCapacity= ClientCapacity,
                                                                        LineCapacity= LineCapacity,
                                                                        ServiceIdList= list(lightpath.ServiceIdList),
                                                                        DemandIdList= [DemandId for i in range(10)],
                                                                        LightPathId= id,
                                                                        LightPath_flag= 1,
                                                                        Destination= Source,
                                                                        DualPanelsId= (panelid, (str(int(panelid) + 1))))


                """ ## debug section
                print(DemandTabDataBase["Panels"][Source][panelid].__dict__)

                ## end of debug section """
                DemandTabDataBase["Panels"][Source][str(int(panelid) + 1)] = MP1H_R(    LeftId= panelid,
                                                                                        Destination= Destination,
                                                                                        DualPanelsId= DualPanelsId)

                # ** Dual **
                DemandTabDataBase["Panels"][Destination][DualPanelsId[1]] = MP1H_R(    LeftId= DualPanelsId[0],
                                                                                        Destination= Source,
                                                                                        DualPanelsId= (panelid, (str(int(panelid) + 1))))


                print(f"panels part--> Source:{Source} panels:{DemandTabDataBase['Panels'][Source]}")
                print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
            
            # lightPath part ( part 2 )
            setattr(self, "LightPath_item_" + str(Data["LightPath_item_num"]), QListWidgetItem("100GE", self.Demand_LineList))
            item = getattr(self, "LightPath_item_" + str(Data["LightPath_item_num"]))
            Data["LightPath_item_num"] += 1
            UserData = {"LightPathId":id, "Source":Source, "Destination":Destination, "Capacity":Capacity, "Type": type, "PanelId": panelid}
            item.setToolTip(f"Source: {Source}\nDestination: {Destination}\nCapacity: {Capacity}\nType: {type}")
            item.setData(Qt.UserRole, UserData)
            item.setTextAlignment(Qt.AlignCenter)

            DemandTabDataBase["Lightpathes"][(Source, Destination)][id] = item

            # ** Dual **

            setattr(self, "LightPath_item_" + str(Data["LightPath_item_num"]), QListWidgetItem("100GE", self.Demand_LineList))
            item = getattr(self, "LightPath_item_" + str(Data["LightPath_item_num"]))
            Data["LightPath_item_num"] += 1
            UserData = {"LightPathId":id, "Source":Destination, "Destination":Source, "Capacity":Capacity, "Type": type, "PanelId": DualPanelsId[0]}
            item.setToolTip(f"Source: {Destination}\nDestination: {Source}\nCapacity: {Capacity}\nType: {type}")
            item.setData(Qt.UserRole, UserData)
            item.setTextAlignment(Qt.AlignCenter)

            DemandTabDataBase["Lightpathes"][(Destination, Source)][id] = item




    def fill_DemandTabDataBase_MP2X(self, full_MP2X_Dict, half_MP2X_Dict, netobj):

        # Full MP2X Section
        for DemandId, Servicetuple in full_MP2X_Dict.items():
            Source = self.IdNodeMap[netobj.TrafficMatrix.DemandDict[DemandId].Source]
            Destination = self.IdNodeMap[netobj.TrafficMatrix.DemandDict[DemandId].Destination]

            DualPanelsId = self.generate_dual_panel_num(Destination)
            
            # panel part ( creating panels object )
            PanelId = self.get_panel_num(Source)

            ClientsCapacity_1 , LineCapacity_1 = self.create_ClientsCapacityList(DemandId, netobj.TrafficMatrix.GroomOut10Dict[(DemandId, Servicetuple[0])].ServiceIdList, netobj)
            ClientsCapacity_2 , LineCapacity_2 = self.create_ClientsCapacityList(DemandId, netobj.TrafficMatrix.GroomOut10Dict[(DemandId, Servicetuple[1])].ServiceIdList, netobj)

            ClientsCapacity = []
            ClientsCapacity.extend(ClientsCapacity_1)
            ClientsCapacity.extend(ClientsCapacity_2)

            ServiceIdList = []
            ServiceIdList.extend(netobj.TrafficMatrix.GroomOut10Dict[(DemandId, Servicetuple[0])].ServiceIdList)
            ServiceIdList.extend(netobj.TrafficMatrix.GroomOut10Dict[(DemandId, Servicetuple[1])].ServiceIdList)

            LightPathId_1 = netobj.TrafficMatrix.GroomOut10Dict[(DemandId, Servicetuple[0])].LightPathId
            LightPathId_2 = netobj.TrafficMatrix.GroomOut10Dict[(DemandId, Servicetuple[1])].LightPathId

            ClientLen = len(ClientsCapacity) 
            if ClientLen != 16:
                for i in range(16 - ClientLen):
                    ClientsCapacity.append(0)

            # creating left panel of MP2X
            DemandTabDataBase["Panels"][Source][PanelId] = MP2X_L(  ClientsCapacity= ClientsCapacity,
                                                                    LinesCapacity= [LineCapacity_1, LineCapacity_2],
                                                                    ServiceIdList= ServiceIdList,
                                                                    DemandIdList= [DemandId for _ in range(16)],
                                                                    LineIdList= list(Servicetuple),
                                                                    Line_1_ServiceIdList= list(netobj.TrafficMatrix.GroomOut10Dict[(DemandId, Servicetuple[0])].ServiceIdList),
                                                                    Line_2_ServiceIdList= list(netobj.TrafficMatrix.GroomOut10Dict[(DemandId, Servicetuple[1])].ServiceIdList),
                                                                    Destination= Destination,
                                                                    DualPanelsId= DualPanelsId)

            # ** Dual **
            DemandTabDataBase["Panels"][Destination][DualPanelsId[0]] = MP2X_L(  ClientsCapacity= ClientsCapacity,
                                                                    LinesCapacity= [LineCapacity_1, LineCapacity_2],
                                                                    ServiceIdList= ServiceIdList,
                                                                    DemandIdList= [DemandId for _ in range(16)],
                                                                    LineIdList= list(Servicetuple),
                                                                    Line_1_ServiceIdList= list(netobj.TrafficMatrix.GroomOut10Dict[(DemandId, Servicetuple[0])].ServiceIdList),
                                                                    Line_2_ServiceIdList= list(netobj.TrafficMatrix.GroomOut10Dict[(DemandId, Servicetuple[1])].ServiceIdList),
                                                                    Destination= Source,
                                                                    DualPanelsId= (PanelId, (str(int(PanelId) + 1))))
            
            # Creating Right Panel of MP2X
            DemandTabDataBase["Panels"][Source][str(int(PanelId) + 1)] = MP2X_R(LeftId= PanelId,
                                                                                Destination= Destination,
                                                                                DualPanelsId= DualPanelsId)

            # ** Dual **
            DemandTabDataBase["Panels"][Destination][DualPanelsId[1]] = MP2X_R(LeftId= DualPanelsId[0],
                                                                                Destination= Source,
                                                                                DualPanelsId= (PanelId, (str(int(PanelId) + 1))))


            # creating Qlistwidgetitem item part
            item_1 = QListWidgetItem("GroomOut10", self.groomout10_list)
            UserData_1 = {"GroomOut10Id":Servicetuple[0], "Source":Source, "Destination":Destination, "Capacity":LineCapacity_1, "Type": "GroomOut10", "PanelId": PanelId, "DemandId": DemandId}
            item_1.setToolTip(f"Source: {Source}\nDestination: {Destination}\nCapacity: {LineCapacity_1}\nType: GroomOut10")
            item_1.setData(Qt.UserRole, UserData_1)
            item_1.setTextAlignment(Qt.AlignCenter)

            # ** Dual **
            item_1_d = QListWidgetItem("GroomOut10", self.groomout10_list)
            UserData_1_d = {"GroomOut10Id":Servicetuple[0], "Source":Destination, "Destination":Source, "Capacity":LineCapacity_1, "Type": "GroomOut10", "PanelId": DualPanelsId[0], "DemandId": DemandId}
            item_1_d.setToolTip(f"Source: {Destination}\nDestination: {Source}\nCapacity: {LineCapacity_1}\nType: GroomOut10")
            item_1_d.setData(Qt.UserRole, UserData_1_d)
            item_1_d.setTextAlignment(Qt.AlignCenter)

            # stricking out item if its assigned to a lightpath
            if LightPathId_1 is not None:
                font = item_1.font()
                font.setStrikeOut(True)
                item_1.setFont(font)

                # ** Dual **
                item_1_d.setFont(font)

                MP1H_data = DemandTabDataBase["Lightpathes"][(Source, Destination)][LightPathId_1].data(Qt.UserRole)
                MP1H_Id = MP1H_data["PanelId"]

                index = DemandTabDataBase["Panels"][Source][MP1H_Id].ServiceIdList.index(Servicetuple[0])
                UserData_1["MP1H_Client_Id"] = (MP1H_Id, str(index + 1))

                # ** Dual **
                MP1H_data = DemandTabDataBase["Lightpathes"][(Destination, Source)][LightPathId_1].data(Qt.UserRole)
                MP1H_Id = MP1H_data["PanelId"]

                index = DemandTabDataBase["Panels"][Destination][MP1H_Id].ServiceIdList.index(Servicetuple[0])
                UserData_1_d["MP1H_Client_Id"] = (MP1H_Id, str(index + 1))

                item_1.setData(Qt.UserRole, UserData_1)

                # ** Dual **
                item_1_d.setData(Qt.UserRole, UserData_1_d)

            DemandTabDataBase["GroomOut10"][(Source, Destination)][Servicetuple[0]] = item_1

            # ** Dual **
            DemandTabDataBase["GroomOut10"][(Destination, Source)][Servicetuple[0]] = item_1_d

            item_2 = QListWidgetItem("GroomOut10", self.groomout10_list)
            UserData_2 = {"GroomOut10Id":Servicetuple[1], "Source":Source, "Destination":Destination, "Capacity":LineCapacity_2, "Type": "GroomOut10", "PanelId": PanelId, "DemandId": DemandId}
            item_2.setToolTip(f"Source: {Source}\nDestination: {Destination}\nCapacity: {LineCapacity_2}\nType: GroomOut10")
            item_2.setData(Qt.UserRole, UserData_2)
            item_2.setTextAlignment(Qt.AlignCenter)

            # ** Dual **
            item_2_d = QListWidgetItem("GroomOut10", self.groomout10_list)
            UserData_2_d = {"GroomOut10Id":Servicetuple[1], "Source":Destination, "Destination":Source, "Capacity":LineCapacity_2, "Type": "GroomOut10", "PanelId": DualPanelsId[0], "DemandId": DemandId}
            item_2_d.setToolTip(f"Source: {Destination}\nDestination: {Source}\nCapacity: {LineCapacity_2}\nType: GroomOut10")
            item_2_d.setData(Qt.UserRole, UserData_2_d)
            item_2_d.setTextAlignment(Qt.AlignCenter)

            # stricking out item if its assigned to a lightpath
            if LightPathId_2 is not None:
                font = item_2.font()
                font.setStrikeOut(True)
                item_2.setFont(font)

                # ** Dual **
                item_2_d.setFont(font)

                MP1H_data = DemandTabDataBase["Lightpathes"][(Source, Destination)][LightPathId_2].data(Qt.UserRole)
                MP1H_Id = MP1H_data["PanelId"]

                index = DemandTabDataBase["Panels"][Source][MP1H_Id].ServiceIdList.index(Servicetuple[1])
                UserData_2["MP1H_Client_Id"] = (MP1H_Id, str(index + 1))

                # ** Dual **
                MP1H_data = DemandTabDataBase["Lightpathes"][(Destination, Source)][LightPathId_2].data(Qt.UserRole)
                MP1H_Id = MP1H_data["PanelId"]

                index = DemandTabDataBase["Panels"][Destination][MP1H_Id].ServiceIdList.index(Servicetuple[1])
                UserData_2_d["MP1H_Client_Id"] = (MP1H_Id, str(index + 1))

                item_2.setData(Qt.UserRole, UserData_2)

                # ** Dual **
                item_2_d.setData(Qt.UserRole, UserData_2_d)

            DemandTabDataBase["GroomOut10"][(Source, Destination)][Servicetuple[1]] = item_2

            # ** Dual **
            DemandTabDataBase["GroomOut10"][(Destination, Source)][Servicetuple[1]] = item_2_d
        
        # Half MP2X Part
        for DemandId , GroomOutId in half_MP2X_Dict.items():
            

            Source = self.IdNodeMap[netobj.TrafficMatrix.DemandDict[DemandId].Source]
            Destination = self.IdNodeMap[netobj.TrafficMatrix.DemandDict[DemandId].Destination]

            DualPanelsId = self.generate_dual_panel_num(Destination)

            LightPathId = netobj.TrafficMatrix.GroomOut10Dict[(DemandId, GroomOutId)].LightPathId
            
            # panel part ( creating panels object )
            PanelId = self.get_panel_num(Source)

            ClientsCapacity , LineCapacity = self.create_ClientsCapacityList(DemandId, netobj.TrafficMatrix.GroomOut10Dict[(DemandId, GroomOutId)].ServiceIdList, netobj)

            ClientLen = len(ClientsCapacity) 
            if ClientLen != 16:
                for i in range(16 - ClientLen):
                    ClientsCapacity.append(0)
            
            # creating left panel of MP2X
            DemandTabDataBase["Panels"][Source][PanelId] = MP2X_L(  ClientsCapacity= list(ClientsCapacity),
                                                                    LinesCapacity= [LineCapacity, 0],
                                                                    ServiceIdList= list(netobj.TrafficMatrix.GroomOut10Dict[(DemandId, GroomOutId)].ServiceIdList),
                                                                    DemandIdList= [DemandId for _ in range(16)],
                                                                    LineIdList= [GroomOutId, None],
                                                                    Line_1_ServiceIdList= list(netobj.TrafficMatrix.GroomOut10Dict[(DemandId, GroomOutId)].ServiceIdList),
                                                                    Destination= Destination,
                                                                    DualPanelsId= DualPanelsId)

            # ** Dual **
            DemandTabDataBase["Panels"][Destination][DualPanelsId[0]] = MP2X_L(  ClientsCapacity= list(ClientsCapacity),
                                                                    LinesCapacity= [LineCapacity, 0],
                                                                    ServiceIdList= list(netobj.TrafficMatrix.GroomOut10Dict[(DemandId, GroomOutId)].ServiceIdList),
                                                                    DemandIdList= [DemandId for _ in range(16)],
                                                                    LineIdList= [GroomOutId, None],
                                                                    Line_1_ServiceIdList= list(netobj.TrafficMatrix.GroomOut10Dict[(DemandId, GroomOutId)].ServiceIdList),
                                                                    Destination= Source,
                                                                    DualPanelsId= (PanelId, (str(int(PanelId) + 1))))
            
            # Creating Right Panel of MP2X
            DemandTabDataBase["Panels"][Source][str(int(PanelId) + 1)] = MP2X_R(LeftId= PanelId,
                                                                                Destination= Destination,
                                                                                DualPanelsId= DualPanelsId)

            # ** Dual **
            DemandTabDataBase["Panels"][Destination][DualPanelsId[1]] = MP2X_R(LeftId= DualPanelsId[0],
                                                                                Destination= Source,
                                                                                DualPanelsId = (PanelId, (str(int(PanelId) + 1))) )

            # creating Qlistwidgetitem item part
            item = QListWidgetItem("GroomOut10", self.groomout10_list)
            UserData = {"GroomOut10Id":GroomOutId, "Source":Source, "Destination":Destination, "Capacity":LineCapacity, "Type": "GroomOut10", "PanelId": PanelId, "DemandId": DemandId}
            item.setToolTip(f"Source: {Source}\nDestination: {Destination}\nCapacity: {LineCapacity}\nType: GroomOut10")
            item.setData(Qt.UserRole, UserData)
            item.setTextAlignment(Qt.AlignCenter)

            # ** Dual **
            item_d = QListWidgetItem("GroomOut10", self.groomout10_list)
            UserData_d = {"GroomOut10Id":GroomOutId, "Source":Destination, "Destination":Source, "Capacity":LineCapacity, "Type": "GroomOut10", "PanelId": DualPanelsId[0], "DemandId": DemandId}
            item_d.setToolTip(f"Source: {Destination}\nDestination: {Source}\nCapacity: {LineCapacity}\nType: GroomOut10")
            item_d.setData(Qt.UserRole, UserData)
            item_d.setTextAlignment(Qt.AlignCenter)

            # stricking out item if its assigned to a lightpath
            if LightPathId is not None:
                font = item.font()
                font.setStrikeOut(True)
                item.setFont(font)

                # ** Dual **
                item_d.setFont(font)

                # finding MP1H_Client_id
                MP1H_data = DemandTabDataBase["Lightpathes"][(Source, Destination)][LightPathId].data(Qt.UserRole)
                MP1H_Id = MP1H_data["PanelId"]

                index = DemandTabDataBase["Panels"][Source][MP1H_Id].ServiceIdList.index(GroomOutId)
                UserData["MP1H_Client_Id"] = (MP1H_Id, str(index + 1))

                # ** Dual **
                MP1H_data = DemandTabDataBase["Lightpathes"][(Destination, Source)][LightPathId].data(Qt.UserRole)
                MP1H_Id = MP1H_data["PanelId"]

                index = DemandTabDataBase["Panels"][Destination][MP1H_Id].ServiceIdList.index(GroomOutId)
                UserData["MP1H_Client_Id"] = (MP1H_Id, str(index + 1))

                item.setData(Qt.UserRole, UserData)

                # ** Dual **
                item_d.setData(Qt.UserRole, UserData_d)

            DemandTabDataBase["GroomOut10"][(Source, Destination)][GroomOutId] = item

            # ** Dual **
            DemandTabDataBase["GroomOut10"][(Destination, Source)][GroomOutId] = item_d

    
    def generate_dual_panel_num(self, Destination):

        IdList = list(DemandTabDataBase["Panels"][Destination].keys())
            
        # if shelf is empty this method must return 1 in ## string ##
        if not IdList:
            return ("1", "2")
        IdList = list(map(lambda x : int(x), IdList))
        if len(IdList) == max(IdList):
            MaxId = max(IdList)

            if ((MaxId + 1) // 15) + 1 > DemandTabDataBase["Shelf_Count"][Destination]:
                DemandTabDataBase["Shelf_Count"][Destination] = ((MaxId + 1) // 15) + 1
            return (str(MaxId + 1), str(MaxId + 2))
        else:
            for i in range(1,max(IdList), 2):
                if ( i in IdList ) is False:
                    return (str(i), str(i+1))

    
    def fill_GroomingTabDataBase(self, netobj, RWA_Runtime):

        
        for id, lightpath in list(netobj.LightPathDict.items()):

            if isinstance(id, str):
                netobj.LightPathDict[int(id)] = netobj.LightPathDict.pop(id)
                id = int(id)
            
            Source = self.IdNodeMap[lightpath.Source]
            Destination = self.IdNodeMap[lightpath.Destination]
            Working = lightpath.WorkingPath
            Protection = lightpath.ProtectionPath
            DemandId = lightpath.DemandId
            WaveLength = lightpath.WaveLength
            RG_w = lightpath.RegeneratorNode_w
            RG_p = lightpath.RegeneratorNode_p
            SNR_w = list(map(lambda x : round(x, 2), lightpath.SNR_w))
            SNR_p = list(map(lambda x : round(x, 2), lightpath.SNR_p))
            WorkingLambdaList = lightpath.WaveLength
            ProtectionLambdaList = lightpath.WaveLength

            # adding pathes to to GroomingTabDataBase ( lightpath part )
            GroomingTabDataBase["LightPathes"][(Source, Destination)][id] = {}
            GroomingTabDataBase["LightPathes"][(Source, Destination)][id]["Working"] = Working
            GroomingTabDataBase["LightPathes"][(Source, Destination)][id]["Protection"] = Protection
            GroomingTabDataBase["LightPathes"][(Source, Destination)][id]["RG_w"] = RG_w
            GroomingTabDataBase["LightPathes"][(Source, Destination)][id]["RG_p"] = RG_p
            GroomingTabDataBase["LightPathes"][(Source, Destination)][id]["SNR_w"] = SNR_w
            GroomingTabDataBase["LightPathes"][(Source, Destination)][id]["SNR_p"] = SNR_p
            GroomingTabDataBase["LightPathes"][(Source, Destination)][id]["WorkingLambdaList"] = WorkingLambdaList
            GroomingTabDataBase["LightPathes"][(Source, Destination)][id]["ProtectionLambdaList"] = ProtectionLambdaList

            # ** Dual **
            GroomingTabDataBase["LightPathes"][(Destination, Source)][id] = {}
            GroomingTabDataBase["LightPathes"][(Destination, Source)][id]["Working"] = Working
            GroomingTabDataBase["LightPathes"][(Destination, Source)][id]["Protection"] = Protection
            GroomingTabDataBase["LightPathes"][(Destination, Source)][id]["RG_w"] = RG_w
            GroomingTabDataBase["LightPathes"][(Destination, Source)][id]["RG_p"] = RG_p
            GroomingTabDataBase["LightPathes"][(Destination, Source)][id]["SNR_w"] = SNR_w
            GroomingTabDataBase["LightPathes"][(Destination, Source)][id]["SNR_p"] = SNR_p
            GroomingTabDataBase["LightPathes"][(Destination, Source)][id]["WorkingLambdaList"] = WorkingLambdaList
            GroomingTabDataBase["LightPathes"][(Destination, Source)][id]["ProtectionLambdaList"] = ProtectionLambdaList

            
        # filling LinkSate Part
        self.Max_LinkState = 0
        for key, value in netobj.PhysicalTopology.LinkDict.items():
            GroomingTabDataBase["LinkState"][(self.IdNodeMap[key[0]], self.IdNodeMap[key[1]])] = value.LinkState


            if len(value.LinkState) > self.Max_LinkState:
                self.Max_LinkState = len(value.LinkState)
        
        for key, value in netobj.PhysicalTopology.NodeDict.items():
            GroomingTabDataBase["NodeState"][self.IdNodeMap[int(key)]] = value.NodeState

        
        for key in list(netobj.PhysicalTopology.NodeDict.keys()):
            if isinstance(key, str):
                netobj.PhysicalTopology.NodeDict[int(key)] = netobj.PhysicalTopology.NodeDict.pop(key)

        self.send_lambdas_to_JS()
        self.create_legend(Num_WL= netobj.ResultObj.Num_WL,
                            Num_RG= netobj.ResultObj.Num_RG,
                            Algorithm= netobj.ParamsObj.Algorithm,
                            Worst_SNR= round(netobj.ResultObj.Worst_SNR, 2),
                            RWA_Runtime= round(RWA_Runtime, 2))

    def send_lambdas_to_JS(self):
        print(self.webengine.geometry())
        for key , value in GroomingTabDataBase["LinkState"].items():
            Source = key[0]
            Destination = key[1]
            self.webengine.page().runJavaScript("receive_lambdas(\"%s\", \"%s\", \"%s\")" %(Source, Destination, value))
    
    def create_legend(self, Num_WL, Num_RG, Algorithm, Worst_SNR, RWA_Runtime):
        self.webengine.page().runJavaScript("createLegend(\"%s\", \"%s\", \"%s\", \"%s\", \"%s\")" %(Num_WL, Num_RG, Algorithm, Worst_SNR, RWA_Runtime))
                
         
    def failed_grooming_nodes(self):

        # finding failed nodes
        NotifiedNodes = self.find_grooming_failed_sources()

        # finding failed nodes cluster and their color and creating a dictionary for senting to JS
        #print(f" -- >> clustering database : {Data['Clustering']}")
        failed_nodes = {}
        Num_failed_nodes = len(NotifiedNodes)
        for GateWay , value in Data["Clustering"].items():

            if GateWay in NotifiedNodes:
                failed_nodes[GateWay] = {"Color": value["Color"], "SubNode": 0}
                NotifiedNodes.remove(GateWay)
                Num_failed_nodes -= 1

                if Num_failed_nodes == 0:
                    break
            
            intersect_nodes = list(set(NotifiedNodes) & set(value["SubNodes"]))

            for failed_node in intersect_nodes:
                failed_nodes[failed_node] =  {"Color": value["Color"], "SubNode": 1}
                NotifiedNodes.remove(failed_node)
                Num_failed_nodes -= 1

                if Num_failed_nodes == 0:
                    break

        for remained_nodes in NotifiedNodes:
            # NOTE: default color is blue in this moment
            failed_nodes[remained_nodes] = {"Color": "blue", "SubNode": 0}
        
        """ class Double_quote(dict):
            def __str__(self):
                return json.dumps(self)
        failed_nodes = Double_quote(failed_nodes) """
        self.failed_nodes = failed_nodes
        print(f" -->> failed nodes : {failed_nodes}")
        self.failed_nodes_javascript(failed_nodes)


    def failed_nodes_javascript(self,failed_nodes):
        for nodename , value in failed_nodes.items():
            color = value["Color"]
            SubNode = value["SubNode"]
            self.webengine.page().runJavaScript("receive_failed_nodes(\"%s\", \"%s\", \"%s\")" %(nodename, color, SubNode))
        
        self.webengine.page().runJavaScript("change_failed_nodes_icon()")

    def set_failed_nodes_default(self, source):
        if source in self.failed_nodes:
            self.webengine.page().runJavaScript("set_failed_node_default(\"%s\")" %source)

        
    def open_ImportUI_fun(self):

        self.ImportUI_dialog = QtWidgets.QDialog()
        self.ImportUI = Ui_ImportMenuUI()
        self.ImportUI.setupUi(self.ImportUI_dialog)
        self.ImportUI_dialog.show()


    
    def grooming_button_fun(self):        

        self.groomingwindow_dialog = QtWidgets.QDialog()
        self.grooming_window_ui = Ui_grooming_window()
        self.grooming_window_ui.setupUi(self.groomingwindow_dialog)
        self.groomingwindow_dialog.show()
        

    def grooming_procedure(self, MP1H_Threshold):

        self.clean_database_for_grooming(self.network)

        Remain_lower100,full_mp2x_lines, half_mp2x_lines  = grooming_fun(self.network, int(MP1H_Threshold))

        self.fill_basic_demandtabdatabase(self.network)

        # creating new 
        self.create_new_demand_services(self.network)
        
        
        # filling Demand DataBase 
        self.fill_DemandTabDataBase(self.network)

        # fill MP2X DataBase
        self.fill_DemandTabDataBase_MP2X(full_MP2X_Dict= full_mp2x_lines,
                                            half_MP2X_Dict= half_mp2x_lines,
                                            netobj= self.network)

        """ # NOTE: start debugging
        print(f"Panels part of DemandTabDataBase: {DemandTabDataBase['Panels']}")
        # NOTE: end of debugging """

        # changing failed nodes icon ( change to notified version )
        self.failed_grooming_nodes()
        self.Failed_Nodes_flag = True

        self.Grooming_pushbutton.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"    font: 75 10pt \"Bahnschrift Condensed\";\n"
"    \n"
"    border: 2px solid #8f8f91; min-width: 80px;\n"
"    border-color: #EB8686; \n"
"    border-radius: 25px;\n"
"    background-color: green; \n"
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

    def clean_database_for_grooming(self, netobj):

        DemandTabDataBase["Source_Destination"].clear()
        DemandTabDataBase["Services"].clear()
        DemandTabDataBase["Services_static"].clear()
        DemandTabDataBase["Panels"].clear()
        DemandTabDataBase["GroomOut10"].clear()
        DemandTabDataBase["Lightpathes"].clear()

    
    def fill_basic_demandtabdatabase(self, netobj):

        SourceList = []
        DestinationList = []
        for DemandId, value in netobj.TrafficMatrix.DemandDict.items():

            Source = self.IdNodeMap[value.Source]
            Destination = self.IdNodeMap[value.Destination]

            DemandTabDataBase["Panels"][Source] = {}
            DemandTabDataBase["Panels"][Destination] = {}

            DemandTabDataBase["GroomOut10"][(Source, Destination)] = {}
            DemandTabDataBase["GroomOut10"][(Destination, Source)] = {}

            DemandTabDataBase["Lightpathes"][(Source, Destination)] = {}
            DemandTabDataBase["Lightpathes"][(Destination, Source)] = {}

            DemandTabDataBase["Shelf_Count"][Source] = 1
            DemandTabDataBase["Shelf_Count"][Destination] = 1

            if not ((Source, Destination) in GroomingTabDataBase["LightPathes"]):
                GroomingTabDataBase["LightPathes"][(Source, Destination)] = {}
            
            if not ((Destination, Source) in GroomingTabDataBase["LightPathes"]):
                GroomingTabDataBase["LightPathes"][(Destination, Source)] = {}

            SourceList.append(Source)
            DestinationList.append(Destination)
        
        for Source in SourceList:
            if ( Source in DemandTabDataBase["Source_Destination"] ) == False:
                DemandTabDataBase["Source_Destination"][Source] = {"Source": Source, "DestinationList": []}
        
        for Destination in DestinationList:
            if ( Destination in DemandTabDataBase["Source_Destination"] ) is False:
                DemandTabDataBase["Source_Destination"][Destination] = {"Source": Destination, "DestinationList": []}

        for i in range(len(SourceList)):
            Destination = DestinationList[i]
            Source = SourceList[i]
            DemandTabDataBase["Source_Destination"][Source]["DestinationList"].append(Destination)
            DemandTabDataBase["Source_Destination"][Destination]["DestinationList"].append(Source)
        
            

    def create_new_demand_services(self, netobj):
        for DemandId, value in netobj.TrafficMatrix.DemandDict.items():
            Source = self.IdNodeMap[value.Source]
            Destination = self.IdNodeMap[value.Destination]

            dynamic_service = {}
            static_service = {}

            dynamic_service_d = {}
            static_service_d = {}

            for ServiceId, object in value.ServiceDict.items():
                LightPathId = object.LightPathId
                Type = object.Type
                OriginalSource = object.OriginalSource
                OriginalDestination = object.OriginalDestination
                
                if LightPathId is not None:
                    dynamic_service[(DemandId, ServiceId)] = 1
                    dynamic_service_d[(DemandId, ServiceId)] = 1
                else:
                    dynamic_service[(DemandId, ServiceId)] = 0
                    dynamic_service_d[(DemandId, ServiceId)] = 0
            

                setattr(self, "Service_item_" + str(Data["Service_item_num"]), QListWidgetItem(Type, self.Demand_ServiceList))
                item = getattr(self, "Service_item_" + str(Data["Service_item_num"]))
                Data["Service_item_num"] += 1
                item.setTextAlignment(Qt.AlignCenter)
                item.setToolTip(f"Type: {Type}\nSource: {Source}\nDestination: {Destination}")
                data = {"DemandId": DemandId, "ServiceId": ServiceId}

                if OriginalSource is not None:
                    data["OriginalSource"] = self.IdNodeMap[OriginalSource]
                    data["OriginalDestination"] = self.IdNodeMap[OriginalDestination]

                    item.setToolTip(f"Type: {Type}\nSource: {Source}\nDestination: {Destination}\nOriginal Source: {data['OriginalSource']}\nOriginal Destination: {data['OriginalDestination']}")

                item.setData(Qt.UserRole, data)

                if LightPathId is None:
                    item.setBackground(QBrush(QColor('#6088C6'), Qt.SolidPattern))
                else:
                    item.setBackground(QBrush(Qt.white, Qt.SolidPattern))

                static_service[(DemandId, ServiceId)] = item


                # ** Dual ** 
                setattr(self, "Service_item_" + str(Data["Service_item_num"]), QListWidgetItem(Type, self.Demand_ServiceList))
                item = getattr(self, "Service_item_" + str(Data["Service_item_num"]))
                Data["Service_item_num"] += 1
                item.setTextAlignment(Qt.AlignCenter)
                item.setToolTip(f"Type: {Type}\nSource: {Destination}\nDestination: {Source}")
                data = {"DemandId": DemandId, "ServiceId": ServiceId}

                if OriginalSource is not None:
                    data["OriginalSource"] = self.IdNodeMap[OriginalSource]
                    data["OriginalDestination"] = self.IdNodeMap[OriginalDestination]

                    item.setToolTip(f"Type: {Type}\nSource: {Destination}\nDestination: {Source}\nOriginal Source: {data['OriginalDestination']}\nOriginal Destination: {data['OriginalSource']}")

                item.setData(Qt.UserRole, data)

                if LightPathId is None:
                    item.setBackground(QBrush(QColor('#6088C6'), Qt.SolidPattern))
                else:
                    item.setBackground(QBrush(Qt.white, Qt.SolidPattern))

                static_service_d[(DemandId, ServiceId)] = item
            
            DemandTabDataBase["Services"][(Source, Destination)] = copy.copy(dynamic_service)
            DemandTabDataBase["Services"][(Destination, Source)] = copy.copy(dynamic_service_d)

            if not ( Source in DemandTabDataBase["Services_static"]): 
                DemandTabDataBase["Services_static"][Source] = copy.copy(static_service)
            else:
                DemandTabDataBase["Services_static"][Source].update(copy.copy(static_service))

            if not ( Destination in DemandTabDataBase["Services_static"]):
                DemandTabDataBase["Services_static"][Destination] = copy.copy(static_service_d)
            else:
                DemandTabDataBase["Services_static"][Destination].update(copy.copy(static_service_d))


    def find_grooming_failed_sources(self):

        for S_D_Pair, value in DemandTabDataBase["Services"].items():
            for state in value.values():
                if state == 0:

                    Source = S_D_Pair[0]
                    Destination = S_D_Pair[1]

                    if not (Source in DemandTabDataBase["Failed_Demands"]):
                        DemandTabDataBase["Failed_Demands"][Source] = [Destination]

                    elif not (Destination in DemandTabDataBase["Failed_Demands"][Source]):
                        DemandTabDataBase["Failed_Demands"][Source].append(Destination)

                    break
                

                    
        
        return list(DemandTabDataBase["Failed_Demands"].keys())

    def notify_sources(self):
        pass


    def open_RWA_window_fun(self):
        
        x = 0
        for S_D_Pair in DemandTabDataBase["Services"].values():
            for state in S_D_Pair.values():
                if state == 0:
                    x = 1
                    break
            
            if x == 1:
                break
        
        # TODO: show appropriate message to user
        if x == 0:
            self.RWA_window_dialog = QtWidgets.QDialog()
            self.RWA_window = Ui_RWA_Window()
            self.RWA_window.setupUi(self.RWA_window_dialog)
            self.RWA_window_dialog.show()


    def RWA_procedure(self, merge, alpha, iterations, margin, processors, k, MaxNW, GroupSize,
                            History, Algorithm):

        self.insert_params_into_obj(merge, alpha, iterations, margin, processors, k, MaxNW, GroupSize, History, Algorithm)
        RWA_Start_Time = time.time()
        self.RWA_button_fun()
        RWA_Runtime = time.time() - RWA_Start_Time
        self.fill_GroomingTabDataBase(self.decoded_network, RWA_Runtime)
        self.RWA_Success = True

        # Enabling View GroupBox
        self.ViewGroupbox.setEnabled(True)

        # disabling Clustering GroupBox except ShowSubNodes
        self.SetGatewayNode_button.setEnabled(False)
        self.SelectSubNode_button.setEnabled(False)
        self.OK_button.setEnabled(False)
        self.Cancel_button.setEnabled(False)
        self.cluster_type_combobox.setEnabled(False)
        self.ClusterColor_combobox.setEnabled(False)

        self.RWA_pushbutton.setStyleSheet("QPushButton {\n"
"    \n"
"    \n"
"    font: 75 10pt \"Bahnschrift Condensed\";\n"
"    \n"
"    border: 2px solid #8f8f91; min-width: 80px;\n"
"    border-color: #EB8686; \n"
"    border-radius: 25px;\n"
"    background-color: green; \n"
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



    def insert_params_into_obj(self, merge, alpha, iterations, margin, processors, k, MaxNW, GroupSize, History, Algorithm):
        self.network.put_params(merge= merge,
                                alpha= alpha,
                                iterations= iterations,
                                margin= margin,
                                processors= processors,
                                k= k,
                                MaxNW= MaxNW,
                                GroupSize= GroupSize,
                                History= History,
                                Algorithm= Algorithm)
        
        self.MaxNW = MaxNW


        

    def RWA_button_fun(self):

        for lightpath in self.network.LightPathDict.values():
            print(lightpath.__dict__)

        # socketio event handling

        sio = socketio.Client()

        @sio.event
        def connect():
            print('connection established')
            #sio.emit('my_message', {'response': 'Connection on client side'})

        @sio.on('rwa_toClient_message')
        def message(data):
            print('Server log (RWA): ', data)
            sio.emit('rwa_message:', "log received on client")
            
        @sio.on('grooming_toClient_message')
        def message(data):
            print('Server log (Grooming): ', data)
            sio.emit('grooming_message:', "log received on client")    

        @sio.event
        def disconnect():
            print('disconnected from the server.')

        def convert_to_dict(obj):
            """
            A function takes in a custom object and returns a dictionary representation of the object.
            This dict representation includes meta data such as the object's module and class names.
            """
            # print(type(obj))
            #  Populate the dictionary with object meta data 
            if isinstance(obj, numpy.int64):
                obj_dict = int(obj)
                return obj_dict
            else:
                obj_dict = {
                    "__class__": obj.__class__.__name__,
                    "__module__": obj.__module__
                }
                #  Populate the dictionary with object properties
                obj_dict.update(obj.__dict__)
                return obj_dict
        net = copy.copy(self.network)

        use_sockets = False

        # Convert keys to String
        tuple_keys = list(net.PhysicalTopology.LinkDict.keys())
        for key in tuple_keys:
            net.PhysicalTopology.LinkDict[str(key)] = net.PhysicalTopology.LinkDict.pop(key)

        ##############################################
        # Convert the Network object to JSON message
        # data = json.dumps(net.PhysicalTopology.ClusterDict[1],default=convert_to_dict,indent=4, sort_keys=True)
        # print(data)
        # assert False
        data = json.dumps(net,default=convert_to_dict,indent=4, sort_keys=True)

        # This line tests whether the JSON encoded common object is reconstructable!
        decoded_n = Network.from_json(json.loads(data)) 
        assert(isinstance(decoded_n, Network))
        # print(list(decoded_n.LightPathDict.keys()))
        # data = json.dumps(decoded_n,default=convert_to_dict,indent=4, sort_keys=True)
        # assert False
        # Establishing a socket.io connection for logging purposes
        if use_sockets:
            sio.connect('http://localhost:5000')

        ##Run the grooming function on the server
        # print('####################################################')
        # print('Transmitting data to server for client side grooming.')
        # res = requests.get('http://localhost:5000/grooming/', json = data)

        # if res.ok:
            # print(res.json())
            # print('Grooming finished successfully!')
            
        print('####################################################')
        print('Transmitting data to server to solve RWA planning.') 
        # Run the RWA planner on the server

        try:
            res = requests.get('http://localhost:5000/RWA/', json = data)
            connected_to_server = True
        except:
            warnings.warn("Something goes wrong!\nThe application can not connect to the server.")
            connected_to_server = False
        if connected_to_server:
            if res.ok:
                # print('####################################################')
                # print(json.dumps(res.json()))
                decoded_network = Network.from_json(json.loads(json.dumps(res.json())))
                # data = json.dumps(decoded_network.LightPathDict,default=convert_to_dict,indent=4, sort_keys=True)
                # print(data) #PhysicalTopology.LinkDict ResultObj
                # Converting keys to original version ( Server Side )
                str_keys = list(decoded_network.PhysicalTopology.LinkDict.keys())
                for key in str_keys:
                    n_key = ''.join(key.split())
                    Lkey = n_key[1:-1].split(',')
                    ActualKey =( int(Lkey[1]) , int(Lkey[-2]) )
                    decoded_network.PhysicalTopology.LinkDict[ActualKey] = decoded_network.PhysicalTopology.LinkDict.pop(key)
                
                decoded_network.LightPathDict = {int(key): value for key, value in decoded_network.LightPathDict.items()}
            if use_sockets:  
                sio.disconnect()
                sio.sleep(0)
            # sio.wait()
            print('RWA finished and data received in client') 
            # try:
            #     print('Sample WaveLength output', decoded_network.LightPathDict[0].WaveLength)
            #     print('Sample Path output', decoded_network.LightPathDict[0].WorkingPath)
                
            # except:
            #     pass
        self.decoded_network = decoded_network


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    # NOTE: added
    Data["ui"] = ui
    MainWindow.show()
    sys.exit(app.exec_())

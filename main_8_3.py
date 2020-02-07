from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QApplication,QTableWidget,QTableWidgetItem,QFileDialog,QMdiSubWindow,QWidget,QLabel,QAbstractItemView,QListWidgetItem,QMenu,QFontComboBox
from PySide2.QtCore import SIGNAL,QObject,Slot
from PySide2.QtGui import QPixmap
import pickle
import sys, os
import pandas as pd
from PySide2 import QtWebEngineWidgets
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
from newcheck import  Ui_checking
from Common_Object_def import Network
from math import ceil
import requests
import json
import socketio  
import time
import copy , math, warnings

from add_node import Ui_add_node_window

from data import *
from Node_View_Data import Panel_Data


from BLANK_panel.BLANK_panel import BLANK_panel
from SC_panel_final.SC_panel import SC_panel
from BAF3_panel.BAF3_panel import BAF3_panel
from LAF3_panel.LAF3_panel import LAF3_panel
from PAF3_panel.PAF3_panel import PAF3_panel
from MP2X_panel.MP2X_panel import MP2X_panel
#from MP2D_panel.MP2D_panel import MP2D_panel
from MP2D_panel.MP2D_panel_L import MP2D_panel_L
from MP2D_panel.MP2D_panel_R import MP2D_panel_R
from TP2X_panel.TP2X_panel import TP2X_panel

from TP1H_Grooming.TP1H_L_Grooming import TP1H_L_Grooming
from TP1H_Grooming.TP1H_R_Grooming import TP1H_R_Grooming
from MP1H_Grooming.MP1H_L_Grooming import MP1H_L_Grooming
from MP1H_Grooming.MP1H_R_Grooming import MP1H_R_Grooming

from BLANK_Demand.BLANK_Demand import BLANK_Demand
from MP2X_Demand.MP2X_L_Demand import MP2X_L_Demand
from MP2X_Demand.MP2X_R_Demand import MP2X_R_Demand
from MP1H_Demand.MP1H_L_Demand import MP1H_L_Demand
from MP1H_Demand.MP1H_R_Demand import MP1H_R_Demand
from TP1H_Demand.TP1H_L_Demand import TP1H_L_Demand
from TP1H_Demand.TP1H_R_Demand import TP1H_R_Demand

#from mapwidget import MapWidget
from mapwidget import MapWidget

from  matplotlib.backends.backend_qt5agg  import  FigureCanvas
from  matplotlib.figure  import  Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
#from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import networkx as nx
from numpy import cos, sin
import numpy


class Backend_map(QObject):

    @Slot(str)
    def Create_DataBase(self,text):
        print("last GateWay: ",text)
        self.LastGateWay = text

        # creating grouping database
        print("we are grouping")
        Data["Grouping"][text] = {}
        Data["Grouping"][text]["Color"] = ui.lastgroup_color
        Data["Grouping"][text]["Type"] = ui.lastgroup_type
        Data["Grouping"][text]["SubNodes"] = {}


    
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
        Data["Grouping"][self.LastGateWay]["SubNodes"][node] = {}

    @Slot()
    def TurnSubNodeSelect_off(self):
        ui.SelectSubNode_button_fun()


    @Slot(str)
    def change_tab_to4(self,degreename):
        print(">>>>>>",degreename)
        if Data["Stage_flag"] == "Grooming":
            Data["TabWidget"].setCurrentIndex(3)
            Data["SelectNodeCombo"].setCurrentText(degreename.strip())
            # TODO: check this function and delete it
            #ui.SelectNode_combo_change()

        if Data["Stage_flag"] == "Demand":
            Data["TabWidget"].setCurrentIndex(4)
            Data["Demand_Source_combo"].setCurrentText(degreename.strip())

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")

        #TODO: commented
        #MainWindow.resize(1219, 841)

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
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.TopologyTab = QtWidgets.QWidget()
        self.TopologyTab.setObjectName("TopologyTab")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.TopologyTab)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.OpenTopology_button = QtWidgets.QPushButton(self.TopologyTab)
        self.OpenTopology_button.setMaximumSize(QtCore.QSize(81, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.OpenTopology_button.setFont(font)
        self.OpenTopology_button.setStyleSheet("QPushButton {\n"
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
        self.OpenTopology_button.setObjectName("OpenTopology_button")
        self.horizontalLayout_2.addWidget(self.OpenTopology_button)
        self.SaveTopology_button = QtWidgets.QPushButton(self.TopologyTab)
        self.SaveTopology_button.setMaximumSize(QtCore.QSize(81, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.SaveTopology_button.setFont(font)
        self.SaveTopology_button.setStyleSheet("QPushButton {\n"
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
        self.SaveTopology_button.setObjectName("SaveTopology_button")
        self.horizontalLayout_2.addWidget(self.SaveTopology_button)
        self.add_node_button = QtWidgets.QPushButton(self.TopologyTab)
        self.add_node_button.setMaximumSize(QtCore.QSize(81, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.add_node_button.setFont(font)
        self.add_node_button.setStyleSheet("QPushButton {\n"
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
        self.add_node_button.setObjectName("add_node_button")
        self.horizontalLayout_2.addWidget(self.add_node_button)
        self.OpenLinks_pushbutton = QtWidgets.QPushButton(self.TopologyTab)
        self.OpenLinks_pushbutton.setMinimumSize(QtCore.QSize(84, 30))
        self.OpenLinks_pushbutton.setMaximumSize(QtCore.QSize(81, 50))
        font = QtGui.QFont()
        font.setFamily("IRANSans")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.OpenLinks_pushbutton.setFont(font)
        self.OpenLinks_pushbutton.setStyleSheet("QPushButton {\n"
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
        self.OpenLinks_pushbutton.setObjectName("OpenLinks_pushbutton")
        self.horizontalLayout_2.addWidget(self.OpenLinks_pushbutton)
        self.pushButton_5 = QtWidgets.QPushButton(self.TopologyTab)
        self.pushButton_5.setMinimumSize(QtCore.QSize(84, 30))
        self.pushButton_5.setMaximumSize(QtCore.QSize(81, 50))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    min-width: 80px;\n"
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
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_7 = QtWidgets.QPushButton(self.TopologyTab)
        self.pushButton_7.setMinimumSize(QtCore.QSize(84, 28))
        self.pushButton_7.setMaximumSize(QtCore.QSize(81, 50))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    min-width: 80px;\n"
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
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_2.addWidget(self.pushButton_7)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.TopologyTab)
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    min-width: 80px;\n"
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
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_3.addWidget(self.pushButton_6, 0, 1, 1, 1)

        #TODO: edited
        self.webengine = QtWebEngineWidgets.QWebEngineView()
        self.webengine.setObjectName("webengine")
        self.gridLayout_3.addWidget(self.webengine, 1, 0, 1, 1)

        self.T_groupbox = QtWidgets.QGroupBox(self.TopologyTab)
        self.T_groupbox.setEnabled(True)
        self.T_groupbox.setMaximumSize(QtCore.QSize(300, 16777215))
        self.T_groupbox.setStyleSheet("QGroupBox {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #E0E0E0, stop: 1 #FFFFFF);\n"
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
        self.Planning_groupbox = QtWidgets.QGroupBox(self.T_groupbox)
        self.Planning_groupbox.setObjectName("Planning_groupbox")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.Planning_groupbox)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.PanelThreshold_pushbutton = QtWidgets.QPushButton(self.Planning_groupbox)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.PanelThreshold_pushbutton.setFont(font)
        self.PanelThreshold_pushbutton.setStyleSheet("background-color: rgb(255, 129, 131);\n"
"border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: dark-orange;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"")
        self.PanelThreshold_pushbutton.setObjectName("PanelThreshold_pushbutton")
        self.verticalLayout_2.addWidget(self.PanelThreshold_pushbutton)
        self.Grooming_pushbutton = QtWidgets.QPushButton(self.Planning_groupbox)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Grooming_pushbutton.setFont(font)
        self.Grooming_pushbutton.setStyleSheet("\n"
"background-color: rgb(255, 85, 88);\n"
"border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: dark-orange;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;")
        self.Grooming_pushbutton.setCheckable(False)
        self.Grooming_pushbutton.setObjectName("Grooming_pushbutton")
        self.verticalLayout_2.addWidget(self.Grooming_pushbutton)
        self.RWA_pushbutton = QtWidgets.QPushButton(self.Planning_groupbox)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.RWA_pushbutton.setFont(font)
        self.RWA_pushbutton.setStyleSheet("\n"
"background-color: rgb(255, 44, 47);\n"
"border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: dark-orange;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;")
        self.RWA_pushbutton.setObjectName("RWA_pushbutton")
        self.verticalLayout_2.addWidget(self.RWA_pushbutton)
        self.FinalPlan_pushbutton = QtWidgets.QPushButton(self.Planning_groupbox)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.FinalPlan_pushbutton.setFont(font)
        self.FinalPlan_pushbutton.setStyleSheet("\n"
"background-color: rgb(255, 0, 4);\n"
"border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: dark-orange;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;")
        self.FinalPlan_pushbutton.setObjectName("FinalPlan_pushbutton")
        self.verticalLayout_2.addWidget(self.FinalPlan_pushbutton)
        self.gridLayout_11.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.gridLayout_14.addWidget(self.Planning_groupbox, 1, 0, 1, 1)
        self.ViewGroupbox = QtWidgets.QGroupBox(self.T_groupbox)
        self.ViewGroupbox.setObjectName("ViewGroupbox")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.ViewGroupbox)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.NormalMode_checkbox = QtWidgets.QCheckBox(self.ViewGroupbox)
        font = QtGui.QFont()
        font.setFamily("IRANSans")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.NormalMode_checkbox.setFont(font)
        self.NormalMode_checkbox.setStyleSheet("")
        self.NormalMode_checkbox.setObjectName("NormalMode_checkbox")
        self.verticalLayout_3.addWidget(self.NormalMode_checkbox)
        self.Working_checkbox = QtWidgets.QCheckBox(self.ViewGroupbox)
        font = QtGui.QFont()
        font.setFamily("IRANSans")
        font.setBold(True)
        font.setWeight(75)
        self.Working_checkbox.setFont(font)
        self.Working_checkbox.setObjectName("Working_checkbox")
        self.verticalLayout_3.addWidget(self.Working_checkbox)
        self.Protection_checkbox = QtWidgets.QCheckBox(self.ViewGroupbox)
        font = QtGui.QFont()
        font.setFamily("IRANSans")
        font.setBold(True)
        font.setWeight(75)
        self.Protection_checkbox.setFont(font)
        self.Protection_checkbox.setObjectName("Protection_checkbox")
        self.verticalLayout_3.addWidget(self.Protection_checkbox)
        self.Restoration_checkbox = QtWidgets.QCheckBox(self.ViewGroupbox)
        font = QtGui.QFont()
        font.setFamily("IRANSans")
        font.setBold(True)
        font.setWeight(75)
        self.Restoration_checkbox.setFont(font)
        self.Restoration_checkbox.setObjectName("Restoration_checkbox")
        self.verticalLayout_3.addWidget(self.Restoration_checkbox)
        self.gridLayout_18.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.gridLayout_14.addWidget(self.ViewGroupbox, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_14.addItem(spacerItem1, 3, 0, 1, 1)
        self.Grouping_groupbox = QtWidgets.QGroupBox(self.T_groupbox)
        self.Grouping_groupbox.setObjectName("Grouping_groupbox")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.Grouping_groupbox)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.gridLayout_16 = QtWidgets.QGridLayout()
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.SetGatewayNode_button = QtWidgets.QPushButton(self.Grouping_groupbox)
        self.SetGatewayNode_button.setMinimumSize(QtCore.QSize(84, 30))
        self.SetGatewayNode_button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.SetGatewayNode_button.setFont(font)
        self.SetGatewayNode_button.setStyleSheet("QPushButton {\n"
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
        self.SetGatewayNode_button.setObjectName("SetGatewayNode_button")
        self.gridLayout_16.addWidget(self.SetGatewayNode_button, 0, 0, 1, 3)
        self.GroupName = QtWidgets.QLabel(self.Grouping_groupbox)
        self.GroupName.setStyleSheet(" QLabel {\n"
"    border: 2px solid green;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"    \n"
"}")
        self.GroupName.setObjectName("GroupName")
        self.gridLayout_16.addWidget(self.GroupName, 1, 0, 1, 1)
        self.GroupName_edit = QtWidgets.QLineEdit(self.Grouping_groupbox)
        self.GroupName_edit.setStyleSheet("QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.GroupName_edit.setObjectName("GroupName_edit")
        self.gridLayout_16.addWidget(self.GroupName_edit, 1, 1, 1, 2)
        self.GroupID = QtWidgets.QLabel(self.Grouping_groupbox)
        self.GroupID.setStyleSheet(" QLabel {\n"
"    border: 2px solid green;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"    \n"
"}")
        self.GroupID.setObjectName("GroupID")
        self.gridLayout_16.addWidget(self.GroupID, 2, 0, 1, 1)
        self.cluster_type_combobox = QtWidgets.QFontComboBox(self.Grouping_groupbox)
        self.cluster_type_combobox.setMaximumSize(QtCore.QSize(126, 22))
        self.cluster_type_combobox.setStyleSheet("QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(/usr/share/icons/crystalsvg/16x16/actions/1downarrow.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}")
        self.cluster_type_combobox.setFrame(True)
        self.cluster_type_combobox.setObjectName("cluster_type_combobox")
        self.gridLayout_16.addWidget(self.cluster_type_combobox, 2, 1, 1, 2)
        self.GroupColor = QtWidgets.QLabel(self.Grouping_groupbox)
        self.GroupColor.setStyleSheet(" QLabel {\n"
"    border: 2px solid green;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"    \n"
"}")
        self.GroupColor.setObjectName("GroupColor")
        self.gridLayout_16.addWidget(self.GroupColor, 3, 0, 1, 1)
        self.ClusterColor_combobox = QtWidgets.QFontComboBox(self.Grouping_groupbox)
        self.ClusterColor_combobox.setMaximumSize(QtCore.QSize(126, 22))
        self.ClusterColor_combobox.setStyleSheet("QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(/usr/share/icons/crystalsvg/16x16/actions/1downarrow.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}")
        self.ClusterColor_combobox.setObjectName("ClusterColor_combobox")
        self.gridLayout_16.addWidget(self.ClusterColor_combobox, 3, 1, 1, 2)
        self.SelectSubNode_button = QtWidgets.QPushButton(self.Grouping_groupbox)
        self.SelectSubNode_button.setMinimumSize(QtCore.QSize(84, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.SelectSubNode_button.setFont(font)
        self.SelectSubNode_button.setStyleSheet("QPushButton {\n"
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
        self.SelectSubNode_button.setObjectName("SelectSubNode_button")
        self.gridLayout_16.addWidget(self.SelectSubNode_button, 4, 0, 1, 1)
        self.SelectSubNode = QtWidgets.QLabel(self.Grouping_groupbox)
        palette = QtGui.QPalette()
        self.SelectSubNode.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.SelectSubNode.setFont(font)
        self.SelectSubNode.setStyleSheet(" QLabel {\n"
"    border: 2px solid green;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"    \n"
"}")
        self.SelectSubNode.setAlignment(QtCore.Qt.AlignCenter)
        self.SelectSubNode.setObjectName("SelectSubNode")
        self.gridLayout_16.addWidget(self.SelectSubNode, 4, 2, 1, 1)
        self.Cancel_button = QtWidgets.QPushButton(self.Grouping_groupbox)
        self.Cancel_button.setMinimumSize(QtCore.QSize(84, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Cancel_button.setFont(font)
        self.Cancel_button.setStyleSheet("QPushButton {\n"
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
        self.Cancel_button.setObjectName("Cancel_button")
        self.gridLayout_16.addWidget(self.Cancel_button, 5, 0, 1, 1)
        self.OK_button = QtWidgets.QPushButton(self.Grouping_groupbox)
        self.OK_button.setMinimumSize(QtCore.QSize(84, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.OK_button.setFont(font)
        self.OK_button.setStyleSheet("QPushButton {\n"
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
        self.OK_button.setObjectName("OK_button")
        self.gridLayout_16.addWidget(self.OK_button, 5, 2, 1, 1)
        self.ShowSubNodes = QtWidgets.QCheckBox(self.Grouping_groupbox)
        self.ShowSubNodes.setStyleSheet("")
        self.ShowSubNodes.setObjectName("ShowSubNodes")
        self.gridLayout_16.addWidget(self.ShowSubNodes, 6, 0, 1, 2)
        self.gridLayout_17.addLayout(self.gridLayout_16, 0, 0, 1, 1)
        self.gridLayout_14.addWidget(self.Grouping_groupbox, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.T_groupbox, 1, 1, 1, 1)
        self.gridLayout_19.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.TopologyTab, "")
        self.TrafficMatrixTab = QtWidgets.QWidget()
        self.TrafficMatrixTab.setObjectName("TrafficMatrixTab")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.TrafficMatrixTab)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.Traffic_matrix = QtWidgets.QTableWidget(self.TrafficMatrixTab)
        self.Traffic_matrix.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Traffic_matrix.setStyleSheet("QTableWidget {\n"
"    selection-background-color: qlineargradient(x1: 0, y1: 0, x2: 0.5, y2: 0.5,\n"
"                                stop: 0 #FF92BB, stop: 1 white);\n"
"}\n"
"QTableWidget QTableCornerButton::section {\n"
"    background: red;\n"
"    border: 2px outset red;\n"
"}")
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
        self.gridLayout_6.addWidget(self.Traffic_matrix, 0, 1, 1, 1)
        self.General_TM = QtWidgets.QTableWidget(self.TrafficMatrixTab)
        self.General_TM.setStyleSheet("QTableWidget {\n"
"    selection-background-color: qlineargradient(x1: 0, y1: 0, x2: 0.5, y2: 0.5,\n"
"                                stop: 0 #FF92BB, stop: 1 white);\n"
"}\n"
"QTableWidget QTableCornerButton::section {\n"
"    background: red;\n"
"    border: 2px outset red;\n"
"}")
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
        self.gridLayout_6.addWidget(self.General_TM, 0, 0, 1, 1)
        self.TM_groupbox = QtWidgets.QGroupBox(self.TrafficMatrixTab)
        self.TM_groupbox.setMouseTracking(False)
        self.TM_groupbox.setAccessibleDescription("")
        self.TM_groupbox.setFlat(True)
        self.TM_groupbox.setCheckable(True)
        self.TM_groupbox.setChecked(True)
        self.TM_groupbox.setObjectName("TM_groupbox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.TM_groupbox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_7 = QtWidgets.QLabel(self.TM_groupbox)
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 0, 0, 1, 1)
        self.List_tab = QtWidgets.QTabWidget(self.TM_groupbox)
        self.List_tab.setObjectName("List_tab")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(self.tab_4)
        self.listWidget.setStyleSheet("QListWidget {\n"
"    alternate-background-color: yellow;\n"
"    border: 5px double;\n"
"    border-color: blue;\n"
"    border-radius: 10px;\n"
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
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.verticalLayout.addWidget(self.listWidget)
        self.List_tab.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.List_tab.addTab(self.tab_5, "")
        self.gridLayout_5.addWidget(self.List_tab, 1, 0, 1, 2)
        self.SaveTM_button = QtWidgets.QPushButton(self.TM_groupbox)
        self.SaveTM_button.setMinimumSize(QtCore.QSize(84, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.SaveTM_button.setFont(font)
        self.SaveTM_button.setToolTip("")
        self.SaveTM_button.setStyleSheet("QPushButton {\n"
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
        self.SaveTM_button.setObjectName("SaveTM_button")
        self.gridLayout_5.addWidget(self.SaveTM_button, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.TM_groupbox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 2, 1, 1, 1)
        self.LoadTM_button = QtWidgets.QPushButton(self.TM_groupbox)
        self.LoadTM_button.setMinimumSize(QtCore.QSize(84, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.LoadTM_button.setFont(font)
        self.LoadTM_button.setStyleSheet("QPushButton {\n"
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
        self.LoadTM_button.setObjectName("LoadTM_button")
        self.gridLayout_5.addWidget(self.LoadTM_button, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.TM_groupbox)
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 3, 1, 1, 1)
        self.filter = QtWidgets.QPushButton(self.TM_groupbox)
        self.filter.setMinimumSize(QtCore.QSize(84, 30))
        self.filter.setStyleSheet("QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    min-width: 80px;\n"
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
        self.filter.setObjectName("filter")
        self.gridLayout_5.addWidget(self.filter, 4, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.TM_groupbox)
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 4, 1, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.TM_groupbox)
        self.pushButton_10.setMinimumSize(QtCore.QSize(84, 30))
        self.pushButton_10.setStyleSheet("QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    min-width: 80px;\n"
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
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_5.addWidget(self.pushButton_10, 5, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.TM_groupbox)
        self.label_6.setObjectName("label_6")
        self.gridLayout_5.addWidget(self.label_6, 5, 1, 1, 1)
        self.SaveChanges_button = QtWidgets.QPushButton(self.TM_groupbox)
        self.SaveChanges_button.setMinimumSize(QtCore.QSize(84, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.SaveChanges_button.setFont(font)
        self.SaveChanges_button.setStyleSheet("QPushButton {\n"
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
        self.SaveChanges_button.setObjectName("SaveChanges_button")
        self.gridLayout_5.addWidget(self.SaveChanges_button, 6, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.TM_groupbox)
        self.label_4.setObjectName("label_4")
        self.gridLayout_5.addWidget(self.label_4, 6, 1, 1, 1)
        self.insert_link_button = QtWidgets.QPushButton(self.TM_groupbox)
        self.insert_link_button.setMinimumSize(QtCore.QSize(84, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.insert_link_button.setFont(font)
        self.insert_link_button.setStyleSheet("QPushButton {\n"
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
        self.insert_link_button.setObjectName("insert_link_button")
        self.gridLayout_5.addWidget(self.insert_link_button, 7, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.TM_groupbox)
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 7, 1, 1, 1)
        self.gridLayout_6.addWidget(self.TM_groupbox, 0, 2, 1, 1)
        self.tabWidget.addTab(self.TrafficMatrixTab, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.tabWidget.addTab(self.tab_9, "")
        self.NodeViewTab = QtWidgets.QWidget()
        self.NodeViewTab.setObjectName("NodeViewTab")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.NodeViewTab)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.RackTab = QtWidgets.QTabWidget(self.NodeViewTab)
        self.RackTab.setStyleSheet("")
        self.RackTab.setTabPosition(QtWidgets.QTabWidget.North)
        self.RackTab.setObjectName("RackTab")
        self.Rack1 = QtWidgets.QWidget()
        self.Rack1.setObjectName("Rack1")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.Rack1)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.ShelfTab = QtWidgets.QTabWidget(self.Rack1)
        self.ShelfTab.setMinimumSize(QtCore.QSize(1530, 810))
        self.ShelfTab.setTabPosition(QtWidgets.QTabWidget.West)
        self.ShelfTab.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.ShelfTab.setIconSize(QtCore.QSize(20, 20))
        self.ShelfTab.setElideMode(QtCore.Qt.ElideNone)
        self.ShelfTab.setObjectName("ShelfTab")
        self.Shelf1 = QtWidgets.QWidget()
        self.Shelf1.setObjectName("Shelf1")
        self.Shelf1_grid = QtWidgets.QGridLayout(self.Shelf1)
        self.Shelf1_grid.setObjectName("Shelf1_grid")
        self.mdi_11 = QtWidgets.QMdiArea(self.Shelf1)
        self.mdi_11.setMinimumSize(QtCore.QSize(1530, 810))
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.mdi_11.setBackground(brush)
        self.mdi_11.setViewMode(QtWidgets.QMdiArea.SubWindowView)
        self.mdi_11.setObjectName("mdi_11")
        self.Shelf1_grid.addWidget(self.mdi_11, 0, 0, 1, 1)
        self.ShelfTab.addTab(self.Shelf1, "")
        self.Shelf2 = QtWidgets.QWidget()
        self.Shelf2.setObjectName("Shelf2")
        self.Shelf2_grid = QtWidgets.QGridLayout(self.Shelf2)
        self.Shelf2_grid.setObjectName("Shelf2_grid")
        self.mdi_12 = QtWidgets.QMdiArea(self.Shelf2)
        self.mdi_12.setMinimumSize(QtCore.QSize(1530, 810))
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.mdi_12.setBackground(brush)
        self.mdi_12.setObjectName("mdi_12")
        self.Shelf2_grid.addWidget(self.mdi_12, 0, 0, 1, 1)
        self.ShelfTab.addTab(self.Shelf2, "")
        self.Shelf3 = QtWidgets.QWidget()
        self.Shelf3.setObjectName("Shelf3")
        self.Shelf3_grid = QtWidgets.QGridLayout(self.Shelf3)
        self.Shelf3_grid.setObjectName("Shelf3_grid")
        self.mdi_13 = QtWidgets.QMdiArea(self.Shelf3)
        self.mdi_13.setMinimumSize(QtCore.QSize(1530, 810))
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.mdi_13.setBackground(brush)
        self.mdi_13.setObjectName("mdi_13")
        self.Shelf3_grid.addWidget(self.mdi_13, 0, 0, 1, 1)
        self.ShelfTab.addTab(self.Shelf3, "")
        self.Shelf4 = QtWidgets.QWidget()
        self.Shelf4.setObjectName("Shelf4")
        self.Shelf4_grid = QtWidgets.QGridLayout(self.Shelf4)
        self.Shelf4_grid.setObjectName("Shelf4_grid")
        self.mdi_14 = QtWidgets.QMdiArea(self.Shelf4)
        self.mdi_14.setMinimumSize(QtCore.QSize(1530, 810))
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.mdi_14.setBackground(brush)
        self.mdi_14.setObjectName("mdi_14")
        self.Shelf4_grid.addWidget(self.mdi_14, 0, 0, 1, 1)
        self.ShelfTab.addTab(self.Shelf4, "")
        self.gridLayout_9.addWidget(self.ShelfTab, 0, 0, 1, 1)
        self.RackTab.addTab(self.Rack1, "")
        self.gridLayout_8.addWidget(self.RackTab, 1, 1, 1, 1)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.ClientList = QtWidgets.QListWidget(self.NodeViewTab)
        self.ClientList.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.ClientList.setStyleSheet("QListWidget {\n"
"    alternate-background-color: yellow;\n"
"    border: 5px double;\n"
"    border-color: blue;\n"
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
        self.ClientList.setDragEnabled(True)
        self.ClientList.setObjectName("ClientList")
        self.gridLayout_7.addWidget(self.ClientList, 1, 0, 1, 2)
        self.ClientLabel = QtWidgets.QLabel(self.NodeViewTab)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ClientLabel.setFont(font)
        self.ClientLabel.setStyleSheet(" QLabel {\n"
"    border: 2px solid green;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"    \n"
"}")
        self.ClientLabel.setObjectName("ClientLabel")
        self.gridLayout_7.addWidget(self.ClientLabel, 0, 0, 1, 2)
        self.PanelLabel = QtWidgets.QLabel(self.NodeViewTab)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.PanelLabel.setFont(font)
        self.PanelLabel.setStyleSheet(" QLabel {\n"
"    border: 2px solid green;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"    \n"
"}")
        self.PanelLabel.setObjectName("PanelLabel")
        self.gridLayout_7.addWidget(self.PanelLabel, 4, 0, 1, 2)
        self.AddShelf_button = QtWidgets.QPushButton(self.NodeViewTab)
        self.AddShelf_button.setObjectName("AddShelf_button")
        self.gridLayout_7.addWidget(self.AddShelf_button, 6, 1, 1, 1)
        self.AddRack_button = QtWidgets.QPushButton(self.NodeViewTab)
        self.AddRack_button.setObjectName("AddRack_button")
        self.gridLayout_7.addWidget(self.AddRack_button, 6, 0, 1, 1)
        self.PanelList = QtWidgets.QListWidget(self.NodeViewTab)
        self.PanelList.setMaximumSize(QtCore.QSize(16777215, 200))
        self.PanelList.setStyleSheet("QListWidget {\n"
"    alternate-background-color: yellow;\n"
"    border: 5px double;\n"
"    border-color: blue;\n"
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
        self.PanelList.setObjectName("PanelList")
        item = QtWidgets.QListWidgetItem()
        self.PanelList.addItem(item)
        self.gridLayout_7.addWidget(self.PanelList, 5, 0, 1, 2)
        self.pushButton_14 = QtWidgets.QPushButton(self.NodeViewTab)
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout_7.addWidget(self.pushButton_14, 7, 1, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.NodeViewTab)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout_7.addWidget(self.pushButton_13, 7, 0, 1, 1)
        self.LineLabel = QtWidgets.QLabel(self.NodeViewTab)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.LineLabel.setFont(font)
        self.LineLabel.setStyleSheet(" QLabel {\n"
"    border: 2px solid green;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"    \n"
"}")
        self.LineLabel.setObjectName("LineLabel")
        self.gridLayout_7.addWidget(self.LineLabel, 2, 0, 1, 2)
        self.LineList = QtWidgets.QListWidget(self.NodeViewTab)
        self.LineList.setEnabled(True)
        self.LineList.setMaximumSize(QtCore.QSize(200000, 140))
        self.LineList.setStyleSheet("QListWidget {\n"
"    alternate-background-color: yellow;\n"
"    border: 5px double;\n"
"    border-color: blue;\n"
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
        self.LineList.setObjectName("LineList")
        self.gridLayout_7.addWidget(self.LineList, 3, 0, 1, 2)
        self.gridLayout_8.addLayout(self.gridLayout_7, 0, 0, 2, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.SelectNode_Label = QtWidgets.QLabel(self.NodeViewTab)
        self.SelectNode_Label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.SelectNode_Label.setFont(font)
        self.SelectNode_Label.setStyleSheet(" QLabel {\n"
"    border: 2px solid green;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"    \n"
"}")
        self.SelectNode_Label.setObjectName("SelectNode_Label")
        self.horizontalLayout.addWidget(self.SelectNode_Label)
        self.SelectNode_combo = QtWidgets.QFontComboBox(self.NodeViewTab)
        self.SelectNode_combo.setMinimumSize(QtCore.QSize(119, 20))
        self.SelectNode_combo.setMaximumSize(QtCore.QSize(16777215, 20))
        self.SelectNode_combo.setStyleSheet("QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(/usr/share/icons/crystalsvg/16x16/actions/1downarrow.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}")
        self.SelectNode_combo.setObjectName("SelectNode_combo")
        self.horizontalLayout.addWidget(self.SelectNode_combo)
        self.gridLayout_8.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.tabWidget.addTab(self.NodeViewTab, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setObjectName("formLayout_4")
        self.SelectNode_Label_13 = QtWidgets.QLabel(self.tab)
        self.SelectNode_Label_13.setMinimumSize(QtCore.QSize(80, 0))
        self.SelectNode_Label_13.setMaximumSize(QtCore.QSize(43, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.SelectNode_Label_13.setFont(font)
        self.SelectNode_Label_13.setStyleSheet(" QLabel {\n"
"    border: 2px solid green;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"    \n"
"}")
        self.SelectNode_Label_13.setObjectName("SelectNode_Label_13")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.SelectNode_Label_13)
        self.Demand_Source_combobox = QtWidgets.QFontComboBox(self.tab)
        self.Demand_Source_combobox.setMinimumSize(QtCore.QSize(119, 30))
        self.Demand_Source_combobox.setMaximumSize(QtCore.QSize(226, 30))
        self.Demand_Source_combobox.setStyleSheet("QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(/usr/share/icons/crystalsvg/16x16/actions/1downarrow.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}")
        self.Demand_Source_combobox.setObjectName("Demand_Source_combobox")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Demand_Source_combobox)
        self.gridLayout_12.addLayout(self.formLayout_4, 0, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setMinimumSize(QtCore.QSize(120, 0))
        self.label_8.setMaximumSize(QtCore.QSize(62, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(" QLabel {\n"
"    border: 2px solid green;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"    \n"
"}")
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.Demand_Destination_combobox = QtWidgets.QFontComboBox(self.tab)
        self.Demand_Destination_combobox.setMinimumSize(QtCore.QSize(119, 30))
        self.Demand_Destination_combobox.setMaximumSize(QtCore.QSize(743, 30))
        self.Demand_Destination_combobox.setStyleSheet("QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(/usr/share/icons/crystalsvg/16x16/actions/1downarrow.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}")
        self.Demand_Destination_combobox.setObjectName("Demand_Destination_combobox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Demand_Destination_combobox)
        self.gridLayout_12.addLayout(self.formLayout, 0, 2, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Demand_ServiceList = QtWidgets.QListWidget(self.tab)
        self.Demand_ServiceList.setMinimumSize(QtCore.QSize(256, 133))
        self.Demand_ServiceList.setMaximumSize(QtCore.QSize(256, 133))
        self.Demand_ServiceList.setStyleSheet("QListWidget {\n"
"    alternate-background-color: yellow;\n"
"    border: 5px double;\n"
"    border-color: blue;\n"
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
        self.Demand_ServiceList.setObjectName("Demand_ServiceList")
        self.gridLayout_2.addWidget(self.Demand_ServiceList, 5, 0, 1, 1)
        self.Demand_PanelList = QtWidgets.QListWidget(self.tab)
        self.Demand_PanelList.setMinimumSize(QtCore.QSize(256, 130))
        self.Demand_PanelList.setMaximumSize(QtCore.QSize(256, 130))
        self.Demand_PanelList.setStyleSheet("QListWidget {\n"
"    alternate-background-color: yellow;\n"
"    border: 5px double;\n"
"    border-color: blue;\n"
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
        self.Demand_PanelList.setObjectName("Demand_PanelList")
        self.gridLayout_2.addWidget(self.Demand_PanelList, 1, 0, 1, 1)
        self.ClientLabel_22 = QtWidgets.QLabel(self.tab)
        self.ClientLabel_22.setMinimumSize(QtCore.QSize(256, 30))
        self.ClientLabel_22.setMaximumSize(QtCore.QSize(256, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ClientLabel_22.setFont(font)
        self.ClientLabel_22.setStyleSheet(" QLabel {\n"
"    border: 2px solid green;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"    \n"
"}")
        self.ClientLabel_22.setObjectName("ClientLabel_22")
        self.gridLayout_2.addWidget(self.ClientLabel_22, 2, 0, 1, 1)
        self.Demand_LineList = QtWidgets.QListWidget(self.tab)
        self.Demand_LineList.setMinimumSize(QtCore.QSize(256, 133))
        self.Demand_LineList.setMaximumSize(QtCore.QSize(256, 133))
        self.Demand_LineList.setStyleSheet("QListWidget {\n"
"    alternate-background-color: yellow;\n"
"    border: 5px double;\n"
"    border-color: blue;\n"
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
        self.Demand_LineList.setObjectName("Demand_LineList")
        self.gridLayout_2.addWidget(self.Demand_LineList, 3, 0, 1, 1)
        self.ClientLabel_23 = QtWidgets.QLabel(self.tab)
        self.ClientLabel_23.setMinimumSize(QtCore.QSize(256, 30))
        self.ClientLabel_23.setMaximumSize(QtCore.QSize(256, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ClientLabel_23.setFont(font)
        self.ClientLabel_23.setStyleSheet(" QLabel {\n"
"    border: 2px solid green;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"    \n"
"}")
        self.ClientLabel_23.setObjectName("ClientLabel_23")
        self.gridLayout_2.addWidget(self.ClientLabel_23, 4, 0, 1, 1)
        self.ClientLabel_20 = QtWidgets.QLabel(self.tab)
        self.ClientLabel_20.setMinimumSize(QtCore.QSize(256, 30))
        self.ClientLabel_20.setMaximumSize(QtCore.QSize(256, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ClientLabel_20.setFont(font)
        self.ClientLabel_20.setStyleSheet(" QLabel {\n"
"    border: 2px solid green;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"    \n"
"}")
        self.ClientLabel_20.setObjectName("ClientLabel_20")
        self.gridLayout_2.addWidget(self.ClientLabel_20, 6, 0, 1, 1)
        self.NodeType_combobox = QtWidgets.QFontComboBox(self.tab)
        self.NodeType_combobox.setMinimumSize(QtCore.QSize(119, 30))
        self.NodeType_combobox.setMaximumSize(QtCore.QSize(256, 22))
        self.NodeType_combobox.setStyleSheet("QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(/usr/share/icons/crystalsvg/16x16/actions/1downarrow.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}")
        self.NodeType_combobox.setObjectName("NodeType_combobox")
        self.gridLayout_2.addWidget(self.NodeType_combobox, 9, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setMinimumSize(QtCore.QSize(256, 30))
        self.label_9.setMaximumSize(QtCore.QSize(256, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(" QLabel {\n"
"    border: 2px solid green;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"    \n"
"}")
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 8, 0, 1, 1)
        self.ClientLabel_21 = QtWidgets.QLabel(self.tab)
        self.ClientLabel_21.setMinimumSize(QtCore.QSize(256, 30))
        self.ClientLabel_21.setMaximumSize(QtCore.QSize(256, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ClientLabel_21.setFont(font)
        self.ClientLabel_21.setStyleSheet(" QLabel {\n"
"    border: 2px solid green;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"    \n"
"}")
        self.ClientLabel_21.setObjectName("ClientLabel_21")
        self.gridLayout_2.addWidget(self.ClientLabel_21, 0, 0, 1, 1)
        self.listWidget_8 = QtWidgets.QListWidget(self.tab)
        self.listWidget_8.setMinimumSize(QtCore.QSize(256, 135))
        self.listWidget_8.setMaximumSize(QtCore.QSize(256, 135))
        self.listWidget_8.setStyleSheet("QListWidget {\n"
"    alternate-background-color: yellow;\n"
"    border: 5px double;\n"
"    border-color: blue;\n"
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
        self.listWidget_8.setObjectName("listWidget_8")
        self.gridLayout_2.addWidget(self.listWidget_8, 7, 0, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_2, 1, 0, 3, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.Demand_tab = QtWidgets.QTabWidget(self.tab)
        self.Demand_tab.setEnabled(True)
        self.Demand_tab.setMinimumSize(QtCore.QSize(821, 442))
        self.Demand_tab.setObjectName("Demand_tab")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.tab_8)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.Demand_mdi = QtWidgets.QMdiArea(self.tab_8)
        self.Demand_mdi.setMinimumSize(QtCore.QSize(1575, 521))
        self.Demand_mdi.setObjectName("Demand_mdi")
        self.gridLayout_13.addWidget(self.Demand_mdi, 0, 0, 1, 1)
        self.Demand_tab.addTab(self.tab_8, "")
        self.gridLayout_4.addWidget(self.Demand_tab, 0, 0, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_4, 1, 1, 1, 2)
        self.ClientLabel_25 = QtWidgets.QLabel(self.tab)
        self.ClientLabel_25.setMinimumSize(QtCore.QSize(50, 30))
        self.ClientLabel_25.setMaximumSize(QtCore.QSize(60, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ClientLabel_25.setFont(font)
        self.ClientLabel_25.setStyleSheet(" QLabel {\n"
"    border: 2px solid green;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"    \n"
"}")
        self.ClientLabel_25.setObjectName("ClientLabel_25")
        self.gridLayout_12.addWidget(self.ClientLabel_25, 2, 1, 1, 1)
        self.gridLayout_15 = QtWidgets.QGridLayout()
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.MapWidget = MapWidget(self.tab)
        self.MapWidget.setMinimumSize(QtCore.QSize(821, 259))
        self.MapWidget.setObjectName("MapWidget")
        self.gridLayout_15.addWidget(self.MapWidget, 0, 0, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_15, 3, 1, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem3, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.gridLayout_10.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_10, 0, 0, 1, 1)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(4)
        self.List_tab.setCurrentIndex(0)
        self.RackTab.setCurrentIndex(0)
        self.ShelfTab.setCurrentIndex(3)
        self.Demand_tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



        # TODO: added

        self.SelectNode_combo.clear()
        self.NodeType_combobox.clear()
        self.Demand_Source_combobox.clear()
        self.Demand_Destination_combobox.clear()
        self.cluster_type_combobox.clear()
        self.ClusterColor_combobox.clear()
        
        ClusterColors = ["green", "blue", "black", "orange", "yellow"]
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

        backend_map = Backend_map(MainWindow)
        self.backend_map = backend_map
        channel = QWebChannel(MainWindow)
        channel.registerObject('backend_map', backend_map)
        self.webengine.page().setWebChannel(channel)

        self.Traffic_matrix.cellChanged.connect(self.TM_CellChange_fun)

        self.SaveTM_button.clicked.connect(self.SaveTM_fun)

        self.General_TM.cellChanged.connect(self.GTM_CellChange_fun)

        self.LoadTM_button.clicked.connect(self.LoadTM_fun)
        self.insert_link_button.clicked.connect(self.insert_link_fun)


        self.PanelList.setDragEnabled(True)

        self.panels_name = ["BAF3","BLANK","LAF3","MP1H","MP2D","MP2X","OS5","PAF3","SC","SM2","TP1H","TP2X","TPAX","WS4"]

        self.panelList_fun()

        self.SaveChanges_button.clicked.connect(self.SaveChanges_button_fun)

        self.tabWidget.currentChanged["int"].connect(self.main_tab_clicked)

        self.Data_file_Flag = False

        MainWindow.showMaximized()

        self.TMSliderBar = self.Traffic_matrix.verticalScrollBar()
		
        self.GMTSliderBar = self.General_TM.verticalScrollBar()
        QObject.connect(self.TMSliderBar,SIGNAL("actionTriggered(int)"),self.SyncScroll_1)
        QObject.connect(self.GMTSliderBar,SIGNAL("actionTriggered(int)"),self.SyncScroll_2)

        self.SaveTopology_button.clicked.connect(self.SaveTopology_fun)

        self.OpenTopology_button.clicked.connect(self.OpenTopology_fun)

        Data["mdi_11"] = self.mdi_11
        Data["mdi_11_flag"] = False
        Data["mdi_12"] = self.mdi_12
        Data["mdi_12_flag"] = False
        Data["mdi_13"] = self.mdi_13
        Data["mdi_13_flag"] = False
        Data["mdi_14"] = self.mdi_14
        Data["mdi_14_flag"] = False

        self.ShelfTab.currentChanged["int"].connect(self.Shelf_tab_clicked)

        self.SelectNode_combo.currentIndexChanged["int"].connect(self.SelectNode_combo_change)

        Data["first_run_flag"] = False
        Data["demand_first_run_flag"] = False

        Data["ClientList"] = self.ClientList
        Data["LineList"] = self.LineList

        #self.ShelfTab.setStyleSheet("QTabBar::tab:selected {background-color: #4FA600}")

        Data["TabWidget"] = self.tabWidget

        Data["SelectNodeCombo"] = self.SelectNode_combo

        self.network = Network()


        #TODO: edited
        self.listWidget.clicked['QModelIndex'].connect(self.list_click)

        self.SelectSubNode.setText("Off")

        self.SetGatewayNode_button.clicked.connect(self.SetNode_gateway_fun)

        self.SelectSubNode_button.clicked.connect(self.SelectSubNode_button_fun)
        self.CurrentDegreename = None

        self.Demand_Source_combobox.currentTextChanged.connect(self.Demand_Source_combobox_Change)
        self.Demand_Destination_combobox.currentTextChanged.connect(self.Demand_Destination_combobox_change)

        Data["Demand_mdi"] = self.Demand_mdi

        self.OpenLinks_pushbutton.clicked.connect(self.open_links_fun)

        self.OK_button.clicked.connect(self.OK_button_fun)

        Data["Stage_flag"] = "Demand"
        Data["Demand_Source_combo"] = self.Demand_Source_combobox

        Data["Demand_LightPath_list"] = self.Demand_LineList
        Data["Demand_Service_list"] = self.Demand_ServiceList

        Data["DemandTab_firststart_flag"] = False

        self.Demand_ServiceList.setDragEnabled(True)
        self.Demand_LineList.setDragEnabled(True)

        self.Grooming_pushbutton.clicked.connect(self.grooming_button_fun)
        self.RWA_pushbutton.clicked.connect(self.RWA_button_fun)
        self.FinalPlan_pushbutton.clicked.connect(self.print_r)

        self.window = MainWindow

        Data["NetworkObj"] = self.network

        self.Demand_LineList.clicked['QModelIndex'].connect(self.Demand_LineList_fun)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Form"))
        self.tabWidget.setAccessibleName(_translate("MainWindow", "maintab"))
        self.OpenTopology_button.setText(_translate("MainWindow", "Open\n"
" Nodes"))
        self.SaveTopology_button.setText(_translate("MainWindow", "Save\n"
" Topology"))
        self.add_node_button.setText(_translate("MainWindow", "Add\n"
" Node"))
        self.OpenLinks_pushbutton.setText(_translate("MainWindow", "Open\n"
" Links"))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_7.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_6.setText(_translate("MainWindow", "Help\n"
" Ctrl + H"))
        self.Planning_groupbox.setTitle(_translate("MainWindow", "Planning"))
        self.PanelThreshold_pushbutton.setText(_translate("MainWindow", "Enter Panels Threshold"))
        self.Grooming_pushbutton.setText(_translate("MainWindow", "Grooming"))
        self.RWA_pushbutton.setText(_translate("MainWindow", "RWA"))
        self.FinalPlan_pushbutton.setText(_translate("MainWindow", "Final Plan"))
        self.ViewGroupbox.setTitle(_translate("MainWindow", "View Modes"))
        self.NormalMode_checkbox.setText(_translate("MainWindow", "Normal Mode"))
        self.Working_checkbox.setText(_translate("MainWindow", "Working View"))
        self.Protection_checkbox.setText(_translate("MainWindow", "Protection View"))
        self.Restoration_checkbox.setText(_translate("MainWindow", "Restoration View"))
        self.Grouping_groupbox.setTitle(_translate("MainWindow", "Clustering"))
        self.SetGatewayNode_button.setText(_translate("MainWindow", "Set Node as Gateway"))
        self.GroupName.setText(_translate("MainWindow", "Cluster Name:"))
        self.GroupID.setText(_translate("MainWindow", "Cluster Type :"))
        self.GroupColor.setText(_translate("MainWindow", "Cluster Color:"))
        self.SelectSubNode_button.setText(_translate("MainWindow", "Select Sub Nodes"))
        self.SelectSubNode.setText(_translate("MainWindow", "Off"))
        self.Cancel_button.setText(_translate("MainWindow", "Cancel"))
        self.OK_button.setText(_translate("MainWindow", "Ok"))
        self.ShowSubNodes.setText(_translate("MainWindow", "Show Sub Nodes"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TopologyTab), _translate("MainWindow", "Topology Tab"))
        self.Traffic_matrix.setSortingEnabled(False)
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
        self.TM_groupbox.setTitle(_translate("MainWindow", "Tools"))
        self.label_7.setText(_translate("MainWindow", "TextLabel"))
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
        item = self.listWidget.item(11)
        item.setText(_translate("MainWindow", "Main Route"))
        item = self.listWidget.item(12)
        item.setText(_translate("MainWindow", "Protection Route"))
        item = self.listWidget.item(13)
        item.setText(_translate("MainWindow", "Protection Route 1"))
        item = self.listWidget.item(14)
        item.setText(_translate("MainWindow", "Protection Route 2"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.List_tab.setTabText(self.List_tab.indexOf(self.tab_4), _translate("MainWindow", "Tab 1"))
        self.List_tab.setTabText(self.List_tab.indexOf(self.tab_5), _translate("MainWindow", "Service Type"))
        self.SaveTM_button.setText(_translate("MainWindow", "Save Traffic Matrix"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.LoadTM_button.setText(_translate("MainWindow", "Load Traffic Matrix"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.filter.setText(_translate("MainWindow", "Filter"))
        self.label_5.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_10.setText(_translate("MainWindow", "PushButton"))
        self.label_6.setText(_translate("MainWindow", "TextLabel"))
        self.SaveChanges_button.setText(_translate("MainWindow", "Save Changes"))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        self.insert_link_button.setText(_translate("MainWindow", "Insert Links"))
        self.label.setText(_translate("MainWindow", "Load File"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TrafficMatrixTab), _translate("MainWindow", "Traffic Matrix Tab"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), _translate("MainWindow", "Page"))
        self.ShelfTab.setTabText(self.ShelfTab.indexOf(self.Shelf1), _translate("MainWindow", "_1_"))
        self.ShelfTab.setTabText(self.ShelfTab.indexOf(self.Shelf2), _translate("MainWindow", "_2_"))
        self.ShelfTab.setTabText(self.ShelfTab.indexOf(self.Shelf3), _translate("MainWindow", "_3_"))
        self.ShelfTab.setTabText(self.ShelfTab.indexOf(self.Shelf4), _translate("MainWindow", "_4_"))
        self.RackTab.setTabText(self.RackTab.indexOf(self.Rack1), _translate("MainWindow", "Rack 1"))
        self.ClientLabel.setText(_translate("MainWindow", "Client Side Services:"))
        self.PanelLabel.setText(_translate("MainWindow", "List Of Network Panels"))
        self.AddShelf_button.setText(_translate("MainWindow", "Add Shelf"))
        self.AddRack_button.setText(_translate("MainWindow", "Add Rack"))
        __sortingEnabled = self.PanelList.isSortingEnabled()
        self.PanelList.setSortingEnabled(False)
        item = self.PanelList.item(0)
        item.setText(_translate("MainWindow", "SC"))
        self.PanelList.setSortingEnabled(__sortingEnabled)
        self.pushButton_14.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_13.setText(_translate("MainWindow", "PushButton"))
        self.LineLabel.setText(_translate("MainWindow", "Line side Services:"))
        self.SelectNode_Label.setText(_translate("MainWindow", "Select A Node:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.NodeViewTab), _translate("MainWindow", "Grooming Tab"))
        self.SelectNode_Label_13.setText(_translate("MainWindow", "Source:"))
        self.label_8.setText(_translate("MainWindow", "Destination:"))
        self.ClientLabel_22.setText(_translate("MainWindow", "List of LightPathes :"))
        self.ClientLabel_23.setText(_translate("MainWindow", "Client Side Services:"))
        self.ClientLabel_20.setText(_translate("MainWindow", "Setting:"))
        self.label_9.setText(_translate("MainWindow", "Node Type:"))
        self.ClientLabel_21.setText(_translate("MainWindow", "List Of Network Panels:"))
        self.Demand_tab.setTabText(self.Demand_tab.indexOf(self.tab_8), _translate("MainWindow", "Shelf"))
        self.ClientLabel_25.setText(_translate("MainWindow", "Map:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Demand tab"))
    
    def loc_dict_init(self):
        R = 6371 
        self.loc_dict={}
        for id, node in Data["Nodes"].items():
            node_name = node["Node"]
            location = node["Location"]
            lat = location[0]
            lon = location[1]
            x = R * cos(lat) * cos(lon)
            y = R * cos(lat) * sin(lon)
            self.loc_dict[node_name] = [x, y]


    def map_plot(self):
        #ax = self.figure.add_subplot(111)
        map = Basemap(projection='mill',llcrnrlat=+25,urcrnrlat=40,\
        llcrnrlon=+44,urcrnrlon=64,resolution="l",ax = self.MapWidget.canvas.axes)
        map.drawcoastlines()
        map.fillcontinents(color='w',lake_color='aqua')
        map.drawcountries(linewidth=2,color="b")

        map.drawmapboundary(fill_color='aqua')
        Tlat,Tlng = 51.3890,35.6892
        Slat,Slng = 52.5836,29.5926
        Tx,Ty = map(Tlat,Tlng)
        Sx,Sy = map(Slat,Slng)
        xs = [Tx,Sx]
        ys = [Ty,Sy]
        #self.MapWidget.canvas.axes.clear()
        self.MapWidget.canvas.axes.plot(Tx,Ty,marker ="o",markersize = 12,color = "blue",alpha = 0.8)
        self.MapWidget.canvas.axes.plot(Sx,Sy,marker ="o",markersize = 12,color = "red",alpha = 0.8) 
        #self.MapWidget.canvas.axes.draw()
        #plt.show()
        self.MapWidget.canvas.axes.plot(xs,ys)

    def Set_DemandMap(self):
        R = 6371 
        self.loc_dict={}
        for id, node in Data["Nodes"].items():
            node_name = node["Node"]
            location = node["Location"]
            lat = location[0]
            lon = location[1]
            x = R * cos(lat) * cos(lon)
            y = R * cos(lat) * sin(lon)
            self.loc_dict[node_name] = [x, y]
           # self.MapWidget.canvas.axes.annotate(node_name, xy=(1, 1), xytext=(x+0.1, y+0.1))
            self.MapWidget.canvas.axes.text(x + 80, y - 100, node_name, {'color': 'blueviolet'})
            self.MapWidget.canvas.axes.plot(x, y, marker ="o", ms=13, color = 'black')

        for key in Data["Links"].keys():
            loc_source = key[0]
            loc_destination = key[1]

            source_node_loc = self.loc_dict[loc_source]
            destination_node_loc = self.loc_dict[loc_destination]
            xl = [source_node_loc[0], destination_node_loc[0]]
            yl = [source_node_loc[1], destination_node_loc[1]]
            self.MapWidget.canvas.axes.plot(xl,yl, c='black')

        #self.MapWidget.canvas.axes.plot(G)
        self.MapWidget.canvas.axes.get_xaxis().set_visible(False)
        self.MapWidget.canvas.axes.get_yaxis().set_visible(False)
        self.MapWidget.canvas.axes.set_frame_on(False)
        #self.MapWidget.canvas.figure.clf()
        #self.MapWidget.canvas.axes.cla()
        #trick for legend!!!!!!
        """ self.MapWidget.canvas.axes.plot(0, 0, ms=0.000000001, color = 'blue')
        self.MapWidget.canvas.axes.legend(loc = 'best')
        self.MapWidget.canvas.axes.plot(0, 0, ms=0.000000001, color = 'red')
        self.MapWidget.canvas.axes.legend(loc = 'best') """
        #trick for legend!!!!!!

    def DemandMap_Change(self, Working = None, Protection = None):
        self.MapWidget.canvas.axes.cla()
        ####
        R = 6371 
        #self.loc_dict={}
        Source = self.Demand_Source_combobox.currentText()
        Destination = self.Demand_Destination_combobox.currentText()

        for node in Data["Nodes"].values():
            #node_name = node["Node"]
            #location = node["Location"]
            #lat = location[0]
            #lon = location[1]
            #x = R * cos(lat) * cos(lon)
            #y = R * cos(lat) * sin(lon)
            #self.loc_dict[node_name] = [x, y]
           # self.MapWidget.canvas.axes.annotate(node_name, xy=(1, 1), xytext=(x+0.1, y+0.1))

            

            NodeName = node["Node"]
            id = self.NodeIdMap[NodeName]
            lat, lon = self.IdLocationMap[id]

            x = R * cos(lat) * cos(lon)
            y = R * cos(lat) * sin(lon)

            if NodeName == Source or NodeName == Destination:
                self.MapWidget.canvas.axes.plot(x, y, marker ="o", ms=13, color = 'gold')
            else:
                self.MapWidget.canvas.axes.plot(x, y, marker ="o", ms=13, color = 'black')

            self.MapWidget.canvas.axes.text(x + 80, y - 100, NodeName, {'color': 'blueviolet'})

        for key in Data["Links"].keys():
            InNodeName = key[0]
            OutNodeName = key[1]

            InNodeId = self.NodeIdMap[InNodeName]
            OutNodeId = self.NodeIdMap[OutNodeName]

            InNodeLocation = self.IdLocationMap[InNodeId]
            OutNodeLocation = self.IdLocationMap[OutNodeId]

            xIn = R * cos(InNodeLocation[0]) * cos(InNodeLocation[1])
            yIn = R * cos(InNodeLocation[0]) * sin(InNodeLocation[1])

            xOut = R * cos(OutNodeLocation[0]) * cos(OutNodeLocation[1])
            yOut = R * cos(OutNodeLocation[0]) * sin(OutNodeLocation[1])

            xl = [xIn, xOut]
            yl = [yIn, yOut]
            self.MapWidget.canvas.axes.plot(xl,yl, c='black')

        #self.MapWidget.canvas.axes.plot(G)
        self.MapWidget.canvas.axes.get_xaxis().set_visible(False)
        self.MapWidget.canvas.axes.get_yaxis().set_visible(False)
        self.MapWidget.canvas.axes.set_frame_on(False)
        


        
        """ R = 6371 
        self.loc_dict={}
        for node in Data["Nodes"].items():
            #print(node)
            node_ID = node[0]
            node_name = node[1]["Node"]
            location = node[1]["Location"]
            lat = location[0]
            lon = location[1]
            x = R * cos(lat) * cos(lon)
            y = R * cos(lat) * sin(lon)
            self.loc_dict[node_ID] = [x, y] """


           # self.MapWidget.canvas.axes.annotate(node_name, xy=(1, 1), xytext=(x+0.1, y+0.1))
            

            #self.setupUi(MainWindow)
            #setMinimumSize(QtCore.QSize(1125, 817))
            #self.MapWidget.canvas.figure.subplots_adjust()
            #FigureCanvas.resize(255,0,0)


        x_list_W = []
        y_list_W = []
        if Working != None:
            for key in Working:

                lat = self.IdLocationMap[key][0]
                lon = self.IdLocationMap[key][1]

                x1 = R * cos(lat) * cos(lon)
                y1 = R * cos(lat) * sin(lon)

                x_list_W.append(x1)
                y_list_W.append(y1)

            
            self.MapWidget.canvas.axes.plot(x_list_W, y_list_W, c='blue', alpha = 0.8, linewidth=3, label="Working")
            self.MapWidget.canvas.axes.legend(loc = 'best')

        x_list_P = []
        y_list_P = []
        if Protection != None:
            for key in Protection:

                lat = self.IdLocationMap[key][0]
                lon = self.IdLocationMap[key][1]

                x1 = R * cos(lat) * cos(lon)
                y1 = R * cos(lat) * sin(lon)

                x_list_P.append(x1)
                y_list_P.append(y1)
           
            self.MapWidget.canvas.axes.plot(x_list_P, y_list_P, c='red', alpha = 0.8, linewidth=3, label="Protection")
            self.MapWidget.canvas.axes.legend(loc = 'best')
        
        
        self.window.resize(1919, 1000)
        print(self.window.geometry())
        self.window.resize(1920, 1000)
        print(self.window.geometry())
        #plt.pause(0.0005)
        #plt.ion()
        #self.MapWidget.canvas.axes.plot.update()
        #self.MapWidget.canvas.update()
    
    def OK_button_fun(self):
        SubNodes = []
        for node in Data["Grouping"][self.backend_map.LastGateWay]["SubNodes"].keys():
            SubNodes.append(self.NodeIdMap[node])
        
        self.network.PhysicalTopology.add_cluster(self.NodeIdMap[self.backend_map.LastGateWay], SubNodes, Data["Grouping"][self.backend_map.LastGateWay]["Color"])
        self.SelectSubNode_button_fun()
        print(self.network.PhysicalTopology.ClusterDict[0].SubNodesId)

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
        
        text = self.SelectSubNode.text()
        if text == "Off":
            self.SelectSubNode.setText("On")
            self.backend_map.SubNodeSelect_flag_fun("True")
            self.SelectSubNode_flag_javascript("True")
        else:
            self.SelectSubNode.setText("Off")
            self.backend_map.SubNodeSelect_flag_fun("False")
            self.SelectSubNode_flag_javascript("False")


    def SetNode_gateway_fun(self):
        self.backend_map.SetNode_flag_fun("False")
        self.SetNode_flag_javascript("False")
        self.lastgroup_name = self.GroupName_edit.text()
        self.lastgroup_type = self.cluster_type_combobox.currentText()
        self.lastgroup_color = self.Clustercolor_combobox.currentText()
        if self.lastgroup_name == "":


            #TODO: make a popup window for this
            print("please enter group details first")
        else:
            self.backend_map.SetNode_flag_fun("True",self.lastgroup_color)
            self.SetNode_flag_javascript("True")
        
        #TODO: also change button color after above procedure


    def SelectNode_combo_change(self):
        self.ShelfTab.setCurrentIndex(0)
        if Data["first_run_flag"] == True:
            self.set_panels()

        # degree 1 Grooming
        
        '''nodename  = self.SelectNode_combo.currentText()
        print("we are in grooming:",nodename)
        if Data["Nodes"][nodename]["Client_Services"]["flag"]["1"] == False:
            self.calculate_services(nodename,0)
        self.ClientList.clear()
        for service in list(Data["Nodes"][nodename]["Client_Services"]["data"]["1"].keys()):
            if Data["Nodes"][nodename]["Client_Services"]["data"]["1"][service] != 0:
                self.ClientList.addItem(str(Data["Nodes"][nodename]["Client_Services"]["data"]["1"][service])+" * "+service)

        # degree 1 grooming ( line side )
        self.LineList.clear()
        for service in list(Data["Nodes"][nodename]["Line_Services"]["1"].keys()):
            if Data["Nodes"][nodename]["Line_Services"]["1"][service] != 0:
                self.LineList.addItem(str(Data["Nodes"][nodename]["Line_Services"]["1"][service]) + " * "+service)'''

    # FIXME: this code 
    def set_panels(self):
        Source = self.SelectNode_combo.currentText()
        
        # getting tuple keys
        DegreeList = list(self.GroomingTabDataBase["Panels"].keys())

        # getting ids list
        DegreeIdList = list(map(lambda x : x[1], DegreeList))

        for DegreeId in DegreeIdList:

        #for i in range(1, 5):
            for j in range(1, 15):
                id = "1" + str( DegreeId ) + str(j)
                if id in GroomingTabDataBase["Panels"][nodename]:
                    panel = GroomingTabDataBase["Panels"][nodename][id]

                    if isinstance(panel , SC):
                        Data[id].setWidget(SC_panel(id,nodename))

                    elif isinstance(panel, BAF3):
                        Data[id].setWidget(BAF3_panel(id,nodename))

                    elif isinstance(panel , LAF3):
                        Data[id].setWidget(LAF3_panel(id,nodename))

                    elif isinstance(panel , PAF3):
                        Data[id].setWidget(PAF3_panel(id,nodename))

                    elif isinstance(panel, MP1H_L):
                        Data[id].setWidget(MP2X_panel(id,nodename))

                    elif isinstance(panel, MP2D_L):
                        # FIXME: this block needs correction
                        # from here
                        Data[id].setWidget(MP2D_panel_L(id,nodename))
                        if Data["Nodes"][nodename]["Panels"][id]["Sockets"]["Client1"] == "green":
                            Data[id].widget().label_client1.setPixmap(QPixmap(os.path.join("MP2D_panel", "client_green.png")))
                        elif Data["Nodes"][nodename]["Panels"]["1"+str(i)+str(j)]["Sockets"]["Client1"] == "red":
                            Data["1"+str(i)+str(j)].widget().label_client1.setPixmap(QPixmap(os.path.join("MP2D_panel", "client_red.png")))

                        if Data["Nodes"][nodename]["Panels"]["1"+str(i)+str(j)]["Sockets"]["Client2"] == "green":
                            Data["1"+str(i)+str(j)].widget().label_client2.setPixmap(QPixmap(os.path.join("MP2D_panel", "client_green.png")))
                        elif Data["Nodes"][nodename]["Panels"]["1"+str(i)+str(j)]["Sockets"]["Client2"] == "red":
                            Data["1"+str(i)+str(j)].widget().label_client2.setPixmap(QPixmap(os.path.join("MP2D_panel", "client_red.png")))

                        if Data["Nodes"][nodename]["Panels"]["1"+str(i)+str(j)]["Sockets"]["Line"] == 2:
                            Data["1"+str(i)+str(j)].widget().label_line.setPixmap(QPixmap(os.path.join("MP2D_panel", "line_green.png")))
                        
                        # to here

                    elif isinstance(panel, MP2D_R):
                        Data[id].setWidget(MP2D_panel_R(id, nodename))

                    elif isinstance(panel, TP2X):
                        Data[id].setWidget(TP2X_panel(id, nodename))
                    
                    elif isinstance(panel, TP1H_L):
                        Data[id].setWidget(TP1H_L_Grooming(id, nodename))
                        # TODO: change color

                    elif isinstance(panel, TP1H_R):
                        Data[id].setWidget(TP1H_R_Grooming(id, nodename))

                    elif isinstance(panel, MP1H_L):
                        Data[id].setWidget(MP1H_L_Grooming(id, nodename))
                        # TODO: change color
                           
                    elif isinstance(panel, MP1H_R):
                        Data[id].setWidget(MP1H_R_Grooming(id, nodename))
                else:
                    Data[id].setWidget(BLANK_panel(id, nodename))
    
    
    def set_demand_panels(self):


        Source = self.Demand_Source_combobox.currentText()
        Destination = self.Demand_Destination_combobox.currentText()
        for i in range(1, 15):
            if str(i) in DemandTabDataBase["Panels"][Source]:
                panel = DemandTabDataBase["Panels"][Source][str(i)]
                if isinstance(panel , MP2X_L):
                    Data["DemandPanel_" + str(i)].setWidget(MP2X_L_Demand(str(i), Source, Destination))
                    for client in panel.ClientsType:
                        if client != 0:
                            pass
                            # TODO: changing client label to green
                elif isinstance(panel, MP2X_R):
                    Data["DemandPanel_" + str(i)].setWidget(MP2X_R_Demand(str(i), Source))
                
                elif isinstance(panel, MP1H_L):
                    Data["DemandPanel_" + str(i)].setWidget(MP1H_L_Demand(str(i), Source, Destination))

                    # finding panel widget
                    widget = Data["DemandPanel_" + str(i)].widget()
                        
                    for i in range(len(panel.ClientsCapacity)):
                        if panel.ClientsCapacity[i] != 0:

                            # finding object of client customlabel
                            text = "client" + str( i + 1 )
                            clientvar = getattr(widget, text)

                            # filling customlabel attributes
                            clientvar.setPixmap(QPixmap(os.path.join("MP1H_Demand", "client_green.png")))
                            clientvar.setToolTip(DemandTabDataBase["Services_static"][Source][(panel.DemandIdList[i],panel.ServiceIdList[i])])
                            clientvar.servicetype = panel.ClientsCapacity[i]
                            clientvar.nodename = Source
                            clientvar.Destination = Destination
                            clientvar.ids = [panel.DemandIdList[i], panel.ServiceIdList[i]]
                            clientvar.setAcceptDrops(False)

                elif isinstance(panel, MP1H_R):
                    Data["DemandPanel_" + str(i)].setWidget(MP1H_R_Demand(str(i), Source))
                
                elif isinstance(panel, TP1H_L):
                    Data["DemandPanel_" + str(i)].setWidget(TP1H_L_Demand(str(i), Source, Destination))

                    # finding panel widget
                    widget = Data["DemandPanel_" + str(i)].widget()

                    if panel.Line == "100GE":

                        # finding object of client customlabel
                        clientvar = getattr(widget, "client")

                        # filling customlabel attributes 
                        clientvar.setToolTip(DemandTabDataBase["Services_static"][Source][(panel.DemandId, panel.ServiceId)])
                        clientvar.servicetype = "100GE"
                        self.nodename = Source
                        self.Destination = Destination
                        self.ids = [panel.DemandId, panel.ServiceId]
                        clientvar.setAcceptDrops(False)

                        # TODO: change client color to green
                
                elif isinstance(panel, TP1H_R):
                    Data["DemandPanel_" + str(i)].setWidget(TP1H_R_Demand(str(i), Source))
            
            else:
                Data["DemandPanel_" + str(i)].setWidget(BLANK_Demand(str(i), Source, Destination))

                         




    def SaveTopology_fun(self):
        TSD = {}    # TSD: Topology Save Dictionary
        TSD["Nodes"] = Data["Nodes"]
        TSD["Links"] = Data["Links"]
        name = QFileDialog.getSaveFileName(MainWindow, "Save Topology")

        if name[0] != 0:
            with open(name[0], 'wb') as handle:
                pickle.dump(TSD, handle, protocol=pickle.HIGHEST_PROTOCOL)
            handle.close()
    
    def OpenTopology_fun(self):
        # this method imports Nodes Information
        name = QFileDialog.getOpenFileName(MainWindow, "Open Topology")

        if name[0] != 0 :
            with pd.ExcelFile(name[0]) as handle:
                Temp_data = handle.parse(header=0, skipfooter=0)
            temp_dic ={}
            handle.close() 
            headers = ['ID','Node','Location','Type'] 

            for pointer in headers:
                temp_dic[pointer] = {}
                temp_dic[pointer].update(Temp_data[pointer])
            
            ProperDict = {}
            for Row in temp_dic["ID"].keys():
                Id = temp_dic["ID"][Row]
                Node = temp_dic["Node"][Row]
                Location = str(temp_dic["Location"][Row]).split(',')
                Location = list(map(lambda x : float(x), Location))

                Type = temp_dic["Type"][Row]

                ProperDict[Id] = {"Node": Node, "Location": Location, "Type":Type}

            Data["Nodes"].update(ProperDict)
            
            
    
    def open_links_fun(self):
        name = QFileDialog.getOpenFileName(MainWindow, "Open Topology")
        

        if name[0] != 0 :
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
        



    def SyncScroll_1(self):
        sliderValue = self.TMSliderBar.value()
        self.GMTSliderBar.setValue(sliderValue - 3)
    
    def SyncScroll_2(self):
        sliderValue = self.GMTSliderBar.value()
        self.TMSliderBar.setValue(sliderValue + 3)

    def main_tab_clicked(self,index):
        if index == 3:
            print("%s " %(self.mdi_11.geometry()))
            if Data["first_run_flag"] == False:
                for i in range(1,5):
                    self.shelfset(i)
                    Data["mdi_1"+str(i)+"_flag"] = True


            Data["first_run_flag"] = True
        if index == 4:
            if Data["DemandTab_firststart_flag"] == False:
                self.Demand_Shelf_set()
                Data["DemandTab_firststart_flag"] = True

            self.UpdateDemand_ServiceList()
            

            # TODO: run shelf set function for Demand Tab and turn its relevant flag on
    

    def Shelf_tab_clicked(self,index):
        Data["width"] = MainWindow.geometry().width()
        Data["height"] = MainWindow.geometry().height()

        # TODO: Update Light Path list
                    

    
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
    
    def Demand_LineList_fun(self):
        CurrentText = str(self.Demand_LineList.currentItem().text())

        # detecting Lightpath id, working path and protection path
        LightpathId = CurrentText.split('#')[0]
        LightpathId =int( LightpathId.strip() )
        Source = self.Demand_Source_combobox.currentText()
        Destination = self.Demand_Destination_combobox.currentText()

        if (Source, Destination) in GroomingTabDataBase["LightPathes"]:
            key = (Source, Destination)
        elif (Destination, Source) in GroomingTabDataBase["LightPathes"]:
            key = (Destination, Source)
        else:
            print("key not found")

        WorkingPath = GroomingTabDataBase["LightPathes"][(Source, Destination)][LightpathId]["Working"]
        ProtectionPath = GroomingTabDataBase["LightPathes"][(Source, Destination)][LightpathId]["Protection"]

        #print(f"here for calling demand change function <before> ")

        # calling Demand map change function
        self.DemandMap_Change(WorkingPath, ProtectionPath)

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

    def LoadTM_fun(self):
        name = QFileDialog.getOpenFileName(MainWindow, "Load Traffic Matrix")

        if name[0] != 0:
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
            self.update_cells()
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
                    self.network.TrafficMatrix.DemandDict[id].add_service(service, Sla, IgnoringNodes, Wavelength, Granularity, Granularity_xVC12, Granularity_xVC4)
            
            # initializing DataBases 
            self.initialize_DemandTabDataBase(Source, Destination)
            self.FillDemandTabDataBase_Services(id ,Source, Destination, ServiceDict)
            self.initialize_GroomingTabDataBase(Source, Destination)
            
    def initialize_DemandTabDataBase(self, Source, Destination):
        DemandTabDataBase["Lightpathes"][(Source, Destination)] = {}
        DemandTabDataBase["Panels"][Source] = {}

    def initialize_GroomingTabDataBase(self, Source, Destination):
        GroomingTabDataBase["LightPathes"][(Source, Destination)] = {}
        GroomingTabDataBase["Panels"][Source] = {}
        GroomingTabDataBase["Links"][(Source, Destination)] = []
        
    


    def FillDemandTabDataBase_Services(self, id, Source, Destination, ServiceDict):
        
        ServiceDict_2 = {}
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
            if isinstance(service, Network.Traffic.Demand.E1):
                servicetitle = "[%s , %s] # %s" %(id, serviceId, "E1")
                ServiceDict_2[(id, serviceId)] = servicetitle

            elif isinstance(service, Network.Traffic.Demand.STM_1_Electrical):
                servicetitle = "[%s , %s] # %s" %(id, serviceId, "STM_1_Electrical")
                ServiceDict_2[(id, serviceId)] = servicetitle

            elif isinstance(service, Network.Traffic.Demand.STM_1_Optical):
                servicetitle = "[%s , %s] # %s" %(id, serviceId, "STM_1_Optical")
                ServiceDict_2[(id, serviceId)] = servicetitle

            elif isinstance(service, Network.Traffic.Demand.STM_4):
                servicetitle = "[%s , %s] # %s" %(id, serviceId, "STM_4")
                ServiceDict_2[(id, serviceId)] = servicetitle

            elif isinstance(service, Network.Traffic.Demand.STM_16):
                servicetitle = "[%s , %s] # %s" %(id, serviceId, "STM_16")
                ServiceDict_2[(id, serviceId)] = servicetitle

            elif isinstance(service, Network.Traffic.Demand.STM_64):
                servicetitle = "[%s , %s] # %s" %(id, serviceId, "STM_64")
                ServiceDict_2[(id, serviceId)] = servicetitle

            elif isinstance(service, Network.Traffic.Demand.FE):
                servicetitle = "[%s , %s] # %s" %(id, serviceId, "FE")
                ServiceDict_2[(id, serviceId)] = servicetitle

            elif isinstance(service, Network.Traffic.Demand.G_1):
                servicetitle = "[%s , %s] # %s" %(id, serviceId, "1GE")
                ServiceDict_2[(id, serviceId)] = servicetitle

            elif isinstance(service, Network.Traffic.Demand.G_10):
                servicetitle = "[%s , %s] # %s" %(id, serviceId, "10GE")
                ServiceDict_2[(id, serviceId)] = servicetitle

            elif isinstance(service, Network.Traffic.Demand.G_40):
                servicetitle = "[%s , %s] # %s" %(id, serviceId, "40GE")
                ServiceDict_2[(id, serviceId)] = servicetitle

            elif isinstance(service, Network.Traffic.Demand.G_100):
                servicetitle = "[%s , %s] # %s" %(id, serviceId, "100GE")
                ServiceDict_2[(id, serviceId)] = servicetitle
        
        """ def manual_update(ServiceDict):
            print(f"before adding : {DemandTabDataBase['Services_static'][Source]}")
            for key, value in ServiceDict.items():
                DemandTabDataBase["Services_static"][Source][key] = value
                print(f"key : {key}, value: {value}") """
                

        DemandTabDataBase["Services"][(Source,Destination)] = ServiceDict_2
        if Source in DemandTabDataBase["Services_static"]:
            DemandTabDataBase["Services_static"][Source].update(ServiceDict_2.copy())
        else:
            DemandTabDataBase["Services_static"][Source] = {}
            DemandTabDataBase["Services_static"][Source].update(ServiceDict_2.copy())

    
    def Fill_Demand_SourceandDestination_combobox(self):

        SourceList = list(Data["General"]["DataSection"]["1"].values())
        DestinationList = list(Data["General"]["DataSection"]["2"].values())

        for Source in SourceList :
            if (Source in DemandTabDataBase["Source_Destination"] ) == False:
                DemandTabDataBase["Source_Destination"][Source] = []
        
        for i in range(len(SourceList)):
            Destination = DestinationList[i]
            Source = SourceList[i]
            DemandTabDataBase["Source_Destination"][Source].append(Destination)

        self.Demand_Source_combobox.clear()
        self.Demand_Source_combobox.addItems(list(DemandTabDataBase["Source_Destination"].keys()))
    
    def UpdateDemand_ServiceList(self):

        Source = self.Demand_Source_combobox.currentText()
        Destination = self.Demand_Destination_combobox.currentText()
        ServiceList = list(DemandTabDataBase["Services"][(Source,Destination)].values())
        self.Demand_ServiceList.clear()
        self.Demand_ServiceList.addItems(ServiceList)
    
    def Demand_Source_combobox_Change(self):
        Source = self.Demand_Source_combobox.currentText()

        if Source != '':
            self.Demand_Destination_combobox.clear()
            self.Demand_Destination_combobox.addItems(list(set(DemandTabDataBase["Source_Destination"][Source])))

        self.DemandMap_Change()
    
    def Demand_Destination_combobox_change(self):
        Source = self.Demand_Source_combobox.currentText()
        Destination = self.Demand_Destination_combobox.currentText()

        if self.Demand_Destination_combobox.currentText() != '':
            self.UpdateDemand_ServiceList()
            self.update_Demand_lightpath_list()
            self.set_demand_panels()

        self.DemandMap_Change()
        
        
            


    def PhysicalTopologyToObject(self):

        self.NodeIdMap = {}        # { name: id }
        self.IdNodeMap = {}        # {id : name}
        self.IdLocationMap = {}     # {id : [x , y]}

        for NodeData in Data["Nodes"].values():
            self.NodeIdMap[NodeData["Node"]] = self.network.Topology.Node.ReferenceId
            self.IdNodeMap[self.network.Topology.Node.ReferenceId] = NodeData["Node"]
            self.IdLocationMap[self.network.Topology.Node.ReferenceId] = NodeData["Location"]
            self.network.PhysicalTopology.add_node(NodeData["Location"], NodeData["Type"])
        
        for LinkId , LinkData in Data["Links"].items():
            self.network.PhysicalTopology.add_link(self.NodeIdMap[LinkId[0]], self.NodeIdMap[LinkId[1]], LinkData["NumSpan"])

            for i in range(LinkData["NumSpan"]):
                self.network.PhysicalTopology.LinkDict[(self.NodeIdMap[LinkId[0]], self.NodeIdMap[LinkId[1]])].put_fiber_Type(LinkData["Length"][i],
                 LinkData["Loss"][i], LinkData["Dispersion"][i], LinkData["Beta"][i], LinkData["Gamma"][i], i)
        
        # for using in panels widget
        Data["NodeIdMap"] = self.NodeIdMap
    
    def update_Demand_lightpath_list(self):
        #if Data["Stage_flag"] == "Grooming":
        Source = self.Demand_Source_combobox.currentText()
        Destination = self.Demand_Destination_combobox.currentText()
        lightpath_list = list(DemandTabDataBase["Lightpathes"][(Source, Destination)].values())
        self.Demand_LineList.clear()
        self.Demand_LineList.addItems(lightpath_list)
        
                




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
            Data["General"]["DataSection"][str(column)][str(row)] = value
        
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
            Icon = folium.features.CustomIcon('server_v5.png',icon_size=(30, 30),icon_anchor=(20,30))
            folium.Marker(Node_cor ,icon = Icon, popup=  "<h2>%s</h2>" %NodeName).add_to(self.m)
        
        for link in Data["Links"].keys():
            Source_cor = NodeCorDict[link[0]]
            DesTination_cor = NodeCorDict[link[1]]
            loc = [Source_cor, DesTination_cor]
            folium.PolyLine(loc ,weight = 3,popup = "Link ID: %s"%(id),color = "black",opacity = 0.8).add_to(self.m)

        self.m.save("map.html")

        # adding js events and settings on map

        Fig = self.m.get_root()
        Figtext = Fig.render()
        MapVar = re.findall("var( map_.*)=", Figtext)[0].strip()
        channel = "qrc:///qtwebchannel/qwebchannel.js"
        Fig.header.add_child(Element("<script src=%s></script>" %channel))
        '''Fig.script.add_child(Element("""window.onload = function() {
        new QWebChannel(qt.webChannelTransport, function (channel) {
        window.backend = channel.objects.backend;
        });"""))'''
        Fig.script.add_child(Element("""

        var  SetNodeGateWay_flag = null;
        var SelectSubNode_flag = null;
        var groupcolor = null;
        var marker_num = 0;

        function setcolor(text){
            groupcolor = text;
        }


        function SetNode_flag_fun(text){
            SetNodeGateWay_flag = text;
        }
        function SelectSubNode_flag_fun(text){
            SelectSubNode_flag = text;
        }
        var backend_map = null;
        new QWebChannel(qt.webChannelTransport, function (channel) {
        window.backend_map = channel.objects.backend_map;
        });"""))
        Fig.script.add_child(Element("var myFeatureGroup = L.featureGroup().addTo(%s).on(\"click\", groupClick);" %MapVar))

        Fig.script.add_child(Element("""%s.eachLayer(function (layer) {
               if (layer instanceof L.Marker){
                  layer.addTo(myFeatureGroup);
               }
               
            });""" %MapVar))

        Fig.script.add_child(Element("""function groupClick(event) {
            var degreename = event.layer.getPopup().getContent().textContent
            // TODO: change popup to tooltip
            //var degreename = event.layer.getTooltip().getContent()
            //alert(degreename)

            //alert(groupcolor)
            

            if (SetNodeGateWay_flag == "True") {

                backend_map.Create_DataBase(degreename)

                var latlng = event.layer.getLatLng();
                event.layer.remove()
                var icon =  L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "white", "markerColor": groupcolor, "prefix": "glyphicon"}
            );

                var mark = L.marker(latlng).setIcon(icon).addTo(%s);

                var pop = L.popup({"maxWidth": "100%%"});
                var htm = $(`<div id="htm" style="width: 100.0%%; height: 100.0%%;"><h2>${degreename}</h2></div>`)[0];
                pop.setContent(htm);
                mark.bindPopup(pop);

                

                mark.addTo(myFeatureGroup);

                backend_map.SetNode_flag_fun("False",groupcolor)

            } else if ( SelectSubNode_flag == "True") {

                backend_map.AddNode_DataBase(degreename)

                var latlng = event.layer.getLatLng();
                event.layer.remove()
                var icon =  L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "white", "markerColor": groupcolor, "prefix": "glyphicon"}
            );
                var mark = L.marker(latlng,{opacity:0.5}).setIcon(icon).addTo(%s);

                var pop = L.popup({"maxWidth": "100%%"});
                var htm = $(`<div id="htm" style="width: 100.0%%; height: 100.0%%;"><h2>${degreename}</h2></div>`)[0];
                pop.setContent(htm);
                mark.bindPopup(pop);

                

               

                mark.addTo(myFeatureGroup);
                


            } else{
                backend_map.change_tab_to4(degreename);
            }

            
            }
            """ %(MapVar,MapVar)))
        
        Fig.save("map.html")

        self.webengine.load(QUrl.fromLocalFile(os.path.abspath('map.html')))
        self.webengine.show()

      
    def panelList_fun(self):
        for panel in self.panels_name:
            if panel != "SC":
                item = QListWidgetItem(panel)
                self.PanelList.addItem(item)

    def SelectNode_combo_fun(self):
        self.SelectNode_combo.clear()
        nodesname = list(Data["Nodes"].keys())
        self.SelectNode_combo.addItems(nodesname)

    def SaveChanges_button_fun(self):
        # filling Network Object
        self.PhysicalTopologyToObject()
        self.TrafficMatrixToObject()
        self.DemandTabDataBase_Setup()
        self.GroomingTabDataBase_Setup()
        self.Fill_Demand_SourceandDestination_combobox()



        #self.SelectNode_combo_fun()
    
    def DemandTabDataBase_Setup(self):
        for node in Data["Nodes"].values():
            nodename = node["Node"]
            DemandTabDataBase["Panels"][nodename] = {}
        

    def GroomingTabDataBase_Setup(self):

        nodelist = []
        for node in Data["Nodes"].values():
            nodename = node["Node"]
            nodelist.append(nodename)
            GroomingTabDataBase["Panels"][nodename] = {}
        self.SelectNode_combo.addItems(nodelist)
        

    def shelfset(self,shelfnum):
        nodename = self.SelectNode_combo.currentText()
        print("nodename:",nodename)
        for i in range(1,15):
            setattr(self,"panel_1" + str(shelfnum) + str(i),QMdiSubWindow())
            Data["1"+str(shelfnum)+str(i)] = getattr(ui,"panel_1"+str(shelfnum)+str(i))
            Data["1"+str(shelfnum)+str(i)].setWindowFlag(Qt.FramelessWindowHint)
            Data["1"+str(shelfnum)+str(i)].setWidget(BLANK_panel("1"+str(shelfnum)+str(i), nodename))
            
            Data["mdi_1"+str(shelfnum)].addSubWindow(Data["1"+str(shelfnum)+str(i)])              

            Data["1"+str(shelfnum)+str(i)].show()
    
    def Demand_Shelf_set(self):
        # TODO: add this method to Demand tab initializer 
        Source = self.Demand_Source_combobox.currentText()
        Destination = self.Demand_Destination_combobox.currentText()
        for i in range(1,15):
            setattr(self, "DemandPanel_" + str(i),QMdiSubWindow())
            Data["DemandPanel_" + str(i)] = getattr(ui, "DemandPanel_" + str(i))
            Data["DemandPanel_" + str(i)].setWindowFlag(Qt.FramelessWindowHint)
            Data["DemandPanel_" + str(i)].setWidget(BLANK_Demand(str(i), Source, Destination))

            Data["Demand_mdi"].addSubWindow(Data["DemandPanel_" + str(i)])
            Data["DemandPanel_" + str(i)].show()


    # obsoleted 
    def shelf_1_rack_1(self):

        for i in range(1,15):
            setattr(self,"panel_11"+str(i),QMdiSubWindow())
            Data["11"+str(i)] = getattr(ui,"panel_11"+str(i))
            Data["11"+str(i)].setWindowFlag(Qt.FramelessWindowHint)
            Data["11"+str(i)].setWidget(BLANK_panel("11"+str(i)))
            
            Data["mdi_11"].addSubWindow(Data["11"+str(i)])              

            Data["11"+str(i)].show()
    
    def put_demandtab_results(self):
        pass
    
    def put_groomingtab_results(self):
        for id, lightpath in self.network.LightPathDict.items():
            working = lightpath.WorkingPath
            protection = lightpath.ProtectionPath

            for i in range(0, len(working), 2):
                innode = self.NodeIdMap[working[i]]
                outnode = self.NodeIdMap[working[i+1]]

                #if (innode, outnode) 




    """ def grooming_fun(self):

        MP1H_th = 7

        for demand, demandobj in self.network.TrafficMatrix.DemandDict.items():
            ServiceList =list(demandobj.ServiceDict.items())

            STM_64_List = list(filter(lambda x : isinstance( x[1] , Network.Traffic.Demand.STM_64 ) , ServiceList))
            STM_64_List = list(map(lambda x : x[0] , STM_64_List ))
            NumSTM_64 = len(STM_64_List)

            G10_List = list(filter(lambda x : isinstance( x[1] , Network.Traffic.Demand.G_10 ) , ServiceList))
            G10_List = list(map(lambda x : x[0] , G10_List ))
            NumG10 = len(G10_List)

            G100_List = list(filter(lambda x : isinstance( x[1] , Network.Traffic.Demand.G_100 ) , ServiceList))
            G100_List = list(map(lambda x : x[0] , G100_List ))
            NumG100 = len(G100_List)

            # Number Of MP1H Calculation

            NumClientPorts_MP1H = NumSTM_64 + NumG10
            MP1H_servicelist = G10_List + STM_64_List
            NumFullLightPath = NumClientPorts_MP1H // 10
            RemClients_MP1H = NumClientPorts_MP1H % 10
            NumMP1H = ceil(NumClientPorts_MP1H / 10)

            for no in range(NumFullLightPath):
                self.network.add_lightpath(demandobj.Source, demandobj.Destination, "100GE", MP1H_servicelist[0:10]
                ,"100GE", demand)
                for i in reversed(range(10)) :
                    DemandTabDataBase["Services"][(demandobj.Source, demandobj.Destination)][(demand, str(MP1H_servicelist[i]))]
                    MP1H_servicelist.pop(i)

            
            if RemClients_MP1H >= MP1H_th:
                print("th_List:" , MP1H_servicelist)
                x = list(MP1H_servicelist)
                for i in range(10-len(MP1H_servicelist)):
                    x.append(None)
                self.network.add_lightpath(demandobj.Source, demandobj.Destination, "100GE", x, "100GE", demand)

                for i in reversed(range(len(MP1H_servicelist))):
                    DemandTabDataBase["Services"][(demandobj.Source, demandobj.Destination)][(demand, str(MP1H_servicelist[i]))]
                    MP1H_servicelist.pop(i)
            
            # Number Of TP1H Calculation
            NumTP1H = NumG100


            for no in reversed(range(NumG100)):
                if isinstance(G100_List, int):
                    x = [G100_List]
                    for i in range(9):
                        x.append(None)
                else:
                    x = [G100_List[no]]
                    for i in range(9):
                        x.append(None)
                self.network.add_lightpath(demandobj.Source, demandobj.Destination, "100GE", G100_List[no], "100GE", demand)

                DemandTabDataBase["Services"][(demandobj.Source, demandobj.Destination)][(demand, str(G100_List[no]))]
                G100_List.pop(no) """




    def print_r(self, obj):
        with open("object.obj", 'rb') as handle:
            pickle.dump(obj, handle, protocol=pickle.HIGHEST_PROTOCOL)
        handle.close()
    
    def fill_lightpath(self):
        for i in range(4):
            path = [0, 1]
            self.network.put_results(i, list(path), list(path), [i + 1], "x", "x", "x", "x", "x", "x")
        
        for i in range(4, 9):
            path = [0 ,2]
            self.network.put_results(i, list(path), list(path), [i - 3], "x", "x", "x", "x", "x", "x")
        for i in range(9, 11):
            path = [2, 1]
            self.network.put_results(i, list(path), list(path), [i - 8], "x", "x", "x", "x", "x", "x")
        
        for i in range(11, 13):
            path = [0 ,3]
            self.network.put_results(i, list(path), list(path), [i - 10], "x", "x", "x", "x", "x", "x")
        
        path = [3, 0, 1]
        self.network.put_results(13, list(path), list(path), [5], "x", "x", "x", "x", "x", "x")

        path = [3, 0 ,2]
        self.network.put_results(14, list(path), list(path), [6], "x", "x", "x", "x", "x", "x")
    
    def fill_DemandTabDataBase(self, netobj):

        def get_panel_num(Source):
            IdList = list(DemandTabDataBase["Panels"][Source].keys())
            
            # if shelf is empty this method must return 1 in ## string ##
            if not IdList:
                return "1"
            IdList = list(map(lambda x : int(x), IdList))
            MaxId = max(IdList)
            return str(MaxId + 1)
        
        def create_ClientsCapacityList(DemandId, ServiceIdList):
            OutputList = []
            for ServiceId in ServiceIdList:
                ServiceObj = netobj.TrafficMatrix.DemandDict[DemandId].ServiceDict[ServiceId]
                if isinstance(ServiceObj, Network.Traffic.Demand.G_10):
                    OutputList.append("10GE")
                else:
                    OutputList.append("STM_64")
            
            return OutputList

        # lightpath and panel part
        for id, lightpath in netobj.LightPathDict.items():
            
            
            Source = self.IdNodeMap[lightpath.Source]
            Destination = self.IdNodeMap[lightpath.Destination]
            type = lightpath.Type
            DemandId = lightpath.DemandId
            DemandTabDataBase["Lightpathes"][(Source, Destination)][id] = "%s # %s" %(id, type)

            ## debug section
            print("Source: ", Source)
            print("Destination:" , Destination)
            print("DemandId :", DemandId)
            print("serviceIdList :", lightpath.ServiceIdList)

            ## end of debug section
            
            # checking wheather lightpath is created by tp1h or not
            if len(lightpath.ServiceIdList) == 1:
                panelid = get_panel_num(Source)
                DemandTabDataBase["Panels"][Source][panelid] = TP1H_L(DemandId, lightpath.ServiceIdList[0], "100GE", id)

                ## debug section
                print(DemandTabDataBase["Panels"][Source][panelid].__dict__)

                ## end of debug section
                DemandTabDataBase["Panels"][Source][str(int(panelid) + 1)] = TP1H_R(panelid)

                # omitting handeled services from DemandTabDataBase
                DemandTabDataBase["Services"][(Source, Destination)].pop((DemandId, lightpath.ServiceIdList[0]))
            else:
                panelid = get_panel_num(Source)
                ClientCapacity = create_ClientsCapacityList(DemandId, lightpath.ServiceIdList)
                LineCapacity = len(ClientCapacity) * 10
                
                ClientLen = len(ClientCapacity) 
                if ClientLen != 10:
                    for i in range(10 - ClientLen):
                        ClientCapacity.append(0)
                
                
                DemandTabDataBase["Panels"][Source][panelid] = MP1H_L(ClientCapacity, LineCapacity, lightpath.ServiceIdList, [DemandId for i in range(10)], id, LightPath_flag= 1)

                ## debug section
                print(DemandTabDataBase["Panels"][Source][panelid].__dict__)

                ## end of debug section
                DemandTabDataBase["Panels"][Source][str(int(panelid) + 1)] = MP1H_R(panelid)

                # omitting handeled services from DemandTabDataBase
                for ServiceId in lightpath.ServiceIdList:
                    DemandTabDataBase["Services"][(Source, Destination)].pop((DemandId, ServiceId))
                print(f"panels part--> Source:{Source} panels:{DemandTabDataBase['Panels'][Source]}")
                print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    
    def fill_GroomingTabDataBase(self, netobj):

        def get_panel_num(Source):
            IdList = list(DemandTabDataBase["Panels"][Source].keys())
            
            # if shelf is empty this method must return 1 in ## string ##
            if not IdList:
                return "1"
            IdList = list(map(lambda x : int(x), IdList))
            MaxId = max(IdList)
            return str(MaxId + 1)
        
        def create_ClientsCapacityList(DemandId, ServiceIdList):
            OutputList = []
            for ServiceId in ServiceIdList:
                
                # FIXME: very important
                if ServiceId in self.network.TrafficMatrix.DemandDict[DemandId].ServiceDict:
                    ServiceObj = self.network.TrafficMatrix.DemandDict[DemandId].ServiceDict[ServiceId]
                else:
                    ServiceObj = 0
                ##

                if isinstance(ServiceObj, Network.Traffic.Demand.G_10):
                    OutputList.append("10GE")
                else:
                    OutputList.append("STM_64")
            
            return OutputList
        
        
        for id, lightpath in netobj.LightPathDict.items():
            Source = self.IdNodeMap[lightpath.Source]
            Destination = self.IdNodeMap[lightpath.Destination]
            Working = lightpath.WorkingPath
            Protection = lightpath.ProtectionPath
            DemandId = lightpath.DemandId
            WaveLength = lightpath.WaveLength

            # adding pathes to to GroomingTabDataBase
            GroomingTabDataBase["LightPathes"][(Source, Destination)][id] = {}
            GroomingTabDataBase["LightPathes"][(Source, Destination)][id]["Working"] = Working
            GroomingTabDataBase["LightPathes"][(Source, Destination)][id]["Protection"] = Protection

            # Detecting Degrees and Filling GroomingTabDataBase ( Panels Part )

            DegreeNode = self.IdNodeMap[Working[1]]     # second node of each lightpath

            # BUG: be careful here we are calculating degrees based on working path only
            if not( DegreeNode in GroomingTabDataBase["Panels"]):
                DegreeId = len(GroomingTabDataBase["Panels"][Source]) + 1   
                GroomingTabDataBase["Panels"][( DegreeNode, DegreeId )] = {}
            
            # TODO: separate lightpathes based on their degree
            PanelId = get_panel_num(Source)

            # checking the lightpath is TP1H or MP1H
            if len(lightpath.ServiceIdList) == 1:
                DemandTabDataBase["Panels"][Source][PanelId] = TP1H_L(DemandId, lightpath.ServiceIdList[0], "100GE", id)
                DemandTabDataBase["Panels"][Source][str(int(PanelId) + 1)] = TP1H_R(PanelId)

            else:
                ClientCapacity = create_ClientsCapacityList(DemandId ,lightpath.ServiceIdList)
                DemandTabDataBase["Panels"][Source][PanelId] = MP1H_L(ClientCapacity, "100GE", lightpath.ServiceIdList, [DemandId for i in range(10)], id)
                DemandTabDataBase["Panels"][Source][str(int(PanelId) + 1)] = MP1H_R(PanelId)

            # filling GroomingTabDataBase ( Links or lambdas part )
            for i in range(len(Working) - 1):
                InNodeName = self.IdNodeMap[Working[ i ]]
                OutNodeName = self.IdNodeMap[Working[ i + 1 ]]

                if ( InNodeName , OutNodeName) in GroomingTabDataBase["Links"]:
                    keyW = ( InNodeName , OutNodeName)
                elif ( OutNodeName , InNodeName ) in GroomingTabDataBase["Links"]:
                    keyW = ( OutNodeName , InNodeName )
                else:
                    print("$$ key not found $$")

                if WaveLength in GroomingTabDataBase["Links"][keyW]:
                    # TODO: raise error --> this wavelength has been used
                    pass
                else:
                    GroomingTabDataBase["Links"][keyW].append(WaveLength)
            
            for i in range(len(Protection) - 1):
                InNodeName = self.IdNodeMap[Protection[ i ]]
                OutNodeName = self.IdNodeMap[Protection[ i + 1 ]]

                if ( InNodeName , OutNodeName) in GroomingTabDataBase["Links"]:
                    keyP = ( InNodeName , OutNodeName)
                elif ( OutNodeName , InNodeName ) in GroomingTabDataBase["Links"]:
                    keyP = ( OutNodeName , InNodeName )
                else:
                    print("$$ key not found $$")

                if WaveLength in GroomingTabDataBase["Links"][keyP]:
                    pass
                    # TODO: raise error --> this wavelength has been used
                else:
                    GroomingTabDataBase["Links"][keyP].append(WaveLength)

        for tup in GroomingTabDataBase["LightPathes"]:
            for key in GroomingTabDataBase["LightPathes"][tup]:
                GroomingTabDataBase["LightPathes"][tup][int(key)] = GroomingTabDataBase["LightPathes"][tup].pop(key)

                
            

    def grooming_fun(self, n):
        # n: network object

        service_lower10=[]
        service_lower100=[]
        output_10=[]                                            #(DemandId,Service)
        output_100=[]
        remain=[]
        threshold=70
        for i in n.TrafficMatrix.DemandDict:
            y=[]
            z=[]
            for j in n.TrafficMatrix.DemandDict[i].ServiceDict:
                if (n.TrafficMatrix.DemandDict[i].ServiceDict[j].BW < 10):
                    y.append((n.TrafficMatrix.DemandDict[i].ServiceDict[j].Id,n.TrafficMatrix.DemandDict[i].ServiceDict[j].BW))
                elif (n.TrafficMatrix.DemandDict[i].ServiceDict[j].BW == 10):
                    z.append((n.TrafficMatrix.DemandDict[i].ServiceDict[j].Id,n.TrafficMatrix.DemandDict[i].ServiceDict[j].BW))
                else:
                    n.add_lightpath(n.TrafficMatrix.DemandDict[i].Source, n.TrafficMatrix.DemandDict[i].Destination, 100, [n.TrafficMatrix.DemandDict[i].ServiceDict[j].Id], 100, i)
            if z:
                service_lower100.append((i,z))
            
        for i in range(0,len(service_lower100)):
            NO_LP= math.ceil(len(service_lower100[i][1])/10)
            for j in range(0,NO_LP):
                list_of_service=[]
                cap=0
                for k in range(j*10,(j+1)*10):
                    if (k < len(service_lower100[i][1])):
                        list_of_service.append(service_lower100[i][1][k][0])
                        cap=cap+service_lower100[i][1][k][1]
    #          print(service_lower100[2][0])
                if cap ==10:
                    typee="10GE"
                else:
                    typee="100GE"
                if cap < threshold:
                    remain.append((i,list_of_service))
                else:
                    n.add_lightpath(n.TrafficMatrix.DemandDict[service_lower100[i][0]].Source, n.TrafficMatrix.DemandDict[service_lower100[i][0]].Destination, cap, list_of_service, typee, service_lower100[i][0])    
    #         
        return remain
         
    def failed_grooming_nodes():
        # detecting node where grooming algorithm has been failed

        # changing their icon based on their cluster

        # NOTE: keep this in mind that you have to change icons againg when ever 
        #   Service section of that node gets empty ( based on its degree ) 
        # this should be done in another method ( manual service manipulations method in panels object)
        pass
        
        
    
    def grooming_button_fun(self):

        print("before grooming")
        for lightpath in self.network.LightPathDict.values():
            print(lightpath.__dict__)

        RemainServices = self.grooming_fun(self.network)
        print(f"remained services : {RemainServices}")

        self.fill_DemandTabDataBase(self.network)

        


        

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

        # Convert keys to String
        tuple_keys = list(net.PhysicalTopology.LinkDict.keys())
        for key in tuple_keys:
            net.PhysicalTopology.LinkDict[str(key)] = net.PhysicalTopology.LinkDict.pop(key)

            
        ##############################################
        # Convert the Network object to JSON message
        data = json.dumps(net,default=convert_to_dict,indent=4, sort_keys=True)
        # print(data)

        decoded_network = Network.from_json(json.loads(data)) 
        str_keys = list(decoded_network.PhysicalTopology.LinkDict.keys())
        for key in str_keys:
            Lkey = list(key)
            ActualKey =( int(Lkey[1]) , int(Lkey[-2]) )
            decoded_network.PhysicalTopology.LinkDict[ActualKey] = decoded_network.PhysicalTopology.LinkDict.pop(key)

        # assert False
        # This line tests whether the JSON encoded common object is reconstructable!
        decoded_n = Network.from_json(json.loads(data)) 
        assert(isinstance(decoded_n, Network))

        # Establishing a socket.io connection for logging purposes
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
        res = requests.get('http://localhost:5000/RWA/', json = data)

        if res.ok:
            # print('####################################################')
            # print(json.dumps(res.json()))
            decoded_network = Network.from_json(json.loads(json.dumps(res.json())))
            # Converting keys to original version ( Server Side )
            str_keys = list(decoded_network.PhysicalTopology.LinkDict.keys())
            for key in str_keys:
                n_key = ''.join(key.split())
                Lkey = n_key[1:-1].split(',')
                ActualKey =( int(Lkey[1]) , int(Lkey[-2]) )
                decoded_network.PhysicalTopology.LinkDict[ActualKey] = decoded_network.PhysicalTopology.LinkDict.pop(key)
                
            str_keys = decoded_network.LightPathDict.keys()
            for key in str_keys:
                decoded_network.LightPathDict[int(key)] = decoded_network.LightPathDict.pop(key)
            

        sio.disconnect()
        time.sleep(3)
        print('RWA finished and data received in client') 
        try:
            print('Sample WaveLength output', decoded_network.LightPathDict[0].WaveLength)
            print('Sample Path output', decoded_network.LightPathDict[0].WorkingPath)
        except:
            pass
        
        for lightpath in decoded_network.LightPathDict.values():
            print(lightpath.__dict__)

        self.fill_GroomingTabDataBase(decoded_network)
        

        




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    # NOTE: dont forget this
    Data["ui"] = ui
    MainWindow.show()
    sys.exit(app.exec_())

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
from geopy.geocoders import Nominatim
import re
from PySide2.QtWebChannel import QWebChannel
import branca
from branca.element import Element
import xlrd 
import xlsxwriter
from pandas import ExcelWriter 
from newcheck import  Ui_checking
from Common_Object_def import Network

from add_node import Ui_add_node_window

from data import Data, DemandTabDataBase
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



class Backend_map(QObject):

    @Slot(str)
    def Create_DataBase(self,text):
        print("last GateWay: ",text)
        self.LastGateWay = text

        # creating grouping database
        print("we are grouping")
        Data["Grouping"][text] = {}
        Data["Grouping"][text]["Color"] = ui.lastgroup_color
        Data["Grouping"][text]["ID"] = ui.lastgroup_id
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
        Panel_Data["TabWidget"].setCurrentIndex(3)
        Panel_Data["SelectNodeCombo"].setCurrentText(degreename.strip())
        ui.SelectNode_combo_change()




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")

        #TODO: commented
        #MainWindow.resize(1133, 805)

        self.gridLayout = QtWidgets.QGridLayout(MainWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(MainWindow)
        self.tabWidget.setObjectName("tabWidget")
        self.TopologyTab = QtWidgets.QWidget()
        self.TopologyTab.setObjectName("TopologyTab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.TopologyTab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.TopologyTab)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_3.addWidget(self.pushButton_4, 0, 3, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.TopologyTab)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_3.addWidget(self.pushButton_5, 0, 4, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.TopologyTab)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_3.addWidget(self.pushButton_6, 0, 6, 1, 1)
        self.add_node_button = QtWidgets.QPushButton(self.TopologyTab)
        self.add_node_button.setObjectName("add_node_button")
        self.gridLayout_3.addWidget(self.add_node_button, 0, 2, 1, 1)
        self.OpenTopology_button = QtWidgets.QPushButton(self.TopologyTab)
        self.OpenTopology_button.setObjectName("OpenTopology_button")
        self.gridLayout_3.addWidget(self.OpenTopology_button, 0, 0, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.TopologyTab)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_3.addWidget(self.pushButton_7, 0, 5, 1, 1)

        #TODO: edited
        self.webengine = QtWebEngineWidgets.QWebEngineView()
        self.webengine.setObjectName("webengine")
        self.gridLayout_3.addWidget(self.webengine, 2, 0, 1, 6)


        self.SaveTopology_button = QtWidgets.QPushButton(self.TopologyTab)
        self.SaveTopology_button.setObjectName("SaveTopology_button")
        self.gridLayout_3.addWidget(self.SaveTopology_button, 0, 1, 1, 1)
        self.T_groupbox = QtWidgets.QGroupBox(self.TopologyTab)
        self.T_groupbox.setEnabled(True)
        self.T_groupbox.setObjectName("T_groupbox")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.T_groupbox)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.Grouping_groupbox = QtWidgets.QGroupBox(self.T_groupbox)
        self.Grouping_groupbox.setObjectName("Grouping_groupbox")
        self.grouping_grid = QtWidgets.QGridLayout(self.Grouping_groupbox)
        self.grouping_grid.setObjectName("grouping_grid")
        self.GroupingLayout = QtWidgets.QGridLayout()
        self.GroupingLayout.setObjectName("GroupingLayout")
        self.SelectSubNode_button = QtWidgets.QPushButton(self.Grouping_groupbox)
        self.SelectSubNode_button.setObjectName("SelectSubNode_button")
        self.GroupingLayout.addWidget(self.SelectSubNode_button, 4, 0, 1, 2)
        self.SelectSubNode = QtWidgets.QLabel(self.Grouping_groupbox)
        self.SelectSubNode.setObjectName("SelectSubNode")
        self.GroupingLayout.addWidget(self.SelectSubNode, 4, 3, 1, 1)
        self.Cancel_button = QtWidgets.QPushButton(self.Grouping_groupbox)
        self.Cancel_button.setObjectName("Cancel_button")
        self.GroupingLayout.addWidget(self.Cancel_button, 5, 1, 1, 2)
        self.SelectColor_edit = QtWidgets.QLineEdit(self.Grouping_groupbox)
        self.SelectColor_edit.setObjectName("SelectColor_edit")
        self.GroupingLayout.addWidget(self.SelectColor_edit, 3, 2, 1, 2)
        self.GroupId_edit = QtWidgets.QLineEdit(self.Grouping_groupbox)
        self.GroupId_edit.setObjectName("GroupId_edit")
        self.GroupingLayout.addWidget(self.GroupId_edit, 2, 2, 1, 2)
        self.GroupColor = QtWidgets.QLabel(self.Grouping_groupbox)
        self.GroupColor.setObjectName("GroupColor")
        self.GroupingLayout.addWidget(self.GroupColor, 3, 0, 1, 2)
        self.SetGatewayNode_button = QtWidgets.QPushButton(self.Grouping_groupbox)
        self.SetGatewayNode_button.setObjectName("SetGatewayNode_button")
        self.GroupingLayout.addWidget(self.SetGatewayNode_button, 0, 0, 1, 4)
        self.GroupName = QtWidgets.QLabel(self.Grouping_groupbox)
        self.GroupName.setObjectName("GroupName")
        self.GroupingLayout.addWidget(self.GroupName, 1, 0, 1, 2)
        self.GroupName_edit = QtWidgets.QLineEdit(self.Grouping_groupbox)
        self.GroupName_edit.setObjectName("GroupName_edit")
        self.GroupingLayout.addWidget(self.GroupName_edit, 1, 2, 1, 2)
        self.OK_button = QtWidgets.QPushButton(self.Grouping_groupbox)
        self.OK_button.setObjectName("OK_button")
        self.GroupingLayout.addWidget(self.OK_button, 5, 3, 1, 1)
        self.GroupID = QtWidgets.QLabel(self.Grouping_groupbox)
        self.GroupID.setObjectName("GroupID")
        self.GroupingLayout.addWidget(self.GroupID, 2, 0, 1, 2)
        self.ShowSubNodes = QtWidgets.QCheckBox(self.Grouping_groupbox)
        self.ShowSubNodes.setObjectName("ShowSubNodes")
        self.GroupingLayout.addWidget(self.ShowSubNodes, 6, 0, 1, 3)
        self.grouping_grid.addLayout(self.GroupingLayout, 0, 0, 1, 1)
        self.gridLayout_11.addWidget(self.Grouping_groupbox, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_11.addItem(spacerItem, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.T_groupbox, 2, 6, 1, 1)
        self.tabWidget.addTab(self.TopologyTab, "")
        self.TrafficMatrixTab = QtWidgets.QWidget()
        self.TrafficMatrixTab.setObjectName("TrafficMatrixTab")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.TrafficMatrixTab)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.Traffic_matrix = QtWidgets.QTableWidget(self.TrafficMatrixTab)
        self.Traffic_matrix.setMaximumSize(QtCore.QSize(16777215, 16777215))
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
        self.SaveTM_button.setToolTip("")
        self.SaveTM_button.setObjectName("SaveTM_button")
        self.gridLayout_5.addWidget(self.SaveTM_button, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.TM_groupbox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 2, 1, 1, 1)
        self.LoadTM_button = QtWidgets.QPushButton(self.TM_groupbox)
        self.LoadTM_button.setObjectName("LoadTM_button")
        self.gridLayout_5.addWidget(self.LoadTM_button, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.TM_groupbox)
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 3, 1, 1, 1)
        self.filter = QtWidgets.QPushButton(self.TM_groupbox)
        self.filter.setObjectName("filter")
        self.gridLayout_5.addWidget(self.filter, 4, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.TM_groupbox)
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 4, 1, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.TM_groupbox)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_5.addWidget(self.pushButton_10, 5, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.TM_groupbox)
        self.label_6.setObjectName("label_6")
        self.gridLayout_5.addWidget(self.label_6, 5, 1, 1, 1)
        self.SaveChanges_button = QtWidgets.QPushButton(self.TM_groupbox)
        self.SaveChanges_button.setObjectName("SaveChanges_button")
        self.gridLayout_5.addWidget(self.SaveChanges_button, 6, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.TM_groupbox)
        self.label_4.setObjectName("label_4")
        self.gridLayout_5.addWidget(self.label_4, 6, 1, 1, 1)

        #TODO: edited
        self.insert_link_button = QtWidgets.QPushButton(self.TM_groupbox)
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
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.ClientList = QtWidgets.QListWidget(self.NodeViewTab)
        self.ClientList.setDragEnabled(True)
        self.ClientList.setObjectName("ClientList")
        self.gridLayout_7.addWidget(self.ClientList, 1, 0, 1, 2)
        self.ClientLabel = QtWidgets.QLabel(self.NodeViewTab)
        self.ClientLabel.setObjectName("ClientLabel")
        self.gridLayout_7.addWidget(self.ClientLabel, 0, 0, 1, 2)
        self.PanelLabel = QtWidgets.QLabel(self.NodeViewTab)
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
        self.LineLabel.setObjectName("LineLabel")
        self.gridLayout_7.addWidget(self.LineLabel, 2, 0, 1, 2)
        self.LineList = QtWidgets.QListWidget(self.NodeViewTab)
        self.LineList.setEnabled(True)
        self.LineList.setMaximumSize(QtCore.QSize(200000, 140))
        self.LineList.setObjectName("LineList")
        self.gridLayout_7.addWidget(self.LineList, 3, 0, 1, 2)
        self.gridLayout_8.addLayout(self.gridLayout_7, 0, 0, 2, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.SelectNode_Label = QtWidgets.QLabel(self.NodeViewTab)
        self.SelectNode_Label.setObjectName("SelectNode_Label")
        self.horizontalLayout.addWidget(self.SelectNode_Label)
        self.SelectNode_combo = QtWidgets.QFontComboBox(self.NodeViewTab)
        self.SelectNode_combo.setObjectName("SelectNode_combo")
        self.horizontalLayout.addWidget(self.SelectNode_combo)
        
        #TODO: added
        self.SelectNode_combo.clear()

        self.gridLayout_8.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.RackTab = QtWidgets.QTabWidget(self.NodeViewTab)
        self.RackTab.setTabPosition(QtWidgets.QTabWidget.North)
        self.RackTab.setObjectName("RackTab")
        self.Rack1 = QtWidgets.QWidget()
        self.Rack1.setObjectName("Rack1")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.Rack1)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.ShelfTab = QtWidgets.QTabWidget(self.Rack1)
        self.ShelfTab.setTabPosition(QtWidgets.QTabWidget.West)
        self.ShelfTab.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.ShelfTab.setElideMode(QtCore.Qt.ElideNone)
        self.ShelfTab.setObjectName("ShelfTab")
        self.Shelf1 = QtWidgets.QWidget()
        self.Shelf1.setObjectName("Shelf1")
        self.Shelf1_grid = QtWidgets.QGridLayout(self.Shelf1)
        self.Shelf1_grid.setObjectName("Shelf1_grid")
        self.mdi_11 = QtWidgets.QMdiArea(self.Shelf1)
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
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.mdi_14.setBackground(brush)
        self.mdi_14.setObjectName("mdi_14")
        self.Shelf4_grid.addWidget(self.mdi_14, 0, 0, 1, 1)
        self.ShelfTab.addTab(self.Shelf4, "")
        self.gridLayout_9.addWidget(self.ShelfTab, 0, 0, 1, 1)
        self.RackTab.addTab(self.Rack1, "")
        self.gridLayout_8.addWidget(self.RackTab, 1, 1, 1, 1)
        self.tabWidget.addTab(self.NodeViewTab, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        self.List_tab.setCurrentIndex(0)
        self.RackTab.setCurrentIndex(0)
        self.ShelfTab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        #TODO: added

        self.tabWidget.setCurrentIndex(0)

        self.add_node_button.clicked.connect(self.add_node_button_fun)
        self.m = folium.Map(location=[35.6892,51.3890],zoom_start=6)
        self.m.save("map.html")
        Panel_Data["Map_Var"] = self.m
        Panel_Data["Web_Engine"] = self.webengine
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

        Panel_Data["mdi_11"] = self.mdi_11
        Panel_Data["mdi_11_flag"] = False
        Panel_Data["mdi_12"] = self.mdi_12
        Panel_Data["mdi_12_flag"] = False
        Panel_Data["mdi_13"] = self.mdi_13
        Panel_Data["mdi_13_flag"] = False
        Panel_Data["mdi_14"] = self.mdi_14
        Panel_Data["mdi_14_flag"] = False

        self.ShelfTab.currentChanged["int"].connect(self.Shelf_tab_clicked)

        self.SelectNode_combo.currentIndexChanged["int"].connect(self.SelectNode_combo_change)

        Panel_Data["first_run_flag"] = False

        Panel_Data["ClientList"] = self.ClientList
        Panel_Data["LineList"] = self.LineList

        #self.ShelfTab.setStyleSheet("QTabBar::tab:selected {background-color: #4FA600}")

        self.filter.clicked.connect(self.printev)

        Panel_Data["TabWidget"] = self.tabWidget

        Panel_Data["SelectNodeCombo"] = self.SelectNode_combo

        self.network = Network()

        #TODO: edited
        self.listWidget.clicked['QModelIndex'].connect(self.list_click)

        self.SelectSubNode.setText("Off")

        self.SetGatewayNode_button.clicked.connect(self.SetNode_gateway_fun)

        self.SelectSubNode_button.clicked.connect(self.SelectSubNode_button_fun)
        self.CurrentDegreename = None



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Form"))
        self.pushButton_4.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_6.setText(_translate("MainWindow", "Help\n"
" Ctrl + H"))
        self.add_node_button.setText(_translate("MainWindow", "Add Node\n"
" Ctrl + ?"))
        self.OpenTopology_button.setText(_translate("MainWindow", "Open Topology\n"
"Ctrl + O"))
        self.pushButton_7.setText(_translate("MainWindow", "PushButton"))
        self.SaveTopology_button.setText(_translate("MainWindow", "Save Topology\n"
" Ctrl + S"))
        self.T_groupbox.setTitle(_translate("MainWindow", "View Options"))
        self.Grouping_groupbox.setTitle(_translate("MainWindow", "Grouping"))
        self.SelectSubNode_button.setText(_translate("MainWindow", "Select Sub Nodes"))
        self.SelectSubNode.setText(_translate("MainWindow", "TextLabel"))
        self.Cancel_button.setText(_translate("MainWindow", "Cancel"))
        #self.SelectColor_edit.setText(_translate("MainWindow", "Select Color"))
        self.GroupColor.setText(_translate("MainWindow", "Group Color:"))
        self.SetGatewayNode_button.setText(_translate("MainWindow", "Set Node as Gateway"))
        self.GroupName.setText(_translate("MainWindow", "Group Name:"))
        self.OK_button.setText(_translate("MainWindow", "Ok"))
        self.GroupID.setText(_translate("MainWindow", "Group ID:"))
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
        self.ShelfTab.setTabText(self.ShelfTab.indexOf(self.Shelf1), _translate("MainWindow", "1"))
        self.ShelfTab.setTabText(self.ShelfTab.indexOf(self.Shelf2), _translate("MainWindow", "2"))
        self.ShelfTab.setTabText(self.ShelfTab.indexOf(self.Shelf3), _translate("MainWindow", "3"))
        self.ShelfTab.setTabText(self.ShelfTab.indexOf(self.Shelf4), _translate("MainWindow", "4"))
        self.RackTab.setTabText(self.RackTab.indexOf(self.Rack1), _translate("MainWindow", "Rack 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.NodeViewTab), _translate("MainWindow", "Node View Tab"))

    
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
        self.lastgroup_id = self.GroupId_edit.text()
        self.lastgroup_color = self.SelectColor_edit.text()
        if self.lastgroup_name == "" and self.lastgroup_id == "" and self.lastgroup_color == "":


            #TODO: make a popup window for this
            print("please enter group details first")
        else:
            self.backend_map.SetNode_flag_fun("True",self.lastgroup_color)
            self.SetNode_flag_javascript("True")
        
        #TODO: also change button color after above procedure


    def SelectNode_combo_change(self):
        self.ShelfTab.setCurrentIndex(0)
        if Panel_Data["first_run_flag"] == True:
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


    def set_panels(self):
        nodename = self.SelectNode_combo.currentText()
        #self.reset_panels()
        #for id,panel in list(Data["Nodes"][nodename]["Panels"].items()):
        for i in range(1,5):
            for j in range(1,15):
                if "1"+str(i)+str(j) in Data["Nodes"][nodename]["Panels"]:
                    panel = Data["Nodes"][nodename]["Panels"]["1"+str(i)+str(j)]["Name"]
                    if panel == "SC":
                        Panel_Data["1"+str(i)+str(j)].setWidget(SC_panel("1"+str(i)+str(j),nodename))
                    elif panel == "BAF3":
                        Panel_Data["1"+str(i)+str(j)].setWidget(BAF3_panel("1"+str(i)+str(j),nodename))
                    elif panel == "LAF3":
                        Panel_Data["1"+str(i)+str(j)].setWidget(LAF3_panel("1"+str(i)+str(j),nodename))
                    elif panel == "PAF3":
                        Panel_Data["1"+str(i)+str(j)].setWidget(PAF3_panel("1"+str(i)+str(j),nodename))
                    elif panel == "MP2X":
                        Panel_Data["1"+str(i)+str(j)].setWidget(MP2X_panel("1"+str(i)+str(j),nodename))
                    elif panel == "MP2D":
                        position = Data["Nodes"][nodename]["Panels"]["1"+str(i)+str(j)]["Position"]
                        if position == "L":

                            Panel_Data["1"+str(i)+str(j)].setWidget(MP2D_panel_L("1"+str(i)+str(j),nodename))
                            if Data["Nodes"][nodename]["Panels"]["1"+str(i)+str(j)]["Sockets"]["Client1"] == "green":
                                Panel_Data["1"+str(i)+str(j)].widget().label_client1.setPixmap(QPixmap(os.path.join("MP2D_panel", "client_green.png")))
                            elif Data["Nodes"][nodename]["Panels"]["1"+str(i)+str(j)]["Sockets"]["Client1"] == "red":
                                Panel_Data["1"+str(i)+str(j)].widget().label_client1.setPixmap(QPixmap(os.path.join("MP2D_panel", "client_red.png")))

                            if Data["Nodes"][nodename]["Panels"]["1"+str(i)+str(j)]["Sockets"]["Client2"] == "green":
                                Panel_Data["1"+str(i)+str(j)].widget().label_client2.setPixmap(QPixmap(os.path.join("MP2D_panel", "client_green.png")))
                            elif Data["Nodes"][nodename]["Panels"]["1"+str(i)+str(j)]["Sockets"]["Client2"] == "red":
                                Panel_Data["1"+str(i)+str(j)].widget().label_client2.setPixmap(QPixmap(os.path.join("MP2D_panel", "client_red.png")))

                            if Data["Nodes"][nodename]["Panels"]["1"+str(i)+str(j)]["Sockets"]["Line"] == 2:
                                Panel_Data["1"+str(i)+str(j)].widget().label_line.setPixmap(QPixmap(os.path.join("MP2D_panel", "line_green.png")))
                        
                        elif position == "R":
                            Panel_Data["1"+str(i)+str(j)].setWidget(MP2D_panel_R("1"+str(i)+str(j),nodename))

                    elif panel == "TP2X":
                        Panel_Data["1"+str(i)+str(j)].setWidget(TP2X_panel("1"+str(i)+str(j),nodename))
                else:
                    Panel_Data["1"+str(i)+str(j)].setWidget(BLANK_panel("1"+str(i)+str(j), nodename))
        


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
        name = QFileDialog.getOpenFileName(MainWindow, "Open Topology")
        TOD = {}

        if name[0] != 0 :
            with open(name[0],'rb') as handle:
                Temp_data = pickle.load(handle)
            handle.close()
        TOD.update(Temp_data)
        Data["Nodes"].update(TOD["Nodes"])
        Data["Links"].update(TOD["Links"])



    def SyncScroll_1(self):
        sliderValue = self.TMSliderBar.value()
        self.GMTSliderBar.setValue(sliderValue - 3)
    
    def SyncScroll_2(self):
        sliderValue = self.GMTSliderBar.value()
        self.TMSliderBar.setValue(sliderValue + 3)

    def main_tab_clicked(self,index):
        if index == 3:
            #Panel_Data["width"] = MainWindow.geometry().width()
            #Panel_Data["height"] = MainWindow.geometry().height()
            if Panel_Data["first_run_flag"] == False:
                for i in range(1,5):
                    self.shelfset(i)
                    Panel_Data["mdi_1"+str(i)+"_flag"] = True

            Panel_Data["first_run_flag"] = True
    

    def Shelf_tab_clicked(self,index):
        Panel_Data["width"] = MainWindow.geometry().width()
        Panel_Data["height"] = MainWindow.geometry().height()

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
        ServiceTypes = ["E1", "STM_1_Electrical", "STM_1_Optical", "STM_4", "STM_16", "STM_64", "FE", "1GE", "10GE",
                           "40GE", "100GE"]

        SubHeaders = [["Quantity", "SLA"], ["Quantity", "SLA"], ["Quantity", "λ", "SLA"],
                  ["Quantity", "λ", "concat.", "SLA"], ["Quantity", "λ", "concat.", "SLA"],
                  ["Quantity", "λ", "concat.", "SLA"],
                  ["Quantity", "Granularity_xVC12", "Granularity_xVC4", "λ", "SLA"],
                  ["Quantity", "Granularity", "λ", "SLA"], ["Quantity", "Granularity", "λ", "SLA"],
                  ["Quantity", "Granularity", "λ", "SLA"], ["Quantity", "Granularity", "λ", "SLA"]]

        for Row in RowsNumber:
            id = Data["General"]["DataSection"]["0"][Row]
            Source = Data["General"]["DataSection"]["1"][Row]
            Destination = Data["General"]["DataSection"]["2"][Row]

            # TODO: find Type in Traffic Matrix
            Type = None
            i = 0
            ServiceDict = {}
            ServiceCount = 0
            for service in ServiceTypes:
                PropertyDict = {}
                for PropNum in range(0,len(SubHeaders[i])):
                    Prop = SubHeaders[i][PropNum]
                    if PropNum == 0:
                        ServiceCount += Data[service]["DataSection"][Prop][Row]
                        PropertyDict[Prop] = ServiceCount
                    else:
                        PropertyDict[Prop] = Data[service]["DataSection"][Prop][Row]
                i += 1
                ServiceDict[service] = PropertyDict
            self.network.TrafficMatrix.add_demand(id,Source,Destination,Type)

            self.FillDemandTabDataBase_Services(Source, Destination, ServiceDict)

            for service in list(ServiceDict.keys()):

                Sla = ServiceDict[service["SLA"]]

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
                    
    def FillDemandTabDataBase_Services(self, Source, Destination, ServiceDict):

        DemandTabDataBase["Services"][(Source,Destination)] = []
        for Service in ServiceDict.values():
            Quantity = ServiceDict[Service]
            item = str(Quantity) + " * " + str(Service)
            DemandTabDataBase["Services"][(Source,Destination)].append(item)

        DemandTabDataBase["Services"][(Source,Destination)] = DemandTabDataBase["Services"][(Destination,Source)]
            


    def PhysicalTopologyToObject(self):
        for NodeData in Data["Nodes"].values():
            self.network.PhysicalTopology.add_node(NodeData["Location"], NodeData["Type"])
        
        for LinkId , LinkData in Data["Links"]:
            self.network.PhysicalTopology.add_link(LinkId[0], LinkId[1], LinkData["NumSpan"])

            for i in range(LinkData["NumSpan"]):
                self.network.PhysicalTopology.LinkDict[(LinkId[0], LinkId[1])].put_fiber_Type(LinkId[0], LinkId[1],
                 LinkData["Length"][i], LinkData["Loss"][i], LinkData["Dispersion"][i], LinkData["Beta"][i], LinkData["Gamma"][i], 
                 i, LinkData["Snr"][i])
                




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
        added = []
        for id in list(Data["Links"].keys()):
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

        self.SelectNode_combo_fun()

    def shelfset(self,shelfnum):
        nodename = self.SelectNode_combo.currentText()
        print("nodename:",nodename)
        for i in range(1,15):
            setattr(self,"panel_1" + str(shelfnum) + str(i),QMdiSubWindow())
            Panel_Data["1"+str(shelfnum)+str(i)] = getattr(ui,"panel_1"+str(shelfnum)+str(i))
            Panel_Data["1"+str(shelfnum)+str(i)].setWindowFlag(Qt.FramelessWindowHint)
            Panel_Data["1"+str(shelfnum)+str(i)].setWidget(BLANK_panel("1"+str(shelfnum)+str(i), nodename))
            
            Panel_Data["mdi_1"+str(shelfnum)].addSubWindow(Panel_Data["1"+str(shelfnum)+str(i)])              

            Panel_Data["1"+str(shelfnum)+str(i)].show()


    # obsoleted 
    def shelf_1_rack_1(self):

        for i in range(1,15):
            setattr(self,"panel_11"+str(i),QMdiSubWindow())
            Panel_Data["11"+str(i)] = getattr(ui,"panel_11"+str(i))
            Panel_Data["11"+str(i)].setWindowFlag(Qt.FramelessWindowHint)
            Panel_Data["11"+str(i)].setWidget(BLANK_panel("11"+str(i)))
            
            Panel_Data["mdi_11"].addSubWindow(Panel_Data["11"+str(i)])              

            Panel_Data["11"+str(i)].show()
    
    


    



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

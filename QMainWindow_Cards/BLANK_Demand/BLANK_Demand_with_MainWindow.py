from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import sys
import os

'''from data import *
from MP2X_Demand.MP2X_L_Demand import MP2X_L_Demand
from MP2X_Demand.MP2X_R_Demand import MP2X_R_Demand
from MP1H_Demand.MP1H_L_Demand import MP1H_L_Demand
from MP1H_Demand.MP1H_R_Demand import MP1H_R_Demand
from TP1H_Demand.TP1H_L_Demand import TP1H_L_Demand
from TP1H_Demand.TP1H_R_Demand import TP1H_R_Demand
from BLANK_Demand import BLANK_SOURCE'''
import BLANK_SOURCE

class BLANK_Demand(QtWidgets.QMainWindow):

    def __init__(self, Panel_ID, nodename, Destination):
        super(BLANK_Demand, self).__init__()

        self.setEnabled(False)
        self.resize(178, 705)
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.setIconSize(QtCore.QSize(0, 0))
        self.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setStyleSheet("border: 4px solid black;\n" 
"")
        self.horizontalLayout.addWidget(self.widget)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setStyleSheet("border-image: url(:/BLANK_DEMAND_SOURCE/BLANK.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.horizontalLayout.addWidget(self.widget)
        self.setCentralWidget(self.centralwidget)

        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        
        #TODO: update this
        DoublePanels = ["MP2D","MP2X","TPAX","MPBD","MPAD","RG1H", "MP1H", "TP1H"]

        model = QStandardItemModel()
        model.dropMimeData(event.mimeData(), Qt.CopyAction, 0,0, QModelIndex())
        text = model.item(0,0).text()

        if DoublePanels.count(text) != 0:
            #if Data["Nodes"][self.nodename]["Panels"].get(uppernum,0) == 0:
            if DemandTabDataBase["Panels"][self.nodename].get(self.uppernum, 0) == 0:
                event.accept()
        else:
            event.accept()

        
        super(BLANK_Demand,self).dragEnterEvent(event)

    def dragMoveEvent(self, event):
        event.accept()
        super(BLANK_Demand,self).dragMoveEvent(event)

    def dropEvent(self, event):
        event.accept()
        model = QStandardItemModel()
        model.dropMimeData(event.mimeData(), Qt.CopyAction, 0,0, QModelIndex())
        text = model.item(0,0).text()
        #self.label.setText(text)

        # TODO: Take Care of this very soon

        if text == "SC":
            #Data["DemandPanel_" + str(self.id)].setWidget(SC_Demand(self.id, self.nodename))
            DemandTabDataBase["Panels"][self.nodename][self.id] = SC()
        elif text == "MP2X":
            Data["DemandPanel_" + str(self.id)].setWidget(MP2X_L_Demand(self.id , self.nodename, self.Destination))
            DemandTabDataBase["Panels"][self.nodename][self.id] = MP2X_L()

            Data["DemandPanel_" + self.uppernum].setWidget(MP2X_R_Demand(self.id, self.nodename))
            DemandTabDataBase["Panels"][self.nodename][self.uppernum] = MP2X_R(self.uppernum, self.Destination)


        elif text == "MP1H":
            Data["DemandPanel_" + str(self.id)].setWidget(MP1H_L_Demand(self.id , self.nodename, self.Destination))
            DemandTabDataBase["Panels"][self.nodename][self.id] = MP1H_L()

            Data["DemandPanel_" + self.uppernum].setWidget(MP1H_R_Demand(self.id, self.nodename))
            DemandTabDataBase["Panels"][self.nodename][self.uppernum] = MP1H_R(self.uppernum, self.Destination)
        
        elif text == "TP1H":
            Data["DemandPanel_" + str(self.id)].setWidget(TP1H_L_Demand(self.id , self.nodename, self.Destination))
            DemandTabDataBase["Panels"][self.nodename][self.id] = TP1H_L()

            Data["DemandPanel_" + self.uppernum].setWidget(TP1H_R_Demand(self.id, self.nodename))
            DemandTabDataBase["Panels"][self.nodename][self.uppernum] = TP1H_R(self.uppernum, self.Destination)
        
        super(BLANK_Demand, self).dropEvent(event)



if __name__ == "__main__":

    app = QtWidgets.QApplication([])
    window = BLANK_Demand(1,2,3)
    window.show()
    sys.exit(app.exec_())

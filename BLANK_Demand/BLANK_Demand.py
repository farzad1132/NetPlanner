from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import sys
import os

from data import *
from MP2X_Demand.MP2X_L_Demand import MP2X_L_Demand
from MP2X_Demand.MP2X_R_Demand import MP2X_R_Demand
from MP1H_Demand.MP1H_L_Demand import MP1H_L_Demand
from MP1H_Demand.MP1H_R_Demand import MP1H_R_Demand
from TP1H_Demand.TP1H_L_Demand import TP1H_L_Demand
from TP1H_Demand.TP1H_R_Demand import TP1H_R_Demand

class BLANK_Demand(QWidget):

    def __init__(self, Panel_ID, nodename, Destination):
        super(BLANK_Demand, self).__init__()

        self.resize(164, 577)

        self.id = str(Panel_ID)
        # nodename == Source in Demand Tab
        self.nodename = nodename
        self.Destination = Destination
        self.uppernum = str(int(self.id) + 1)

    
        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QLabel(self)
        self.horizontalLayout.setMargin(0)
        self.label.setStyleSheet("border-image: url(:/BLANK.png);" )
        self.setStyleSheet("border: 10px solid black;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        

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

    app = QApplication([])
    window = BLANK_Demand(1,2,3)
    window.show()
    sys.exit(app.exec_())

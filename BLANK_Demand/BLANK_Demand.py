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
from BLANK_Demand import BLANK_SOURCE

class BLANK_Demand(QtWidgets.QWidget):

    def __init__(self, Panel_ID, nodename, Destination):
        super(BLANK_Demand, self).__init__()

        #self.resize(159, 639)

        self.id = str(Panel_ID)
        # nodename == Source in Demand Tab
        self.nodename = nodename
        self.Destination = Destination
        self.uppernum = str(int(self.id) + 1)

        self.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.BLANK_Demand_1 = QtWidgets.QLabel(self)
        self.BLANK_Demand_1.setStyleSheet("border-image: url(:/BLANK_DEMAND_SOURCE/BLANK.png);")
        self.horizontalLayout.addWidget(self.BLANK_Demand_1)
        self.BLANK_Demand_1.setText("")
        self.BLANK_Demand_1.setObjectName("BLANK_Demand_1")

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

        # removing old panel ( left only )
        panel_widget = Data["DemandPanel_" + str(self.id)].takeAt(0).widget()
        self.horizontalLayout.removeWidget(panel_widget)
        panel_widget.deleteLater()

        # getting dual panels id
        DualPanelsId = self.generate_dual_panel_num(self.Destination)


        if text == "SC":
            #Data["DemandPanel_" + str(self.id)].addWidget(SC_Demand(self.id, self.nodename))
            DemandTabDataBase["Panels"][self.nodename][self.id] = SC()
        elif text == "MP2X":
            Data["DemandPanel_" + str(self.id)].addWidget(MP2X_L_Demand(self.id , self.nodename, self.Destination))
            DemandTabDataBase["Panels"][self.nodename][self.id] = MP2X_L(Destination= self.Destination)

            # removing old right panel
            panel_widget = Data["DemandPanel_" + str(self.uppernum)].takeAt(0).widget()
            Data["ui"].horizontalLayout.removeWidget(panel_widget)
            panel_widget.deleteLater()

            Data["DemandPanel_" + self.uppernum].addWidget(MP2X_R_Demand(self.id, self.nodename, self.Destination))
            DemandTabDataBase["Panels"][self.nodename][self.uppernum] = MP2X_R(self.uppernum, self.Destination)


        elif text == "MP1H":
            Data["DemandPanel_" + str(self.id)].addWidget(MP1H_L_Demand(self.id , self.nodename, self.Destination))
            DemandTabDataBase["Panels"][self.nodename][self.id] = MP1H_L(Destination= self.Destination)

            # removing old right panel
            panel_widget = Data["DemandPanel_" + str(self.uppernum)].takeAt(0).widget()
            Data["ui"].horizontalLayout.removeWidget(panel_widget)
            panel_widget.deleteLater()

            Data["DemandPanel_" + self.uppernum].addWidget(MP1H_R_Demand(self.id, self.nodename, self.Destination))
            DemandTabDataBase["Panels"][self.nodename][self.uppernum] = MP1H_R(self.uppernum, self.Destination)
        
        elif text == "TP1H":
            Data["DemandPanel_" + str(self.id)].addWidget(TP1H_L_Demand(self.id , self.nodename, self.Destination, DualPanelsId))
            DemandTabDataBase["Panels"][self.nodename][self.id] = TP1H_L(Destination= self.Destination, DualPanelsId= DualPanelsId)

            # ** Dual **
            #Data["DemandPanel_" + DualPanelsId[0]].addWidget(TP1H_L_Demand(DualPanelsId[0] , self.Destination, self.nodename, (self.id, self.uppernum)))
            DemandTabDataBase["Panels"][self.Destination][DualPanelsId[0]] = TP1H_L(Destination= self.nodename, DualPanelsId= (self.id, self.uppernum))

            # removing old right panel
            panel_widget = Data["DemandPanel_" + str(self.uppernum)].takeAt(0).widget()
            Data["ui"].horizontalLayout.removeWidget(panel_widget)
            panel_widget.deleteLater()


            Data["DemandPanel_" + self.uppernum].addWidget(TP1H_R_Demand(self.id, self.nodename, self.Destination, DualPanelsId))
            DemandTabDataBase["Panels"][self.nodename][self.uppernum] = TP1H_R(self.uppernum, self.Destination, DualPanelsId)

            # ** Dual **
            #Data["DemandPanel_" + DualPanelsId[1]].addWidget(TP1H_R_Demand(DualPanelsId[1], self.Destination, self.nodename))
            DemandTabDataBase["Panels"][self.Destination][DualPanelsId[1]] = TP1H_R(DualPanelsId[1], self.nodename, DualPanelsId)
        
        super(BLANK_Demand, self).dropEvent(event)

    
    def generate_dual_panel_num(self, Destination):

        IdList = list(DemandTabDataBase["Panels"][Destination].keys())
            
        # if shelf is empty this method must return 1 in ## string ##
        if not IdList:
            return ("1", "2")
        IdList = list(map(lambda x : int(x), IdList))
        MaxId = max(IdList)
        return (str(MaxId + 1), str(MaxId + 2))



if __name__ == "__main__":

    app = QtWidgets.QApplication([])
    window = BLANK_Demand(1,2,3)
    window.show()
    sys.exit(app.exec_())

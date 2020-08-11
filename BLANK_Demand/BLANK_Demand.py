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

class BLANK_Demand(QtWidgets.QMainWindow):

    def __init__(self, Panel_ID, nodename, Destination, Panels):
        super(BLANK_Demand, self).__init__()

        #self.resize(159, 639)

        self.id = str(Panel_ID)
        # nodename == Source in Demand Tab
        self.nodename = nodename
        self.Destination = Destination
        self.uppernum = str(int(self.id) + 1)
        self.Panels = Panels

        #self.setEnabled(False)
        #self.resize(178, 705)
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.setIconSize(QtCore.QSize(0, 0))
        self.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setStyleSheet("border: 2px solid black;\n" 
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
        AcceptedPanels = ["MP2X", "MP1H", "TP1H"]

        

        
        #TODO: update this
        DoublePanels = ["MP2D","MP2X","TPAX","MPBD","MPAD","RG1H", "MP1H", "TP1H"]

        model = QStandardItemModel()
        model.dropMimeData(event.mimeData(), Qt.CopyAction, 0,0, QModelIndex())
        text = model.item(0,0).text()

        if text in AcceptedPanels:
            # updateing Destination
            self.Destination = Data["ui"].Demand_Destination_combobox.currentText()

            # checking if next (right) slot if free or not
            if text in DoublePanels:
                panel = self.Panels.PanelsObjectDict.get(self.uppernum)
                if isinstance(panel, self.Panels.BLANK) or panel is None:
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


        self.Panels.add_widget(self.id, self.nodename, self.Destination, text)
        
        super(BLANK_Demand, self).dropEvent(event)



if __name__ == "__main__":

    app = QtWidgets.QApplication([])
    window = BLANK_Demand(1,2,3,4)
    window.show()
    sys.exit(app.exec_())

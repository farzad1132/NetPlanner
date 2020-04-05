from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import sys
import os

from data import *
from MP2X_Demand import MP2X_R_SOURCE

class MP2X_R_Demand(QtWidgets.QWidget):

    def __init__(self, Panel_ID, nodename, Destination):
        super(MP2X_R_Demand, self).__init__()

        self.resize(114, 703)

        self.id = str(Panel_ID)
        # nodename == Source in Demand Tab
        self.nodename = nodename
        self.Destination = Destination
        self.uppernum = str(int(self.id) + 1)

        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.MP2X_R_D = QtWidgets.QLabel(self)
        self.MP2X_R_D.setStyleSheet("image: url(:/MP2X_R_SOURCE/MP2X_R_Demand.png);")
        self.MP2X_R_D.setText("")
        self.MP2X_R_D.setObjectName("MP2X_R_D")
        self.horizontalLayout.addWidget(self.MP2X_R_D)

if __name__ == "__main__":
    
    app = QtWidgets.QApplication([])
    window = MP2X_R_Demand(1,2,3)
    window.show()
    sys.exit(app.exec_())

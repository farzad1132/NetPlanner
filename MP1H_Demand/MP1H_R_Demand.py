from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import sys
import os

from data import *
from MP1H_Demand import MP1H_R_SOURCE

class MP1H_R_Demand(QtWidgets.QWidget):

    def __init__(self, Panel_ID, nodename, Destination, DualPanelsId):
        super(MP1H_R_Demand, self).__init__()

        self.resize(94, 455)

        self.id = str(Panel_ID)
        # nodename == Source in Demand Tab
        self.nodename = nodename
        self.Destination = Destination
        self.uppernum = str(int(self.id) + 1)

        self.DualPanelsId = DualPanelsId

        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.MP1H_R_D = QtWidgets.QLabel(self)
        self.MP1H_R_D.setStyleSheet("image: url(:/MP1H_R_SOURCE/MP1H_R_Demand.png);")
        self.MP1H_R_D.setText("")
        self.MP1H_R_D.setObjectName("MP1H_R_D")
        self.horizontalLayout.addWidget(self.MP1H_R_D)


if __name__ == "__main__":

    app = QtWidgets.QApplication([])
    window = MP1H_R_Demand(1,2,3)
    window.show()
    sys.exit(app.exec_())

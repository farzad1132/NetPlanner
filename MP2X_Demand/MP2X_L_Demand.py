from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import sys
import os

from data import *
from Common_Object_def import *
from MP2X_Demand import CLIENT_L
from MP2X_Demand import CLIENT_R
from MP2X_Demand import LINE_L
from MP2X_Demand import LINE_R
from MP2X_Demand import MP2X_Title
from MP2X_Demand import Socket_bottom
from MP2X_Demand import Socket_top
from MP2X_Demand import CLIENT_L_Selected
from MP2X_Demand import CLIENT_R_Selected

# USE THIS CODE TO CHANGE THE CLIENT TO SELECTED CLIENT:
#1)
# For left clients:
# self.Client(number of client).setStyleSheet("image: url(:/CLIENT_L_Selected_SOURCE/CLIENT_L_Selected.png);")
#2)
# For left clients:
# self.Client(number of client).setStyleSheet("image: url(:/CLIENT_R_Selected_SOURCE/CLIENT_R_Selected.png);")

class MP2X_L_Demand(QtWidgets.QWidget):

    def __init__(self, Panel_ID, nodename, Destination):
        super(MP2X_L_Demand, self).__init__()

        self.resize(106, 694)

        self.id = str(Panel_ID)
        # nodename == Source in Demand Tab
        self.nodename = nodename
        self.Destination = Destination
        self.uppernum = str(int(self.id) + 1)

        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setContentsMargins(5, 9, 5, 5)
        self.gridLayout.setObjectName("gridLayout")
        self.LINE1 = QtWidgets.QLabel(self)
        self.LINE1.setStyleSheet("image: url(:/Line_L_SOURCE/LINE_L.png);")
        self.LINE1.setText("")
        self.LINE1.setObjectName("LINE1")
        self.gridLayout.addWidget(self.LINE1, 3, 0, 1, 1)
        self.LINE2 = QtWidgets.QLabel(self)
        self.LINE2.setStyleSheet("image: url(:/Line_R_SOURCE/LINE_R.png);")
        self.LINE2.setText("")
        self.LINE2.setObjectName("LINE2")
        self.gridLayout.addWidget(self.LINE2, 3, 1, 1, 1)
        self.CLIENT11 = QtWidgets.QLabel(self)
        self.CLIENT11.setStyleSheet("image: url(:/Client_L_Source/CLIENT_L.png);")
        self.CLIENT11.setText("")
        self.CLIENT11.setObjectName("CLIENT11")
        self.gridLayout.addWidget(self.CLIENT11, 9, 0, 1, 1)
        self.CLIENT1 = QtWidgets.QLabel(self)
        self.CLIENT1.setStyleSheet("image: url(:/Client_L_Source/CLIENT_L.png);")
        self.CLIENT1.setText("")
        self.CLIENT1.setObjectName("CLIENT1")
        self.gridLayout.addWidget(self.CLIENT1, 4, 0, 1, 1)
        self.Socket_bottom = QtWidgets.QLabel(self)
        self.Socket_bottom.setStyleSheet("image: url(:/Socket_bottom_Source/Socket_bottom.png);")
        self.Socket_bottom.setText("")
        self.Socket_bottom.setObjectName("Socket_bottom")
        self.gridLayout.addWidget(self.Socket_bottom, 14, 0, 1, 1)
        self.CLIENT3 = QtWidgets.QLabel(self)
        self.CLIENT3.setStyleSheet("image: url(:/Client_L_Source/CLIENT_L.png);")
        self.CLIENT3.setText("")
        self.CLIENT3.setObjectName("CLIENT3")
        self.gridLayout.addWidget(self.CLIENT3, 5, 0, 1, 1)
        self.MP2X_Title = QtWidgets.QLabel(self)
        self.MP2X_Title.setStyleSheet("image: url(:/MP2X_Title_Source/MP2X_Title.png);")
        self.MP2X_Title.setText("")
        self.MP2X_Title.setObjectName("MP2X_Title")
        self.gridLayout.addWidget(self.MP2X_Title, 1, 2, 2, 1)
        self.CLIENT10 = QtWidgets.QLabel(self)
        self.CLIENT10.setStyleSheet("image: url(:/Client_R_Source/CLIENT_R.png);")
        self.CLIENT10.setText("")
        self.CLIENT10.setObjectName("CLIENT10")
        self.gridLayout.addWidget(self.CLIENT10, 8, 1, 1, 1)
        self.CLIENT15 = QtWidgets.QLabel(self)
        self.CLIENT15.setStyleSheet("image: url(:/Client_L_Source/CLIENT_L.png);")
        self.CLIENT15.setText("")
        self.CLIENT15.setObjectName("CLIENT15")
        self.gridLayout.addWidget(self.CLIENT15, 11, 0, 1, 1)
        self.CLIENT14 = QtWidgets.QLabel(self)
        self.CLIENT14.setStyleSheet("image: url(:/Client_R_Source/CLIENT_R.png);")
        self.CLIENT14.setText("")
        self.CLIENT14.setObjectName("CLIENT14")
        self.gridLayout.addWidget(self.CLIENT14, 10, 1, 1, 1)
        self.CLIENT12 = QtWidgets.QLabel(self)
        self.CLIENT12.setStyleSheet("image: url(:/Client_R_Source/CLIENT_R.png);")
        self.CLIENT12.setText("")
        self.CLIENT12.setObjectName("CLIENT12")
        self.gridLayout.addWidget(self.CLIENT12, 9, 1, 1, 1)
        self.CLIENT13 = QtWidgets.QLabel(self)
        self.CLIENT13.setStyleSheet("image: url(:/Client_L_Source/CLIENT_L.png);")
        self.CLIENT13.setText("")
        self.CLIENT13.setObjectName("CLIENT13")
        self.gridLayout.addWidget(self.CLIENT13, 10, 0, 1, 1)
        self.CLIENT4 = QtWidgets.QLabel(self)
        self.CLIENT4.setStyleSheet("image: url(:/Client_R_Source/CLIENT_R.png);")
        self.CLIENT4.setText("")
        self.CLIENT4.setObjectName("CLIENT4")
        self.gridLayout.addWidget(self.CLIENT4, 5, 1, 1, 1)
        self.CLIENT6 = QtWidgets.QLabel(self)
        self.CLIENT6.setStyleSheet("image: url(:/Client_R_Source/CLIENT_R.png);")
        self.CLIENT6.setText("")
        self.CLIENT6.setObjectName("CLIENT6")
        self.gridLayout.addWidget(self.CLIENT6, 6, 1, 1, 1)
        self.Not_used = QtWidgets.QLabel(self)
        self.Not_used.setText("")
        self.Not_used.setObjectName("Not_used")
        self.gridLayout.addWidget(self.Not_used, 12, 0, 1, 1)
        self.CLIENT8 = QtWidgets.QLabel(self)
        self.CLIENT8.setStyleSheet("image: url(:/Client_R_Source/CLIENT_R.png);")
        self.CLIENT8.setText("")
        self.CLIENT8.setObjectName("CLIENT8")
        self.gridLayout.addWidget(self.CLIENT8, 7, 1, 1, 1)
        self.CLIENT16 = QtWidgets.QLabel(self)
        self.CLIENT16.setStyleSheet("image: url(:/Client_R_Source/CLIENT_R.png);")
        self.CLIENT16.setText("")
        self.CLIENT16.setObjectName("CLIENT16")
        self.gridLayout.addWidget(self.CLIENT16, 11, 1, 1, 1)
        self.CLIENT7 = QtWidgets.QLabel(self)
        self.CLIENT7.setStyleSheet("image: url(:/Client_L_Source/CLIENT_L.png);")
        self.CLIENT7.setText("")
        self.CLIENT7.setObjectName("CLIENT7")
        self.gridLayout.addWidget(self.CLIENT7, 7, 0, 1, 1)
        self.CLIENT5 = QtWidgets.QLabel(self)
        self.CLIENT5.setStyleSheet("image: url(:/Client_L_Source/CLIENT_L.png);")
        self.CLIENT5.setText("")
        self.CLIENT5.setObjectName("CLIENT5")
        self.gridLayout.addWidget(self.CLIENT5, 6, 0, 1, 1)
        self.CLIENT9 = QtWidgets.QLabel(self)
        self.CLIENT9.setStyleSheet("image: url(:/Client_L_Source/CLIENT_L.png);")
        self.CLIENT9.setText("")
        self.CLIENT9.setObjectName("CLIENT9")
        self.gridLayout.addWidget(self.CLIENT9, 8, 0, 1, 1)
        self.CLIENT2 = QtWidgets.QLabel(self)
        self.CLIENT2.setStyleSheet("image: url(:/Client_R_Source/CLIENT_R.png);")
        self.CLIENT2.setText("")
        self.CLIENT2.setObjectName("CLIENT2")
        self.gridLayout.addWidget(self.CLIENT2, 4, 1, 1, 1)
        self.Socket_Top = QtWidgets.QLabel(self)
        self.Socket_Top.setStyleSheet("image: url(:/Socket_Top_Source/Socket_top.png);")
        self.Socket_Top.setText("")
        self.Socket_Top.setObjectName("Socket_Top")
        self.gridLayout.addWidget(self.Socket_Top, 1, 0, 1, 1)


if __name__ == "__main__":
    
    app = QtWidgets.QApplication([])
    window = MP2X_L_Demand(1,2,3)
    window.show()
    sys.exit(app.exec_())

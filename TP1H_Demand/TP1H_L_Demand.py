from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import sys
import os

from data import *
from Common_Object_def import Network
from TP1H_Demand import Client
from TP1H_Demand import Line
from TP1H_Demand import Socket_bottom
from TP1H_Demand import Socket
from TP1H_Demand import TP1H_R
from TP1H_Demand import title

class TP1H_L_Demand(QtWidgets.QWidget):

    def __init__(self, Panel_ID, nodename, Destination):
        super(TP1H_L_Demand, self).__init__()

        self.resize(94, 511)

        self.id = str(Panel_ID)
        # nodename == Source in Demand Tab
        self.nodename = nodename
        self.Destination = Destination
        self.uppernum = str(int(self.id) + 1)

        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setObjectName("gridLayout")
        self.Line = QtWidgets.QLabel(self)
        self.Line.setMinimumSize(QtCore.QSize(0, 25))
        self.Line.setMaximumSize(QtCore.QSize(100, 200))
        self.Line.setStyleSheet("image: url(:/Line/tp1h_line.png);")
        self.Line.setText("")
        self.Line.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Line.setObjectName("Line")
        self.gridLayout.addWidget(self.Line, 1, 0, 3, 1)
        self.not_used_1 = QtWidgets.QLabel(self)
        self.not_used_1.setMaximumSize(QtCore.QSize(16777215, 20))
        self.not_used_1.setText("")
        self.not_used_1.setObjectName("not_used_1")
        self.gridLayout.addWidget(self.not_used_1, 4, 0, 1, 1)
        self.Socket_Top = QtWidgets.QLabel(self)
        self.Socket_Top.setStyleSheet("image: url(:/Socket/socket1.png);")
        self.Socket_Top.setText("")
        self.Socket_Top.setObjectName("Socket_Top")
        self.gridLayout.addWidget(self.Socket_Top, 0, 0, 1, 1)
        self.Socket_Bottom = QtWidgets.QLabel(self)
        self.Socket_Bottom.setStyleSheet("image: url(:/Socket_bottom/socket2.png);")
        self.Socket_Bottom.setText("")
        self.Socket_Bottom.setObjectName("Socket_Bottom")
        self.gridLayout.addWidget(self.Socket_Bottom, 7, 0, 1, 1)
        self.Client = QtWidgets.QLabel(self)
        self.Client.setMinimumSize(QtCore.QSize(0, 25))
        self.Client.setStyleSheet("image: url(:/Client/TP1H_CLIENT.png);")
        self.Client.setText("")
        self.Client.setObjectName("Client")
        self.gridLayout.addWidget(self.Client, 5, 0, 2, 1)
        self.Line_Title = QtWidgets.QLabel(self)
        self.Line_Title.setObjectName("Line_Title")
        self.gridLayout.addWidget(self.Line_Title, 2, 2, 1, 1)
        self.Client_Title = QtWidgets.QLabel(self)
        self.Client_Title.setObjectName("Client_Title")
        self.gridLayout.addWidget(self.Client_Title, 5, 2, 2, 1)
        self.TP1H_Title = QtWidgets.QLabel(self)
        self.TP1H_Title.setMaximumSize(QtCore.QSize(35, 16777215))
        self.TP1H_Title.setStyleSheet("image: url(:/title/title.png);")
        self.TP1H_Title.setText("")
        self.TP1H_Title.setObjectName("TP1H_Title")
        self.gridLayout.addWidget(self.TP1H_Title, 0, 2, 2, 1)

if __name__ == "__main__":

    app = QtWidgets.QApplication([])
    window = TP1H_L_Demand(1,2,3)
    window.show()
    sys.exit(app.exec_())

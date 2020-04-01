from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import sys
import os

from data import *
from Common_Object_def import Network
from MP1H_Demand import CLIENT_R
from MP1H_Demand import MP1H_Title
from MP1H_Demand import Socket_bottom
from MP1H_Demand import Socket_top
from MP1H_Demand import client
from MP1H_Demand import line

class MP1H_L_Demand(QtWidgets.QWidget):

    def __init__(self, Panel_ID, nodename, Destination):
        super(MP1H_L_Demand, self).__init__()

        self.resize(118, 633)

        self.id = str(Panel_ID)
        # nodename == Source in Demand Tab
        self.nodename = nodename
        self.Destination = Destination
        self.uppernum = str(int(self.id) + 1)

        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setObjectName("gridLayout")
        self.Client8 = QtWidgets.QLabel(self)
        self.Client8.setStyleSheet("image: url(:/client_r/CLIENT_R.png);")
        self.Client8.setText("")
        self.Client8.setObjectName("Client8")
        self.gridLayout.addWidget(self.Client8, 5, 1, 1, 1)
        self.Client5 = QtWidgets.QLabel(self)
        self.Client5.setStyleSheet("image: url(:/CLIENT_L1/CLIENT_L.png);")
        self.Client5.setText("")
        self.Client5.setObjectName("Client5")
        self.gridLayout.addWidget(self.Client5, 4, 0, 1, 1)
        self.Client7 = QtWidgets.QLabel(self)
        self.Client7.setStyleSheet("image: url(:/CLIENT_L1/CLIENT_L.png);")
        self.Client7.setText("")
        self.Client7.setObjectName("Client7")
        self.gridLayout.addWidget(self.Client7, 5, 0, 1, 1)
        self.Line = QtWidgets.QLabel(self)
        self.Line.setMinimumSize(QtCore.QSize(0, 100))
        self.Line.setStyleSheet("image: url(:/line/line.png);")
        self.Line.setText("")
        self.Line.setObjectName("Line")
        self.gridLayout.addWidget(self.Line, 7, 0, 1, 1)
        self.Socket_Top = QtWidgets.QLabel(self)
        self.Socket_Top.setMaximumSize(QtCore.QSize(16777215, 50))
        self.Socket_Top.setStyleSheet("image: url(:/Socket_top/Socket_top.png);")
        self.Socket_Top.setText("")
        self.Socket_Top.setObjectName("Socket_Top")
        self.gridLayout.addWidget(self.Socket_Top, 1, 0, 1, 1)
        self.Client1 = QtWidgets.QLabel(self)
        self.Client1.setStyleSheet("image: url(:/CLIENT_L1/CLIENT_L.png);")
        self.Client1.setText("")
        self.Client1.setObjectName("Client1")
        self.gridLayout.addWidget(self.Client1, 2, 0, 1, 1)
        self.Client6 = QtWidgets.QLabel(self)
        self.Client6.setStyleSheet("image: url(:/client_r/CLIENT_R.png);")
        self.Client6.setText("")
        self.Client6.setObjectName("Client6")
        self.gridLayout.addWidget(self.Client6, 4, 1, 1, 1)
        self.Client4 = QtWidgets.QLabel(self)
        self.Client4.setStyleSheet("image: url(:/client_r/CLIENT_R.png);")
        self.Client4.setText("")
        self.Client4.setObjectName("Client4")
        self.gridLayout.addWidget(self.Client4, 3, 1, 1, 1)
        self.Socket_Bottom = QtWidgets.QLabel(self)
        self.Socket_Bottom.setMaximumSize(QtCore.QSize(16777215, 50))
        self.Socket_Bottom.setStyleSheet("image: url(:/Socket_Bottom/Socket_bottom.png);")
        self.Socket_Bottom.setText("")
        self.Socket_Bottom.setObjectName("Socket_Bottom")
        self.gridLayout.addWidget(self.Socket_Bottom, 8, 0, 1, 1)
        self.Client10 = QtWidgets.QLabel(self)
        self.Client10.setStyleSheet("image: url(:/client_r/CLIENT_R.png);")
        self.Client10.setText("")
        self.Client10.setObjectName("Client10")
        self.gridLayout.addWidget(self.Client10, 6, 1, 1, 1)
        self.Client2 = QtWidgets.QLabel(self)
        self.Client2.setStyleSheet("image: url(:/client_r/CLIENT_R.png);")
        self.Client2.setText("")
        self.Client2.setObjectName("Client2")
        self.gridLayout.addWidget(self.Client2, 2, 1, 1, 1)
        self.Client9 = QtWidgets.QLabel(self)
        self.Client9.setStyleSheet("image: url(:/CLIENT_L1/CLIENT_L.png);")
        self.Client9.setText("")
        self.Client9.setObjectName("Client9")
        self.gridLayout.addWidget(self.Client9, 6, 0, 1, 1)
        self.Client3 = QtWidgets.QLabel(self)
        self.Client3.setStyleSheet("image: url(:/CLIENT_L1/CLIENT_L.png);")
        self.Client3.setText("")
        self.Client3.setObjectName("Client3")
        self.gridLayout.addWidget(self.Client3, 3, 0, 1, 1)
        self.MP1H_Title = QtWidgets.QLabel(self)
        self.MP1H_Title.setStyleSheet("image: url(:/title/MP1H_title.png);")
        self.MP1H_Title.setText("")
        self.MP1H_Title.setObjectName("MP1H_Title")
        self.gridLayout.addWidget(self.MP1H_Title, 1, 2, 2, 1)


if __name__ == "__main__":

    app = QtWidgets.QApplication([])
    window = MP1H_L_Demand(1,2,3)
    window.show()
    sys.exit(app.exec_())

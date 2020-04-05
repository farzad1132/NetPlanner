from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import sys
import os
from data import *


class TP1H_L_Grooming(QWidget):

    def __init__(self,Panel_ID,nodename):

        self.id = Panel_ID
        self.nodename = nodename

        super(TP1H_L_Grooming, self).__init__()
        self.setFixedSize(109, 810)

        self.title = QLabel(self)
        self.title.setGeometry(QRect(60, 60, 55, 131))
        self.title.setText("")
        self.title.setPixmap(QPixmap(os.path.join("TP1H_Grooming", "title.png")))
        self.title.setObjectName("title") 

        self.client = QLabel(self)
        self.client.setGeometry(QRect(30, 450, 55, 241))
        self.client.setText("")
        self.client.setPixmap(QPixmap(os.path.join("TP1H_Grooming", "TP1H_CLIENT.png")))
        self.client.setObjectName("client") 

        self.upper_socket = QLabel(self)
        self.upper_socket.setGeometry(QRect(10, -10, 55, 61))
        self.upper_socket.setText("")
        self.upper_socket.setPixmap(QPixmap(os.path.join("TP1H_Grooming", "socket1.png")))
        self.upper_socket.setObjectName("upper_socket") 

        self.line = QLabel(self)
        self.line.setGeometry(QRect(30, 220, 55, 231))
        self.line.setText("")
        self.line.setPixmap(QPixmap(os.path.join("TP1H_Grooming", "tp1h_line.png")))
        self.line.setObjectName("line") 

        self.socket = QLabel(self)
        self.socket.setGeometry(QRect(10, 760, 55, 61))
        self.socket.setText("")
        self.socket.setPixmap(QPixmap(os.path.join("TP1H_Grooming", "socket2.png")))
        self.socket.setObjectName("socket")

        self.retranslateUi()
        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))

class customlabel(QLabel):
    def __init__(self, parent, nodename, ID):
        super().__init__(parent)
        self.nodename = nodename
        self.id = ID
        self.text = text
        self.setAcceptDrops(True)
    
    def dragEnterEvent(self, event):
        e = event.mimeData()
        model = QStandardItemModel()
        model.dropMimeData(event.mimeData(), Qt.CopyAction, 0,0, QModelIndex())
        dragtext = model.item(0,0).text()
        print(dragtext)
        servicetype = dragtext.split("*")[1]
        servicetype = servicetype.strip()
        if servicetype == "100GE":
            self.setPixmap(QPixmap(os.path.join("MP2D_panel", "client_green.png")))
            #self.line.setPixmap(self.setPixmap(QPixmap(os.path.join("MP2D_panel", "line_green.png"))))
            
        else:
            self.setPixmap(QPixmap(os.path.join("MP2D_panel", "client_red.png")))
        event.accept()

        super(customlabel,self).dragEnterEvent(event)
    

    def dragLeaveEvent(self, event):
        self.setPixmap(QPixmap(os.path.join("MP2D_panel", "client.png")))

    def dropEvent(self, event):
        event.accept()
        e = event.mimeData()
        model = QStandardItemModel()
        model.dropMimeData(event.mimeData(), Qt.CopyAction, 0,0, QModelIndex())
        dragtext = model.item(0,0).text()
        servicetype = dragtext.split("*")[1]
        servicetype = servicetype.strip()
        if servicetype == "100GE":
            Data["Nodes"][self.nodename]["Panels"][self.id]["Sockets"][self.text] = "green"
            Data["Nodes"][self.nodename]["Panels"][self.id]["Sockets"]["Line"] += 1
            self.countdown_fun(self.nodename,"100GE",-1)
            if Data["Nodes"][self.nodename]["Panels"][self.id]["Sockets"]["Line"] == 2:
                self.modify_linelist(self.nodename,+1)
                # TODO: doing sth with line socket ( changing its color to green )
                Data[self.id].widget().label_line.setPixmap(QPixmap(os.path.join("MP2D_panel", "line_green.png")))

            # TODO: be Careful !!!!!
            self.setAcceptDrops(False)  
        else:
            #Data["Nodes"][self.nodename]["Panels"][self.id]["Sockets"][self.text] = "red"
            self.setPixmap(QPixmap(os.path.join("MP2D_panel", "client.png")))
            # TODO: changing color

    def contextMenuEvent(self, event):
        ContextMenu = QMenu(self)
        ClearAction = ContextMenu.addAction("..Clear Socket..")
        
        action = ContextMenu.exec_(self.mapToGlobal(event.pos()))

        if action == ClearAction:
            if Data["Nodes"][self.nodename]["Panels"][self.id]["Sockets"][self.text] == "green":
                self.setPixmap(QPixmap(os.path.join("MP2D_panel", "client.png")))
                Data["Nodes"][self.nodename]["Panels"][self.id]["Sockets"][self.text] = None
                Data["Nodes"][self.nodename]["Panels"][self.id]["Sockets"]["Line"] -= 1
                self.countdown_fun(self.nodename,"100GE",1)
                self.setAcceptDrops(True)
                if Data["Nodes"][self.nodename]["Panels"][self.id]["Sockets"]["Line"] == 1:
                    self.modify_linelist(self.nodename,-1)
                    # TODO: doing sth with line socket ( changing its color to default )
                    Data[self.id].widget().label_line.setPixmap(QPixmap(os.path.join("MP2D_panel", "line.png")))
                    

            elif Data["Nodes"][self.nodename]["Panels"][self.id]["Sockets"][self.text] == "red":
                Data["Nodes"][self.nodename]["Panels"][self.id]["Sockets"][self.text] = None
                self.setPixmap(QPixmap(os.path.join("MP2D_panel", "client.png")))

    def countdown_fun(self,nodename,header,value):
        degree = self.id[1]
        Data["Nodes"][nodename]["Client_Services"]["data"][degree][header] += value
        Data["ClientList"].clear()
        for service in list(Data["Nodes"][nodename]["Client_Services"]["data"][degree].keys()):
            if Data["Nodes"][nodename]["Client_Services"]["data"][degree][service] !=0 :
                Data["ClientList"].addItem(str(Data["Nodes"][nodename]["Client_Services"]["data"][degree][service])+" * "+service)
    
    def modify_linelist(self,nodename,value):
        degree = self.id[1]
        Data["Nodes"][nodename]["Line_Services"][degree]["2*OTU4"] += value
        Data["LineList"].clear()
        for service in list(Data["Nodes"][nodename]["Line_Services"][degree].keys()):
            if Data["Nodes"][nodename]["Line_Services"][degree][service] != 0:
                Data["LineList"].addItem(str(Data["Nodes"][nodename]["Line_Services"][degree][service]) + " * "+service)
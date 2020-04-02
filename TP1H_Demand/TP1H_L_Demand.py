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
    

    def contextMenuEvent(self, event):
        from BLANK_Demand.BLANK_Demand import BLANK_Demand
        ContextMenu = QMenu(self)
        CloseAction = ContextMenu.addAction("Close Panel")
        RefreshAction = ContextMenu.addAction(" Refresh ")
            
        action = ContextMenu.exec_(self.mapToGlobal(event.pos()))

        if action == CloseAction:

            Data["DemandPanel_" + self.id].setWidget(BLANK_Demand(self.id ,  self.nodename, self.Destination))
            Data["DemandPanel_" + self.uppernum].setWidget(BLANK_Demand(self.id ,  self.nodename, self.Destination))

            # TODO: undo every service or lightpath that is created in this panel
            if DemandTabDataBase["Panels"][self.nodename][self.id].Line == "100GE":
                ids = [DemandTabDataBase["Panels"][self.nodename][self.id].DemandId, DemandTabDataBase["Panels"][self.nodename][self.id].ServiceId]
                self.modify_ServiceList(ids, self.nodename, self.Destination, "add", "100GE")

                LightPathId = DemandTabDataBase["Panels"][self.nodename][self.id].LightPathId
                
                self.modify_LightPathList(LightPathId, self.nodename, self.Destination, mode="delete", type="100GE")
                Network.Lightpath.update_id(-1)
            DemandTabDataBase["Panels"][self.nodename].pop(self.id)
            DemandTabDataBase["Panels"][self.nodename].pop(self.uppernum)
        
        if action == RefreshAction:
            # TODO: recalculate line capacity
            pass
    
    def modify_LightPathList(self, id, Source, Destination, mode = "add", type = None):

        if mode == "add":
            DemandTabDataBase["Lightpathes"][(Source, Destination)][id] = "%s # %s" %(id, type)
        
        if mode == "delete":
            for Des in DemandTabDataBase["Source_Destination"][Source]:
                if id in DemandTabDataBase["Lightpathes"][(Source, Destination)]:
                    DemandTabDataBase["Lightpathes"][(Source, Destination)].pop(id)
        
        Data["ui"].update_Demand_lightpath_list()
    
    def modify_ServiceList(self, ids, source, destination, mode = "delete", type = None):

        key = (ids[0] , ids[1])
        if mode == "delete":
            DemandTabDataBase["Services"][(source, destination)].pop(key)
            
        elif mode == "add":
            DemandTabDataBase["Services"][(source, destination)][key] = "[%s , %s] # %s" % (ids[0], ids[1], type)
            
        Data["ui"].UpdateDemand_ServiceList()
        

class customlabel(QLabel):
    def __init__(self, parent, nodename, Destination, ID, tooltip = None):
        super().__init__(parent)
        self.nodename = nodename
        self.id = ID
        self.Destination = Destination
        self.tooltip = tooltip
        self.setAcceptDrops(True)

        if tooltip != None:
            self.setToolTip(tooltip)
    
    def dragEnterEvent(self, event):
        e = event.mimeData()
        model = QStandardItemModel()
        model.dropMimeData(event.mimeData(), Qt.CopyAction, 0,0, QModelIndex())
        dragtext = model.item(0,0).text()
        

        self.allowedservices = ["100GE"]
        text = dragtext

        text = text.split("#")
        n_key = "".join(text[0].split())
        ids = n_key[1:-1].split(',')
        ids = list(map(lambda x : int(x), ids))          # [ Demand Number, Service Number ]
        servicetype = text[1].strip()   # service type = 100Ge , 10GE , ....

        if servicetype in self.allowedservices:
            #TODO: change client color to green
            #self.setPixmap(QPixmap(os.path.join("TP1H_Demand", "client_green.png")))
            pass
            
        else:
            #TODO: change client color to red
            #self.setPixmap(QPixmap(os.path.join("TP1H_Demand", "client_red.png")))
            pass
        event.accept()

        super(customlabel,self).dragEnterEvent(event)
    

    def dragLeaveEvent(self, event):
        self.setPixmap(QPixmap(os.path.join("TP1H_Demand", "TP1H_CLIENT.png")))

    def dropEvent(self, event):
        event.accept()
        e = event.mimeData()
        model = QStandardItemModel()
        model.dropMimeData(event.mimeData(), Qt.CopyAction, 0,0, QModelIndex())
        dragtext = model.item(0,0).text()

        text = dragtext
        text = text.split("#")
        n_key = "".join(text[0].split())
        ids = n_key[1:-1].split(',')
        ids = list(map(lambda x : int(x), ids))          # [ Demand Number, Service Number ]
        servicetype = text[1].strip()   # service type = 100Ge , 10GE , ....

        if servicetype in self.allowedservices:
            
            self.servicetype = servicetype
            self.setToolTip(dragtext)
            self.ids = [ids[0], ids[1]]

            DemandTabDataBase["Panels"][self.nodename][self.id].Line = "100GE"
            DemandTabDataBase["Panels"][self.nodename][self.id].ServiceId = ids[1]
            DemandTabDataBase["Panels"][self.nodename][self.id].DemandId = ids[0]
            self.modify_ServiceList(ids, self.nodename, self.Destination)


            # self.LightPathId = Network.Lightpath.get_id()

            # adding lightpath to network obj
            Data["NetworkObj"].add_lightpath(Data["NodeIdMap"][self.nodename], Data["NodeIdMap"][self.Destination], 100, [ids[1]], "100GE", ids[0])
            self.LightPathId = max(Data["NetworkObj"].LightPathDict.keys())

            # adding lightpath to internal database
            DemandTabDataBase["Panels"][self.nodename][self.id].LightPathId = self.LightPathId

            self.modify_LightPathList(self.LightPathId, self.nodename, self.Destination, mode= "add", type="100GE")


            # TODO: be Careful !!!!!
            self.setAcceptDrops(False)  
        else:
            self.setPixmap(QPixmap(os.path.join("TP1H_Demand", "TP1H_CLIENT.png")))

    def contextMenuEvent(self, event):
        ContextMenu = QMenu(self)
        ClearAction = ContextMenu.addAction("..Clear Socket..")
        
        action = ContextMenu.exec_(self.mapToGlobal(event.pos()))

        if action == ClearAction:
            if DemandTabDataBase["Panels"][self.nodename][self.id].Line == "100GE":
                self.setToolTip("")
                
                DemandTabDataBase["Panels"][self.nodename][self.id].Line = 0
                DemandTabDataBase["Panels"][self.nodename][self.id].LightPathId = None
                DemandTabDataBase["Panels"][self.nodename][self.id].ServiceId = None
                self.setPixmap(QPixmap(os.path.join("TP1H_Demand", "TP1H_CLIENT.png")))
                self.setAcceptDrops(True)
                self.modify_ServiceList(self.ids, self.nodename, self.Destination, mode = "add", type = "100GE")
                self.modify_LightPathList(self.LightPathId, self.nodename, self.Destination, mode="delete", type="100GE")
                
                #Network.Lightpath.update_id(-1)

                # deleting lightpath from network object
                Data["NetworkObj"].del_lightpath([self.ids[1]])
    

    def modify_ServiceList(self, ids, source, destination, mode = "delete", type = None):
        

        key = (ids[0] , ids[1])
        if mode == "delete":
            DemandTabDataBase["Services"][(source, destination)].pop(key)
        
            # statement bellow checks for removing notification
            x = 0
            for dest in DemandTabDataBase["Source_Destination"][source]["DestinationList"]:
                if DemandTabDataBase["Services"][(source, dest)]:
                    x = 1
                    break
            if x == 0:        
                Data["ui"].set_failed_nodes_default(source)
            
        elif mode == "add":
            DemandTabDataBase["Services"][(source, destination)][key] = "[%s , %s] # %s" % (ids[0], ids[1], type)
            
        Data["ui"].UpdateDemand_ServiceList()
    
    def modify_LightPathList(self, id, Source, Destination, mode = "add", type = None):

        if mode == "add":
            DemandTabDataBase["Lightpathes"][(Source, Destination)][id] = "%s # %s" %(id, type)
        
        if mode == "delete":
            for Des in DemandTabDataBase["Source_Destination"][Source]:
                if id in DemandTabDataBase["Lightpathes"][(Source, Destination)]:
                    DemandTabDataBase["Lightpathes"][(Source, Destination)].pop(id)
        
        Data["ui"].update_Demand_lightpath_list()

if __name__ == "__main__":

    app = QtWidgets.QApplication([])
    window = TP1H_L_Demand(1,2,3)
    window.show()
    sys.exit(app.exec_())

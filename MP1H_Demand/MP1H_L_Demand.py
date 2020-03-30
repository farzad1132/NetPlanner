from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import sys
import os
from data import *
from Common_Object_def import Network



class MP1H_L_Demand(QWidget):
    def __init__(self, Panel_ID, nodename, Destination):
        super(MP1H_L_Demand, self).__init__()

        self.id = Panel_ID
        self.nodename = nodename
        self.Destination = Destination
        self.uppernum = str(int(Panel_ID) + 1)

        self.setFixedSize(116, 521)
        
        self.client1 = customlabel(self, self.nodename, self.Destination, self.id, 1)
        self.client1.setGeometry(QRect(40, 140, 31, 41))
        self.client1.setText("")
        self.client1.setPixmap(QPixmap(os.path.join("MP1H_Demand","client.png")))
        self.client1.setObjectName("client1") 

        self.client2 = customlabel(self, self.nodename, self.Destination, self.id, 2)
        self.client2.setGeometry(QRect(60, 140, 31, 41))
        self.client2.setText("")
        self.client2.setPixmap(QPixmap(os.path.join("MP1H_Demand","client.png")))
        self.client2.setObjectName("client2")
        
        self.client3 = customlabel(self, self.nodename, self.Destination, self.id, 3)
        self.client3.setGeometry(QRect(40, 180, 31, 41))
        self.client3.setText("")
        self.client3.setPixmap(QPixmap(os.path.join("MP1H_Demand","client.png")))
        self.client3.setObjectName("client3") 

        self.client4 = customlabel(self, self.nodename, self.Destination, self.id, 4)
        self.client4.setGeometry(QRect(60, 180, 31, 41))
        self.client4.setText("")
        self.client4.setPixmap(QPixmap(os.path.join("MP1H_Demand","client.png")))
        self.client4.setObjectName("client4") 

        self.client5 = customlabel(self, self.nodename, self.Destination, self.id, 5)
        self.client5.setGeometry(QRect(40, 220, 31, 41))
        self.client5.setText("")
        self.client5.setPixmap(QPixmap(os.path.join("MP1H_Demand","client.png")))
        self.client5.setObjectName("client5") 

        self.client6 = customlabel(self, self.nodename, self.Destination, self.id, 6)
        self.client6.setGeometry(QRect(60, 220, 31, 41))
        self.client6.setText("")
        self.client6.setPixmap(QPixmap(os.path.join("MP1H_Demand","client.png")))
        self.client6.setObjectName("client6") 

        self.client7 = customlabel(self, self.nodename, self.Destination, self.id, 7)
        self.client7.setGeometry(QRect(40, 260, 31, 41))
        self.client7.setText("")
        self.client7.setPixmap(QPixmap(os.path.join("MP1H_Demand","client.png")))
        self.client7.setObjectName("client7") 

        self.client8 = customlabel(self, self.nodename, self.Destination, self.id, 8)
        self.client8.setGeometry(QRect(60, 260, 31, 41))
        self.client8.setText("")
        self.client8.setPixmap(QPixmap(os.path.join("MP1H_Demand","client.png")))
        self.client8.setObjectName("client8") 

        self.client9 = customlabel(self, self.nodename, self.Destination, self.id, 9)
        self.client9.setGeometry(QRect(40, 300, 31, 41))
        self.client9.setText("")
        self.client9.setPixmap(QPixmap(os.path.join("MP1H_Demand","client.png")))
        self.client9.setObjectName("client9") 

        self.client10 = customlabel(self, self.nodename, self.Destination, self.id, 10)
        self.client10.setGeometry(QRect(60, 300, 31, 41))
        self.client10.setText("")
        self.client10.setPixmap(QPixmap(os.path.join("MP1H_Demand","client.png")))
        self.client10.setObjectName("client10") 

        
        self.title = QLabel(self)
        self.title.setGeometry(QRect(70, 10, 41, 121))
        self.title.setText("")
        self.title.setPixmap(QPixmap(os.path.join("MP1H_Demand","title.png")))
        self.title.setObjectName("title") 

        self.line = QLabel(self)
        self.line.setGeometry(QRect(40, 350, 55, 101))
        self.line.setText("")
        self.line.setPixmap(QPixmap(os.path.join("MP1H_Demand","line.png")))
        self.line.setObjectName("line") 

        self.socket = QLabel(self)
        self.socket.setGeometry(QRect(20, 470, 55, 51))
        self.socket.setText("")
        self.socket.setPixmap(QPixmap(os.path.join("MP1H_Demand","socket2.png")))
        self.socket.setObjectName("socket") 

        self.upper_socket = QLabel(self)
        self.upper_socket.setGeometry(QRect(20, 0, 55, 41))
        self.upper_socket.setText("")
        self.upper_socket.setPixmap(QPixmap(os.path.join("MP1H_Demand","socket1.png")))
        self.upper_socket.setObjectName("upper_socket")

        self.retranslateUi()
        QMetaObject.connectSlotsByName(self)


    def retranslateUi(self):
        _translate = QCoreApplication.translate

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
            if DemandTabDataBase["Panels"][self.nodename][self.id].LineCapacity != 0:

                for i in range(len(DemandTabDataBase["Panels"][self.nodename][self.id].ClientsCapacity)):
                    if DemandTabDataBase["Panels"][self.nodename][self.id].ClientsCapacity[i] != 0:
                        ids = [DemandTabDataBase["Panels"][self.nodename][self.id].DemandIdList[i], DemandTabDataBase["Panels"][self.nodename][self.id].ServiceIdList[i]]
                        type = DemandTabDataBase["Panels"][self.nodename][self.id].ClientsCapacity[i]

                        self.modify_ServiceList(ids, self.nodename, self.Destination, "add", type)

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
    def __init__(self, parent, nodename, Destination, ID, ClientNum, tooltip = None):
        super().__init__(parent)
        self.STM_64_BW = 10
        self.GE_10_BW = 10
        self.nodename = nodename
        self.id = ID
        self.ClientNum  = ClientNum - 1          # because list indices starts with 0
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
        

        self.allowedservices = ["10GE", "STM_64"]
        text = dragtext
        # FIXME: why we need this if ????
        if text != "MP1H":
            text = text.split("#")
            n_key = "".join(text[0].split())
            ids = n_key[1:-1].split(',')
            ids = list(map(lambda x : int(x), ids))          # [ Demand Number, Service Number ]
            servicetype = text[1].strip()   # service type = 100Ge , 10GE , ....

            if servicetype in self.allowedservices:
                self.setPixmap(QPixmap(os.path.join("MP1H_Demand", "client_green.png")))
                
            else:
                self.setPixmap(QPixmap(os.path.join("MP1H_Demand", "client_red.png")))

            event.accept()

            super(customlabel,self).dragEnterEvent(event)
    

    def dragLeaveEvent(self, event):
        self.setPixmap(QPixmap(os.path.join("MP1H_Demand", "client.png")))

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

            self.setToolTip(dragtext)
            self.servicetype = servicetype
            self.ids = [ids[0], ids[1]]
            if servicetype == "10GE":
                DemandTabDataBase["Panels"][self.nodename][self.id].LineCapacity += self.GE_10_BW
            else:
                DemandTabDataBase["Panels"][self.nodename][self.id].LineCapacity += self.STM_64_BW
            #DemandTabDataBase["Panels"][self.nodename][self.id].Line = "100GE"
            DemandTabDataBase["Panels"][self.nodename][self.id].ClientsCapacity[self.ClientNum] = servicetype

            ServiceListLen = len(DemandTabDataBase["Panels"][self.nodename][self.id].ServiceIdList)
            if self.ClientNum >= ServiceListLen:
                for i in range(ServiceListLen - self.ClientNum + 1):
                    DemandTabDataBase["Panels"][self.nodename][self.id].ServiceIdList.append(None) 
            DemandTabDataBase["Panels"][self.nodename][self.id].ServiceIdList[self.ClientNum] = ids[1]
            print(f"debug in MP1H--> demandid : {ids[0]}")
            DemandTabDataBase["Panels"][self.nodename][self.id].DemandIdList[self.ClientNum] = ids[0]
            self.modify_ServiceList(ids, self.nodename, self.Destination)

            if DemandTabDataBase["Panels"][self.nodename][self.id].LightPath_flag == 0:

                #DemandTabDataBase["Panels"][self.nodename][self.id].LightPathId = Network.Lightpath.get_id()

                # updating networkobj
                ServiceIdList = [ids[1]]
                Data["NetworkObj"].add_lightpath(Data["NodeIdMap"][self.nodename], Data["NodeIdMap"][self.Destination], 10, ServiceIdList, "100GE", ids[0])
                LightPathId = max(Data["NetworkObj"].LightPathDict.keys())
                DemandTabDataBase["Panels"][self.nodename][self.id].LightPathId = LightPathId

                self.modify_LightPathList(DemandTabDataBase["Panels"][self.nodename][self.id].LightPathId, self.nodename, self.Destination, mode= "add", type="100GE")
                DemandTabDataBase["Panels"][self.nodename][self.id].LightPath_flag = 1


            # TODO: be Careful !!!!!
            self.setAcceptDrops(False)
        else:
            self.setPixmap(QPixmap(os.path.join("MP1H_Demand", "client.png")))

    def contextMenuEvent(self, event):

        def check_clients(ClientsList):
                x = 0
                for i in range(10):
                    if ClientsList[i] != 0:
                        x = 1
                return x

        ContextMenu = QMenu(self)
        ClearAction = ContextMenu.addAction("..Clear Socket..")
        
        action = ContextMenu.exec_(self.mapToGlobal(event.pos()))

        if action == ClearAction:
            if DemandTabDataBase["Panels"][self.nodename][self.id].ClientsCapacity[self.ClientNum] != 0:
                self.setToolTip("")
                if self.servicetype == "10GE":
                    DemandTabDataBase["Panels"][self.nodename][self.id].LineCapacity -= self.GE_10_BW
                else:
                    DemandTabDataBase["Panels"][self.nodename][self.id].LineCapacity -= self.STM_64_BW
                #DemandTabDataBase["Panels"][self.nodename][self.id].Line = 0
                DemandTabDataBase["Panels"][self.nodename][self.id].ClientsCapacity[self.ClientNum] = 0
                
                DemandTabDataBase["Panels"][self.nodename][self.id].ServiceIdList[self.ClientNum] = None
                self.setPixmap(QPixmap(os.path.join("MP1H_Demand", "client.png")))
                self.setAcceptDrops(True)


                self.modify_ServiceList(self.ids, self.nodename, self.Destination, mode = "add", type = self.servicetype)
                x = check_clients(DemandTabDataBase["Panels"][self.nodename][self.id].ClientsCapacity)

                if x == 0:
                    
                    self.modify_LightPathList(DemandTabDataBase["Panels"][self.nodename][self.id].LightPathId, self.nodename, self.Destination, mode="delete", type="100GE")


                    DemandTabDataBase["Panels"][self.nodename][self.id].LightPathId = None
                    #Network.Lightpath.update_id(-1)
                    DemandTabDataBase["Panels"][self.nodename][self.id].LightPath_flag = 0

                    # deleting lightpath object from network obj
                    Data["NetworkObj"].del_lightpath(list(DemandTabDataBase["Panels"][self.nodename][self.id].ClientsList))
            
    

    def modify_ServiceList(self, ids, source, destination, mode = "delete", type = None):
        

        key = (int(ids[0]) , int(ids[1]))
        if mode == "delete":
            DemandTabDataBase["Services"][(source, destination)].pop(key)
            
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
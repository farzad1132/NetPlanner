from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import sys
import os
from data import *
from Common_Object_def import Network


class TP1H_L_Demand(QWidget):
    def __init__(self, Panel_ID, nodename , Destination):
        super(TP1H_L_Demand, self).__init__()

        self.id = Panel_ID
        self.nodename = nodename
        self.Destination = Destination
        self.uppernum = str(int(Panel_ID) + 1)

        self.setFixedSize(112, 521)
        self.line = QLabel(self)
        self.line.setGeometry(QRect(30, 140, 55, 191))
        self.line.setText("")
        self.line.setPixmap(QPixmap(os.path.join("TP1H_Demand","tp1h_line.png")))
        self.line.setObjectName("line")
        self.client = customlabel(self, self.nodename, self.Destination, self.id)
        self.client.setGeometry(QRect(30, 320, 55, 141))
        self.client.setText("")
        self.client.setPixmap(QPixmap(os.path.join("TP1H_Demand","TP1H_CLIENT.png")))
        self.client.setObjectName("client")
        self.title = QLabel(self)
        self.title.setGeometry(QRect(60, 30, 55, 111))
        self.title.setText("")
        self.title.setPixmap(QPixmap(os.path.join("TP1H_Demand","title.png")))
        self.title.setObjectName("title") 
        self.upper_socket = QLabel(self)
        self.upper_socket.setGeometry(QRect(20, -20, 41, 81))
        self.upper_socket.setText("")
        self.upper_socket.setPixmap(QPixmap(os.path.join("TP1H_Demand","socket1.png")))
        self.upper_socket.setObjectName("upper_soclet") 

        self.socket = QLabel(self)
        self.socket.setGeometry(QRect(20, 470, 55, 61))
        self.socket.setText("")
        self.socket.setPixmap(QPixmap(os.path.join("TP1H_Demand","socket2.png")))
        self.socket.setObjectName("socket") 

        self.retranslateUi()
        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
    
    def contextMenuEvent(self, event):
        from BLANK_Demand.BLANK_Demand import BLANK_Demand
        ContextMenu = QMenu(self)
        CloseAction = ContextMenu.addAction("Close Panel")
            
        action = ContextMenu.exec_(self.mapToGlobal(event.pos()))

        if action == CloseAction:

            Data["DemandPanel_" + self.id].setWidget(BLANK_Demand(self.id ,  self.nodename, self.Destination))
            Data["DemandPanel_" + self.uppernum].setWidget(BLANK_Demand(self.id ,  self.nodename, self.Destination))

            # TODO: undo every service or lightpath that is created in this panel
            if DemandTabDataBase["Panels"][self.nodename][self.id].Line == "100GE":
                ids = [DemandTabDataBase["Panels"][self.nodename][self.id].DemandId, DemandTabDataBase["Panels"][self.nodename][self.id].ServiceId]

                self.modify_ServiceList(ids= ids,
                                            source= self.nodename,
                                            destination= self.Destination,
                                            mode= "add",
                                            type= "100GE")

                LightPathId = DemandTabDataBase["Panels"][self.nodename][self.id].LightPathId
                
                #self.modify_LightPathList(LightPathId, self.nodename, self.Destination, mode="delete", type="100GE")
                self.modify_LightPathList(  id= LightPathId,
                                            Source= self.nodename,
                                            Destination= self.Destination,
                                            mode= "delete",
                                            type= "100GE")

                Data["NetworkObj"].del_lightpath(LightPathId)

            DemandTabDataBase["Panels"][self.nodename].pop(self.id)
            DemandTabDataBase["Panels"][self.nodename].pop(self.uppernum)
        
    
    def modify_LightPathList(self, id, Source, Destination, Capacity = None, mode = "add", type = None):

        if mode == "add":
            #DemandTabDataBase["Lightpathes"][(Source, Destination)][id] = "%s # %s" %(id, type)
            item = QListWidgetItem(type, Data["Demand_LightPath_list"])
            UserData = {"LightPathId":id, "Source":Source, "Destination":Destination, "Capacity":Capacity, "Type": type}
            item.setToolTip(f"Source: {Source}\nDestination: {Destination}\nCapacity: {Capacity}\nType: {type}")
            item.setData(Qt.UserRole, UserData)
            item.setTextAlignment(Qt.AlignCenter)

            DemandTabDataBase["Lightpathes"][(Source, Destination)][id] = item
        
        if mode == "delete":
            # deleting desired lightpath from database
            DemandTabDataBase["Lightpathes"][(Source, Destination)].pop(id)

            # correcting upper lightpath id's 
            for Des in DemandTabDataBase["Source_Destination"][Source]["DestinationList"]:
                for UpperId in sorted(list(DemandTabDataBase["Lightpathes"][(Source, Des)].keys())):
                    if UpperId > id:
                        DemandTabDataBase["Lightpathes"][(Source, Des)][UpperId - 1] = DemandTabDataBase["Lightpathes"][(Source, Des)].pop(UpperId)
                        UserData = DemandTabDataBase["Lightpathes"][(Source, Des)][UpperId - 1].data(Qt.UserRole)
                        UserData["LightPathId"] -= 1
                        DemandTabDataBase["Lightpathes"][(Source, Des)][UpperId - 1].setData(Qt.UserRole, UserData) 
 
        
        Data["ui"].update_Demand_lightpath_list()
    
    def modify_ServiceList(self, ids, source, destination, mode = "delete", type = None):

        key = (ids[0] , ids[1])
        if mode == "delete":
            DemandTabDataBase["Services"][(source, destination)].pop(key)
            
        elif mode == "add":
            DemandTabDataBase["Services"][(source, destination)][key] = None
            
        Data["ui"].UpdateDemand_ServiceList()
        

class customlabel(QLabel):
    def __init__(self, parent, nodename, Destination, ID, LineVar, tooltip = None):
        super().__init__(parent)
        self.nodename = nodename
        self.LineVar = LineVar
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
        UserData = model.item(0).data(Qt.UserRole)

        self.allowedservices = ["100GE"]
        #text = dragtext

        """ text = text.split("#")
        n_key = "".join(text[0].split())
        ids = n_key[1:-1].split(',')
        ids = list(map(lambda x : int(x), ids))          # [ Demand Number, Service Number ]
        servicetype = text[1].strip()   # service type = 100Ge , 10GE , .... """
        servicetype = dragtext.strip()
        ids = [UserData["DemandId"], UserData["ServiceId"]]         # [ Demand Number, Service Number ]

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
        UserData = model.item(0).data(Qt.UserRole)

        """ text = dragtext
        text = text.split("#")
        n_key = "".join(text[0].split())
        ids = n_key[1:-1].split(',')
        ids = list(map(lambda x : int(x), ids))          # [ Demand Number, Service Number ]
        servicetype = text[1].strip()   # service type = 100Ge , 10GE , .... """
        servicetype = dragtext.strip()


        if servicetype in self.allowedservices:
            
            self.servicetype = servicetype
            self.setToolTip(DemandTabDataBase["Services_static"][self.nodename][self.ids].toolTip())
            self.ids = (UserData["DemandId"], UserData["ServiceId"])

            DemandTabDataBase["Panels"][self.nodename][self.id].Line = "100GE"
            DemandTabDataBase["Panels"][self.nodename][self.id].ServiceId = ids[1]
            DemandTabDataBase["Panels"][self.nodename][self.id].DemandId = ids[0]
            self.modify_ServiceList(self.ids, self.nodename, self.Destination)


            # self.LightPathId = Network.Lightpath.get_id()

            # adding lightpath to network obj
            Data["NetworkObj"].add_lightpath(Data["NodeIdMap"][self.nodename], Data["NodeIdMap"][self.Destination], 100, [ids[1]], "100GE", ids[0])
            self.LightPathId = max(Data["NetworkObj"].LightPathDict.keys())

            # adding lightpath to internal database
            DemandTabDataBase["Panels"][self.nodename][self.id].LightPathId = self.LightPathId

            #self.modify_LightPathList(self.LightPathId, self.nodename, self.Destination, mode= "add", type="100GE")
            self.modify_LightPathList(      id= DemandTabDataBase["Panels"][self.nodename][self.id].LightPathId,
                                            Source= self.nodename,
                                            Destination= self.Destination,
                                            Capacity= DemandTabDataBase["Panels"][self.nodename][self.id].Line,
                                            mode= "add",
                                            type= "100GE",
                                            PanelId= self.id)

            # setting line port tooltip                                        
            self.LineVar.setToolTip(DemandTabDataBase["Lightpathes"][(self.nodename, self.Destination)][LightPathId].toolTip())


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

                # deleting lightpath from network object
                
                
                DemandTabDataBase["Panels"][self.nodename][self.id].Line = 0
                DemandTabDataBase["Panels"][self.nodename][self.id].LightPathId = None
                DemandTabDataBase["Panels"][self.nodename][self.id].ServiceId = None
                self.setPixmap(QPixmap(os.path.join("TP1H_Demand", "TP1H_CLIENT.png")))
                self.setAcceptDrops(True)
                #self.modify_ServiceList(self.ids, self.nodename, self.Destination, mode = "add", type = "100GE")
                self.modify_LightPathList(id= DemandTabDataBase["Panels"][self.nodename][self.id].LightPathId,
                                            Source= self.nodename,
                                            Destination= self.Destination,
                                            Capacity= DemandTabDataBase["Panels"][self.nodename][self.id].Line,
                                            mode= "add",
                                            type= "100GE",
                                            PanelId= self.id)

                #self.modify_LightPathList(self.LightPathId, self.nodename, self.Destination, mode="delete", type="100GE")
                self.modify_LightPathList(  id= DemandTabDataBase["Panels"][self.nodename][self.id].LightPathId,
                                                Source= self.nodename,
                                                Destination= self.Destination,
                                                mode= "delete",
                                                type= "100GE")
                
                #Network.Lightpath.update_id(-1)
                Data["NetworkObj"].del_lightpath(DemandTabDataBase["Panels"][self.nodename][self.id].LightPathId)

                
    

    def modify_ServiceList(self, ids, source, destination, mode = "delete", type = None):
        

        key = (int(ids[0]) , int(ids[1]))
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
            DemandTabDataBase["Services"][(source, destination)][key] = None
            
        Data["ui"].UpdateDemand_ServiceList()
    
    def modify_LightPathList(self, id, Source, Destination, Capacity = None, mode = "add", type = None, PanelId = None):

        if mode == "add":
            #DemandTabDataBase["Lightpathes"][(Source, Destination)][id] = "%s # %s" %(id, type)
            item = QListWidgetItem(type, Data["Demand_LightPath_list"])
            UserData = {"LightPathId":id, "Source":Source, "Destination":Destination, "Capacity":Capacity, "Type": type, "PanelId": PanelId}
            item.setToolTip(f"Source: {Source}\nDestination: {Destination}\nCapacity: {Capacity}\nType: {type}")
            item.setData(Qt.UserRole, UserData)
            item.setTextAlignment(Qt.AlignCenter)

            DemandTabDataBase["Lightpathes"][(Source, Destination)][id] = item
        
        if mode == "delete":
            # deleting desired lightpath from database
            DemandTabDataBase["Lightpathes"][(Source, Destination)].pop(id)

            # correcting upper lightpath id's 
            for Des in DemandTabDataBase["Source_Destination"][Source]["DestinationList"]:
                for UpperId in sorted(list(DemandTabDataBase["Lightpathes"][(Source, Des)].keys())):
                    if UpperId > id:
                        DemandTabDataBase["Lightpathes"][(Source, Des)][UpperId - 1] = DemandTabDataBase["Lightpathes"][(Source, Des)].pop(UpperId)
                        UserData = DemandTabDataBase["Lightpathes"][(Source, Des)][UpperId - 1].data(Qt.UserRole)
                        UserData["LightPathId"] -= 1
                        DemandTabDataBase["Lightpathes"][(Source, Des)][UpperId - 1].setData(Qt.UserRole, UserData) 
 
        
        Data["ui"].update_Demand_lightpath_list()
        

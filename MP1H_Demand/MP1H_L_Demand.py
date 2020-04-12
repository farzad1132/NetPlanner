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
from MP1H_Demand import CLIENT_L_Selected
from MP1H_Demand import CLIENT_R_Selected


# USE THIS CODE TO CHANGE THE CLIENT TO SELECTED CLIENT:
#1)
# For left clients:
# self.Client(number of client).setStyleSheet("image: url(:/CLIENT_L_Selected_SOURCE/CLIENT_L_Selected.png);")
#2)
# For left clients:
# self.Client(number of client).setStyleSheet("image: url(:/CLIENT_R_Selected_SOURCE/CLIENT_R_Selected.png);")

class MP1H_L_Demand(QtWidgets.QWidget):

    def __init__(self, Panel_ID, nodename, Destination):
        super(MP1H_L_Demand, self).__init__()

        #self.resize(118, 633)

        self.id = str(Panel_ID)
        # nodename == Source in Demand Tab
        self.nodename = nodename
        self.Destination = Destination
        self.uppernum = str(int(self.id) + 1)


        self.Line = QtWidgets.QLabel(self)
        self.Line.setMinimumSize(QtCore.QSize(0, 125))
        self.Line.setStyleSheet("image: url(:/line/line.png);")
        self.Line.setText("")
        self.Line.setObjectName("Line")

        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setObjectName("gridLayout")
        self.Client8 = customlabel(self, self.nodename, self.Destination, self.id, 8, self.Line)
        self.Client8.setStyleSheet("image: url(:/client_r/CLIENT_R.png);")
        self.Client8.setText("")
        self.Client8.setObjectName("Client8")
        self.gridLayout.addWidget(self.Client8, 5, 1, 1, 1)
        self.Client5 = customlabel(self, self.nodename, self.Destination, self.id, 5, self.Line)
        self.Client5.setStyleSheet("image: url(:/CLIENT_L1/CLIENT_L.png);")
        self.Client5.setText("")
        self.Client5.setObjectName("Client5")
        self.gridLayout.addWidget(self.Client5, 4, 0, 1, 1)
        self.Client7 = customlabel(self, self.nodename, self.Destination, self.id, 7, self.Line)
        self.Client7.setStyleSheet("image: url(:/CLIENT_L1/CLIENT_L.png);")
        self.Client7.setText("")
        self.Client7.setObjectName("Client7")
        self.gridLayout.addWidget(self.Client7, 5, 0, 1, 1)
        
        self.gridLayout.addWidget(self.Line, 7, 0, 1, 1)
        self.Socket_Top = QtWidgets.QLabel(self)
        self.Socket_Top.setMaximumSize(QtCore.QSize(16777215, 50))
        self.Socket_Top.setStyleSheet("image: url(:/Socket_top/Socket_top.png);")
        self.Socket_Top.setText("")
        self.Socket_Top.setObjectName("Socket_Top")
        self.gridLayout.addWidget(self.Socket_Top, 1, 0, 1, 1)
        self.Client1 = customlabel(self, self.nodename, self.Destination, self.id, 1, self.Line)
        self.Client1.setStyleSheet("image: url(:/CLIENT_L1/CLIENT_L.png);")
        self.Client1.setText("")
        self.Client1.setObjectName("Client1")
        self.gridLayout.addWidget(self.Client1, 2, 0, 1, 1)
        self.Client6 = customlabel(self, self.nodename, self.Destination, self.id, 6, self.Line)
        self.Client6.setStyleSheet("image: url(:/client_r/CLIENT_R.png);")
        self.Client6.setText("")
        self.Client6.setObjectName("Client6")
        self.gridLayout.addWidget(self.Client6, 4, 1, 1, 1)
        self.Client4 = customlabel(self, self.nodename, self.Destination, self.id, 4, self.Line)
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
        self.Client10 = customlabel(self, self.nodename, self.Destination, self.id, 10, self.Line)
        self.Client10.setStyleSheet("image: url(:/client_r/CLIENT_R.png);")
        self.Client10.setText("")
        self.Client10.setObjectName("Client10")
        self.gridLayout.addWidget(self.Client10, 6, 1, 1, 1)
        self.Client2 = customlabel(self, self.nodename, self.Destination, self.id, 2, self.Line)
        self.Client2.setStyleSheet("image: url(:/client_r/CLIENT_R.png);")
        self.Client2.setText("")
        self.Client2.setObjectName("Client2")
        self.gridLayout.addWidget(self.Client2, 2, 1, 1, 1)
        self.Client9 = customlabel(self, self.nodename, self.Destination, self.id, 9, self.Line)
        self.Client9.setStyleSheet("image: url(:/CLIENT_L1/CLIENT_L.png);")
        self.Client9.setText("")
        self.Client9.setObjectName("Client9")
        self.gridLayout.addWidget(self.Client9, 6, 0, 1, 1)
        self.Client3 = customlabel(self, self.nodename, self.Destination, self.id, 3, self.Line)
        self.Client3.setStyleSheet("image: url(:/CLIENT_L1/CLIENT_L.png);")
        self.Client3.setText("")
        self.Client3.setObjectName("Client3")
        self.gridLayout.addWidget(self.Client3, 3, 0, 1, 1)
        self.MP1H_Title = QtWidgets.QLabel(self)
        self.MP1H_Title.setStyleSheet("image: url(:/title/MP1H_title.png);")
        self.MP1H_Title.setText("")
        self.MP1H_Title.setObjectName("MP1H_Title")
        self.gridLayout.addWidget(self.MP1H_Title, 1, 2, 2, 1)

    def contextMenuEvent(self, event):
        from BLANK_Demand.BLANK_Demand import BLANK_Demand
        ContextMenu = QMenu(self)
        CloseAction = ContextMenu.addAction("Close Panel")
            
        action = ContextMenu.exec_(self.mapToGlobal(event.pos()))

        if action == CloseAction:
            # removing old left panel
            panel_widget = Data["DemandPanel_" + str(self.id)].takeAt(0).widget()
            Data["ui"].horizontalLayout.removeWidget(panel_widget)
            panel_widget.deleteLater()
            Data["DemandPanel_" + self.id].addWidget(BLANK_Demand(self.id ,  self.nodename, self.Destination))

            # removing old right panel
            panel_widget = Data["DemandPanel_" + str(self.uppernum)].takeAt(0).widget()
            Data["ui"].horizontalLayout.removeWidget(panel_widget)
            panel_widget.deleteLater()
            Data["DemandPanel_" + self.uppernum].addWidget(BLANK_Demand(self.id ,  self.nodename, self.Destination))

            # TODO: undo every service or lightpath that is created in this panel
            if DemandTabDataBase["Panels"][self.nodename][self.id].LineCapacity != 0:

                for i in range(len(DemandTabDataBase["Panels"][self.nodename][self.id].ClientsCapacity)):
                    if DemandTabDataBase["Panels"][self.nodename][self.id].ClientsCapacity[i] != 0:
                        ids = [DemandTabDataBase["Panels"][self.nodename][self.id].DemandIdList[i], DemandTabDataBase["Panels"][self.nodename][self.id].ServiceIdList[i]]
                        type = DemandTabDataBase["Panels"][self.nodename][self.id].ClientsCapacity[i]

                        #self.modify_ServiceList(ids, self.nodename, self.Destination, "add", type)
                        self.modify_ServiceList(ids= ids,
                                                source= self.nodename,
                                                destination= self.Destination,
                                                mode= "add",
                                                type= type)

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
    def __init__(self, parent, nodename, Destination, ID, ClientNum, LineVar, tooltip = None):
        super().__init__(parent)
        self.STM_64_BW = 10
        self.GE_10_BW = 10
        self.LineVar = LineVar
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
        UserData = model.item(0).data(Qt.UserRole)
        

        self.allowedservices = ["10GE", "STM_64"]
        #text = dragtext
        # FIXME: why we need this if ????
        if dragtext != "MP1H":
            servicetype = dragtext.strip()
            ids = [UserData["DemandId"], UserData["ServiceId"]]         # [ Demand Number, Service Number ]
            """ text = text.split("#")
            n_key = "".join(text[0].split())
            ids = n_key[1:-1].split(',')
            ids = list(map(lambda x : int(x), ids))          
            servicetype = text[1].strip()   # service type = 100Ge , 10GE , .... """

            if servicetype in self.allowedservices:
                if self.ClientNum % 2 == 0:
                    self.setStyleSheet("image: url(:/CLIENT_L_Selected_SOURCE/CLIENT_L_Selected.png);")
                else:
                    self.setStyleSheet("image: url(:/CLIENT_R_Selected_SOURCE/CLIENT_R_Selected.png);")
                

            event.accept()

            super(customlabel,self).dragEnterEvent(event)
    

    def dragLeaveEvent(self, event):
        if self.ClientNum % 2 == 0:
            self.setStyleSheet("image: url(:/CLIENT_L1/CLIENT_L.png);")
        else:
            self.setStyleSheet("image: url(:/client_r/CLIENT_R.png);")

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
            self.ids = (UserData["DemandId"], UserData["ServiceId"])
            self.setToolTip(DemandTabDataBase["Services_static"][self.nodename][self.ids].toolTip())


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
            DemandTabDataBase["Panels"][self.nodename][self.id].ServiceIdList[self.ClientNum] = self.ids[1]
            #print(f"debug in MP1H--> demandid : {ids[0]}")
            DemandTabDataBase["Panels"][self.nodename][self.id].DemandIdList[self.ClientNum] = self.ids[0]
            
            self.modify_ServiceList(self.ids, self.nodename, self.Destination)

            if DemandTabDataBase["Panels"][self.nodename][self.id].LightPath_flag == 0:

                #DemandTabDataBase["Panels"][self.nodename][self.id].LightPathId = Network.Lightpath.get_id()

                # updating networkobj
                ServiceIdList = [self.ids[1]]
                Data["NetworkObj"].add_lightpath(Data["NodeIdMap"][self.nodename], Data["NodeIdMap"][self.Destination], 10, ServiceIdList, "100GE", self.ids[0])
                LightPathId = max(Data["NetworkObj"].LightPathDict.keys())
                DemandTabDataBase["Panels"][self.nodename][self.id].LightPathId = LightPathId

                #self.modify_LightPathList(DemandTabDataBase["Panels"][self.nodename][self.id].LightPathId, self.nodename, self.Destination, mode= "add", type="100GE")
                self.modify_LightPathList(id= DemandTabDataBase["Panels"][self.nodename][self.id].LightPathId,
                                            Source= self.nodename,
                                            Destination= self.Destination,
                                            Capacity= DemandTabDataBase["Panels"][self.nodename][self.id].LineCapacity,
                                            mode= "add",
                                            type= "100GE",
                                            PanelId= self.id)
                DemandTabDataBase["Panels"][self.nodename][self.id].LightPath_flag = 1

                


            else:
                ServiceIdList = [self.ids[1]]
                LightPathId = DemandTabDataBase["Panels"][self.nodename][self.id].LightPathId
                Data["NetworkObj"].LightPathDict[LightPathId].ServiceIdList.extend(ServiceIdList)

            # TODO: be Careful !!!!!
            self.setAcceptDrops(False)
            
            # updating LightPath ListWidgetItem Capacity
            self.Update_LineListWidgetItem_Tooltip( Item= DemandTabDataBase["Lightpathes"][(self.nodename, self.Destination)][LightPathId],
                                                    Capacity= DemandTabDataBase["Panels"][self.nodename][self.id].LineCapacity)

            # setting line port tooltip                                        
            self.LineVar.setToolTip(DemandTabDataBase["Lightpathes"][(self.nodename, self.Destination)][LightPathId].toolTip())
        else:
            if self.ClientNum % 2 == 0:
                self.setStyleSheet("image: url(:/CLIENT_L1/CLIENT_L.png);")
            else:
                self.setStyleSheet("image: url(:/client_r/CLIENT_R.png);")

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

                if self.ClientNum % 2 == 0:
                    self.setStyleSheet("image: url(:/CLIENT_L1/CLIENT_L.png);")
                else:
                    self.setStyleSheet("image: url(:/client_r/CLIENT_R.png);")

                self.setAcceptDrops(True)


                #self.modify_ServiceList(self.ids, self.nodename, self.Destination, mode = "add", type = self.servicetype)
                self.modify_ServiceList(ids= self.ids,
                                        source= self.nodename,
                                        destination= self.Destination,
                                        mode= "add",
                                        type= self.servicetype)

                # removing service id from lightpath object in common object
                LightPathId = DemandTabDataBase["Panels"][self.nodename][self.id].LightPathId
                Data["NetworkObj"].LightPathDict[LightPathId].ServiceIdList.remove(self.ids[1])

                # updating LightPath ListWidgetItem Capacity
                self.Update_LineListWidgetItem_Tooltip( Item= DemandTabDataBase["Lightpathes"][(self.nodename, self.Destination)][LightPathId],
                                                        Capacity= DemandTabDataBase["Panels"][self.nodename][self.id].LineCapacity)

                # setting line port tooltip                                        
                self.LineVar.setToolTip(DemandTabDataBase["Lightpathes"][(self.nodename, self.Destination)][LightPathId].toolTip())

                x = check_clients(DemandTabDataBase["Panels"][self.nodename][self.id].ClientsCapacity)

                if x == 0:
                    
                    #self.modify_LightPathList(DemandTabDataBase["Panels"][self.nodename][self.id].LightPathId, self.nodename, self.Destination, mode="delete", type="100GE")
                    self.modify_LightPathList(  id= LightPathId,
                                                Source= self.nodename,
                                                Destination= self.Destination,
                                                mode= "delete",
                                                type= "100GE")

                    # deleting lightpath object from network obj
                    Data["NetworkObj"].del_lightpath(LightPathId)

                    DemandTabDataBase["Panels"][self.nodename][self.id].LightPathId = None
                    #Network.Lightpath.update_id(-1)
                    DemandTabDataBase["Panels"][self.nodename][self.id].LightPath_flag = 0

                    
    def Update_LineListWidgetItem_Tooltip(self, Item, Capacity):       
        
        UserData = Item.data(Qt.UserRole)
        #UserData = {"LightPathId":id, "Source":Source, "Destination":Destination, "Capacity":Capacity, "Type": type}
        UserData["Capacity"] = Capacity
        Item.setData(Qt.UserRole, UserData)
        Item.setToolTip(f"Source: {UserData['Source']}\nDestination: {UserData['Destination']}\nCapacity: {Capacity}\nType: {UserData['Type']}")

    def modify_ServiceList(self, ids, source, destination, mode = "delete", type = None):
        

        key = (int(ids[0]) , int(ids[1]))
        if mode == "delete":
            DemandTabDataBase["Services"][(source, destination)].pop(key)

            # statement bellow checks for removing notification ( if there is such a node)
            if source in Data["ui"].failed_nodes:
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


if __name__ == "__main__":

    app = QtWidgets.QApplication([])
    window = MP1H_L_Demand(1,2,3)
    window.show()
    sys.exit(app.exec_())

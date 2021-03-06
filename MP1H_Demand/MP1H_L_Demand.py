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
from MP1H_Demand import Line_Selected
from MP1H_Demand import Border_L

# USE THIS CODE TO CHANGE THE CLIENT TO SELECTED CLIENT:
#1)
# For left clients:
# self.Client(number of client).setStyleSheet("image: url(:/CLIENT_L_Selected_SOURCE/CLIENT_L_Selected.png);")
#2)
# For left clients:
# self.Client(number of client).setStyleSheet("image: url(:/CLIENT_R_Selected_SOURCE/CLIENT_R_Selected.png);")

# USE THIS CODE TO CHANGE THE LINE TO SELECTED LINE:
# self.Line.setStyleSheet("QLabel{ image: url(:/Line_Selected_SOURCE/Line_Selected.png); }")

class MP1H_L_Demand(QtWidgets.QWidget):

    def __init__(self, Panel_ID, nodename, Destination, DualPanelsId):
        super(MP1H_L_Demand, self).__init__()

        #self.resize(118, 633)

        self.id = str(Panel_ID)
        # nodename == Source in Demand Tab
        self.nodename = nodename
        self.Destination = Destination
        self.uppernum = str(int(self.id) + 1)

        self.DualPanelsId = DualPanelsId

        grid=QtWidgets.QGridLayout(self)
        widget=QtWidgets.QWidget(self)
        widget.setStyleSheet("border-image:url(:/Border_L_Source/Border_L.png); ")
        grid.setMargin(0)
        grid.addWidget(widget)
        self.Line = line_class(self, Destination)
        self.Line.setMinimumSize(QtCore.QSize(0, 125))
        self.Line.setStyleSheet("QLabel{ image: url(:/line/line.png); }")
        self.Line.setText("")
        self.Line.setObjectName("Line")

        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setObjectName("gridLayout")
        self.Client8 = customlabel(self, self.nodename, self.Destination, self.id, 8, self.Line, DualPanelsId= DualPanelsId)
        self.Client8.setStyleSheet(" QLabel { image: url(:/client_r/CLIENT_R.png); } ")
        self.Client8.setText("")
        self.Client8.setObjectName("Client8")
        self.gridLayout.addWidget(self.Client8, 5, 1, 1, 1)
        self.Client5 = customlabel(self, self.nodename, self.Destination, self.id, 5, self.Line, DualPanelsId= DualPanelsId)
        self.Client5.setStyleSheet("QLabel{ image: url(:/CLIENT_L1/CLIENT_L.png); }")
        self.Client5.setText("")
        self.Client5.setObjectName("Client5")
        self.gridLayout.addWidget(self.Client5, 4, 0, 1, 1)
        self.Client7 = customlabel(self, self.nodename, self.Destination, self.id, 7, self.Line, DualPanelsId= DualPanelsId)
        self.Client7.setStyleSheet("QLabel{ image: url(:/CLIENT_L1/CLIENT_L.png); }")
        self.Client7.setText("")
        self.Client7.setObjectName("Client7")
        self.gridLayout.addWidget(self.Client7, 5, 0, 1, 1)
        
        self.gridLayout.addWidget(self.Line, 7, 0, 1, 1)
        self.Socket_Top = QtWidgets.QLabel(self)
        self.Socket_Top.setMaximumSize(QtCore.QSize(16777215, 50))
        self.Socket_Top.setStyleSheet("QLabel{ image: url(:/Socket_top/Socket_top.png); }")
        self.Socket_Top.setText("")
        self.Socket_Top.setObjectName("Socket_Top")
        self.gridLayout.addWidget(self.Socket_Top, 1, 0, 1, 1)
        self.Client1 = customlabel(self, self.nodename, self.Destination, self.id, 1, self.Line, DualPanelsId= DualPanelsId)
        self.Client1.setStyleSheet("QLabel{ image: url(:/CLIENT_L1/CLIENT_L.png); }")
        self.Client1.setText("")
        self.Client1.setObjectName("Client1")
        self.gridLayout.addWidget(self.Client1, 2, 0, 1, 1)
        self.Client6 = customlabel(self, self.nodename, self.Destination, self.id, 6, self.Line, DualPanelsId= DualPanelsId)
        self.Client6.setStyleSheet("QLabel{ image: url(:/client_r/CLIENT_R.png); }")
        self.Client6.setText("")
        self.Client6.setObjectName("Client6")
        self.gridLayout.addWidget(self.Client6, 4, 1, 1, 1)
        self.Client4 = customlabel(self, self.nodename, self.Destination, self.id, 4, self.Line, DualPanelsId= DualPanelsId)
        self.Client4.setStyleSheet("QLabel{ image: url(:/client_r/CLIENT_R.png); }")
        self.Client4.setText("")
        self.Client4.setObjectName("Client4")
        self.gridLayout.addWidget(self.Client4, 3, 1, 1, 1)
        self.Socket_Bottom = QtWidgets.QLabel(self)
        self.Socket_Bottom.setMaximumSize(QtCore.QSize(16777215, 50))
        self.Socket_Bottom.setStyleSheet("QLabel{ image: url(:/Socket_Bottom/Socket_bottom.png); }")
        self.Socket_Bottom.setText("")
        self.Socket_Bottom.setObjectName("Socket_Bottom")
        self.gridLayout.addWidget(self.Socket_Bottom, 8, 0, 1, 1)
        self.Client10 = customlabel(self, self.nodename, self.Destination, self.id, 10, self.Line, DualPanelsId= DualPanelsId)
        self.Client10.setStyleSheet("QLabel{ image: url(:/client_r/CLIENT_R.png); }")
        self.Client10.setText("")
        self.Client10.setObjectName("Client10")
        self.gridLayout.addWidget(self.Client10, 6, 1, 1, 1)
        self.Client2 = customlabel(self, self.nodename, self.Destination, self.id, 2, self.Line, DualPanelsId= DualPanelsId)
        self.Client2.setStyleSheet("QLabel{ image: url(:/client_r/CLIENT_R.png); }")
        self.Client2.setText("")
        self.Client2.setObjectName("Client2")
        self.gridLayout.addWidget(self.Client2, 2, 1, 1, 1)
        self.Client9 = customlabel(self, self.nodename, self.Destination, self.id, 9, self.Line, DualPanelsId= DualPanelsId)
        self.Client9.setStyleSheet("QLabel{ image: url(:/CLIENT_L1/CLIENT_L.png); }")
        self.Client9.setText("")
        self.Client9.setObjectName("Client9")
        self.gridLayout.addWidget(self.Client9, 6, 0, 1, 1)
        self.Client3 = customlabel(self, self.nodename, self.Destination, self.id, 3, self.Line, DualPanelsId= DualPanelsId)
        self.Client3.setStyleSheet("QLabel{ image: url(:/CLIENT_L1/CLIENT_L.png); }")
        self.Client3.setText("")
        self.Client3.setObjectName("Client3")
        self.gridLayout.addWidget(self.Client3, 3, 0, 1, 1)
        self.MP1H_Title = QtWidgets.QLabel(self)
        self.MP1H_Title.setStyleSheet("QLabel{ image: url(:/title/MP1H_title.png); }")
        self.MP1H_Title.setText("")
        self.MP1H_Title.setObjectName("MP1H_Title")
        self.gridLayout.addWidget(self.MP1H_Title, 1, 2, 2, 1)
        grid.addLayout(self.gridLayout,0,0)

    def contextMenuEvent(self, event):
        from BLANK_Demand.BLANK_Demand import BLANK_Demand
        ContextMenu = QMenu(self)
        CloseAction = ContextMenu.addAction("Close Panel")
            
        action = ContextMenu.exec_(self.mapToGlobal(event.pos()))

        if action == CloseAction:
            # removing old left panel
            panel_widget = Data["DemandPanel_" + str(self.id)].takeAt(0).widget()
            Data["DemandPanel_" + str(self.id)].removeWidget(panel_widget)
            panel_widget.deleteLater()
            Data["DemandPanel_" + self.id].addWidget(BLANK_Demand(self.id ,  self.nodename, self.Destination))

            # removing old right panel
            panel_widget = Data["DemandPanel_" + str(self.uppernum)].takeAt(0).widget()
            Data["DemandPanel_" + str(self.uppernum)].removeWidget(panel_widget)
            panel_widget.deleteLater()
            Data["DemandPanel_" + self.uppernum].addWidget(BLANK_Demand(self.id ,  self.nodename, self.Destination))

            if DemandTabDataBase["Panels"][self.nodename][self.id].LineCapacity != 0:

                for i in range(len(DemandTabDataBase["Panels"][self.nodename][self.id].ClientsCapacity)):
                    if DemandTabDataBase["Panels"][self.nodename][self.id].ClientsCapacity[i] != 0:
                        ids = [DemandTabDataBase["Panels"][self.nodename][self.id].DemandIdList[i], DemandTabDataBase["Panels"][self.nodename][self.id].ServiceIdList[i]]
                        type = DemandTabDataBase["Panels"][self.nodename][self.id].ClientsCapacity[i]

                        self.modify_ServiceList(ids= ids,
                                                source= self.nodename,
                                                destination= self.Destination,
                                                mode= "add",
                                                type= type)

                        # ** Dual **
                        self.modify_ServiceList(ids= ids,
                                                source= self.Destination,
                                                destination= self.nodename,
                                                mode= "add",
                                                type= type)

                LightPathId = DemandTabDataBase["Panels"][self.nodename][self.id].LightPathId

                if LightPathId is not None:
                    self.modify_LightPathList(  id= LightPathId,
                                                Source= self.nodename,
                                                Destination= self.Destination,
                                                mode= "delete",
                                                type= "100GE")

                    # ** Dual **
                    self.modify_LightPathList(  id= LightPathId,
                                                Source= self.Destination,
                                                Destination= self.nodename,
                                                mode= "delete",
                                                type= "100GE")

                    Data["NetworkObj"].del_lightpath(LightPathId)

            DemandTabDataBase["Panels"][self.nodename].pop(self.id)
            DemandTabDataBase["Panels"][self.nodename].pop(self.uppernum)

            # ** Dual **
            DemandTabDataBase["Panels"][self.Destination].pop(self.DualPanelsId[0])
            DemandTabDataBase["Panels"][self.Destination].pop(self.DualPanelsId[1])
        
    
    def modify_LightPathList(self, id, Source, Destination, Capacity = None, mode = "add", type = None, PanelId = None):

        if mode == "add":
            
            item = QListWidgetItem(type, Data["Demand_LightPath_list"])
            UserData = {"LightPathId":id, "Source":Source, "Destination":Destination, "Capacity":Capacity, "Type": type, "PanelId": PanelId}
            item.setToolTip(f"Source: {Source}\nDestination: {Destination}\nCapacity: {Capacity}\nType: {type}")
            item.setData(Qt.UserRole, UserData)
            item.setTextAlignment(Qt.AlignCenter)

            DemandTabDataBase["Lightpathes"][(Source, Destination)][id] = item
        
        if mode == "delete":
            # deleting desired lightpath from database
            DemandTabDataBase["Lightpathes"][(Source, Destination)].pop(id)

        Data["ui"].update_Demand_lightpath_list()
    
    def modify_ServiceList(self, ids, source, destination, mode = "delete", type = None, LightPathId = None):
        

        key = (int(ids[0]) , int(ids[1]))
        if mode == "delete":

            # check if its a normal service or not
            if key in DemandTabDataBase["Services"][(source, destination)]:
                DemandTabDataBase["Services"][(source, destination)][key] = 1
                DemandTabDataBase["Services_static"][source][key].setBackground(QBrush(Qt.white, Qt.SolidPattern))
            
            else:
                # adding MP1h_Client_Id to GroomOut10 Item
                UserData = DemandTabDataBase["GroomOut10"][(source, destination)][ids[1]].data(Qt.UserRole)

                MP1H_data = DemandTabDataBase["Lightpathes"][(source, destination)][LightPathId].data(Qt.UserRole)
                MP1H_Id = MP1H_data["PanelId"]

                index = DemandTabDataBase["Panels"][source][MP1H_Id].ServiceIdList.index(ids[1])
                UserData["MP1H_Client_Id"] = (MP1H_Id, str(index + 1))

                DemandTabDataBase["GroomOut10"][(source, destination)][ids[1]].setData(Qt.UserRole, UserData)

                DemandTabDataBase["GroomOut10_status"][(source, destination)][key[1]] = 1
            
            if source in DemandTabDataBase["Failed_Demands"]:
                if destination in DemandTabDataBase["Failed_Demands"][source]:

                    x = 0
                    for value in DemandTabDataBase["Services"][(source, destination)].values():

                        if value == 0:
                            x = 1
                            break
                    
                    for value in DemandTabDataBase["GroomOut10_status"][(source, destination)].values():
                        if value == 0:
                            x = 1
                            break
                    
                    if x == 0:
                        DemandTabDataBase["Failed_Demands"][source].remove(destination)

                        Data["ui"].Demand_combobox_highlight_on_off(Source= source,
                                                                    mode= "off",
                                                                    Target= destination)

                        # ** Dual **

                        DemandTabDataBase["Failed_Demands"][destination].remove(source)
                    
                    if not DemandTabDataBase["Failed_Demands"][source]:
                        Data["ui"].set_failed_nodes_default(source)
                        
                    # ** Dual **
                    if not DemandTabDataBase["Failed_Demands"][destination]:
                        Data["ui"].set_failed_nodes_default(destination)
            
            
        elif mode == "add":
            if type != "GroomOut10":
                DemandTabDataBase["Services"][(source, destination)][key] = 0
                DemandTabDataBase["Services_static"][source][key].setBackground(QBrush(QColor('#6088C6'), Qt.SolidPattern))

            else:
                font = DemandTabDataBase["GroomOut10"][(source, destination)][key[1]].font()
                font.setStrikeOut(False)
                DemandTabDataBase["GroomOut10"][(source, destination)][key[1]].setFont(font)

                DemandTabDataBase["GroomOut10_status"][(source, destination)][key[1]] = 0

                # deleting MP1h_Client_Id from GroomOut10 Item
                UserData = DemandTabDataBase["GroomOut10"][(source, destination)][ids[1]].data(Qt.UserRole)
                if "MP1H_Client_Id" in UserData:
                    UserData.pop("MP1H_Client_Id")

                    DemandTabDataBase["GroomOut10"][(source, destination)][ids[1]].setData(Qt.UserRole, UserData)
            
            if not ( source in DemandTabDataBase["Failed_Demands"]):
                DemandTabDataBase["Failed_Demands"][source] = [destination]
            
            elif not ( destination in DemandTabDataBase["Failed_Demands"][source] ):
                DemandTabDataBase["Failed_Demands"][source].append(destination)
            
            Data["ui"].Demand_combobox_highlight_on_off(Source= source,
                                                        mode= "on",
                                                        Target= destination)


            # ** Dual **
            if not ( destination in DemandTabDataBase["Failed_Demands"]):
                DemandTabDataBase["Failed_Demands"][destination] = [source]
            
            elif not ( source in DemandTabDataBase["Failed_Demands"][destination]):
                DemandTabDataBase["Failed_Demands"][destination].append(source)



            
        Data["ui"].UpdateDemand_ServiceList()


class line_class(QLabel):
    def __init__(self, parent, Destination):
        super().__init__(parent)
        self.Destination = Destination
    
    def mousePressEvent(self, event):
        
        if event.buttons() == QtCore.Qt.LeftButton:

            Data["ui"].Demand_Destination_combobox.setCurrentText(self.Destination)

class customlabel(QLabel):
    def __init__(self, parent, nodename, Destination, ID, ClientNum, LineVar, tooltip = None, DualPanelsId = None):
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

        self.DualPanelsId = DualPanelsId
    
    def dragEnterEvent(self, event):
        e = event.mimeData()
        model = QStandardItemModel()
        model.dropMimeData(event.mimeData(), Qt.CopyAction, 0,0, QModelIndex())
        dragtext = model.item(0,0).text()
        UserData = model.item(0).data(Qt.UserRole)
        
        self.allowedservices = ["10GE", "STM_64", "GroomOut10"]
        
        if dragtext != "MP1H":
            servicetype = dragtext.strip()

            if servicetype in self.allowedservices:
                if servicetype == "GroomOut10":
                    if (not model.item(0).font().strikeOut()) and UserData["GroomOut10Id"] in DemandTabDataBase["GroomOut10"][(self.nodename, self.Destination)]:
                        if self.ClientNum % 2 == 0:
                            self.setStyleSheet("image: url(:/CLIENT_L_Selected_SOURCE/CLIENT_L_Selected.png);")
                        else:
                            self.setStyleSheet("image: url(:/CLIENT_R_Selected_SOURCE/CLIENT_R_Selected.png);")

                        event.accept()
                            
                elif DemandTabDataBase["Services"][(self.nodename, self.Destination)].get((UserData["DemandId"], UserData["ServiceId"])) == 0:
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

        servicetype = dragtext.strip()

        if servicetype in self.allowedservices:

            self.servicetype = servicetype
            if self.servicetype != "GroomOut10":
                self.ids = (UserData["DemandId"], UserData["ServiceId"])
                self.setToolTip(DemandTabDataBase["Services_static"][self.nodename][self.ids].toolTip())
            else:
                self.ids = (UserData["DemandId"], UserData["GroomOut10Id"])
                self.setToolTip(DemandTabDataBase["GroomOut10"][(self.nodename, self.Destination)][self.ids[1]].toolTip())
            
            

            # updating LineCapacity part of panel object
            if servicetype == "10GE":
                DemandTabDataBase["Panels"][self.nodename][self.id].LineCapacity += self.GE_10_BW

                # ** Dual **
                DemandTabDataBase["Panels"][self.Destination][self.DualPanelsId[0]].LineCapacity += self.GE_10_BW

            elif servicetype == "STM_64":
                DemandTabDataBase["Panels"][self.nodename][self.id].LineCapacity += self.STM_64_BW

                # ** Dual ** 
                DemandTabDataBase["Panels"][self.Destination][self.DualPanelsId[0]].LineCapacity += self.STM_64_BW
            else:
                # if its GroomOut10
                DemandTabDataBase["Panels"][self.nodename][self.id].LineCapacity += UserData["Capacity"]

                # ** Dual **
                DemandTabDataBase["Panels"][self.Destination][self.DualPanelsId[0]].LineCapacity += UserData["Capacity"]
                self.GroomOut_Capacity = UserData["Capacity"]

            # updating ClientsCapacity part of Panel object
            DemandTabDataBase["Panels"][self.nodename][self.id].ClientsCapacity[self.ClientNum] = servicetype

            # ** Dual **
            DemandTabDataBase["Panels"][self.Destination][self.DualPanelsId[0]].ClientsCapacity[self.ClientNum] = servicetype

            ServiceListLen = len(DemandTabDataBase["Panels"][self.nodename][self.id].ServiceIdList)
            if self.ClientNum >= ServiceListLen:
                for i in range(ServiceListLen - self.ClientNum + 1):
                    DemandTabDataBase["Panels"][self.nodename][self.id].ServiceIdList.append(None)

                    # ** Dual **
                    DemandTabDataBase["Panels"][self.Destination][self.DualPanelsId[0]].ServiceIdList.append(None)

            # updating ServiceIdList of Panel Object         
            DemandTabDataBase["Panels"][self.nodename][self.id].ServiceIdList[self.ClientNum] = self.ids[1]

            # ** Dual **
            DemandTabDataBase["Panels"][self.Destination][self.DualPanelsId[0]].ServiceIdList[self.ClientNum] = self.ids[1]
            
            # updating DemandIdList of Panel Object
            DemandTabDataBase["Panels"][self.nodename][self.id].DemandIdList[self.ClientNum] = self.ids[0]

            # ** Dual **
            DemandTabDataBase["Panels"][self.Destination][self.DualPanelsId[0]].DemandIdList[self.ClientNum] = self.ids[0]
            
            

            if DemandTabDataBase["Panels"][self.nodename][self.id].LightPath_flag == 0:

                # updating networkobj
                ServiceIdList = [self.ids[1]]

                ClusterNum = 0
                for cluster_id , value in Data["NetworkObj"].PhysicalTopology.ClusterDict.items():

                    if Data["ui"].NodeIdMap[self.nodename] == value.GatewayId and Data["ui"].NodeIdMap[self.Destination] in value.SubNodesId:
                        ClusterNum = cluster_id
                        break
                    
                    elif Data["ui"].NodeIdMap[self.Destination] == value.GatewayId and Data["ui"].NodeIdMap[self.nodename] in value.SubNodesId:
                        ClusterNum = cluster_id
                        break
                    
                    elif Data["ui"].NodeIdMap[self.Destination] in value.SubNodesId and Data["ui"].NodeIdMap[self.nodename] in value.SubNodesId:
                        ClusterNum = cluster_id
                        break

                Data["NetworkObj"].add_lightpath(Data["NodeIdMap"][self.nodename], Data["NodeIdMap"][self.Destination], 10, ServiceIdList, "100GE", self.ids[0], ClusterNum= ClusterNum)
                LightPathId = max(Data["NetworkObj"].LightPathDict.keys())
                DemandTabDataBase["Panels"][self.nodename][self.id].LightPathId = LightPathId

                # ** Dual **
                DemandTabDataBase["Panels"][self.Destination][self.DualPanelsId[0]].LightPathId = LightPathId

                self.modify_LightPathList(id= DemandTabDataBase["Panels"][self.nodename][self.id].LightPathId,
                                            Source= self.nodename,
                                            Destination= self.Destination,
                                            Capacity= DemandTabDataBase["Panels"][self.nodename][self.id].LineCapacity,
                                            mode= "add",
                                            type= "100GE",
                                            PanelId= self.id)

                # ** Dual **
                self.modify_LightPathList(id= DemandTabDataBase["Panels"][self.nodename][self.id].LightPathId,
                                            Source= self.Destination,
                                            Destination= self.nodename,
                                            Capacity= DemandTabDataBase["Panels"][self.nodename][self.id].LineCapacity,
                                            mode= "add",
                                            type= "100GE",
                                            PanelId= self.DualPanelsId[0])

                DemandTabDataBase["Panels"][self.nodename][self.id].LightPath_flag = 1

                # ** Dual **
                DemandTabDataBase["Panels"][self.Destination][self.DualPanelsId[0]].LightPath_flag = 1

                self.modify_ServiceList(self.ids, self.nodename, self.Destination, LightPathId= LightPathId, type= self.servicetype)

                # ** Dual **
                self.modify_ServiceList(self.ids, self.Destination, self.nodename, LightPathId= LightPathId, type= self.servicetype)

                
            else:
                ServiceIdList = [self.ids[1]]
                LightPathId = DemandTabDataBase["Panels"][self.nodename][self.id].LightPathId
                Data["NetworkObj"].LightPathDict[LightPathId].ServiceIdList.extend(ServiceIdList)

                self.modify_ServiceList(self.ids, self.nodename, self.Destination, LightPathId= LightPathId, type= self.servicetype)

                # ** Dual **
                self.modify_ServiceList(self.ids, self.Destination, self.nodename, LightPathId= LightPathId, type= self.servicetype)

            # adding LightPathId to groomOut object
            if self.servicetype == "GroomOut10":
                Data["NetworkObj"].TrafficMatrix.GroomOut10Dict[(self.ids[0],UserData["GroomOut10Id"])].LightPathId = LightPathId

                # stricking out item
                font = DemandTabDataBase["GroomOut10"][(self.nodename, self.Destination)][UserData["GroomOut10Id"]].font()
                font.setStrikeOut(True)
                DemandTabDataBase["GroomOut10"][(self.nodename, self.Destination)][UserData["GroomOut10Id"]].setFont(font)

                DemandTabDataBase["GroomOut10_status"][(self.nodename, self.Destination)][UserData["GroomOut10Id"]] = 1

                # ** Dual **
                DemandTabDataBase["GroomOut10"][(self.Destination, self.nodename)][UserData["GroomOut10Id"]].setFont(font)

                DemandTabDataBase["GroomOut10_status"][(self.Destination, self.nodename)][UserData["GroomOut10Id"]] = 1

            self.setAcceptDrops(False)
            
            # updating LightPath ListWidgetItem Capacity
            self.Update_LineListWidgetItem_Tooltip( Item= DemandTabDataBase["Lightpathes"][(self.nodename, self.Destination)][LightPathId],
                                                    Capacity= DemandTabDataBase["Panels"][self.nodename][self.id].LineCapacity)

            # ** Dual **
            self.Update_LineListWidgetItem_Tooltip( Item= DemandTabDataBase["Lightpathes"][(self.Destination, self.nodename)][LightPathId],
                                                    Capacity= DemandTabDataBase["Panels"][self.nodename][self.id].LineCapacity)

            # setting line port tooltip                                        
            self.LineVar.setToolTip(DemandTabDataBase["Lightpathes"][(self.nodename, self.Destination)][LightPathId].toolTip())

            self.LineVar.setStyleSheet("QLabel{ image: url(:/Line_Selected_SOURCE/Line_Selected.png); }")
        else:
            if self.ClientNum % 2 == 0:
                self.setStyleSheet("image: url(:/CLIENT_L1/CLIENT_L.png);")
            else:
                self.setStyleSheet("image: url(:/client_r/CLIENT_R.png);")
    
    def check_clients(self, ClientsList):
                x = 0
                for i in range(10):
                    if ClientsList[i] != 0:
                        x = 1
                return x

    def contextMenuEvent(self, event):

        

        ContextMenu = QMenu(self)
        ClearAction = ContextMenu.addAction("..Clear Socket..")
        
        action = ContextMenu.exec_(self.mapToGlobal(event.pos()))

        if action == ClearAction:
            if DemandTabDataBase["Panels"][self.nodename][self.id].ClientsCapacity[self.ClientNum] != 0:
                self.setToolTip("")
                
                if self.servicetype == "10GE":
                    DemandTabDataBase["Panels"][self.nodename][self.id].LineCapacity -= self.GE_10_BW

                    # ** Dual **
                    DemandTabDataBase["Panels"][self.Destination][self.DualPanelsId[0]].LineCapacity -= self.GE_10_BW

                elif self.servicetype == "STM_64":
                    DemandTabDataBase["Panels"][self.nodename][self.id].LineCapacity -= self.STM_64_BW

                    # ** Dual **
                    DemandTabDataBase["Panels"][self.Destination][self.DualPanelsId[0]].LineCapacity -= self.STM_64_BW
                else:
                    DemandTabDataBase["Panels"][self.nodename][self.id].LineCapacity -= self.GroomOut_Capacity

                    # ** Dual **
                    DemandTabDataBase["Panels"][self.Destination][self.DualPanelsId[0]].LineCapacity -= self.GroomOut_Capacity
                
                DemandTabDataBase["Panels"][self.nodename][self.id].ClientsCapacity[self.ClientNum] = 0

                # ** Dual **
                DemandTabDataBase["Panels"][self.Destination][self.DualPanelsId[0]].ClientsCapacity[self.ClientNum] = 0

                # removing service id from lightpath object in common object
                LightPathId = DemandTabDataBase["Panels"][self.nodename][self.id].LightPathId
                Data["NetworkObj"].LightPathDict[LightPathId].ServiceIdList.remove(self.ids[1])
                
                if self.servicetype != "GroomOut10":
                    DemandTabDataBase["Panels"][self.nodename][self.id].ServiceIdList[self.ClientNum] = None

                    DemandTabDataBase["Panels"][self.Destination][self.DualPanelsId[0]].ServiceIdList[self.ClientNum] = None

                if self.ClientNum % 2 == 0:
                    self.setStyleSheet("image: url(:/CLIENT_L1/CLIENT_L.png);")
                else:
                    self.setStyleSheet("image: url(:/client_r/CLIENT_R.png);")

                self.setAcceptDrops(True)


                self.modify_ServiceList(ids= self.ids,
                                        source= self.nodename,
                                        destination= self.Destination,
                                        mode= "add",
                                        type= self.servicetype)

                # ** Dual **
                self.modify_ServiceList(ids= self.ids,
                                        source= self.Destination,
                                        destination= self.nodename,
                                        mode= "add",
                                        type= self.servicetype)

                

                # updating LightPath ListWidgetItem Capacity
                self.Update_LineListWidgetItem_Tooltip( Item= DemandTabDataBase["Lightpathes"][(self.nodename, self.Destination)][LightPathId],
                                                        Capacity= DemandTabDataBase["Panels"][self.nodename][self.id].LineCapacity)

                self.Update_LineListWidgetItem_Tooltip( Item= DemandTabDataBase["Lightpathes"][(self.Destination, self.nodename)][LightPathId],
                                                        Capacity= DemandTabDataBase["Panels"][self.nodename][self.id].LineCapacity)

                # setting line port tooltip                                        
                self.LineVar.setToolTip(DemandTabDataBase["Lightpathes"][(self.nodename, self.Destination)][LightPathId].toolTip())

                x = self.check_clients(DemandTabDataBase["Panels"][self.nodename][self.id].ClientsCapacity)

                if x == 0:
                    
                    self.modify_LightPathList(  id= LightPathId,
                                                Source= self.nodename,
                                                Destination= self.Destination,
                                                mode= "delete",
                                                type= "100GE")

                    # ** Dual **
                    self.modify_LightPathList(  id= LightPathId,
                                                Source= self.Destination,
                                                Destination= self.nodename,
                                                mode= "delete",
                                                type= "100GE")

                    # deleting lightpath object from network obj
                    Data["NetworkObj"].del_lightpath(LightPathId)

                    DemandTabDataBase["Panels"][self.nodename][self.id].LightPathId = None

                    # ** Dual **
                    DemandTabDataBase["Panels"][self.Destination][self.DualPanelsId[0]].LightPathId = None
                    
                    DemandTabDataBase["Panels"][self.nodename][self.id].LightPath_flag = 0

                    # ** Dual **
                    DemandTabDataBase["Panels"][self.Destination][self.DualPanelsId[0]].LightPath_flag = 0

                    self.LineVar.setStyleSheet("QLabel{ image: url(:/line/line.png); }")
    
    def Clear_From_MP2X(self):
        if DemandTabDataBase["Panels"][self.nodename][self.id].ClientsCapacity[self.ClientNum] != 0:
            self.setToolTip("")
            
            if self.servicetype == "10GE":
                DemandTabDataBase["Panels"][self.nodename][self.id].LineCapacity -= self.GE_10_BW

                # ** Dual **
                DemandTabDataBase["Panels"][self.Destination][self.DualPanelsId[0]].LineCapacity -= self.GE_10_BW

            elif self.servicetype == "STM_64":
                DemandTabDataBase["Panels"][self.nodename][self.id].LineCapacity -= self.STM_64_BW

                # ** Dual **
                DemandTabDataBase["Panels"][self.Destination][self.DualPanelsId[0]].LineCapacity -= self.STM_64_BW
            else:
                DemandTabDataBase["Panels"][self.nodename][self.id].LineCapacity -= self.GroomOut_Capacity

                # ** Dual **
                DemandTabDataBase["Panels"][self.Destination][self.DualPanelsId[0]].LineCapacity -= self.GroomOut_Capacity
            
            DemandTabDataBase["Panels"][self.nodename][self.id].ClientsCapacity[self.ClientNum] = 0

            # ** Dual **
            DemandTabDataBase["Panels"][self.Destination][self.DualPanelsId[0]].ClientsCapacity[self.ClientNum] = 0

            # removing service id from lightpath object in common object
            LightPathId = DemandTabDataBase["Panels"][self.nodename][self.id].LightPathId
            Data["NetworkObj"].LightPathDict[LightPathId].ServiceIdList.remove(self.ids[1])
            
            if self.servicetype != "GroomOut10":
                DemandTabDataBase["Panels"][self.nodename][self.id].ServiceIdList[self.ClientNum] = None

                DemandTabDataBase["Panels"][self.Destination][self.DualPanelsId[0]].ServiceIdList[self.ClientNum] = None

            if self.ClientNum % 2 == 0:
                self.setStyleSheet("image: url(:/CLIENT_L1/CLIENT_L.png);")
            else:
                self.setStyleSheet("image: url(:/client_r/CLIENT_R.png);")

            self.setAcceptDrops(True)


            self.modify_ServiceList(ids= self.ids,
                                    source= self.nodename,
                                    destination= self.Destination,
                                    mode= "add",
                                    type= self.servicetype)

            # ** Dual **
            self.modify_ServiceList(ids= self.ids,
                                    source= self.Destination,
                                    destination= self.nodename,
                                    mode= "add",
                                    type= self.servicetype)

            

            # updating LightPath ListWidgetItem Capacity
            self.Update_LineListWidgetItem_Tooltip( Item= DemandTabDataBase["Lightpathes"][(self.nodename, self.Destination)][LightPathId],
                                                    Capacity= DemandTabDataBase["Panels"][self.nodename][self.id].LineCapacity)

            self.Update_LineListWidgetItem_Tooltip( Item= DemandTabDataBase["Lightpathes"][(self.Destination, self.nodename)][LightPathId],
                                                    Capacity= DemandTabDataBase["Panels"][self.nodename][self.id].LineCapacity)

            # setting line port tooltip                                        
            self.LineVar.setToolTip(DemandTabDataBase["Lightpathes"][(self.nodename, self.Destination)][LightPathId].toolTip())

            x = self.check_clients(DemandTabDataBase["Panels"][self.nodename][self.id].ClientsCapacity)

            if x == 0:
                
                self.modify_LightPathList(  id= LightPathId,
                                            Source= self.nodename,
                                            Destination= self.Destination,
                                            mode= "delete",
                                            type= "100GE")

                # ** Dual **
                self.modify_LightPathList(  id= LightPathId,
                                            Source= self.Destination,
                                            Destination= self.nodename,
                                            mode= "delete",
                                            type= "100GE")

                # deleting lightpath object from network obj
                Data["NetworkObj"].del_lightpath(LightPathId)

                DemandTabDataBase["Panels"][self.nodename][self.id].LightPathId = None

                # ** Dual **
                DemandTabDataBase["Panels"][self.Destination][self.DualPanelsId[0]].LightPathId = None
                
                DemandTabDataBase["Panels"][self.nodename][self.id].LightPath_flag = 0

                # ** Dual **
                DemandTabDataBase["Panels"][self.Destination][self.DualPanelsId[0]].LightPath_flag = 0

                self.LineVar.setStyleSheet("QLabel{ image: url(:/line/line.png); }")

                    
    def Update_LineListWidgetItem_Tooltip(self, Item, Capacity):       
        
        UserData = Item.data(Qt.UserRole)
        UserData["Capacity"] = Capacity
        Item.setData(Qt.UserRole, UserData)
        Item.setToolTip(f"Source: {UserData['Source']}\nDestination: {UserData['Destination']}\nCapacity: {Capacity}\nType: {UserData['Type']}")

    def modify_ServiceList(self, ids, source, destination, mode = "delete", type = None, LightPathId = None):
        

        key = (int(ids[0]) , int(ids[1]))
        if mode == "delete":

            # check if its a normal service or not
            if key in DemandTabDataBase["Services"][(source, destination)]:
                DemandTabDataBase["Services"][(source, destination)][key] = 1
                DemandTabDataBase["Services_static"][source][key].setBackground(QBrush(Qt.white, Qt.SolidPattern))
            
            else:
                # adding MP1h_Client_Id to GroomOut10 Item
                UserData = DemandTabDataBase["GroomOut10"][(source, destination)][ids[1]].data(Qt.UserRole)

                MP1H_data = DemandTabDataBase["Lightpathes"][(source, destination)][LightPathId].data(Qt.UserRole)
                MP1H_Id = MP1H_data["PanelId"]

                index = DemandTabDataBase["Panels"][source][MP1H_Id].ServiceIdList.index(ids[1])
                UserData["MP1H_Client_Id"] = (MP1H_Id, str(index + 1))

                DemandTabDataBase["GroomOut10"][(source, destination)][ids[1]].setData(Qt.UserRole, UserData)

                DemandTabDataBase["GroomOut10_status"][(source, destination)][key[1]] = 1
            
            if source in DemandTabDataBase["Failed_Demands"]:
                if destination in DemandTabDataBase["Failed_Demands"][source]:

                    x = 0
                    for value in DemandTabDataBase["Services"][(source, destination)].values():

                        if value == 0:
                            x = 1
                            break
                    
                    for value in DemandTabDataBase["GroomOut10_status"][(source, destination)].values():
                        if value == 0:
                            x = 1
                            break
                    
                    if x == 0:
                        DemandTabDataBase["Failed_Demands"][source].remove(destination)

                        Data["ui"].Demand_combobox_highlight_on_off(Source= source,
                                                                    mode= "off",
                                                                    Target= destination)

                        # ** Dual **

                        DemandTabDataBase["Failed_Demands"][destination].remove(source)
                    
                    if not DemandTabDataBase["Failed_Demands"][source]:
                        Data["ui"].set_failed_nodes_default(source)
                        
                    # ** Dual **
                    if not DemandTabDataBase["Failed_Demands"][destination]:
                        Data["ui"].set_failed_nodes_default(destination)
            
            
        elif mode == "add":
            if type != "GroomOut10":
                DemandTabDataBase["Services"][(source, destination)][key] = 0
                DemandTabDataBase["Services_static"][source][key].setBackground(QBrush(QColor('#6088C6'), Qt.SolidPattern))

            else:
                font = DemandTabDataBase["GroomOut10"][(source, destination)][key[1]].font()
                font.setStrikeOut(False)
                DemandTabDataBase["GroomOut10"][(source, destination)][key[1]].setFont(font)

                DemandTabDataBase["GroomOut10_status"][(source, destination)][key[1]] = 0

                # deleting MP1h_Client_Id from GroomOut10 Item
                UserData = DemandTabDataBase["GroomOut10"][(source, destination)][ids[1]].data(Qt.UserRole)
                if "MP1H_Client_Id" in UserData:
                    UserData.pop("MP1H_Client_Id")

                    DemandTabDataBase["GroomOut10"][(source, destination)][ids[1]].setData(Qt.UserRole, UserData)
            
            if not ( source in DemandTabDataBase["Failed_Demands"]):
                DemandTabDataBase["Failed_Demands"][source] = [destination]
            
            elif not ( destination in DemandTabDataBase["Failed_Demands"][source] ):
                DemandTabDataBase["Failed_Demands"][source].append(destination)
            
            Data["ui"].Demand_combobox_highlight_on_off(Source= source,
                                                        mode= "on",
                                                        Target= destination)


            # ** Dual **
            if not ( destination in DemandTabDataBase["Failed_Demands"]):
                DemandTabDataBase["Failed_Demands"][destination] = [source]
            
            elif not ( source in DemandTabDataBase["Failed_Demands"][destination]):
                DemandTabDataBase["Failed_Demands"][destination].append(source)



            
        Data["ui"].UpdateDemand_ServiceList()
        
    
    def modify_LightPathList(self, id, Source, Destination, Capacity = None, mode = "add", type = None, PanelId = None):

        if mode == "add":
            
            item = QListWidgetItem(type, Data["Demand_LightPath_list"])
            UserData = {"LightPathId":id, "Source":Source, "Destination":Destination, "Capacity":Capacity, "Type": type, "PanelId": PanelId}
            item.setToolTip(f"Source: {Source}\nDestination: {Destination}\nCapacity: {Capacity}\nType: {type}")
            item.setData(Qt.UserRole, UserData)
            item.setTextAlignment(Qt.AlignCenter)

            DemandTabDataBase["Lightpathes"][(Source, Destination)][id] = item
        
        if mode == "delete":
            # deleting desired lightpath from database
            DemandTabDataBase["Lightpathes"][(Source, Destination)].pop(id)
            
        Data["ui"].update_Demand_lightpath_list()


if __name__ == "__main__":

    app = QtWidgets.QApplication([])
    window = MP1H_L_Demand(1,2,3)
    window.show()
    sys.exit(app.exec_())

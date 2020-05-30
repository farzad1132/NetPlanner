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
from TP1H_Demand import TP1H_CLIENT_Selected
from TP1H_Demand import Line_Selected
from TP1H_Demand import Border_L

# USE THIS CODE TO CHANGE THE CLIENT TO SELECTED CLIENT:
#self.Client.setStyleSheet("image: url(:/TP1H_CLIENT_Selected_SOURCE/TP1H_CLIENT_Selected.png);")

# USE THIS CODE TO CHANGE THE LINE TO SELECTED LINE:
# self.Line.setStyleSheet("QLabel{ image: url(:/Line_Selected_SOURCE/Line_Selected.png); }")

class TP1H_L_Demand(QtWidgets.QWidget):

    def __init__(self, Panel_ID, nodename, Destination, DualPanelsId):
        super(TP1H_L_Demand, self).__init__()

        #self.resize(94, 511)

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
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setObjectName("gridLayout")
        self.Line = QtWidgets.QLabel(self)
        self.Line.setMinimumSize(QtCore.QSize(0, 25))
        self.Line.setMaximumSize(QtCore.QSize(100, 200))
        self.Line.setStyleSheet("QLabel{ image: url(:/Line/tp1h_line.png); }")
        self.Line.setText("")
        self.Line.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Line.setObjectName("Line")
        self.gridLayout.addWidget(self.Line, 1, 0, 3, 1)
        self.Socket_Top = QtWidgets.QLabel(self)
        self.Socket_Top.setStyleSheet("QLabel{ image: url(:/Socket/socket1.png); }")
        self.Socket_Top.setText("")
        self.Socket_Top.setObjectName("Socket_Top")
        self.gridLayout.addWidget(self.Socket_Top, 0, 0, 1, 1)
        self.Socket_Bottom = QtWidgets.QLabel(self)
        self.Socket_Bottom.setStyleSheet("QLabel{ image: url(:/Socket_bottom/socket2.png); }")
        self.Socket_Bottom.setText("")
        self.Socket_Bottom.setObjectName("Socket_Bottom")
        self.gridLayout.addWidget(self.Socket_Bottom, 7, 0, 1, 1)
        self.Client = customlabel(self, self.nodename, self.Destination, self.id, self.Line, DualPanelsId= DualPanelsId)
        self.Client.setMinimumSize(QtCore.QSize(0, 25))
        self.Client.setStyleSheet("QLabel{ image:  url(:/Client/TP1H_CLIENT.png); }")
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
        self.TP1H_Title.setStyleSheet("QLabel{ image: url(:/title/title.png); }")
        self.TP1H_Title.setText("")
        self.TP1H_Title.setObjectName("TP1H_Title")
        self.gridLayout.addWidget(self.TP1H_Title, 0, 2, 2, 1)
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

            # TODO: undo every service or lightpath that is created in this panel
            if DemandTabDataBase["Panels"][self.nodename][self.id].Line == "100GE":
                ids = [DemandTabDataBase["Panels"][self.nodename][self.id].DemandId, DemandTabDataBase["Panels"][self.nodename][self.id].ServiceId]

                self.modify_ServiceList(ids= ids,
                                            source= self.nodename,
                                            destination= self.Destination,
                                            mode= "add",
                                            type= "100GE")

                # ** Dual **
                self.modify_ServiceList(ids= ids,
                                            source= self.Destination,
                                            destination= self.nodename,
                                            mode= "add",
                                            type= "100GE")

                LightPathId = DemandTabDataBase["Panels"][self.nodename][self.id].LightPathId
                
                #self.modify_LightPathList(LightPathId, self.nodename, self.Destination, mode="delete", type="100GE")
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

                self.Line.setStyleSheet("image:  url(:/Client/TP1H_CLIENT.png);")

            DemandTabDataBase["Panels"][self.nodename].pop(self.id)
            DemandTabDataBase["Panels"][self.nodename].pop(self.uppernum)

            # ** Dual ** 
            DemandTabDataBase["Panels"][self.Destination].pop(self.DualPanelsId[0])
            DemandTabDataBase["Panels"][self.Destination].pop(self.DualPanelsId[1])
        
    
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
            """ for Des in DemandTabDataBase["Source_Destination"][Source]["DestinationList"]:
                for UpperId in sorted(list(DemandTabDataBase["Lightpathes"][(Source, Des)].keys())):
                    if UpperId > id:
                        DemandTabDataBase["Lightpathes"][(Source, Des)][UpperId - 1] = DemandTabDataBase["Lightpathes"][(Source, Des)].pop(UpperId)
                        UserData = DemandTabDataBase["Lightpathes"][(Source, Des)][UpperId - 1].data(Qt.UserRole)
                        UserData["LightPathId"] -= 1
                        DemandTabDataBase["Lightpathes"][(Source, Des)][UpperId - 1].setData(Qt.UserRole, UserData) """ 
 
        
        Data["ui"].update_Demand_lightpath_list()
    
    def modify_ServiceList(self, ids, source, destination, mode = "delete", type = None):
        

        key = (int(ids[0]) , int(ids[1]))
        if mode == "delete":
            DemandTabDataBase["Services"][(source, destination)][key] = 1
            DemandTabDataBase["Services_static"][source][key].setBackground(QBrush(Qt.white, Qt.SolidPattern))

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

                        DemandTabDataBase["Failed_Demands"][destination].remove(source)
                    
                    if not DemandTabDataBase["Failed_Demands"][source]:
                        Data["ui"].set_failed_nodes_default(source)
                    
                    if not DemandTabDataBase["Failed_Demands"][destination]:
                        Data["ui"].set_failed_nodes_default(destination)
            
        elif mode == "add":
            DemandTabDataBase["Services"][(source, destination)][key] = 0
            DemandTabDataBase["Services_static"][source][key].setBackground(QBrush(QColor('#6088C6'), Qt.SolidPattern))

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
        

class customlabel(QLabel):
    def __init__(self, parent, nodename, Destination, ID, LineVar, tooltip = None, DualPanelsId = None):
        super().__init__(parent)
        self.nodename = nodename
        self.LineVar = LineVar
        self.id = ID
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

        self.allowedservices = ["100GE"]
        

        servicetype = dragtext.strip()

        if servicetype in self.allowedservices:
            if DemandTabDataBase["Services"][(self.nodename, self.Destination)].get((UserData["DemandId"], UserData["ServiceId"])) == 0:
            
                self.setStyleSheet("image: url(:/TP1H_CLIENT_Selected_SOURCE/TP1H_CLIENT_Selected.png);")
                event.accept()

        super(customlabel,self).dragEnterEvent(event)
    

    def dragLeaveEvent(self, event):
        self.setStyleSheet("image:  url(:/Client/TP1H_CLIENT.png);")

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
            

            DemandTabDataBase["Panels"][self.nodename][self.id].Line = "100GE"
            DemandTabDataBase["Panels"][self.nodename][self.id].ServiceId = self.ids[1]
            DemandTabDataBase["Panels"][self.nodename][self.id].DemandId = self.ids[0]
            self.modify_ServiceList(self.ids, self.nodename, self.Destination)

            # ** Dual **
            DemandTabDataBase["Panels"][self.Destination][self.DualPanelsId[0]].Line = "100GE"
            DemandTabDataBase["Panels"][self.Destination][self.DualPanelsId[0]].ServiceId = self.ids[1]
            DemandTabDataBase["Panels"][self.Destination][self.DualPanelsId[0]].DemandId = self.ids[0]
            self.modify_ServiceList(self.ids, self.Destination, self.nodename)

            self.setStyleSheet("image: url(:/TP1H_CLIENT_Selected_SOURCE/TP1H_CLIENT_Selected.png);")
            # self.LightPathId = Network.Lightpath.get_id()

            # adding lightpath to network obj

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

            Data["NetworkObj"].add_lightpath(Data["NodeIdMap"][self.nodename], Data["NodeIdMap"][self.Destination], 100, [self.ids[1]], "100GE", self.ids[0])
            self.LightPathId = max(Data["NetworkObj"].LightPathDict.keys())

            # adding lightpath to internal database
            DemandTabDataBase["Panels"][self.nodename][self.id].LightPathId = self.LightPathId

            # ** Dual **
            DemandTabDataBase["Panels"][self.Destination][self.DualPanelsId[0]].LightPathId = self.LightPathId

            #self.modify_LightPathList(self.LightPathId, self.nodename, self.Destination, mode= "add", type="100GE")
            self.modify_LightPathList(      id= DemandTabDataBase["Panels"][self.nodename][self.id].LightPathId,
                                            Source= self.nodename,
                                            Destination= self.Destination,
                                            Capacity= DemandTabDataBase["Panels"][self.nodename][self.id].Line,
                                            mode= "add",
                                            type= "100GE",
                                            PanelId= self.id)

            # ** Dual ** 
            self.modify_LightPathList(      id= DemandTabDataBase["Panels"][self.Destination][self.DualPanelsId[0]].LightPathId,
                                            Source= self.Destination,
                                            Destination= self.nodename,
                                            Capacity= DemandTabDataBase["Panels"][self.nodename][self.id].Line,
                                            mode= "add",
                                            type= "100GE",
                                            PanelId= self.DualPanelsId[0])

            # setting line port tooltip                                        
            self.LineVar.setToolTip(DemandTabDataBase["Lightpathes"][(self.nodename, self.Destination)][self.LightPathId].toolTip())

            self.LineVar.setStyleSheet("QLabel{ image: url(:/Line_Selected_SOURCE/Line_Selected.png); }")


            # TODO: be Careful !!!!!
            self.setAcceptDrops(False)  
        else:
            self.setStyleSheet("image:  url(:/Client/TP1H_CLIENT.png);")

    def contextMenuEvent(self, event):
        ContextMenu = QMenu(self)
        ClearAction = ContextMenu.addAction("..Clear Socket..")
        
        action = ContextMenu.exec_(self.mapToGlobal(event.pos()))

        if action == ClearAction:
            if DemandTabDataBase["Panels"][self.nodename][self.id].Line == "100GE":
                self.setToolTip("")

                # deleting lightpath from network object
                
                
                
                self.setStyleSheet("image:  url(:/Client/TP1H_CLIENT.png);")
                self.setAcceptDrops(True)
                #self.modify_ServiceList(self.ids, self.nodename, self.Destination, mode = "add", type = "100GE")
                self.modify_ServiceList(ids= self.ids,
                                            source= self.nodename,
                                            destination= self.Destination,
                                            mode= "add",
                                            type= "100GE")

                # ** Dual **
                self.modify_ServiceList(ids= self.ids,
                                            source= self.Destination,
                                            destination= self.nodename,
                                            mode= "add",
                                            type= "100GE")

                #self.modify_LightPathList(self.LightPathId, self.nodename, self.Destination, mode="delete", type="100GE")
                self.modify_LightPathList(  id= DemandTabDataBase["Panels"][self.nodename][self.id].LightPathId,
                                                Source= self.nodename,
                                                Destination= self.Destination,
                                                mode= "delete",
                                                type= "100GE")

                # ** Dual **
                self.modify_LightPathList(  id= DemandTabDataBase["Panels"][self.Destination][self.DualPanelsId[0]].LightPathId,
                                                Source= self.Destination,
                                                Destination= self.nodename,
                                                mode= "delete",
                                                type= "100GE")

                self.LineVar.setStyleSheet("QLabel{ image: url(:/Line/tp1h_line.png); }")

                
                
                #Network.Lightpath.update_id(-1)
                Data["NetworkObj"].del_lightpath(DemandTabDataBase["Panels"][self.nodename][self.id].LightPathId)

                DemandTabDataBase["Panels"][self.nodename][self.id].Line = 0
                DemandTabDataBase["Panels"][self.nodename][self.id].LightPathId = None
                DemandTabDataBase["Panels"][self.nodename][self.id].ServiceId = None

                # ** Dual **
                DemandTabDataBase["Panels"][self.Destination][self.DualPanelsId[0]].Line = 0
                DemandTabDataBase["Panels"][self.Destination][self.DualPanelsId[0]].LightPathId = None
                DemandTabDataBase["Panels"][self.Destination][self.DualPanelsId[0]].ServiceId = None

                
    

    def modify_ServiceList(self, ids, source, destination, mode = "delete", type = None):
        

        key = (int(ids[0]) , int(ids[1]))
        if mode == "delete":
            DemandTabDataBase["Services"][(source, destination)][key] = 1
            DemandTabDataBase["Services_static"][source][key].setBackground(QBrush(Qt.white, Qt.SolidPattern))

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

                        DemandTabDataBase["Failed_Demands"][destination].remove(source)
                    
                    if not DemandTabDataBase["Failed_Demands"][source]:
                        Data["ui"].set_failed_nodes_default(source)
                    
                    if not DemandTabDataBase["Failed_Demands"][destination]:
                        Data["ui"].set_failed_nodes_default(destination)
            
        elif mode == "add":
            DemandTabDataBase["Services"][(source, destination)][key] = 0
            DemandTabDataBase["Services_static"][source][key].setBackground(QBrush(QColor('#6088C6'), Qt.SolidPattern))

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

 
        
        Data["ui"].update_Demand_lightpath_list()

if __name__ == "__main__":

    app = QtWidgets.QApplication([])
    window = TP1H_L_Demand(1,2,3)
    window.show()
    sys.exit(app.exec_())

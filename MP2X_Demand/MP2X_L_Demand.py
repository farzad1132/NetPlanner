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
from MP2X_Demand import Line_L_Selected
from MP2X_Demand import Line_R_Selected
from MP2X_Demand import Border_L

# USE THIS CODE TO CHANGE THE CLIENT TO SELECTED CLIENT:
#1)
# For left clients:
# self.Client(number of client).setStyleSheet("image: url(:/CLIENT_L_Selected_SOURCE/CLIENT_L_Selected.png);")
#2)
# For right clients:
# self.Client(number of client).setStyleSheet("image: url(:/CLIENT_R_Selected_SOURCE/CLIENT_R_Selected.png);")

# USE THIS CODE TO CHANGE THE LINE TO SELECTED LINE:
#1)
# For left line:
# self.LINE1.setStyleSheet("QLabel{ image: url(:/Line_L_Selected_SOURCE/Line_L_Selected.png); }")
#2)
# For right line:
# self.LINE2.setStyleSheet("QLabel{ image: url(:/Line_R_Selected_SOURCE/Line_R_Selected.png); }")

class MP2X_L_Demand(QtWidgets.QWidget):

    def __init__(self, Panel_ID, nodename, Destination, DualPanelsId):
        super(MP2X_L_Demand, self).__init__()

        self.resize(106, 694)

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
        self.gridLayout.setContentsMargins(5, 9, 5, 5)
        self.gridLayout.setObjectName("gridLayout")
        self.LINE1 = QtWidgets.QLabel(self)
        self.LINE1.setStyleSheet("QLabel{ image: url(:/Line_L_SOURCE/LINE_L.png); }")
        self.LINE1.setText("")
        self.LINE1.setObjectName("LINE1")
        self.gridLayout.addWidget(self.LINE1, 2, 0, 1, 1)
        self.LINE2 = QtWidgets.QLabel(self)
        self.LINE2.setMinimumSize(QtCore.QSize(0, 0))
        self.LINE2.setStyleSheet("QLabel{ image: url(:/Line_R_SOURCE/LINE_R.png); }")
        self.LINE2.setText("")
        self.LINE2.setObjectName("LINE2")
        self.gridLayout.addWidget(self.LINE2, 2, 1, 1, 1)
        self.MP2X_Title = QtWidgets.QLabel(self)
        self.MP2X_Title.setStyleSheet("QLabel{ image: url(:/MP2X_Title_Source/MP2X_Title.png); }")
        self.MP2X_Title.setText("")
        self.MP2X_Title.setObjectName("MP2X_Title")
        self.gridLayout.addWidget(self.MP2X_Title, 1, 2, 2, 1)
        self.CLIENT13 = customlabel(self, self.nodename, self.Destination, self.id, 13, self.LINE1, self.LINE2, self.DualPanelsId)
        self.CLIENT13.setStyleSheet("QLabel{ image: url(:/Client_L_Source/CLIENT_L.png); }")
        self.CLIENT13.setText("")
        self.CLIENT13.setObjectName("CLIENT13")
        self.gridLayout.addWidget(self.CLIENT13, 10, 0, 1, 1)
        self.Socket_bottom = QtWidgets.QLabel(self)
        self.Socket_bottom.setStyleSheet("QLabel{ image: url(:/Socket_bottom_Source/Socket_bottom.png); }")
        self.Socket_bottom.setText("")
        self.Socket_bottom.setObjectName("Socket_bottom")
        self.gridLayout.addWidget(self.Socket_bottom, 13, 0, 1, 1)
        self.CLIENT3 = customlabel(self, self.nodename, self.Destination, self.id, 3, self.LINE1, self.LINE2, self.DualPanelsId)
        self.CLIENT3.setStyleSheet("QLabel{ image: url(:/Client_L_Source/CLIENT_L.png); }")
        self.CLIENT3.setText("")
        self.CLIENT3.setObjectName("CLIENT3")
        self.gridLayout.addWidget(self.CLIENT3, 5, 0, 1, 1)
        self.CLIENT15 = customlabel(self, self.nodename, self.Destination, self.id, 15, self.LINE1, self.LINE2, self.DualPanelsId)
        self.CLIENT15.setStyleSheet("QLabel{ image: url(:/Client_L_Source/CLIENT_L.png); }")
        self.CLIENT15.setText("")
        self.CLIENT15.setObjectName("CLIENT15")
        self.gridLayout.addWidget(self.CLIENT15, 11, 0, 1, 1)
        self.CLIENT14 = customlabel(self, self.nodename, self.Destination, self.id, 14, self.LINE1, self.LINE2, self.DualPanelsId)
        self.CLIENT14.setStyleSheet("QLabel{ image: url(:/Client_R_Source/CLIENT_R.png); }")
        self.CLIENT14.setText("")
        self.CLIENT14.setObjectName("CLIENT14")
        self.gridLayout.addWidget(self.CLIENT14, 10, 1, 1, 1)
        self.CLIENT4 = customlabel(self, self.nodename, self.Destination, self.id, 4, self.LINE1, self.LINE2, self.DualPanelsId)
        self.CLIENT4.setStyleSheet("QLabel{ image: url(:/Client_R_Source/CLIENT_R.png); }")
        self.CLIENT4.setText("")
        self.CLIENT4.setObjectName("CLIENT4")
        self.gridLayout.addWidget(self.CLIENT4, 5, 1, 1, 1)
        self.CLIENT5 = customlabel(self, self.nodename, self.Destination, self.id, 5, self.LINE1, self.LINE2, self.DualPanelsId)
        self.CLIENT5.setStyleSheet("QLabel{ image: url(:/Client_L_Source/CLIENT_L.png); }")
        self.CLIENT5.setText("")
        self.CLIENT5.setObjectName("CLIENT5")
        self.gridLayout.addWidget(self.CLIENT5, 6, 0, 1, 1)
        self.CLIENT10 = customlabel(self, self.nodename, self.Destination, self.id, 10, self.LINE1, self.LINE2, self.DualPanelsId)
        self.CLIENT10.setStyleSheet("QLabel{ image: url(:/Client_R_Source/CLIENT_R.png); }")
        self.CLIENT10.setText("")
        self.CLIENT10.setObjectName("CLIENT10")
        self.gridLayout.addWidget(self.CLIENT10, 8, 1, 1, 1)
        self.CLIENT16 = customlabel(self, self.nodename, self.Destination, self.id, 16, self.LINE1, self.LINE2, self.DualPanelsId)
        self.CLIENT16.setStyleSheet("QLabel{ image: url(:/Client_R_Source/CLIENT_R.png); }")
        self.CLIENT16.setText("")
        self.CLIENT16.setObjectName("CLIENT16")
        self.gridLayout.addWidget(self.CLIENT16, 11, 1, 1, 1)
        self.CLIENT8 = customlabel(self, self.nodename, self.Destination, self.id, 8, self.LINE1, self.LINE2, self.DualPanelsId)
        self.CLIENT8.setStyleSheet("QLabel{ image: url(:/Client_R_Source/CLIENT_R.png); }")
        self.CLIENT8.setText("")
        self.CLIENT8.setObjectName("CLIENT8")
        self.gridLayout.addWidget(self.CLIENT8, 7, 1, 1, 1)
        self.CLIENT7 = customlabel(self, self.nodename, self.Destination, self.id, 7, self.LINE1, self.LINE2, self.DualPanelsId)
        self.CLIENT7.setStyleSheet("QLabel{ image: url(:/Client_L_Source/CLIENT_L.png); }")
        self.CLIENT7.setText("")
        self.CLIENT7.setObjectName("CLIENT7")
        self.gridLayout.addWidget(self.CLIENT7, 7, 0, 1, 1)
        self.CLIENT9 = customlabel(self, self.nodename, self.Destination, self.id, 9, self.LINE1, self.LINE2, self.DualPanelsId)
        self.CLIENT9.setStyleSheet("QLabel{ image: url(:/Client_L_Source/CLIENT_L.png); }")
        self.CLIENT9.setText("")
        self.CLIENT9.setObjectName("CLIENT9")
        self.gridLayout.addWidget(self.CLIENT9, 8, 0, 1, 1)
        self.CLIENT6 = customlabel(self, self.nodename, self.Destination, self.id, 6, self.LINE1, self.LINE2, self.DualPanelsId)
        self.CLIENT6.setStyleSheet("QLabel{ image: url(:/Client_R_Source/CLIENT_R.png); }")
        self.CLIENT6.setText("")
        self.CLIENT6.setObjectName("CLIENT6")
        self.gridLayout.addWidget(self.CLIENT6, 6, 1, 1, 1)
        self.CLIENT11 = customlabel(self, self.nodename, self.Destination, self.id, 11, self.LINE1, self.LINE2, self.DualPanelsId)
        self.CLIENT11.setStyleSheet("QLabel{ image: url(:/Client_L_Source/CLIENT_L.png); }")
        self.CLIENT11.setText("")
        self.CLIENT11.setObjectName("CLIENT11")
        self.gridLayout.addWidget(self.CLIENT11, 9, 0, 1, 1)
        self.Socket_Top = QtWidgets.QLabel(self)
        self.Socket_Top.setStyleSheet("QLabel{ image: url(:/Socket_Top_Source/Socket_top.png); }")
        self.Socket_Top.setText("")
        self.Socket_Top.setObjectName("Socket_Top")
        self.gridLayout.addWidget(self.Socket_Top, 1, 0, 1, 1)
        self.CLIENT12 = customlabel(self, self.nodename, self.Destination, self.id, 12, self.LINE1, self.LINE2, self.DualPanelsId)
        self.CLIENT12.setStyleSheet("QLabel{ image: url(:/Client_R_Source/CLIENT_R.png); }")
        self.CLIENT12.setText("")
        self.CLIENT12.setObjectName("CLIENT12")
        self.gridLayout.addWidget(self.CLIENT12, 9, 1, 1, 1)
        self.CLIENT1 = customlabel(self, self.nodename, self.Destination, self.id, 1, self.LINE1, self.LINE2, self.DualPanelsId)
        self.CLIENT1.setStyleSheet("QLabel{ image: url(:/Client_L_Source/CLIENT_L.png); }")
        self.CLIENT1.setText("")
        self.CLIENT1.setObjectName("CLIENT1")
        self.gridLayout.addWidget(self.CLIENT1, 3, 0, 1, 1)
        self.CLIENT2 = customlabel(self, self.nodename, self.Destination, self.id, 2, self.LINE1, self.LINE2, self.DualPanelsId)
        self.CLIENT2.setStyleSheet("QLabel{ image: url(:/Client_R_Source/CLIENT_R.png); }")
        self.CLIENT2.setText("")
        self.CLIENT2.setObjectName("CLIENT2")
        self.gridLayout.addWidget(self.CLIENT2, 3, 1, 1, 1)
        grid.addLayout(self.gridLayout,0,0)
    
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

            # undoing every service or lightpath that is created in this panel
            if DemandTabDataBase["Panels"][self.nodename][self.id].LinesCapacity != [0, 0]:

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

                GroomOut_1_Id = DemandTabDataBase["Panels"][self.nodename][self.id].LineIdList[0]
                GroomOut_2_Id = DemandTabDataBase["Panels"][self.nodename][self.id].LineIdList[1]

                self.Update_MP1H_Port(Item= DemandTabDataBase["GroomOut10"][(self.nodename, self.Destination)][GroomOut_1_Id],
                                        Source= self.nodename,
                                        Destination= self.Destination,
                                        Capacity= 0)

                # deleteing GroomOut10 1 from database
                self.modify_GroomOut10List(id= GroomOut_1_Id,
                                            Source= self.nodename,
                                            Destination= self.Destination,
                                            mode= "delete")

                # ** Dual **
                self.modify_GroomOut10List(id= GroomOut_1_Id,
                                            Source= self.Destination,
                                            Destination= self.nodename,
                                            mode= "delete")

    

                # deleting groomout10 from common object ( line 1 )
                Data["NetworkObj"].TrafficMatrix.delete_groom_out_10(GroomOut_1_Id)

                

                if GroomOut_2_Id is not None:

                    self.Update_MP1H_Port(Item= DemandTabDataBase["GroomOut10"][(self.nodename, self.Destination)][GroomOut_2_Id],
                                        Source= self.nodename,
                                        Destination= self.Destination,
                                        Capacity= 0)

                    # deleteing GroomOut10 2 from database
                    self.modify_GroomOut10List(id= GroomOut_2_Id,
                                                Source= self.nodename,
                                                Destination= self.Destination,
                                                mode= "delete")

                    # ** Dual **
                    self.modify_GroomOut10List(id= GroomOut_2_Id,
                                                Source= self.Destination,
                                                Destination= self.nodename,
                                                mode= "delete")

                    # deleting groomout10 from common object ( line 2 )
                    Data["NetworkObj"].TrafficMatrix.delete_groom_out_10(GroomOut_2_Id)

                    

            DemandTabDataBase["Panels"][self.nodename].pop(self.id)
            DemandTabDataBase["Panels"][self.nodename].pop(self.uppernum)

            # ** Dual **
            DemandTabDataBase["Panels"][self.Destination].pop(self.DualPanelsId[0])
            DemandTabDataBase["Panels"][self.Destination].pop(self.DualPanelsId[1])

    
    def Update_MP1H_Port(self, Item, Source, Destination, Capacity):
        UserData = Item.data(Qt.UserRole)

        if "MP1H_Client_Id" in UserData:

            MP1H_Id , Client_Id = UserData["MP1H_Client_Id"]

            MP1H_widget = Data["DemandPanel_" + str(MP1H_Id)].itemAt(0).widget()
            clientvar = getattr(MP1H_widget, "Client" + Client_Id )

            if Capacity > 0.001:
                clientvar.setToolTip(DemandTabDataBase["GroomOut10"][(self.nodename, self.Destination)][UserData["GroomOut10Id"]].toolTip())
            
            else:
                clientvar.Clear_From_MP2X()
        
    
    def modify_ServiceList(self, ids, source, destination, mode = "delete", type = None):
        

        key = (int(ids[0]) , int(ids[1]))
        if mode == "delete":
            DemandTabDataBase["Services"][(source, destination)][key] = 1
            DemandTabDataBase["Services_static"][source][key].setBackground(QBrush(Qt.white, Qt.SolidPattern))

            # statement bellow checks for removing notification
            if hasattr( Data["ui"], "failed_nodes"):
                if source in Data["ui"].failed_nodes:
                    x = 0
                    for dest in DemandTabDataBase["Source_Destination"][source]["DestinationList"]:
                        if DemandTabDataBase["Services"][(source, dest)]:
                            x = 1
                            break
                    if x == 0:        
                        Data["ui"].set_failed_nodes_default(source)
            
        elif mode == "add":
            DemandTabDataBase["Services"][(source, destination)][key] = 0
            DemandTabDataBase["Services_static"][source][key].setBackground(QBrush(QColor('#6088C6'), Qt.SolidPattern))
            
        Data["ui"].UpdateDemand_ServiceList()
    
    def modify_GroomOut10List(self, id, Source, Destination, Capacity = None, mode = "add", type = None, PanelId = None, DemandId = None):

        if mode == "add":
            #DemandTabDataBase["Lightpathes"][(Source, Destination)][id] = "%s # %s" %(id, type)
            item = QListWidgetItem(type, Data["GroomOu10_list"])
            UserData = {"GroomOut10Id":id, "Source":Source, "Destination":Destination, "Capacity":Capacity, "Type": type, "PanelId": PanelId, "DemandId": DemandId}
            item.setToolTip(f"Source: {Source}\nDestination: {Destination}\nCapacity: {Capacity}\nType: {type}")
            item.setData(Qt.UserRole, UserData)
            item.setTextAlignment(Qt.AlignCenter)

            DemandTabDataBase["GroomOut10"][(Source, Destination)][id] = item
        
        if mode == "delete":
            # deleting desired lightpath from database
            DemandTabDataBase["GroomOut10"][(Source, Destination)].pop(id)

            # correcting upper lightpath id's 
            """ for Des in DemandTabDataBase["Source_Destination"][Source]["DestinationList"]:
                for UpperId in sorted(list(DemandTabDataBase["GroomOut10"][(Source, Des)].keys())):
                    if UpperId > id:
                        DemandTabDataBase["GroomOut10"][(Source, Des)][UpperId - 1] = DemandTabDataBase["GroomOut10"][(Source, Des)].pop(UpperId)
                        UserData = DemandTabDataBase["GroomOut10"][(Source, Des)][UpperId - 1].data(Qt.UserRole)
                        UserData["GroomOut10Id"] -= 1
                        DemandTabDataBase["GroomOut10"][(Source, Des)][UpperId - 1].setData(Qt.UserRole, UserData)  """
 
        Data["ui"].update_Demand_groomout10_list()


class customlabel(QLabel):
    Stateflag = 0           # this flag shows that this panel is on or off
    def __init__(self, parent, nodename, Destination, ID, ClientNum , LineVar_1, LineVar_2, DualPanelsId = None):
        super().__init__(parent)
        self.nodename = nodename
        self.id = ID
        self.Destination = Destination
        self.LineVar_1 = LineVar_1
        self.LineVar_2 = LineVar_2
        self.ClientNum = ClientNum - 1  # because list indices starts with 0
        self.setAcceptDrops(True)

        self.BWDict = {"E1": 58.84 / 1024, "STM_1_Electrical": 155.52 / 1024, "STM_1_Optical": 155.52 / 1024, "STM_4": 622.08 / 1024, "STM_16": 2.49}
    
        self.DualPanelsId = DualPanelsId

    def dragEnterEvent(self, event):
        e = event.mimeData()
        model = QStandardItemModel()
        model.dropMimeData(event.mimeData(), Qt.CopyAction, 0,0, QModelIndex())
        dragtext = model.item(0,0).text()
        UserData = model.item(0).data(Qt.UserRole)
        
        self.allowedservices = ["E1", "STM_1_Electrical", "STM_1_Optical", "STM_4", "STM_16"]
        
        servicetype = dragtext.strip()
        
        if servicetype in self.allowedservices:
            if DemandTabDataBase["Services"][(self.nodename, self.Destination)].get((UserData["DemandId"], UserData["ServiceId"])) == 0:

                ids = [UserData["DemandId"], UserData["ServiceId"]]
                Line_1_old_capacity = DemandTabDataBase["Panels"][self.nodename][self.id].LinesCapacity[0]
                Line_2_old_capacity = DemandTabDataBase["Panels"][self.nodename][self.id].LinesCapacity[1]
                DropCapacity = self.BWDict[servicetype]

                # checking weather lines have enough capacity or not
                if Line_1_old_capacity + DropCapacity < 10 or Line_2_old_capacity + DropCapacity < 10:
                    
                    if self.ClientNum % 2 == 0:
                        self.setStyleSheet("image: url(:/CLIENT_L_Selected_SOURCE/CLIENT_L_Selected.png);")
                    else:
                        self.setStyleSheet("image: url(:/CLIENT_R_Selected_SOURCE/CLIENT_R_Selected.png);")
                    event.accept()
                
                else:
                    if self.ClientNum % 2 == 0:
                        self.setStyleSheet("image: url(:/Client_L_Source/CLIENT_L.png);")
                    else:
                        self.setStyleSheet("image: url(:/Client_R_Source/CLIENT_R.png);")

            else:
                if self.ClientNum % 2 == 0:
                    self.setStyleSheet("image: url(:/Client_L_Source/CLIENT_L.png);")
                else:
                    self.setStyleSheet("image: url(:/Client_R_Source/CLIENT_R.png);")
        

        super(customlabel,self).dragEnterEvent(event)
    

    def dragLeaveEvent(self, event):
        if self.ClientNum % 2 == 0:
            self.setStyleSheet("image: url(:/Client_L_Source/CLIENT_L.png);")
        else:
            self.setStyleSheet("image: url(:/Client_R_Source/CLIENT_R.png);")

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
            self.ids = (UserData["DemandId"], UserData["ServiceId"])            # ids : [ serviceId, DemandId ]
            
            self.setToolTip(DemandTabDataBase["Services_static"][self.nodename][self.ids].toolTip())

            # DemandTabDataBase["Panels"][self.nodename][self.id].add_client(self.ClientNum, servicetype)
            Line_1_old_capacity = DemandTabDataBase["Panels"][self.nodename][self.id].LinesCapacity[0]
            Line_2_old_capacity = DemandTabDataBase["Panels"][self.nodename][self.id].LinesCapacity[1]

            # updating ClientsCapacity in panel object
            DemandTabDataBase["Panels"][self.nodename][self.id].ClientsCapacity[self.ClientNum] = servicetype

            # ** Dual **
            DemandTabDataBase["Panels"][self.Destination][self.DualPanelsId[0]].ClientsCapacity[self.ClientNum] = servicetype

            ServiceListLen = len(DemandTabDataBase["Panels"][self.nodename][self.id].ServiceIdList)
            if self.ClientNum >= ServiceListLen:
                for i in range(ServiceListLen - self.ClientNum + 1):
                    DemandTabDataBase["Panels"][self.nodename][self.id].ServiceIdList.append(None)

                    # ** Dual **
                    DemandTabDataBase["Panels"][self.Destination][self.DualPanelsId[0]].ServiceIdList.append(None)

            # updating service id and demand id in panel object 
            DemandTabDataBase["Panels"][self.nodename][self.id].ServiceIdList[self.ClientNum] = self.ids[1]
            DemandTabDataBase["Panels"][self.nodename][self.id].DemandIdList[self.ClientNum] = self.ids[0]

            # ** Dual **
            DemandTabDataBase["Panels"][self.Destination][self.DualPanelsId[0]].ServiceIdList[self.ClientNum] = self.ids[1]
            DemandTabDataBase["Panels"][self.Destination][self.DualPanelsId[0]].DemandIdList[self.ClientNum] = self.ids[0]


            
            DropCapacity = self.BWDict[self.servicetype]
            

            self.modify_ServiceList(ids= self.ids,
                                    source= self.nodename,
                                    destination= self.Destination,
                                    mode= "delete")

            # ** Dual **
            self.modify_ServiceList(ids= self.ids,
                                    source= self.Destination,
                                    destination= self.nodename,
                                    mode= "delete")

            # check if line 1 in on or not
            if Line_1_old_capacity < 0.001:

                # updating line 1 capacity
                DemandTabDataBase["Panels"][self.nodename][self.id].LinesCapacity[0] += DropCapacity

                # ** Dual **
                DemandTabDataBase["Panels"][self.Destination][self.DualPanelsId[0]].LinesCapacity[0] += DropCapacity

                # updating Line_1_ServiceIdList
                DemandTabDataBase["Panels"][self.nodename][self.id].Line_1_ServiceIdList.append(self.ids[1])

                # ** Dual ** 
                DemandTabDataBase["Panels"][self.Destination][self.DualPanelsId[0]].Line_1_ServiceIdList.append(self.ids[1])
                
                # creating new groom out 10
                Data["NetworkObj"].TrafficMatrix.add_groom_out_10(Source= self.nodename,
                                                    Destination= self.Destination,
                                                    DemandId= self.ids[1],
                                                    Capacity= self.BWDict[self.servicetype],
                                                    ServiceIdList= [self.ids[0]])

                GroomOutId = max(Data["NetworkObj"].TrafficMatrix.GroomOut10Dict.keys())

                # updating LineIdList in panel object
                DemandTabDataBase["Panels"][self.nodename][self.id].LineIdList[0] = GroomOutId

                # ** Dual ** 
                DemandTabDataBase["Panels"][self.Destination][self.DualPanelsId[0]].LineIdList[0] = GroomOutId

                self.modify_GroomOut10List(id= GroomOutId,
                                            Source= self.nodename,
                                            Destination= self.Destination,
                                            Capacity= DemandTabDataBase["Panels"][self.nodename][self.id].LinesCapacity[0],
                                            mode= "add",
                                            type= "GroomOut10",
                                            PanelId= self.id,
                                            DemandId= self.ids[0])

                # ** Dual ** 
                self.modify_GroomOut10List(id= GroomOutId,
                                            Source= self.Destination,
                                            Destination= self.nodename,
                                            Capacity= DemandTabDataBase["Panels"][self.Destination][self.DualPanelsId[0]].LinesCapacity[0],
                                            mode= "add",
                                            type= "GroomOut10",
                                            PanelId= self.DualPanelsId[0],
                                            DemandId= self.ids[0])
                
                # setting line port tooltip                                        
                self.LineVar_1.setToolTip(DemandTabDataBase["GroomOut10"][(self.nodename, self.Destination)][GroomOutId].toolTip())

                # setting line port stylesheet
                self.LineVar_1.setStyleSheet("QLabel{ image: url(:/Line_L_Selected_SOURCE/Line_L_Selected.png); }")

            elif Line_1_old_capacity + DropCapacity < 10 :
                
                # updating line 1 capacity
                DemandTabDataBase["Panels"][self.nodename][self.id].LinesCapacity[0] += DropCapacity

                # ** Dual **
                DemandTabDataBase["Panels"][self.Destination][self.DualPanelsId[0]].LinesCapacity[0] += DropCapacity

                # updating Line_1_ServiceIdList
                DemandTabDataBase["Panels"][self.nodename][self.id].Line_1_ServiceIdList.append(self.ids[1])

                # ** Dual ** 
                DemandTabDataBase["Panels"][self.Destination][self.DualPanelsId[0]].Line_1_ServiceIdList.append(self.ids[1])

                GroomOutId = DemandTabDataBase["Panels"][self.nodename][self.id].LineIdList[0]

                ServiceIdList = [self.ids[1]]
                Data["NetworkObj"].TrafficMatrix.GroomOut10Dict[GroomOutId].ServiceIdList.extend(ServiceIdList)

                # updating LightPath ListWidgetItem Capacity
                self.Update_LineListWidgetItem_Tooltip( Item= DemandTabDataBase["GroomOut10"][(self.nodename, self.Destination)][GroomOutId],
                                                        Capacity= DemandTabDataBase["Panels"][self.nodename][self.id].LinesCapacity[0])

                # ** Dual **
                self.Update_LineListWidgetItem_Tooltip( Item= DemandTabDataBase["GroomOut10"][(self.Destination, self.nodename)][GroomOutId],
                                                        Capacity= DemandTabDataBase["Panels"][self.nodename][self.id].LinesCapacity[0])
                
                self.Update_MP1H_Port(Item= DemandTabDataBase["GroomOut10"][(self.nodename, self.Destination)][GroomOutId],
                                            Source= self.nodename,
                                            Destination= self.Destination,
                                            Capacity= DemandTabDataBase["Panels"][self.nodename][self.id].LinesCapacity[0])

                # setting line port tooltip                                        
                self.LineVar_1.setToolTip(DemandTabDataBase["GroomOut10"][(self.nodename, self.Destination)][GroomOutId].toolTip())

                # setting line port stylesheet
                self.LineVar_1.setStyleSheet("QLabel{ image: url(:/Line_L_Selected_SOURCE/Line_L_Selected.png); }")
            
            elif Line_2_old_capacity < 0.001:

                # updating line 2 capacity
                DemandTabDataBase["Panels"][self.nodename][self.id].LinesCapacity[1] += DropCapacity

                # ** Dual **
                DemandTabDataBase["Panels"][self.Destination][self.DualPanelsId[0]].LinesCapacity[1] += DropCapacity

                # updating Line_2_ServiceIdList
                DemandTabDataBase["Panels"][self.nodename][self.id].Line_2_ServiceIdList.append(self.ids[1])

                # ** Dual **
                DemandTabDataBase["Panels"][self.Destination][self.DualPanelsId[0]].Line_2_ServiceIdList.append(self.ids[1])

                # creating new groom out 10
                Data["NetworkObj"].TrafficMatrix.add_groom_out_10(Source= self.nodename,
                                                    Destination= self.Destination,
                                                    DemandId= self.ids[1],
                                                    Capacity= self.BWDict[self.servicetype],
                                                    ServiceIdList= [self.ids[0]])
                

                GroomOutId = max(Data["NetworkObj"].TrafficMatrix.GroomOut10Dict.keys())

                # updating LineIdList in panel object
                DemandTabDataBase["Panels"][self.nodename][self.id].LineIdList[1] = GroomOutId

                # ** Dual **
                DemandTabDataBase["Panels"][self.Destination][self.DualPanelsId[0]].LineIdList[1] = GroomOutId

                self.modify_GroomOut10List(id= GroomOutId,
                                            Source= self.nodename,
                                            Destination= self.Destination,
                                            Capacity= DemandTabDataBase["Panels"][self.nodename][self.id].LinesCapacity[1],
                                            mode= "add",
                                            type= "GroomOut10",
                                            PanelId= self.id,
                                            DemandId = self.ids[0])

                # ** Dual **
                self.modify_GroomOut10List(id= GroomOutId,
                                            Source= self.Destination,
                                            Destination= self.nodename,
                                            Capacity= DemandTabDataBase["Panels"][self.nodename][self.id].LinesCapacity[1],
                                            mode= "add",
                                            type= "GroomOut10",
                                            PanelId= self.DualPanelsId,
                                            DemandId = self.ids[0])
                
                # setting line port tooltip                                        
                self.LineVar_2.setToolTip(DemandTabDataBase["GroomOut10"][(self.nodename, self.Destination)][GroomOutId].toolTip())

                # setting line port stylesheet
                self.LineVar_2.setStyleSheet("QLabel{ image: url(:/Line_R_Selected_SOURCE/Line_R_Selected.png); }")
            
            else:

                # updating line 2 capacity
                DemandTabDataBase["Panels"][self.nodename][self.id].LinesCapacity[1] += DropCapacity

                # ** Dual **
                DemandTabDataBase["Panels"][self.Destination][self.DualPanelsId[0]].LinesCapacity[1] += DropCapacity

                # updating Line_2_ServiceIdList
                DemandTabDataBase["Panels"][self.nodename][self.id].Line_2_ServiceIdList.append(self.ids[1])

                # ** Dual **
                DemandTabDataBase["Panels"][self.Destination][self.DualPanelsId[0]].Line_2_ServiceIdList.append(self.ids[1])

                GroomOutId = DemandTabDataBase["Panels"][self.nodename][self.id].LineIdList[1]

                ServiceIdList = [self.ids[1]]
                Data["NetworkObj"].TrafficMatrix.GroomOut10Dict[GroomOutId].ServiceIdList.extend(ServiceIdList)


                # updating LightPath ListWidgetItem Capacity
                self.Update_LineListWidgetItem_Tooltip( Item= DemandTabDataBase["GroomOut10"][(self.nodename, self.Destination)][GroomOutId],
                                                        Capacity= DemandTabDataBase["Panels"][self.nodename][self.id].LinesCapacity[1])

                # ** Dual **
                self.Update_LineListWidgetItem_Tooltip( Item= DemandTabDataBase["GroomOut10"][(self.Destination, self.nodename)][GroomOutId],
                                                        Capacity= DemandTabDataBase["Panels"][self.nodename][self.id].LinesCapacity[1])

                
                self.Update_MP1H_Port(Item= DemandTabDataBase["GroomOut10"][(self.nodename, self.Destination)][GroomOutId],
                                            Source= self.nodename,
                                            Destination= self.Destination,
                                            Capacity= DemandTabDataBase["Panels"][self.nodename][self.id].LinesCapacity[1])

                # setting line port tooltip                                        
                self.LineVar_2.setToolTip(DemandTabDataBase["GroomOut10"][(self.nodename, self.Destination)][GroomOutId].toolTip())

                # setting line port stylesheet
                self.LineVar_2.setStyleSheet("QLabel{ image: url(:/Line_R_Selected_SOURCE/Line_R_Selected.png); }")


            # NOTE: be Careful !!!!!
            self.setAcceptDrops(False)  
        

    def contextMenuEvent(self, event):
        ContextMenu = QMenu(self)
        ClearAction = ContextMenu.addAction("..Clear Socket..")
        
        action = ContextMenu.exec_(self.mapToGlobal(event.pos()))

        if action == ClearAction:
            if DemandTabDataBase["Panels"][self.nodename][self.id].ClientsCapacity[self.ClientNum] != 0:
                self.setToolTip("")

                ServiceId = DemandTabDataBase["Panels"][self.nodename][self.id].ServiceIdList[self.ClientNum]

                GroomOutId_1 = DemandTabDataBase["Panels"][self.nodename][self.id].LineIdList[0]
                GroomOutId_2 = DemandTabDataBase["Panels"][self.nodename][self.id].LineIdList[1]

                # updating linescapacity part on panel object
                if ServiceId in DemandTabDataBase["Panels"][self.nodename][self.id].Line_1_ServiceIdList:
                    # updating line 1 capacity
                    DemandTabDataBase["Panels"][self.nodename][self.id].LinesCapacity[0] -= self.BWDict[DemandTabDataBase["Panels"][self.nodename][self.id].ClientsCapacity[self.ClientNum]]

                    # ** Dual **
                    DemandTabDataBase["Panels"][self.Destination][self.DualPanelsId[0]].LinesCapacity[0] -= self.BWDict[DemandTabDataBase["Panels"][self.nodename][self.id].ClientsCapacity[self.ClientNum]]

                    # updating line 1 id service id list
                    DemandTabDataBase["Panels"][self.nodename][self.id].Line_1_ServiceIdList.remove(ServiceId)

                    # ** Dual **
                    DemandTabDataBase["Panels"][self.Destination][self.DualPanelsId[0]].Line_1_ServiceIdList.remove(ServiceId)

                    

                    # updating LightPath ListWidgetItem Capacity
                    self.Update_LineListWidgetItem_Tooltip( Item= DemandTabDataBase["GroomOut10"][(self.nodename, self.Destination)][GroomOutId_1],
                                                            Capacity= DemandTabDataBase["Panels"][self.nodename][self.id].LinesCapacity[0])

                    # ** Dual **
                    self.Update_LineListWidgetItem_Tooltip( Item= DemandTabDataBase["GroomOut10"][(self.Destination, self.nodename)][GroomOutId_1],
                                                            Capacity= DemandTabDataBase["Panels"][self.nodename][self.id].LinesCapacity[0])
                    
                    self.Update_MP1H_Port(Item= DemandTabDataBase["GroomOut10"][(self.nodename, self.Destination)][GroomOutId_1],
                                            Source= self.nodename,
                                            Destination= self.Destination,
                                            Capacity= DemandTabDataBase["Panels"][self.nodename][self.id].LinesCapacity[0])

                    # setting line port tooltip                                        
                    self.LineVar_1.setToolTip(DemandTabDataBase["GroomOut10"][(self.nodename, self.Destination)][GroomOutId_1].toolTip())

                else:
                    # updating line 2 capacity
                    DemandTabDataBase["Panels"][self.nodename][self.id].LinesCapacity[1] -= self.BWDict[DemandTabDataBase["Panels"][self.nodename][self.id].ClientsCapacity[self.ClientNum]]

                    # ** Dual **
                    DemandTabDataBase["Panels"][self.Destination][self.DualPanelsId[0]].LinesCapacity[1] -= self.BWDict[DemandTabDataBase["Panels"][self.nodename][self.id].ClientsCapacity[self.ClientNum]]

                    # updating line 2 id service id list
                    DemandTabDataBase["Panels"][self.nodename][self.id].Line_2_ServiceIdList.remove(ServiceId)

                    # ** Dual **
                    DemandTabDataBase["Panels"][self.Destination][self.DualPanelsId[0]].Line_2_ServiceIdList.remove(ServiceId)

                    # updating LightPath ListWidgetItem Capacity
                    self.Update_LineListWidgetItem_Tooltip( Item= DemandTabDataBase["GroomOut10"][(self.nodename, self.Destination)][GroomOutId_2],
                                                            Capacity= DemandTabDataBase["Panels"][self.nodename][self.id].LinesCapacity[1])

                    # ** Dual **
                    self.Update_LineListWidgetItem_Tooltip( Item= DemandTabDataBase["GroomOut10"][(self.Destination, self.nodename)][GroomOutId_2],
                                                            Capacity= DemandTabDataBase["Panels"][self.nodename][self.id].LinesCapacity[1])

                    self.Update_MP1H_Port(Item= DemandTabDataBase["GroomOut10"][(self.nodename, self.Destination)][GroomOutId_2],
                                            Source= self.nodename,
                                            Destination= self.Destination,
                                            Capacity= DemandTabDataBase["Panels"][self.nodename][self.id].LinesCapacity[1])

                    # setting line port tooltip                                        
                    self.LineVar_2.setToolTip(DemandTabDataBase["GroomOut10"][(self.nodename, self.Destination)][GroomOutId_2].toolTip())

                # updating client capacity part of panel object
                DemandTabDataBase["Panels"][self.nodename][self.id].ClientsCapacity[self.ClientNum] = 0

                # ** Dual **
                DemandTabDataBase["Panels"][self.Destination][self.DualPanelsId[0]].ClientsCapacity[self.ClientNum] = 0
                
                # update ServiceIdList part of panel object
                DemandTabDataBase["Panels"][self.nodename][self.id].ServiceIdList[self.ClientNum] = None

                # ** Dual **
                DemandTabDataBase["Panels"][self.Destination][self.DualPanelsId[0]].ServiceIdList[self.ClientNum] = None

                # updating DemandIdList part in panel object
                DemandTabDataBase["Panels"][self.nodename][self.id].DemandIdList[self.ClientNum] = None

                # ** Dual **
                DemandTabDataBase["Panels"][self.Destination][self.DualPanelsId[0]].DemandIdList[self.ClientNum] = None

                self.setAcceptDrops(True)

                if self.ClientNum % 2 == 0:
                    self.setStyleSheet("image: url(:/Client_L_Source/CLIENT_L.png);")
                else:
                    self.setStyleSheet("image: url(:/Client_R_Source/CLIENT_R.png);")

                self.modify_ServiceList(ids= self.ids,
                                        source = self.nodename,
                                        destination= self.Destination,
                                        mode= "add",
                                        type= self.servicetype)

                # ** Dual **
                self.modify_ServiceList(ids= self.ids,
                                        source = self.Destination,
                                        destination= self.nodename,
                                        mode= "add",
                                        type= self.servicetype)

                if DemandTabDataBase["Panels"][self.nodename][self.id].LinesCapacity[0] < 0.001:

                    # updating LineIdList part of panel object
                    DemandTabDataBase["Panels"][self.nodename][self.id].LineIdList[0] = None

                    # ** Dual **
                    DemandTabDataBase["Panels"][self.Destination][self.DualPanelsId[0]].LineIdList[0] = None

                    self.modify_GroomOut10List(id= GroomOutId_1,
                                                Source= self.nodename,
                                                Destination= self.Destination,
                                                mode= "delete",
                                                type= "GroomOut10")

                    # ** Dual **
                    self.modify_GroomOut10List(id= GroomOutId_1,
                                                Source= self.Destination,
                                                Destination= self.nodename,
                                                mode= "delete",
                                                type= "GroomOut10")
                    
                    # deleting groomout10 from common object
                    Data["NetworkObj"].TrafficMatrix.delete_groom_out_10(GroomOutId_1)

                    self.LineVar_1.setStyleSheet("QLabel{ image: url(:/Line_L_SOURCE/LINE_L.png); }")

                elif DemandTabDataBase["Panels"][self.nodename][self.id].LinesCapacity[1] < 0.001 and GroomOutId_2 is not None:

                    # updating LineIdList part of panel object
                    DemandTabDataBase["Panels"][self.nodename][self.id].LineIdList[1] = None

                    # ** Dual **
                    DemandTabDataBase["Panels"][self.Destination][self.DualPanelsId[0]].LineIdList[1] = None

                    self.modify_GroomOut10List(id= GroomOutId_2,
                                                Source= self.nodename,
                                                Destination= self.Destination,
                                                mode= "delete",
                                                type= "GroomOut10")

                    # ** Dual **
                    self.modify_GroomOut10List(id= GroomOutId_2,
                                                Source= self.Destination,
                                                Destination= self.nodename,
                                                mode= "delete",
                                                type= "GroomOut10")

                    # deleting groomout10 from common object
                    Data["NetworkObj"].TrafficMatrix.delete_groom_out_10(GroomOutId_2)

                    self.LineVar_2.setStyleSheet("QLabel{ image: url(:/Line_R_SOURCE/LINE_R.png); }")

    def Update_MP1H_Port(self, Item, Source, Destination, Capacity):
        UserData = Item.data(Qt.UserRole)

        if "MP1H_Client_Id" in UserData:

            MP1H_Id , Client_Id = UserData["MP1H_Client_Id"]

            MP1H_widget = Data["DemandPanel_" + str(MP1H_Id)].itemAt(0).widget()
            clientvar = getattr(MP1H_widget, "Client" + Client_Id )

            if Capacity > 0.001:
                clientvar.setToolTip(DemandTabDataBase["GroomOut10"][(self.nodename, self.Destination)][UserData["GroomOut10Id"]].toolTip())
            
            else:
                clientvar.Clear_From_MP2X()


    def Update_LineListWidgetItem_Tooltip(self, Item, Capacity):       
        
        UserData = Item.data(Qt.UserRole)
        #UserData = {"LightPathId":id, "Source":Source, "Destination":Destination, "Capacity":Capacity, "Type": type}
        UserData["Capacity"] = Capacity
        Item.setData(Qt.UserRole, UserData)
        Item.setToolTip(f"Source: {UserData['Source']}\nDestination: {UserData['Destination']}\nCapacity: {Capacity}\nType: {UserData['Type']}")

    def modify_ServiceList(self, ids, source, destination, mode = "delete", type = None):
        

        key = (int(ids[0]) , int(ids[1]))
        if mode == "delete":
            DemandTabDataBase["Services"][(source, destination)][key] = 1
            DemandTabDataBase["Services_static"][source][key].setBackground(QBrush(Qt.white, Qt.SolidPattern))

            # statement bellow checks for removing notification
            if hasattr( Data["ui"], "failed_nodes"):
                if source in Data["ui"].failed_nodes:
                    x = 0
                    for dest in DemandTabDataBase["Source_Destination"][source]["DestinationList"]:
                        if DemandTabDataBase["Services"][(source, dest)]:
                            x = 1
                            break
                    if x == 0:        
                        Data["ui"].set_failed_nodes_default(source)
            
        elif mode == "add":
            DemandTabDataBase["Services"][(source, destination)][key] = 0
            DemandTabDataBase["Services_static"][source][key].setBackground(QBrush(QColor('#6088C6'), Qt.SolidPattern))
            
        Data["ui"].UpdateDemand_ServiceList()
    
    def modify_GroomOut10List(self, id, Source, Destination, Capacity = None, mode = "add", type = None, PanelId = None, DemandId = None):

        if mode == "add":
            #DemandTabDataBase["Lightpathes"][(Source, Destination)][id] = "%s # %s" %(id, type)
            item = QListWidgetItem(type, Data["GroomOu10_list"])
            UserData = {"GroomOut10Id":id, "Source":Source, "Destination":Destination, "Capacity":Capacity, "Type": type, "PanelId": PanelId, "DemandId": DemandId}
            item.setToolTip(f"Source: {Source}\nDestination: {Destination}\nCapacity: {Capacity}\nType: {type}")
            item.setData(Qt.UserRole, UserData)
            item.setTextAlignment(Qt.AlignCenter)

            DemandTabDataBase["GroomOut10"][(Source, Destination)][id] = item
        
        if mode == "delete":
            # deleting desired lightpath from database
            DemandTabDataBase["GroomOut10"][(Source, Destination)].pop(id)

            """ # correcting upper lightpath id's 
            for Des in DemandTabDataBase["Source_Destination"][Source]["DestinationList"]:
                for UpperId in sorted(list(DemandTabDataBase["GroomOut10"][(Source, Des)].keys())):
                    if UpperId > id:
                        DemandTabDataBase["GroomOut10"][(Source, Des)][UpperId - 1] = DemandTabDataBase["GroomOut10"][(Source, Des)].pop(UpperId)
                        UserData = DemandTabDataBase["GroomOut10"][(Source, Des)][UpperId - 1].data(Qt.UserRole)
                        UserData["GroomOut10Id"] -= 1
                        DemandTabDataBase["GroomOut10"][(Source, Des)][UpperId - 1].setData(Qt.UserRole, UserData) """ 
 
        Data["ui"].update_Demand_groomout10_list()


if __name__ == "__main__":
    
    app = QtWidgets.QApplication([])
    window = MP2X_L_Demand(1,2,3)
    window.show()
    sys.exit(app.exec_())

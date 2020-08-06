from PySide2.QtCore import Qt
from collections import OrderedDict
Data = {}
Data["E1"]  = {}
Data["STM_1_Electrical"] = {}
Data["STM_1_Optical"] = {}
Data["STM_4"] = {}
Data["STM_16"] = {}
Data["STM_64"] = {}
Data["FE"] = {}
Data["1GE"] = {}
Data["10GE"] = {}
Data["40GE"] = {}
Data["100GE"] = {}
Data["General"] = {}
Data["RowCount"] = 20
Data["Last_Node_ID"] = 0
Data["Last_Link_ID"] = 0
Data["Nodes"] = {}  # TODO: write this parts structure
Data["Links"] = {}  # TODO: write this parts structure

Data["Clustering"] = {}
# format :
#          {<NodeName> : {"Color": <ColorName>, "Type" : <TypeName> , "SubNodes" : <SubNodesNameList> } }

# keys are row numbers except nodes and links

Data["error_in_TM"] = {}
#   format:
#   (<RowNumber> , <Column / ServiceType>, <GTM / TM>) : item

# <RowNumber> : int ( keys in Data )
# <Column / ServiceType>: str ( "0" to "8"  or  "STM_4" , ..)
# <GTM / TM>: str ( "GTM" or "TM" )
# item: QListWidgetItem

Data["General"]["ColumnCount"] = 9
Data["General"]["DataSection"] = {}
Data["General"]["DataSection"]["0"] = {} # 0: Id
Data["General"]["DataSection"]["1"] = {} # 1: source
Data["General"]["DataSection"]["2"] = {} # 2: ....
Data["General"]["DataSection"]["3"] = {}
Data["General"]["DataSection"]["4"] = {}
Data["General"]["DataSection"]["5"] = {}
Data["General"]["DataSection"]["6"] = {}
Data["General"]["DataSection"]["7"] = {}
Data["General"]["DataSection"]["8"] = {} # 8: Protection_Type

Data["E1"]["ColumnCount"] = 2
#Data["E1"]["RowCount"] = 20
Data["E1"]["Headers"] = ["Quantity\n","SLA\n"]
Data["E1"]["DataSection"] = {}
Data["E1"]["DataSection"]["Quantity"] = {}
Data["E1"]["DataSection"]["SLA"] = {}

Data["STM_1_Electrical"]["ColumnCount"] = 2
#Data["STM_1_Electrical"]["RowCount"] = 20
Data["STM_1_Electrical"]["Headers"] = ["Quantity\n","SLA\n"]
Data["STM_1_Electrical"]["DataSection"] = {}
Data["STM_1_Electrical"]["DataSection"]["Quantity"] = {}
Data["STM_1_Electrical"]["DataSection"]["SLA"] = {}

Data["STM_1_Optical"]["ColumnCount"] = 3
#Data["STM_1_Electrical"]["RowCount"] = 20
Data["STM_1_Optical"]["Headers"] = ["Quantity\n","\u03bb\n","SLA\n"]
Data["STM_1_Optical"]["DataSection"] = {}
Data["STM_1_Optical"]["DataSection"]["Quantity"] = {}
Data["STM_1_Optical"]["DataSection"]["\u03bb"] = {}
Data["STM_1_Optical"]["DataSection"]["SLA"] = {}

Data["STM_4"]["ColumnCount"] = 4
#Data["STM_4"]["RowCount"] = 20
Data["STM_4"]["Headers"] = ["Quantity\n","\u03bb\n", "concat.\n","SLA\n"]
Data["STM_4"]["DataSection"] = {}
Data["STM_4"]["DataSection"]["Quantity"] = {}
Data["STM_4"]["DataSection"]["\u03bb"] = {}
Data["STM_4"]["DataSection"]["concat."] = {}
Data["STM_4"]["DataSection"]["SLA"]={}

Data["STM_16"]["ColumnCount"] = 4
#Data["STM_16"]["RowCount"] = 20
Data["STM_16"]["Headers"] = ["Quantity\n", "\u03bb\n", "concat.\n", "SLA\n"]
Data["STM_16"]["DataSection"] = {}
Data["STM_16"]["DataSection"]["Quantity"] = {}
Data["STM_16"]["DataSection"]["\u03bb"] = {}
Data["STM_16"]["DataSection"]["concat."] = {}
Data["STM_16"]["DataSection"]["SLA"]={}

Data["STM_64"]["ColumnCount"] = 4
#Data["STM_64"]["RowCount"] = 20
Data["STM_64"]["Headers"] = ["Quantity\n", "\u03bb\n", "concat.\n", "SLA\n"]
Data["STM_64"]["DataSection"] = {}
Data["STM_64"]["DataSection"]["Quantity"] = {}
Data["STM_64"]["DataSection"]["\u03bb"] = {}
Data["STM_64"]["DataSection"]["concat."] = {}
Data["STM_64"]["DataSection"]["SLA"]={}

Data["FE"]["ColumnCount"] = 5
#Data["FE"]["RowCount"] = 20
Data["FE"]["Headers"] = ["Quantity\n", "Granularity_xVC12\n", "Granularity_xVC4\n", "\u03bb\n", "SLA\n"]
Data["FE"]["DataSection"] = {}
Data["FE"]["DataSection"]["Quantity"] = {}
Data["FE"]["DataSection"]["Granularity_xVC12"] = {}
Data["FE"]["DataSection"]["Granularity_xVC4"] = {}
Data["FE"]["DataSection"]["\u03bb"]={}
Data["FE"]["DataSection"]["SLA"]={}

Data["1GE"]["ColumnCount"] = 4
#Data["1GE"]["RowCount"] = 20
Data["1GE"]["Headers"] = ["Quantity\n", "Granularity\n", "\u03bb\n", "SLA\n"]
Data["1GE"]["DataSection"] = {}
Data["1GE"]["DataSection"]["Quantity"] = {}
Data["1GE"]["DataSection"]["Granularity"] = {}
Data["1GE"]["DataSection"]["\u03bb"] = {}
Data["1GE"]["DataSection"]["SLA"] = {}

Data["10GE"]["ColumnCount"] = 4
#Data["10GE"]["RowCount"] = 20
Data["10GE"]["Headers"] = ["Quantity\n", "Granularity\n", "\u03bb\n", "SLA\n"]
Data["10GE"]["DataSection"] = {}
Data["10GE"]["DataSection"]["Quantity"] = {}
Data["10GE"]["DataSection"]["Granularity"] = {}
Data["10GE"]["DataSection"]["\u03bb"]={}
Data["10GE"]["DataSection"]["SLA"]={}

Data["40GE"]["ColumnCount"] = 4
#Data["40GE"]["RowCount"] = 20
Data["40GE"]["Headers"] = ["Quantity\n", "Granularity\n", "\u03bb\n", "SLA\n"]
Data["40GE"]["DataSection"] = {}
Data["40GE"]["DataSection"]["Quantity"] = {}
Data["40GE"]["DataSection"]["Granularity"] = {}
Data["40GE"]["DataSection"]["\u03bb"]={}
Data["40GE"]["DataSection"]["SLA"]={}

Data["100GE"]["ColumnCount"] = 4
#Data["100GE"]["RowCount"] = 20
Data["100GE"]["Headers"] = ["Quantity\n", "Granularity\n", "\u03bb\n", "SLA\n"]
Data["100GE"]["DataSection"] = {}
Data["100GE"]["DataSection"]["Quantity"] = {}
Data["100GE"]["DataSection"]["Granularity"] = {}
Data["100GE"]["DataSection"]["\u03bb"]={}
Data["100GE"]["DataSection"]["SLA"]={}


DemandTabDataBase = {}
DemandTabDataBase["Source_Destination"] = {}
# format:
#       { <ClickedNode> : {"Source": <SourceName>, "DestinationList : <DestinationList>"} }
DemandTabDataBase["Services"] = {} # dynamic one : changes with user actions
# format: 
#       {(Tehran, karaj): { (1,3) : <State> }, ...}         (1 , 3) ---> 1 : Demand Id , 3 : Service Id
# this database just shows that witch services hasn't been assigned
# State:
#   0: means its has not been assigned
#   1: mean it has been assigned

DemandTabDataBase["Services_static"] = {}   # same as Services part but difference is that its not changing with user actions
# format:
#       { <SourceName> : { (<DemandId>, <ServiceId>) : QlistWidgetItem }}
# QlistWidgetItem:
#   text: Service Type
#   data: {"DemandId": <DemandId>, "ServiceId": <ServiceId>}
#   tooltip: "Source: {<Source>}\n Destination: {<Destination>}"
DemandTabDataBase["Lightpathes"] = {}
# format:
#       { (<SourceName>, <DestinationName>) : { <LightPathId> : QlistWidgetItem}}
#   QlistWidgetItem:
#   text: LightPath Type
#   data: { "LightPathId": <LightPathId>, "Capacity": <Capacity> , "Type": <Type>, "Source": <SourceName>, "Destination": <DestinationName>, "PanelId": <PanelId>}
DemandTabDataBase["Panels"] = {}
# format:
#       { Tehran:{1: MP2X, 2: MP1H, ..} , Karaj:{}, ...}

DemandTabDataBase["GroomOut10"] = {}
# format:
#       { ( <SourceName> , <DestinationName> ) : { <GroomGou10_Id> : QlistWidgetItem } }
#   QlistWidgetItem:
#   text:  "GroomOut10"
#   data:   { "GroomOut10Id": <GroomOutId>, "Capacity": <Capacity> , "Type": <Type>, "Source": <SourceName>, "Destination": <DestinationName>, "PanelId": <PanelId>, "DemandId": <DemandId>, "MP1H_Client_Id": (<MP1H Id>, <Client Id>)}

DemandTabDataBase["GroomOut10_status"] = {}
# format: 
#       {(Tehran, karaj): { (1,3) : <State> }, ...}         (1 , 3) ---> 1 : Demand Id , 3 : GroomOut10Id
# this database just shows that witch GroomOuts are connected to MP1H
# State:
#   0: not connected
#   1: connected

DemandTabDataBase["Failed_Demands"] = {}
# format:
#       { <SourceName> : <DestinationsList> }

DemandTabDataBase["Shelf_Count"] = {}
# format:
#       { <SourceName>: <LastShelfNum> }

GroomingTabDataBase = {}
GroomingTabDataBase["LightPathes"] = {}
# format:
#        { ( <SourceName> , <DestinationName> ) : { <Id> : { Working: <WorkingList> , Protection: <ProtectionList>, SNR_w = <Working SNR list>, SNR_p :<Protection SNR list> 
#                                                   RG_w = <Working Regenerator list>, RG_w = <Protection Regenerator list> }}}
# <WorkingList> and <DestinationList> are List of Ids
GroomingTabDataBase["Panels"] = {}
# format:
#       { <NodeName> : { ( <DegreeName>, <DegreeId> ): { <PanelId> : <PanelObject>}}}
# <DegreeName> : by this Node LightPath exits from the Source

GroomingTabDataBase["LinkState"] = {}
# format:
#       { ( <InNodeName> , <OutNodeName> ) : <LambdaList> }
# <LambdaList> : list of lambda ids

GroomingTabDataBase["NodeState"] = {}




from BLANK_Demand.BLANK_Demand import BLANK_Demand
from MP2X_Demand.MP2X_L_Demand import MP2X_L_Demand
from MP2X_Demand.MP2X_R_Demand import MP2X_R_Demand
from MP1H_Demand.MP1H_L_Demand import MP1H_L_Demand
from MP1H_Demand.MP1H_R_Demand import MP1H_R_Demand
from TP1H_Demand.TP1H_L_Demand import TP1H_L_Demand
from TP1H_Demand.TP1H_R_Demand import TP1H_R_Demand


class Panels:
    def __init__(self, NodesList, Shelf_Count_backref):

        self.PanelsHolderDict = {}  # this contains holders ( layouts )
        self.PanelsObjectDict = {}  # this contains Panels Data
        self.PanelsWidgetDict = {}  # this contains panels Widget
        self.Shelf_Count = Shelf_Count_backref

        for Node in NodesList:
            self.PanelsObjectDict[Node] = {}
            self.PanelsWidgetDict[Node] = {}
            self.Shelf_Count[Node] = 1
        # TODO: initialize PanelsHolderDict with 14 or more blank panel widget

    def calculate_dual_num(self, Destination):

        IdList = list(self.PanelsObjectDict[Destination].keys())
            
        # if shelf is empty this method must return 1 in ## string ##
        if not IdList:
            return ("1", "2")
        IdList = list(map(lambda x : int(x), IdList))

        MaxId = max(IdList)

        if ((MaxId + 1) // 14) + 1 > self.Shelf_Count[Destination]:
                self.Shelf_Count[Destination] = ((MaxId + 1) // 14) + 1

        for i in range(1, +1):
            if i not in IdList and (i+1) not in IdList:
                return (str(i), str(i+1))
        
        return (str(MaxId + 1), str(MaxId + 2))
    

    # NOTE: this method adds a panel object to PanelsObjectDict (database)
    def add_panel_data(self, Id, Source, Destination, data_class_l, data_class_r = None):

        DualPanelsNum = self.calculate_dual_num(Destination)
        uppernum = self.get_uppernum(Id)

        if data_class_l is self.BLANK:
            self.PanelsObjectDict[Source][Id] = self.BLANK(Id = Id,
                                                            Source= Source,
                                                            Destination= Destination)
        
        else:

            self.PanelsObjectDict[Source][Id] = data_class_l(Destination= Destination,
                                                        DualPanelsId= DualPanelsNum)
            
            # dual
            self.PanelsObjectDict[Destination][DualPanelsNum[0]] = data_class_l(Destination= Source,
                                                            DualPanelsId= (Id, uppernum))
        
        

        if data_class_r is not None:
            self.PanelsObjectDict[Source][uppernum] = data_class_r(Destination= Destination,
                                                        DualPanelsId= DualPanelsNum)
            
            # dual
            self.PanelsObjectDict[Destination][DualPanelsNum[1]] = data_class_r(Destination= Source,
                                                            DualPanelsId= (Id, uppernum))
        
        
        
        
    # NOTE: 
    def remove_panel_widget(self, Id, Source):
        data_class_l, widget_class_l = self.get_panels_class("BLANK")

        uppernum = self.get_uppernum(Id)

        # deleting left and right widget from holder
        self.del_old_widget(Id)
        self.del_old_widget(uppernum)

        Destination = self.PanelsObjectDict[Source][Id].Destination
        DualPanelsId = self.PanelsObjectDict[Source][Id].DualPanelsId

        # deleting left and right data object
        del self.PanelsObjectDict[Source][Id]
        del self.PanelsObjectDict[Source][uppernum]

        del self.PanelsObjectDict[Destination][DualPanelsId[0]]
        del self.PanelsObjectDict[Destination][DualPanelsId[1]]

        self.add_panel_data(Id, Source, Destination, data_class_l, data_class_l)

        self.PanelsWidgetDict[Id].addWidget(widget_class_l(Id, Source, Destination, self))
        self.PanelsWidgetDict[uppernum].addWidget(widget_class_l(uppernum, Source, Destination, self))
    
    def switch_widget(self, Id, Source, Local_Destination):

        self.del_old_widget(Id)

        if Id not in self.PanelsWidgetDict[Source]:
            
            self.PanelsWidgetDict[Source][Id] = BLANK_Demand(Id, Source, Local_Destination, self)

        

        self.PanelsHolderDict[Id].addWidget(self.PanelsWidgetDict[Source][Id])

        if self.PanelsWidgetDict[Source][Id].isVisible() is False:
            self.PanelsWidgetDict[Source][Id].setVisible(True)


    # NOTE: this method usage is in blank panel 
    def add_widget(self, Id, Source, Destination, Name):
        data_class_l, data_class_r, widget_class_l, widget_class_r = self.get_panels_class(Name)

        self.add_panel_data(Id, Source, Destination, data_class_l, data_class_r)

        uppernum = self.get_uppernum(Id)

        self.del_old_widget(Id)
        self.del_old_widget(uppernum)

        self.PanelsWidgetDict[Source][Id] = widget_class_l(Id, Source, Destination, self)
        self.PanelsWidgetDict[Source][uppernum] = widget_class_r(uppernum, Source, Destination)

        self.PanelsHolderDict[Id].addWidget(self.PanelsWidgetDict[Source][Id])
        self.PanelsHolderDict[uppernum].addWidget(self.PanelsWidgetDict[Source][uppernum])    

    
    def del_old_widget(self, Id):
        x = self.PanelsHolderDict[Id].takeAt(0)
        if x is not None:
            panel_widget = x.widget()
            #panel_widget.hide()
            
            self.PanelsHolderDict[Id].removeWidget(panel_widget)
            #panel_widget.deleteLater()

            panel_widget.hide()

    def add_widget_holder(self, Id, holder, Source, Destination, Name):
        self.PanelsHolderDict[Id] = holder

        """ if Name == "BLANK":
            data_class_l, _ = self.get_panels_class("BLANK")
            self.add_panel_data(Id, Source, Destination, data_class_l)
            self.PanelsWidgetDict[Source][Id] = BLANK_Demand(str(Id), Source, Destination, self)
            self.PanelsHolderDict[Id].addWidget(self.PanelsWidgetDict[Source][Id]) """

    def get_panels_class(self, Name):
        if Name == "BLANK":
            return self.BLANK, BLANK_Demand
        
        elif Name == "MP1H":
            return self.MP1H_L, self.MP1H_R, MP1H_L_Demand, MP1H_R_Demand
    
    def get_uppernum(self, Id):
        return str(int(Id) + 1)
    
    def get_data_object(self, Id, Source):
        return self.PanelsObjectDict[Source][Id]
    
    def clear_panels(self, Source= None, Destination=None):

        if Source is None and Destination is None:
        
            for key in self.Shelf_Count.keys():
                self.Shelf_Count[key] = 1
                self.PanelsWidgetDict[key].clear()
                self.PanelsObjectDict[key].clear()
        else:
            self.PanelsWidgetDict[Source].clear()
            self.PanelsWidgetDict[Destination].clear()

            self.PanelsObjectDict[Source].clear()
            self.PanelsObjectDict[Destination].clear()

            self.Shelf_Count[Source] = 1
            self.Shelf_Count[Destination] = 1
    
    def add_mp1h_widget(self, Id, Source, ClientsCapacity, LineCapacity, ServiceIdList, DemandIdList, LightPathId, LightPath_flag, Destination, DualPanelsId):
        uppernum = self.get_uppernum(Id)
        self.PanelsObjectDict[Source][Id] = self.MP1H_L(  ClientsCapacity= ClientsCapacity,
                                                            LineCapacity= LineCapacity,
                                                            ServiceIdList= ServiceIdList,
                                                            DemandIdList= DemandIdList,
                                                            LightPathId= LightPathId,
                                                            LightPath_flag= LightPath_flag,
                                                            Destination= Destination,
                                                            DualPanelsId= DualPanelsId)

        self.PanelsObjectDict[Destination][DualPanelsId[0]] = self.MP1H_L(  ClientsCapacity= ClientsCapacity,
                                                            LineCapacity= LineCapacity,
                                                            ServiceIdList= ServiceIdList,
                                                            DemandIdList= DemandIdList,
                                                            LightPathId= LightPathId,
                                                            LightPath_flag= LightPath_flag,
                                                            Destination= Source,
                                                            DualPanelsId= (Id, uppernum))
        
        self.PanelsObjectDict[Source][uppernum] = self.MP1H_R(    LeftId= Id,
                                                                    Destination= Destination,
                                                                    DualPanelsId= DualPanelsId)
        
        self.PanelsObjectDict[Destination][DualPanelsId[1]] = self.MP1H_R(    LeftId= DualPanelsId[0],
                                                                    Destination= Source,
                                                                    DualPanelsId= (Id, uppernum))
        
        self.PanelsWidgetDict[Source][Id] = MP1H_L_Demand(Id, Source, Destination, DualPanelsId, self)
        self.PanelsWidgetDict[Destination][DualPanelsId[0]] = MP1H_L_Demand(DualPanelsId[0], Destination, Source, (Id, uppernum), self)

        self.PanelsWidgetDict[Source][uppernum] = MP1H_R_Demand(uppernum, Source, Destination, DualPanelsId)
        self.PanelsWidgetDict[Destination][DualPanelsId[1]] = MP1H_R_Demand(DualPanelsId[1], Destination, Source, (Id, uppernum))

    def complete_MP1H(self, panel, widget, widget_dual, Source, Destination):
        LightPathId = panel.LightPathId
        for i in range(len(panel.ClientsCapacity)):
            
            if panel.ClientsCapacity[i] != 0:
                # finding object of client customlabel
                text = "Client" + str( i + 1 )
                clientvar = getattr(widget, text)
                clientvar_dual = getattr(widget_dual, text)

                if clientvar.ClientNum % 2 == 0:
                    clientvar.setStyleSheet("image: url(:/CLIENT_L_Selected_SOURCE/CLIENT_L_Selected.png);")
                    clientvar_dual.setStyleSheet("image: url(:/CLIENT_L_Selected_SOURCE/CLIENT_L_Selected.png);")
                else:
                    clientvar.setStyleSheet("image: url(:/CLIENT_R_Selected_SOURCE/CLIENT_R_Selected.png);")
                    clientvar_dual.setStyleSheet("image: url(:/CLIENT_R_Selected_SOURCE/CLIENT_R_Selected.png);")
                # checking its GroomOut10 or not
                if (panel.DemandIdList[i],panel.ServiceIdList[i]) in DemandTabDataBase["Services_static"][Source]:
                    clientvar.setToolTip(DemandTabDataBase["Services_static"][Source][(panel.DemandIdList[i],panel.ServiceIdList[i])].toolTip())
                    clientvar_dual.setToolTip(DemandTabDataBase["Services_static"][Destination][(panel.DemandIdList[i],panel.ServiceIdList[i])].toolTip())
                else:
                    clientvar.setToolTip(DemandTabDataBase["GroomOut10"][(Source, Destination)][panel.ServiceIdList[i]].toolTip())
                    clientvar_dual.setToolTip(DemandTabDataBase["GroomOut10"][(Destination, Source)][panel.ServiceIdList[i]].toolTip())

                clientvar.servicetype = panel.ClientsCapacity[i]
                clientvar.nodename = Source
                clientvar.Destination = Destination
                clientvar.ids = [panel.DemandIdList[i], panel.ServiceIdList[i]]

                clientvar_dual.servicetype = panel.ClientsCapacity[i]
                clientvar_dual.nodename = Destination
                clientvar_dual.Destination = Source
                clientvar_dual.ids = [panel.DemandIdList[i], panel.ServiceIdList[i]]

                if panel.ClientsCapacity[i] == "GroomOut10":
                    UserData = DemandTabDataBase["GroomOut10"][(Source, Destination)][panel.ServiceIdList[i]].data(Qt.UserRole)
                    clientvar.GroomOut_Capacity = UserData["Capacity"]
                    clientvar_dual.GroomOut_Capacity = UserData["Capacity"]

                clientvar.setAcceptDrops(False)
                clientvar_dual.setAcceptDrops(False)

                # adding tooltip to line port
                linevar = getattr(widget, "Line")
                linevar_dual = getattr(widget_dual, "Line")

                linevar.setToolTip(DemandTabDataBase["Lightpathes"][(Source, Destination)][LightPathId].toolTip())
                linevar_dual.setToolTip(DemandTabDataBase["Lightpathes"][(Destination, Source)][LightPathId].toolTip())

                linevar.setStyleSheet("QLabel{ image: url(:/Line_Selected_SOURCE/Line_Selected.png); }")
                linevar_dual.setStyleSheet("QLabel{ image: url(:/Line_Selected_SOURCE/Line_Selected.png); }")
    
    def complete_all(self, Name):
        for name in Name:
            if name == "MP1H":
                cls = self.MP1H_L
            elif name == "TP1H":
                cls = self.TP1H_L
            elif name == "MP2X":
                cls = self.MP2X_L


            for Source, obj in self.PanelsObjectDict.items():
                for Id, panel in obj.items():
                    if isinstance(panel, cls):
                        Destination = panel.Destination
                        DualId = panel.DualPanelsId[0]
                        fun = getattr(self, 'complete_' + name)
                        fun(panel= panel,
                            widget= self.PanelsWidgetDict[Source][Id],
                            widget_dual= self.PanelsWidgetDict[Destination][DualId],
                            Source= Source,
                            Destination= Destination)
    
    def add_tp1h_widget(self, Id, Source, DemandId, ServiceId, Line, LightPathId, Destination, DualPanelsId):
        uppernum = self.get_uppernum(Id)

        self.PanelsObjectDict[Source][Id] =  self.TP1H_L(   DemandId= DemandId,
                                                            ServiceId= ServiceId,
                                                            Line= Line,
                                                            LightPathId= LightPathId,
                                                            Destination= Destination,
                                                            DualPanelsId= DualPanelsId)
        
        self.PanelsObjectDict[Destination][DualPanelsId[0]] =  self.TP1H_L( DemandId= DemandId,
                                                                            ServiceId= ServiceId,
                                                                            Line= Line,
                                                                            LightPathId= LightPathId,
                                                                            Destination= Source,
                                                                            DualPanelsId= (Id, uppernum))
        
        self.PanelsObjectDict[Source][uppernum] = self.TP1H_R(LeftId= Id,
                                                                Destination= Destination,
                                                                DualPanelsId= DualPanelsId)
        
        self.PanelsObjectDict[Destination][DualPanelsId[1]] = self.TP1H_R(LeftId= DualPanelsId[0],
                                                                Destination= Source,
                                                                DualPanelsId= (Id, uppernum))

        self.PanelsWidgetDict[Source][Id] = TP1H_L_Demand(Id, Source, Destination, DualPanelsId, self)
        self.PanelsWidgetDict[Destination][DualPanelsId[0]] = TP1H_L_Demand(DualPanelsId[0], Destination, Source, (Id, uppernum), self)

        self.PanelsWidgetDict[Source][uppernum] = TP1H_R_Demand(uppernum, Source, Destination, DualPanelsId)
        self.PanelsWidgetDict[Destination][DualPanelsId[1]] = TP1H_R_Demand(DualPanelsId[1], Destination, Source, (Id, uppernum))

        
    
    def complete_TP1H(self, panel, widget, widget_dual, Source, Destination):
        LightPathId = panel.LightPathId

        if panel.Line == "100GE":

            # finding object of client customlabel
            clientvar = getattr(widget, "Client")
            clientvar_dual = getattr(widget_dual, "Client")

            # filling customlabel attributes 
            clientvar.setToolTip(DemandTabDataBase["Services_static"][Source][(panel.DemandId, panel.ServiceId)].toolTip())
            clientvar.servicetype = "100GE"
            clientvar.nodename = Source
            clientvar.Destination = Destination
            clientvar.ids = [panel.DemandId, panel.ServiceId]
            clientvar.setAcceptDrops(False)

            clientvar_dual.setToolTip(DemandTabDataBase["Services_static"][Destination][(panel.DemandId, panel.ServiceId)].toolTip())
            clientvar_dual.servicetype = "100GE"
            clientvar_dual.nodename = Destination
            clientvar_dual.Destination = Source
            clientvar_dual.ids = [panel.DemandId, panel.ServiceId]
            clientvar_dual.setAcceptDrops(False)

            clientvar.setStyleSheet("image: url(:/TP1H_CLIENT_Selected_SOURCE/TP1H_CLIENT_Selected.png);")
            clientvar_dual.setStyleSheet("image: url(:/TP1H_CLIENT_Selected_SOURCE/TP1H_CLIENT_Selected.png);")


            LineVar = getattr(widget, "Line")
            LineVar_dual = getattr(widget_dual, "Line")

            LineVar.setToolTip(DemandTabDataBase["Lightpathes"][(Source, Destination)][LightPathId].toolTip())

            LineVar.setStyleSheet("QLabel{ image: url(:/Line_Selected_SOURCE/Line_Selected.png); }")

            LineVar_dual.setToolTip(DemandTabDataBase["Lightpathes"][(Destination, Source)][LightPathId].toolTip())

            LineVar_dual.setStyleSheet("QLabel{ image: url(:/Line_Selected_SOURCE/Line_Selected.png); }")

    def add_mp2x_widget(self, Id, Source, ClientsCapacity, LinesCapacity, ServiceIdList, DemandIdList, LineIdList, Line_1_ServiceIdList, Destination, DualPanelsId, Line_2_ServiceIdList= None):
        uppernum = self.get_uppernum(Id)

        self.PanelsObjectDict[Source][Id] = self.MP2X_L(ClientsCapacity= ClientsCapacity,
                                                        LinesCapacity= LinesCapacity,
                                                        ServiceIdList= ServiceIdList,
                                                        DemandIdList= DemandIdList,
                                                        LineIdList= LineIdList,
                                                        Line_1_ServiceIdList= Line_1_ServiceIdList,
                                                        Line_2_ServiceIdList= Line_2_ServiceIdList,
                                                        Destination= Destination,
                                                        DualPanelsId= DualPanelsId)
        

        self.PanelsObjectDict[Destination][DualPanelsId[0]] = self.MP2X_L(  ClientsCapacity= ClientsCapacity,
                                                                            LinesCapacity= LinesCapacity,
                                                                            ServiceIdList= ServiceIdList,
                                                                            DemandIdList= DemandIdList,
                                                                            LineIdList= LineIdList,
                                                                            Line_1_ServiceIdList= Line_1_ServiceIdList,
                                                                            Line_2_ServiceIdList= Line_2_ServiceIdList,
                                                                            Destination= Source,
                                                                            DualPanelsId= (Id, uppernum))
        
        self.PanelsObjectDict[Source][uppernum] = self.MP2X_R(LeftId= Id,
                                                        Destination= Destination,
                                                        DualPanelsId= DualPanelsId)

        self.PanelsObjectDict[Destination][DualPanelsId[1]] = self.MP2X_R(  LeftId= DualPanelsId[0],
                                                                            Destination= Source,
                                                                            DualPanelsId= (Id, uppernum))

        
        self.PanelsWidgetDict[Source][Id] = MP2X_L_Demand(Id, Source, Destination, DualPanelsId, self)
        self.PanelsWidgetDict[Destination][DualPanelsId[0]] = MP2X_L_Demand(DualPanelsId[0], Destination, Source, (Id, uppernum), self)

        self.PanelsWidgetDict[Source][uppernum] = MP2X_R_Demand(uppernum, Source, Destination, DualPanelsId)
        self.PanelsWidgetDict[Destination][DualPanelsId[1]] = MP2X_R_Demand(DualPanelsId[1], Destination, Source, (Id, uppernum))

    def complete_MP2X(self, panel, widget, widget_dual, Source, Destination):

        GroomOutId_1, GroomOutId_2 = panel.LineIdList

        for i in range(len(panel.ClientsCapacity)):
            if panel.ClientsCapacity[i] != 0:

                # finding object of client customlabel
                text = "CLIENT" + str( i + 1 )
                clientvar = getattr(widget, text)
                clientvar_dual = getattr(widget_dual, text)

                if clientvar.ClientNum % 2 == 0:
                    clientvar.setStyleSheet("image: url(:/CLIENT_L_Selected_SOURCE/CLIENT_L_Selected.png);")
                    clientvar_dual.setStyleSheet("image: url(:/CLIENT_L_Selected_SOURCE/CLIENT_L_Selected.png);")
                else:
                    clientvar.setStyleSheet("image: url(:/CLIENT_R_Selected_SOURCE/CLIENT_R_Selected.png);")
                    clientvar_dual.setStyleSheet("image: url(:/CLIENT_R_Selected_SOURCE/CLIENT_R_Selected.png);")
                
                clientvar.setToolTip(DemandTabDataBase["Services_static"][Source][(panel.DemandIdList[i],panel.ServiceIdList[i])].toolTip())
                clientvar_dual.setToolTip(DemandTabDataBase["Services_static"][Destination][(panel.DemandIdList[i],panel.ServiceIdList[i])].toolTip())

                clientvar.servicetype = panel.ClientsCapacity[i]
                clientvar.nodename = Source
                clientvar.Destination = Destination
                clientvar.ids = [panel.DemandIdList[i], panel.ServiceIdList[i]]
                clientvar.setAcceptDrops(False)

                clientvar_dual.servicetype = panel.ClientsCapacity[i]
                clientvar_dual.nodename = Destination
                clientvar_dual.Destination = Source
                clientvar_dual.ids = [panel.DemandIdList[i], panel.ServiceIdList[i]]
                clientvar_dual.setAcceptDrops(False)

                # adding tooltip to line port
                linevar_1 = getattr(widget, "LINE1")
                linevar_1_dual = getattr(widget_dual, "LINE1")

                linevar_1.setToolTip(DemandTabDataBase["GroomOut10"][(Source, Destination)][GroomOutId_1].toolTip())
                linevar_1_dual.setToolTip(DemandTabDataBase["GroomOut10"][(Destination, Source)][GroomOutId_1].toolTip())

                linevar_1.setStyleSheet("QLabel{ image: url(:/Line_L_Selected_SOURCE/Line_L_Selected.png); }")
                linevar_1_dual.setStyleSheet("QLabel{ image: url(:/Line_L_Selected_SOURCE/Line_L_Selected.png); }")

                if GroomOutId_2 is not None:
                    linevar_2 = getattr(widget, "LINE2")
                    linevar_2.setToolTip(DemandTabDataBase["GroomOut10"][(Source, Destination)][GroomOutId_2].toolTip())

                    linevar_2.setStyleSheet("QLabel{ image: url(:/Line_R_Selected_SOURCE/Line_R_Selected.png); }")

                    linevar_2_dual = getattr(widget_dual, "LINE2")
                    linevar_2_dual.setToolTip(DemandTabDataBase["GroomOut10"][(Destination, Source)][GroomOutId_2].toolTip())

                    linevar_2_dual.setStyleSheet("QLabel{ image: url(:/Line_R_Selected_SOURCE/Line_R_Selected.png); }")


    # NOTE: Start of Class Definitions      

    class BLANK:
        def __init__(self, Id, Source, Destination):
            self.Id = Id
            self.Source = Source
            self.Destination = Destination      

    class MP1H_L:

        def __init__(self, ClientsCapacity = None, LineCapacity = 0, ServiceIdList = None, 
        DemandIdList = None, LightPathId = None, LightPath_flag = 0, Destination = None, DualPanelsId = None):

            if ClientsCapacity is None:
                self.ClientsCapacity = [0 for i in range(10)]
            else:
                self.ClientsCapacity = ClientsCapacity
            
            if ServiceIdList is None:
                self.ServiceIdList = [None for i in range(10)]
            else:
                self.ServiceIdList = ServiceIdList
            
            if DemandIdList is None:
                self.DemandIdList = [None for i in range(10)]
            else:
                self.DemandIdList = DemandIdList
            
            self.Destination = Destination
            self.LightPath_flag = LightPath_flag
            self.LightPathId = LightPathId
            self.LineCapacity = LineCapacity
            self.DualPanelsId = DualPanelsId

    class MP1H_R:
        def __init__(self, LeftId, Destination, DualPanelsId):
            self.Destination = Destination
            self.LeftId = LeftId
            self.DualPanelsId = DualPanelsId

    class MP2X_L:
        def __init__(self, ClientsCapacity = None, LinesCapacity = None, ServiceIdList = None, DemandIdList = None
                        , LineIdList = None, Line_1_ServiceIdList = None, Line_2_ServiceIdList = None, Destination = None, DualPanelsId = None):

            if ClientsCapacity is None:
                self.ClientsCapacity = [0 for i in range(16)]
            else:
                self.ClientsCapacity = ClientsCapacity

            if LinesCapacity is None:
                self.LinesCapacity = [0, 0]
            else:
                self.LinesCapacity = LinesCapacity
        
            if ServiceIdList is None:
                self.ServiceIdList = [None for i in range(16)]
            else:
                self.ServiceIdList = ServiceIdList
            
            if DemandIdList is None:
                self.DemandIdList = [None for i in range(16)]
            else:
                self.DemandIdList = DemandIdList
            
            if LineIdList is None:
                self.LineIdList = [None for i in range(2)]
            else:
                self.LineIdList = LineIdList
            
            if Line_1_ServiceIdList is None:
                self.Line_1_ServiceIdList = []
            else:
                self.Line_1_ServiceIdList = Line_1_ServiceIdList

            if Line_2_ServiceIdList is None:
                self.Line_2_ServiceIdList = []
            else:
                self.Line_2_ServiceIdList = Line_2_ServiceIdList
            
            self.Destination = Destination
            self.DualPanelsId = DualPanelsId

    class MP2X_R:
        def __init__(self, LeftId, Destination, DualPanelsId):
            self.LeftId = LeftId
            self.Destination = Destination
            self.DualPanelsId = DualPanelsId

    class TP1H_L:
        def __init__(self, DemandId = None, ServiceId = None, Line = 0, LightPathId = None, Destination = None, DualPanelsId = None):
            self.Destination = Destination
            self.LightPathId = LightPathId
            self.DemandId = DemandId
            self.ServiceId = ServiceId
            self.Line = Line
            self.DualPanelsId = DualPanelsId

    class TP1H_R:
        def __init__(self, LeftId, Destination, DualPanelsId):
            self.Destination = Destination
            self.LeftId = LeftId
            self.DualPanelsId = DualPanelsId



class MP2D_L:
    def __init__(self, ClientsCapacity = [0, 0], LineCapacity = 0, LineType = "200GE"):
        self.ClientsCapacity = ClientsCapacity
        self.LineCapacity = LineCapacity
        self.LineType = LineType
    
    def add_client(self, ClientNum , LineCapacity):
        self.ClientsCapacity[ClientNum] = "100GE"
        self.LineCapacity = LineCapacity

    def del_client(self, ClientNum, LineCapacity):
        self.ClientsCapacity[ClientNum] = 0
        self.LineCapacity = LineCapacity
    
    def set_line_type(self, Type):
        self.LineType = Type

class MP2D_R:
    def __init__(self, LeftId):
        self.LeftId = LeftId




    
    





class SC:
    def __init__(self):
        pass

class BAF3:
    def __init__(self):
        pass

class PAF3:
    def __init__(self):
        pass

class LAF3:
    def __init__(self):
        pass


# TODO: this class is uncompleted
class TP2X:
    def __init__(self):
        pass
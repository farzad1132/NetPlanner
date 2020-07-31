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
        
        
        
        
    # NOTE: this method switches panels widget at single or double slot
    def remove_panel_widget(self, Id, Source):
        data_class_l, widget_class_l = self.get_panels_class("BLANK")

        uppernum = self.get_uppernum(Id)

        # deleting left and right widget from holder
        self.del_old_widget(Id)
        self.del_old_widget(uppernum)

        Destination = self.PanelsObjectDict[Source][Id].Destination

        # deleting left and right data object
        del self.PanelsObjectDict[Source][Id]
        del self.PanelsObjectDict[Source][uppernum]

        self.add_panel_data(Id, Source, Destination, data_class_l, data_class_l)

        self.PanelsWidgetDict[Id].addWidget(widget_class_l(Id, Source, Destination))
        self.PanelsWidgetDict[uppernum].addWidget(widget_class_l(uppernum, Source, Destination))
    
    def switch_widget(self, Id, Source, Local_Destination):

        uppernum = self.get_uppernum(Id)

        self.del_old_widget(Id)
        self.del_old_widget(uppernum)

        if Id  not in self.PanelsWidgetDict[Source]:
            self.PanelsWidgetDict[Source][Id] = BLANK_Demand(Id, Source, Local_Destination)

        self.PanelsHolderDict[Id].addWidget(self.PanelsWidgetDict[Source][Id])

        if uppernum not in self.PanelsWidgetDict[Source]:
            self.PanelsWidgetDict[Source][uppernum] = BLANK_Demand(uppernum, Source, Local_Destination)
        
        self.PanelsHolderDict[uppernum].addWidget(self.PanelsWidgetDict[Source][uppernum])

    
    def add_widget(self, Id, Source, Destination, Name):
        data_class_l, data_class_r, widget_class_l, widget_class_r = self.get_panels_class(Name)

        self.add_panel_data(Id, Source, Destination, data_class_l, data_class_r)

        uppernum = self.get_uppernum(Id)

        self.PanelsWidgetDict[Source][Id] = widget_class_l(Id, Source, Destination)
        self.PanelsWidgetDict[Source][uppernum] = widget_class_r(uppernum, Source, Destination)
            

    
    def del_old_widget(self, Id):

        panel_widget = self.PanelsHolderDict[Id].takeAt(0).widget()
        self.PanelsHolderDict[Id].removeWidget(panel_widget)
        panel_widget.deleteLater()

    def add_widget_holder(self, Id, holder, Source, Destination, Name):
        self.PanelsHolderDict[Id] = holder

        if Name == "BLANK":
            data_class_l, _ = self.get_panels_class("BLANK")
            self.add_panel_data(Id, Source, Destination, data_class_l)
            self.PanelsWidgetDict[Source][Id] = BLANK_Demand(str(Id), Source, Destination)
            self.PanelsHolderDict[Id].addWidget(self.PanelsWidgetDict[Source][Id])

    def get_panels_class(self, Name):
        if Name == "BLANK":
            return self.BLANK, BLANK_Demand
        
        elif Name == "MP1H":
            return self.MP1H_L, self.MP1H_R, MP1H_L_Demand, MP1H_R_Demand
    
    def get_uppernum(self, Id):
        return str(int(Id) + 1)



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
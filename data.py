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
Data["Grouping"] = {}

# keys are row numbers except nodes and links

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
Data["General"]["DataSection"]["8"] = {} # 8: Degree

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
#       { source :  [ Destinations ]}
DemandTabDataBase["Services"] = {}
# format: 
#       {(Tehran, karaj): { (1,3) : '[1 , 3] # 100G ' , ... }, ...}         (1 , 3) ---> 1 : Demand Id , 3 : Service Id
DemandTabDataBase["Lightpathes"] = {}
# format:
#       {(Tehran, Karaj): [ Lightpath Id # 100GE , ...]}
DemandTabDataBase["Panels"] = {}
# format:
#       { Tehran:{1: MP2X, 2: MP1H, ..} , Karaj:{}, ...}

GroomingTabDataBase = {}
GroomingTabDataBase["LightPathes"] = {}
# format:
#        { ( <SourceName> , <DestinationName> ) : { <Id> : { Working: <WorkingList> , Protection: <ProtectionList> }}}
# <WorkingList> and <DestinationList> are List of Ids
GroomingTabDataBase["Panels"] = {}
# format:
#       { <NodeName> : { ( <DegreeName>, <DegreeId> ): { <PanelId> : <PanelObject>}}}
# <DegreeName> : by this Node LightPath exits from the Source

GroomingTabDataBase["Links"] = {}
# format:
#       { ( <InNodeName> , <OutNodeName> ) : <LambdaList> }
# <LambdaList> : list of lambda ids


class MP2D_L:
    def __init__(self, ClientsCapacity = [0, 0], LineCapacity = 0, LineType = "200GE"):
        self.ClientsCapacity = ClientsCapacity
        self.LineCapacity = LineCapacity
        self.LineType = LineType
    
    def add_client(self, ClientNum , LineCapacity):
        self.ClientsCapacity[ClientNum] = "100GE"
        self.LineCapacity = LineCapacity

    def del_client(self, ClientNum, LineCapacity):
        self.self.ClientsCapacity[ClientNum] = 0
        self.LineCapacity = LineCapacity
    
    def set_line_type(self, Type):
        self.LineType = Type

class MP2D_R:
    def __init__(self, LeftId):
        self.LeftId = LeftId

class MP2X_L:
    def __init__(self, ClientsType = [0 for i in range(16)], LinesCapacity = [0, 0]):
        self.ClientsType = ClientsType
        self.LinesCapacity = LinesCapacity
    
    def add_client(self, ClientNum, Type):
        self.ClientsType[ClientNum] = Type
    
    def del_client(self, ClientNum):
        self.ClientsType[ClientNum] = 0

class MP2X_R:
    def __init__(self, LeftId):
        self.LeftId = LeftId

class MP1H_L:
    def __init__(self, ClientsCapacity = None, LineCapacity = 0, ServiceIdList = None, 
    DemandIdList = None, LightPathId = None, LightPath_flag = 0):

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
        

        self.LightPath_flag = LightPath_flag
        self.LightPathId = LightPathId
        self.LineCapacity = LineCapacity
    
    def add_client(self, ClientNum, Type, LineCapacity):
        # type can be 10GE or stm64
        self.ClientsCapacity[ClientNum] = Type
        self.LineCapacity = LineCapacity
    
    def del_client(self, ClientNum, LineCapacity):
        self.ClientsCapacity[ClientNum] = 0
        self.LineCapacity = LineCapacity

class MP1H_R:
    def __init__(self, LeftId):
        self.LeftId = LeftId

class TP1H_L:
    def __init__(self, DemandId = None, ServiceId = None, Line = 0, LightPathId = None):
        self.LightPathId = LightPathId
        self.DemandId = DemandId
        self.ServiceId = ServiceId
        self.Line = Line

class TP1H_R:
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
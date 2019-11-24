class Network:
    def __init__(self,NumWaveLength):
        self.NumWaveLength = NumWaveLength

        self.PhysicalTopology = self.Topology()
        self.TrafficMatrix = self.Traffic()
        

    class Topology:

        def __init__(self):

            self.NodeDict = {}
            self.LinkDict = {}
            self.ClusterDict = {}
        
        def add_node(self, Location, Type = "Not Declared"):
            Id = self.Node.ReferenceId
            self.NodeDict[Id] = self.Node(Location, Type)
            self.Node.ReferenceId += 1
        
        def add_link(self, InNode, OutNode, NumSpan):
            self.LinkDict[(InNode , OutNode)] = self.Link(InNode,OutNode,NumSpan);

        def add_cluster(self,Id,GatewayId, SubNodesId,Color):
            self.ClusterDict.append(self.Cluster(Id,GatewayId, SubNodesId,Color))

        class Node:
            ReferenceId = 1
            # Id must be an int number
            # Location format must be (lat,lng) in int
            def __init__(self, Location, Type = "not declared"):
                self.Id = self.ReferenceId
                self.Location = Location
                self.Type = Type
                self.degrees = []
                self.services = []
                self.AmplifierList = []
            
            def add_amplifier(self,nf):
                self.AmplifierList.append(self.Amplifier(nf))


            class Amplifier:
                def __init__(self, nf):
                    self.Id = Id
                    
                    self.nf = nf        # nf : noise figure
            
        class Link:
            def __init__(self, InNode, OutNode, NumSpan):

                self.InNode = InNode
                self.OutNode = OutNode
                self.NumSpan = NumSpan
                self.SpanObjList = [self.Span(self.InNode,self.OutNode) for i in range(NumSpan)]

                self.WaveLengthList = []
                self.LightPathList = {}    # in  { service : Type of lightpath } format

            def put_fiber_Type(self,SpanPosition, Length, Loss, Dispersion, Beta,Gamma, PositionInLink, Snr):
                self.SpanObjList[SpanPosition].put_fiber_Type(Length, Loss, Dispersion, Beta, Gamma, PositionInLink, Snr)
            
            class Span:
                def __init__(self, InNode, OutNode, Length = None, Loss = None, Dispersion = None, Beta = None,
                Gamma = None, PositionInLink = 0, Snr = None):

                    self.InNode = InNode
                    self.OutNode = OutNode
                    self.Length = Length
                    self.Loss = Loss
                    self.Dispersion = Dispersion
                    self.Beta = Beta
                    self.Gamma = Gamma

                    # Snr is a vector ---> size = NumWaveLength
                    self.Snr = Snr

                    # 0 value for this variable means first and so on ...
                    self.PositionInLink = PositionInLink

                def put_fiber_Type(self, Length, Loss, Dispersion, Beta, Gamma, PositionInLink, Snr):

                    self.Length = Length
                    self.Loss = Loss
                    self.Dispersion = Dispersion
                    self.Beta = Beta
                    self.Gamma = Gamma
                    self.PositionInLink = PositionInLink
                    self.Snr
            
        class Cluster:
            def __init__(self, Id, GatewayId, SubNodesId, Color):
                # the Id can be whether gateway node Id or user-defined Id ( in GUI )
                self.Id = Id
                self.GatewayId = GatewayId 

                # SubNodesId is a list of Ids
                self.SubNodesId = SubNodesId
                self.Color = Color


    class Traffic:
        def __init__(self):
            self.DemandDict = {}    # in { id : DemandObj } format
        
        def add_demand(self, Id, Source, Destination, Type):
            self.DemandDict[Id] = self.Demand(Id, Source, Destination, Type)

        class Demand:
            
            # this class is one row of Traffic Matrix
            def __init__(self, Id, Source, Destination, Type):

                self.ServiceId = 1 
                self.Id = Id
                self.Source = Source
                self.Destination = Destination
                self.Type = Type            # Type must be a string
                self.ServiceDict = {}
            
            class G_100:
                def __init__(self, Id, Granularity, Sla, DemandId, IgnoringNodes, WaveLength = None, LightPathId = None):
                    self.Id = Id
                    self.Granularity = Granularity
                    self.WaveLength = WaveLength
                    self.Sla = Sla
                    self.DemandId = DemandId
                    self.IgnoringNodes = IgnoringNodes
                    self.LightPathId = LightPathId
            
            class G_40:
                def __init__(self, Id, Granularity, Sla, DemandId, IgnoringNodes, WaveLength = None, LightPathId = None):
                    self.Id = Id
                    self.Granularity = Granularity
                    self.WaveLength = WaveLength
                    self.Sla = Sla
                    self.DemandId = DemandId
                    self.IgnoringNodes = IgnoringNodes
                    self.LightPathId = LightPathId

            
            class G_10:
                def __init__(self, Id, Granularity, Sla, DemandId, IgnoringNodes, WaveLength = None, LightPathId = None):
                    self.Id = Id
                    self.Granularity = Granularity
                    self.WaveLength = WaveLength
                    self.Sla = Sla
                    self.DemandId = DemandId
                    self.IgnoringNodes = IgnoringNodes
                    self.LightPathId = LightPathId

            
            class G_1:
                def __init__(self, Id, Granularity, Sla, DemandId, IgnoringNodes, WaveLength = None, LightPathId = None):
                    self.Id = Id
                    self.Granularity = Granularity
                    self.WaveLength = WaveLength
                    self.Sla = Sla
                    self.DemandId = DemandId
                    self.IgnoringNodes = IgnoringNodes
                    self.LightPathId = LightPathId

                    self.BW = 1.244
                
            
            class G_1:
                def __init__(self, Id, Granularity, Sla, DemandId, IgnoringNodes, WaveLength = None, LightPathId = None):
                    self.Id = Id
                    self.Granularity = Granularity
                    self.WaveLength = WaveLength
                    self.Sla = Sla
                    self.DemandId = DemandId
                    self.IgnoringNodes = IgnoringNodes
                    self.LightPathId = LightPathId

                    self.BW = 1.244
            
            class FE:
                def __init__(self, Id, Granularity_vc12 ,Granularity_vc4, Sla,DemandId, IgnoringNodes, WaveLength = None, LightPathId = None):
                    self.Id = Id
                    self.Granularity_vc12 = Granularity_vc12
                    self.Granularity_vc4 = Granularity_vc4
                    self.WaveLength = WaveLength
                    self.Sla = Sla
                    self.DemandId = DemandId
                    self.IgnoringNodes = IgnoringNodes
                    self.LightPathId = LightPathId

                    self.BW = 1
                
            
            class STM_64:
                def __init__(self, Id, Sla, DemandId, IgnoringNodes, WaveLength = None, LightPathId = None):
                    self.Id = Id
                    self.WaveLength = WaveLength
                    self.Sla = Sla
                    self.DemandId = DemandId
                    self.IgnoringNodes = IgnoringNodes
                    self.LightPathId = LightPathId

                    self.BW = 9.95
            
            class STM_16:
                def __init__(self, Id, Sla,DemandId, IgnoringNodes, WaveLength = None, LightPathId = None):
                    self.Id = Id
                    self.WaveLength = WaveLength
                    self.Sla
                    self.DemandId = DemandId
                    self.IgnoringNodes = IgnoringNodes
                    self.LightPathId = LightPathId

                    self.BW = 2.49


            class STM_4:
                def __init__(self, Id, Sla, DemandId, IgnoringNodes, WaveLength = None, LightPathId = None):
                    self.Id = Id
                    self.WaveLength = WaveLength
                    self.Sla = Sla

                    self.sDemandId = DemandId
                    self.IgnoringNodes = IgnoringNodes
                    self.LightPathId = LightPathId

                    # BW : Band WIdth
                    self.BW = 622.08 / 1000

            class STM_1_Optical:
                def __init__(self, Id, Sla, DemandId, IgnoringNodes, WaveLength = None, LightPathId = None):
                    self.Id = Id
                    self.WaveLength = WaveLength
                    self.Sla = Sla
                    self.DemandId = DemandId
                    self.IgnoringNodes = IgnoringNodes
                    self.LightPathId = LightPathId

                    # BW : Band WIdth in Gb/s
                    self.BW = 155.52 / 1000
                
            
            class STM_1_Electrical:
                def __init__(self, Id, Sla, DemandId, IgnoringNodes, LightPathId = None):
                    self.Id = Id
                    self.Sla = Sla
                    self.DemandId =DemandId
                    self.IgnoringNodes = IgnoringNodes
                    self.LightPathId = LightPathId

                    # BW = Band WIdth in Gb/s
                    self.BW = 155.52 / 1000
                
            
            class E1:
                def __init__(self, Id, Sla,DemandId, IgnoringNodes, LightPathId = None):
                    self.Id = Id
                    self.Sla = Sla
                    self.DemandId =DemandId
                    self.IgnoringNodes = IgnoringNodes
                    self.LightPathId = LightPathId

                    # BW : Band WIdth in Gb/s
                    self.BW = 58.84 / 1000
            
            def GenerateId(self):
                self.ServiceId += 1
                return ( self.ServiceId - 1 )
            
            def add_service(self, ServiceType, Sla, IgnoringNodes, WaveLength = None, Granularity = None, Granularity_vc12 = None,
            Granularity_vc4 = None, LightPathId = None):

                ServiceId = self.GenerateId()

                if ServiceType == "E1":
                    self.ServiceDict[ServiceId] = self.E1(ServiceId, Sla, self.Id, IgnoringNodes, LightPathId)

                elif ServiceType == "STM_1_Electrical":
                    self.ServiceDict[ServiceId] = self.STM_1_Electrical(ServiceId, Sla, self.Id, IgnoringNodes, LightPathId)

                elif ServiceType == "STM_1_Optical":
                    self.ServiceDict[ServiceId] = self.STM_1_Optical(ServiceId, Sla, self.Id, IgnoringNodes, WaveLength, LightPathId)

                elif ServiceType == "STM_4":
                    self.ServiceDict[ServiceId] = self.STM_4(ServiceId, Sla, self.Id, IgnoringNodes, WaveLength, LightPathId)

                elif ServiceType == "STM_16":
                    self.ServiceDict[ServiceId] = self.STM_16(ServiceId, Sla, self.Id, IgnoringNodes, WaveLength, LightPathId)

                elif ServiceType == "STM_64":
                    self.ServiceDict[ServiceId] = self.STM_64(ServiceId, Sla, self.Id, IgnoringNodes, WaveLength, LightPathId)

                elif ServiceType == "FE":
                    self.ServiceDict[ServiceId] = self.FE(ServiceId, Granularity_vc12, Granularity_vc4, Sla, self.Id, IgnoringNodes, WaveLength, LightPathId)

                elif ServiceType == "1GE":
                    self.ServiceDict[ServiceId] = self.G_1(ServiceId, Granularity, Sla, self.Id, IgnoringNodes, WaveLength, LightPathId)

                elif ServiceType == "10GE":
                    self.ServiceDict[ServiceId] = self.G_10(ServiceId, Granularity, Sla, self.Id, IgnoringNodes, WaveLength, LightPathId)

                elif ServiceType == "40GE":
                    self.ServiceDict[ServiceId] = self.G_40(ServiceId, Granularity, Sla, self.Id, IgnoringNodes, WaveLength, LightPathId)

                elif ServiceType == "100GE":
                    self.ServiceDict[ServiceId] = self.G_100(ServiceId, Granularity, Sla, self.Id, IgnoringNodes, WaveLength, LightPathId)



#class Lightpath(object):
    #def __init__(self, capacity, services_Id_list, Type, mandatory_nodes_Id, ):

n = Network(20)
n.PhysicalTopology.add_node((2,3))
n.PhysicalTopology.add_node((4,3))
n.PhysicalTopology.add_link(1,2,3)
print(n.PhysicalTopology.Node.ReferenceId)

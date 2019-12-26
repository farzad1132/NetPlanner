class Network:
    def __init__(self):

        self.PhysicalTopology = self.Topology()
        self.TrafficMatrix = self.Traffic()
        

    class Topology:

        def __init__(self):
            # RId
            self.NodeDict = {}
            self.LinkDict = {}
            self.ClusterDict = {}
        
        def add_node(self, Location, Type = "Not Declared"):
            Id = Network.Topology.Node.ReferenceId
            self.NodeDict[Id] = self.Node(Location, Type)
        
        def add_link(self, InNode, OutNode, NumSpan):
            self.LinkDict[(InNode , OutNode)] = self.Link(InNode,OutNode,NumSpan)

            # updating Neighbor Property in InNode and OutNode
            self.NodeDict[InNode].Neighbors.append(OutNode)
            self.NodeDict[OutNode].Neighbors.append(InNode)

        def add_cluster(self, GatewayId, SubNodesId, Color):
            Id = Network.Topology.Cluster.ReferenceId
            self.ClusterDict[Id] = self.Cluster(GatewayId, SubNodesId, Color)
        
        def del_node(self, NodeId):
            # this method deletes a Node and Corrects NodeDict , LinkDict and ClusterDict

            if not( NodeId in self.NodeDict):
                pass
                # TODO: Raise Error
            

            # deleting object from memory
            del self.NodeDict[NodeId]


            # correcting Node ReferenceId
            Network.Topology.Node.ReferenceId -= 1

            # Correcting other Nodes Id
            # finding Nodes that need Correction
            Nodes = list(self.NodeDict.items())
            UpperNodes = list(filter(lambda x : x[0] > NodeId, Nodes))
            UpperNodes = list(map(lambda x : x[0], UpperNodes))
            UpperNodes.sort()

            
            for id in UpperNodes:
                # Correcting NodeDict Ids
                self.NodeDict[id-1] = self.NodeDict.pop(id)

                # Correcting Nodes id Property
                self.NodeDict[id - 1].id = id - 1
            
            # finding links
            links = list(self.LinkDict.items())
            links = list(filter(lambda x : x[0][0] == NodeId or x[0][1] == NodeId, links))

            for link in links:
                link_tuple = link[0]

                # deleting links objects
                del self.LinkDict[link_tuple]

            
            # finding containing cluster
            clusters = list(self.ClusterDict.items())
            ContainingCluster = list(filter(lambda x :  NodeId in x[1].SubNodesId , clusters))
            print(self.ClusterDict[ContainingCluster[0][0]].SubNodesId)
            if ContainingCluster != []:

                IndexOfNode = self.ClusterDict[ContainingCluster[0][0]].SubNodesId.index(NodeId)
                
                # deleting Node Id from SubNodesId List
                self.ClusterDict[ContainingCluster[0][0]].SubNodesId.pop(IndexOfNode)
        
        def del_link(self, InNode, OutNode):

            links = list(self.LinkDict.items())
            # finding link in LinkDict
            if (InNode, OutNode) in self.LinkDict:
                link_tuple = (InNode, OutNode)
            elif (OutNode, InNode) in self.LinkDict:
                link_tuple = (OutNode, InNode)
            else:
                pass
                # TODO: Raise Error

            # deleting Link Object from memory
            del self.LinkDict[link_tuple]


            # Correcting neighbor Property in InNode and OutNode
            index = self.NodeDict[InNode].Neighbors.index(OutNode)
            self.NodeDict[InNode].Neighbors.pop(index)

            index = self.NodeDict[OutNode].Neighbors.index(InNode)
            self.NodeDict[OutNode].Neighbors.pop(index)
        
        def del_cluster(self, GatewayId):

            Clusters = list(self.ClusterDict.items())
            cluster = list(filter(lambda x : x[1].GatewayId == GatewayId, Clusters))

            id = cluster[0]

            # deleting cluster object from memory 
            del self.ClusterDict[id]

            # deleting cluster from ClusterDict 
            self.ClusterDict.pop(id)

            # correcting Cluster ReferenceId 
            Network.Topology.Cluster.ReferenceId -= 1

            UpperClusters = list(filter(lambda x : x[0] > id, Clusters))
            UpperClusters = list(map(lambda x : x[0] , UpperClusters))
            UpperClusters.sort()

            # correcting other Clusters Id
            for id in UpperClusters:
                self.ClusterDict[id - 1] = self.ClusterDict.pop(id)
            

        


        class Node:
            ReferenceId = 0
            # Id must be an int number
            # Location format must be (lat,lng) in int
            def __init__(self, Location, Type = "not declared"):
                self.Id = Network.Topology.Node.ReferenceId
                Network.Topology.Node.ReferenceId += 1
                self.Location = Location
                self.Type = Type
                self.Neighbors = []
                self.degrees = []
                self.services = []
                self.AmplifierList = []
            
            def __del__(self):
                pass
            
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

            def put_fiber_Type(self, Length, Loss, Dispersion, Beta,Gamma, PositionInLink, Snr):
                self.SpanObjList[PositionInLink].put_fiber_Type(Length, Loss, Dispersion, Beta, Gamma, PositionInLink, Snr)
            
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
            ReferenceId = 0
            def __init__(self, GatewayId, SubNodesId, Color):
                self.Id = Network.Topology.Cluster.ReferenceId
                Network.Topology.Cluster.ReferenceId += 1

                self.GatewayId = GatewayId 

                # SubNodesId is a list of Ids
                self.SubNodesId = SubNodesId
                self.Color = Color


    class Traffic:

        def __init__(self):
            self.DemandDict = {}    # in { id : DemandObj } format
        
        def add_demand(self, Id, Source, Destination, Type):
            self.DemandDict[Id] = self.Demand(Id, Source, Destination, Type)
        
        def del_demand(self, Id):
            del self.DemandDict[Id]

            self.DemandDict.pop(Id)

        class Demand:
            
            # this class is one row of Traffic Matrix
            def __init__(self, Id, Source, Destination, Type):

                self.ServiceId = 0
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
                BW = 1.244

                def __init__(self, Id, Granularity, Sla, DemandId, IgnoringNodes, WaveLength = None, LightPathId = None):
                    self.Id = Id
                    self.Granularity = Granularity
                    self.WaveLength = WaveLength
                    self.Sla = Sla
                    self.DemandId = DemandId
                    self.IgnoringNodes = IgnoringNodes
                    self.LightPathId = LightPathId

                    BW = 1.244
            
            class FE:
                BW = 0.1

                def __init__(self, Id, Granularity_vc12 ,Granularity_vc4, Sla,DemandId, IgnoringNodes, WaveLength = None, LightPathId = None):
                    self.Id = Id
                    self.Granularity_vc12 = Granularity_vc12
                    self.Granularity_vc4 = Granularity_vc4
                    self.WaveLength = WaveLength
                    self.Sla = Sla
                    self.DemandId = DemandId
                    self.IgnoringNodes = IgnoringNodes
                    self.LightPathId = LightPathId

                    BW = 0.1
                
            
            class STM_64:
                BW = 9.95

                def __init__(self, Id, Sla, DemandId, IgnoringNodes, WaveLength = None, LightPathId = None):
                    self.Id = Id
                    self.WaveLength = WaveLength
                    self.Sla = Sla
                    self.DemandId = DemandId
                    self.IgnoringNodes = IgnoringNodes
                    self.LightPathId = LightPathId

                    BW = 9.95
            
            class STM_16:
                BW = 2.49

                def __init__(self, Id, Sla, DemandId, IgnoringNodes, WaveLength = None, LightPathId = None):
                    self.Id = Id
                    self.WaveLength = WaveLength
                    self.Sla = Sla
                    self.DemandId = DemandId
                    self.IgnoringNodes = IgnoringNodes
                    self.LightPathId = LightPathId

                    


            class STM_4:
                # BW : Band WIdth
                BW = 622.08 / 1024

                def __init__(self, Id, Sla, DemandId, IgnoringNodes, WaveLength = None, LightPathId = None):
                    self.Id = Id
                    self.WaveLength = WaveLength
                    self.Sla = Sla

                    self.sDemandId = DemandId
                    self.IgnoringNodes = IgnoringNodes
                    self.LightPathId = LightPathId


            class STM_1_Optical:
                # BW : Band WIdth in Gb/s
                BW = 155.52 / 1024

                def __init__(self, Id, Sla, DemandId, IgnoringNodes, WaveLength = None, LightPathId = None):
                    self.Id = Id
                    self.WaveLength = WaveLength
                    self.Sla = Sla
                    self.DemandId = DemandId
                    self.IgnoringNodes = IgnoringNodes
                    self.LightPathId = LightPathId

                    # BW : Band WIdth in Gb/s
                    BW = 155.52 / 1024
                
            
            class STM_1_Electrical:
                # BW = Band WIdth in Gb/s
                BW = 155.52 / 1024

                def __init__(self, Id, Sla, DemandId, IgnoringNodes, LightPathId = None):
                    self.Id = Id
                    self.Sla = Sla
                    self.DemandId =DemandId
                    self.IgnoringNodes = IgnoringNodes
                    self.LightPathId = LightPathId

                    
                
            
            class E1:
                # BW : Band WIdth in Gb/s
                BW = 58.84 / 1024

                def __init__(self, Id, Sla,DemandId, IgnoringNodes, LightPathId = None):
                    self.Id = Id
                    self.Sla = Sla
                    self.DemandId =DemandId
                    self.IgnoringNodes = IgnoringNodes
                    self.LightPathId = LightPathId

                    
            
            def GenerateId(self):
                self.ServiceId += 1
                return ( self.ServiceId - 1 )
            
            def add_service(self, ServiceType, Sla, IgnoringNodes = None, WaveLength = None, Granularity = None, Granularity_vc12 = None,
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
        
    class Lightpath:
                ReferenceId = 0

                def __init__(self, Capacity, ServiceIdList, Type, MandatoryNodesIdList, DemandId):
                    self.id = Network.Lightpath.ReferenceId
                    Network.Lightpath.ReferenceId += 1
                    self.DemandId = DemandId
                    self.Capacity = Capacity
                    self.ServiceIdList = ServiceIdList
                    self.Type = Type
                    self.MandatoryNodesIdList = MandatoryNodesIdList

if __name__ == "__main__":

    n = Network()
    n.PhysicalTopology.add_node((2,3))
    n.PhysicalTopology.add_node((6,7))
    n.PhysicalTopology.add_node((17,-3))
    n.PhysicalTopology.add_link(0,1,4)
    n.PhysicalTopology.add_link(1,2,1)
    n.PhysicalTopology.add_cluster(1,[2,0],"blue")
    print(n.PhysicalTopology.NodeDict[1].Neighbors)
    print("LinkDict: ",n.PhysicalTopology.LinkDict)
    print("NodeDict: ",n.PhysicalTopology.NodeDict)
    print("ClusterDict: ",n.PhysicalTopology.ClusterDict)
    n.PhysicalTopology.del_node(2)
    print("NodeDict after deleting a Node: ",n.PhysicalTopology.NodeDict)

    n.TrafficMatrix.add_demand(1,"Tehran","Mashhad","X")
    n.TrafficMatrix.DemandDict[1].add_service("100GE",2)

    n.TrafficMatrix.add_demand(2,"Tehran", "Shiraz", "")
    n.TrafficMatrix.DemandDict[2].add_service("100GE",2)
    n.TrafficMatrix.DemandDict[2].add_service("10GE",2)
    n.TrafficMatrix.DemandDict[2].add_service("STM_64",2)

    n.TrafficMatrix.add_demand(3, "Tabriz", "Karaj", "")
    n.TrafficMatrix.DemandDict[3].add_service("FE",2)
    n.TrafficMatrix.DemandDict[3].add_service("1GE",2)
    
    print("DemandDict: ",n.TrafficMatrix.DemandDict)
    print("Demand 1: ",n.TrafficMatrix.DemandDict[1].ServiceDict)
    print("Demand 2: ",n.TrafficMatrix.DemandDict[2].ServiceDict)
    print("Demand 3: ",n.TrafficMatrix.DemandDict[3].ServiceDict)
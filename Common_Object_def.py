class Network:

    @classmethod
    def from_json(cls, data):
        instance = cls()
        LightPathDict = dict(zip(data['LightPathDict'].keys(), list(map(Network.Lightpath.from_json, data['LightPathDict'].values()))))
        instance.__dict__['PhysicalTopology'] = Network.Topology.from_json(data['PhysicalTopology'])
        instance.__dict__['LightPathDict'] = LightPathDict
        instance.__dict__['ParamsObj'] = Network.Params.from_json(data['ParamsObj'])
        return instance

    def __init__(self):

        self.PhysicalTopology = self.Topology()
        self.TrafficMatrix = self.Traffic()
        self.ParamsObj = self.Params()
        
        self.LightPathDict = {}

    def put_params(self, merge, alpha, iterations, margin, processors, k, maxNW = None):
        self.ParamsObj.set_results(merge, alpha, iterations, margin, processors, k , maxNW)

    def add_lightpath(self, Source, Destination, Capacity, ServiceIdList, Type, DemandId,
     MandatoryNodesIdList = None, IgnoringNodesIdList = None):

        self.LightPathDict[Network.Lightpath.get_id()] = self.Lightpath(Source, Destination, Capacity, ServiceIdList, Type, DemandId, 
        MandatoryNodesIdList= MandatoryNodesIdList, IgnoringNodesIdList= IgnoringNodesIdList)
    
    def del_lightpath(self, ServiceIdList):
        
        # this function corrects lightpaths id that their id is bigger than deleted lightpath id
        def correct_UpperIds(id):
            for UpperId in list(self.LightPathDict.keys()).sort():
                if UpperId > id:
                    self.LightPathDict[UpperId - 1] = self.LightPathDict.pop(UpperId)

        # finding object that we want to delete
        for id, lightpath in self.LightPathDict.items():
            if lightpath.ServiceIdList == ServiceIdList:
                del lightpath
                if id in self.LightPathDict:
                    self.LightPathDict.pop(id)
                    correct_UpperIds(id)


        # correcting ReferenceId
        Network.Lightpath.update_id(-1)
        
    
    def put_results(self, id, WorkingPath, ProtectionPath, WaveLength, RegeneratorNode_w, RegeneratorNode_p,
                    SNR_th, LaunchPower, ModulationType, SNR_w, SNR_p):
        
        self.LightPathDict[id].set_results(WorkingPath, ProtectionPath, WaveLength, RegeneratorNode_w, RegeneratorNode_p, SNR_th, LaunchPower, ModulationType, SNR_w, SNR_p)


    class Topology:

        @classmethod
        def from_json(cls, data):
            instance = cls()
            NodeDict = dict(zip(data['NodeDict'].keys(), list(map(Network.Topology.Node.from_json, data['NodeDict'].values()))))
            LinkDict = dict(zip(data['LinkDict'].keys(), list(map(Network.Topology.Link.from_json, data['LinkDict'].values()))))
            ClusterDict = dict(zip(data['ClusterDict'].keys(), list(map(Network.Topology.Cluster.from_json, data['ClusterDict'].values()))))
            instance.__dict__['NodeDict'] = NodeDict
            instance.__dict__['LinkDict'] = LinkDict
            instance.__dict__['ClusterDict'] = ClusterDict
            return instance

        def __init__(self):
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
            else: 
                link_tuple = (OutNode, InNode)

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

            @classmethod
            def from_json(cls, data):
                AmplifierList = list(map(Network.Topology.Node.Amplifier.from_json, data["AmplifierList"]))
                instance = cls(Location = data['Location'], Type = data['Type'])
                instance.__dict__['AmplifierList'] = AmplifierList
                instance.__dict__['Neighbors'] = data['Neighbors']
                instance.__dict__['Id'] = data['Id']
                return instance

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
            
            
            def add_amplifier(self, nf):
                self.AmplifierList.append(self.Amplifier(nf))


            class Amplifier:
                @classmethod
                def from_json(cls, data):
                    instance = cls(data['nf'])
                    instance.__dict__['Id'] = data['Id']
                    return instance

                def __init__(self, nf):
                    self.Id = Id
                    
                    self.nf = nf        # nf : noise figure
            
        class Link:

            @classmethod
            def from_json(cls, data):
                SpanObjList = list(map(Network.Topology.Link.Span.from_json, data["SpanObjList"]))
                instance = cls(InNode = data['InNode'], OutNode = data['OutNode'], NumSpan = data['NumSpan'])
                instance.__dict__['SpanObjList'] = SpanObjList
                instance.__dict__['WaveLengthList'] = data['WaveLengthList']
                return instance

            def __init__(self, InNode, OutNode, NumSpan):

                self.InNode = InNode
                self.OutNode = OutNode
                self.NumSpan = NumSpan
                self.SpanObjList = [self.Span(self.InNode,self.OutNode) for i in range(NumSpan)]

                self.WaveLengthList = []
                self.LightPathDict = {}    # in  { id : LightPath Object } format

            def put_fiber_Type(self, Length, Loss, Dispersion, Beta, Gamma, PositionInLink, Snr = None):
                self.SpanObjList[PositionInLink].put_fiber_Type(Length, Loss, Dispersion, Beta, Gamma, PositionInLink, Snr)
                # self.SpanObjList[PositionInLink].Length = 
            
            class Span:

                @classmethod
                def from_json(cls, data):
                    instance = cls(data['InNode'], data['OutNode'], data['Length'],data['Loss'] ,data['Dispersion'], data['Beta'],
                                   data['Gamma'], data['PositionInLink'], data['Snr'])
                    return instance

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

                    # 0 for this variable means first span in link and so on ...
                    self.PositionInLink = PositionInLink

                def put_fiber_Type(self, Length, Loss, Dispersion, Beta, Gamma, PositionInLink, Snr = None):

                    self.Length = Length
                    self.Loss = Loss
                    self.Dispersion = Dispersion
                    self.Beta = Beta
                    self.Gamma = Gamma
                    self.PositionInLink = PositionInLink
                    self.Snr = Snr
            
        class Cluster:

            @classmethod
            def from_json(cls, data):
                instance = cls(GatewayId = data['GatewayId'], SubNodesId = data['SubNodesId'], Color = data['Color'])
                instance.__dict__['Id'] = data['Id']
                return cls

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
        
        def add_demand(self, Source, Destination, Type):
            Id = self.GenerateDemandId()
            self.DemandDict[Id] = self.Demand(Id, Source, Destination, Type)
        
        def del_demand(self, Id):
            del self.DemandDict[Id]

            self.DemandDict.pop(Id)
        
        def GenerateDemandId(self):
                Network.Traffic.Demand.DemandReferenceId += 1
                return ( Network.Traffic.Demand.DemandReferenceId - 1 )

        class Demand:
            ServiceReferencedId = 0
            DemandReferenceId = 0
            # this class is one row of Traffic Matrix
            def __init__(self, Id, Source, Destination, Type):

                self.ServiceId = 0
                self.Id = Id
                self.Source = Source
                self.Destination = Destination
                self.Type = Type            # Type must be a string
                self.ServiceDict = {}
            
            
            
            class G_100:
                BW = 100
                def __init__(self, Id, Granularity, Sla, DemandId, IgnoringNodes, WaveLength = None, LightPathId = None):
                    self.Id = Id
                    self.Granularity = Granularity
                    self.WaveLength = WaveLength
                    self.Sla = Sla
                    self.Type = "G_100"
                    self.DemandId = DemandId
                    self.IgnoringNodes = IgnoringNodes
                    self.LightPathId = LightPathId
            
            class G_40:
                BW = 40
                def __init__(self, Id, Granularity, Sla, DemandId, IgnoringNodes, WaveLength = None, LightPathId = None):
                    self.Id = Id
                    self.Granularity = Granularity
                    self.WaveLength = WaveLength
                    self.Sla = Sla
                    self.Type = "G_40"
                    self.DemandId = DemandId
                    self.IgnoringNodes = IgnoringNodes
                    self.LightPathId = LightPathId

            
            class G_10:
                BW = 10
                def __init__(self, Id, Granularity, Sla, DemandId, IgnoringNodes, WaveLength = None, LightPathId = None):
                    self.Id = Id
                    self.Granularity = Granularity
                    self.WaveLength = WaveLength
                    self.Sla = Sla
                    self.Type = "G_10"
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
                    self.Type = "G_1"
                    self.DemandId = DemandId
                    self.IgnoringNodes = IgnoringNodes
                    self.LightPathId = LightPathId

            
            class FE:
                BW = 0.1

                def __init__(self, Id, Granularity_vc12 ,Granularity_vc4, Sla,DemandId, IgnoringNodes, WaveLength = None, LightPathId = None):
                    self.Id = Id
                    self.Granularity_vc12 = Granularity_vc12
                    self.Granularity_vc4 = Granularity_vc4
                    self.WaveLength = WaveLength
                    self.Sla = Sla
                    self.Type = "FE"
                    self.DemandId = DemandId
                    self.IgnoringNodes = IgnoringNodes
                    self.LightPathId = LightPathId

                
            
            class STM_64:
                BW = 10

                def __init__(self, Id, Sla, DemandId, IgnoringNodes, WaveLength = None, LightPathId = None):
                    self.Id = Id
                    self.WaveLength = WaveLength
                    self.Sla = Sla
                    self.Type = "STM_64"
                    self.DemandId = DemandId
                    self.IgnoringNodes = IgnoringNodes
                    self.LightPathId = LightPathId

            
            class STM_16:
                BW = 2.49

                def __init__(self, Id, Sla, DemandId, IgnoringNodes, WaveLength = None, LightPathId = None):
                    self.Id = Id
                    self.WaveLength = WaveLength
                    self.Sla = Sla
                    self.Type = "STM_16"
                    self.DemandId = DemandId
                    self.IgnoringNodes = IgnoringNodes
                    self.LightPathId = LightPathId

                    


            class STM_4:
                # BW : Band Width
                BW = 622.08 / 1024

                def __init__(self, Id, Sla, DemandId, IgnoringNodes, WaveLength = None, LightPathId = None):
                    self.Id = Id
                    self.WaveLength = WaveLength
                    self.Sla = Sla
                    self.Type = "SYM_4"
                    self.sDemandId = DemandId
                    self.IgnoringNodes = IgnoringNodes
                    self.LightPathId = LightPathId


            class STM_1_Optical:
                # BW : Band Width in Gb/s
                BW = 155.52 / 1024

                def __init__(self, Id, Sla, DemandId, IgnoringNodes, WaveLength = None, LightPathId = None):
                    self.Id = Id
                    self.WaveLength = WaveLength
                    self.Sla = Sla
                    self.Type = "STM_1_Optical"
                    self.DemandId = DemandId
                    self.IgnoringNodes = IgnoringNodes
                    self.LightPathId = LightPathId

                
            
            class STM_1_Electrical:
                # BW = Band Width in Gb/s
                BW = 155.52 / 1024

                def __init__(self, Id, Sla, DemandId, IgnoringNodes, LightPathId = None):
                    self.Id = Id
                    self.Sla = Sla
                    self.Type = "STM_1_Electrical"
                    self.DemandId =DemandId
                    self.IgnoringNodes = IgnoringNodes
                    self.LightPathId = LightPathId

                    
                
            
            class E1:
                # BW : Band Width in Gb/s
                BW = 58.84 / 1024

                def __init__(self, Id, Sla,DemandId, IgnoringNodes, LightPathId = None):
                    self.Id = Id
                    self.Sla = Sla
                    self.Type = "E1"
                    self.DemandId =DemandId
                    self.IgnoringNodes = IgnoringNodes
                    self.LightPathId = LightPathId

            class Groom_out10:
                BW=10

                def __init__(self, Id, Sla, Source, Destination, Capacity, ServiceIdList,  DemandId,
                        IgnoringNodesIdList = None, MandatoryNodesIdList = None, LightPathId = None):

                    self.Id = Id
            
                    self.Source = Source
                    self.Sla = Sla
                    self.Destination = Destination
                    self.DemandId = DemandId
                    self.Capacity = Capacity
                    self.ServiceIdList = ServiceIdList
                    self.Type = "Groom_out10"
                    self.MandatoryNodesIdList = MandatoryNodesIdList
                    self.IgnoringNodesIdList = IgnoringNodesIdList
                    self.LightPathId = LightPathId

                    
            
            def GenerateId(self):
                Network.Traffic.Demand.ServiceReferencedId += 1
                return ( Network.Traffic.Demand.ServiceReferencedId - 1 )
            
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
        
        @classmethod
        def from_json(cls, data):
            instance = cls(Source = data['Source'], Destination = data['Destination'], Capacity = data['Capacity'],
                           ServiceIdList = data['ServiceIdList'], Type = data['Type'], DemandId = data['DemandId'],
                           WorkingPath = data['WorkingPath'], ProtectionPath = data['ProtectionPath'],
                           WaveLength = data['WaveLength'], RegeneratorNode_w = data['RegeneratorNode_w'],
                           RegeneratorNode_p = data['RegeneratorNode_p'], SNR_th = data['SNR_th'], 
                           LaunchPower = data['LaunchPower'], ModulationType = data['ModulationType'], SNR_w = data['SNR_w'], SNR_p = data['SNR_p'])
            instance.__dict__['id'] = data['id']
            return instance

        ReferenceId = 0

        
        @classmethod
        def get_id(cls):
            cls.ReferenceId += 1
            return ( cls.ReferenceId - 1 )
        

        @classmethod
        def update_id(cls, Num):
            # this method usage is when a bunch of instances from this class has been imported and we want to update
            # our ReferencedId ( class variable )
            cls.ReferenceId += Num


        def __init__(self, Source, Destination, Capacity, ServiceIdList, Type,  DemandId, WorkingPath = None, ProtectionPath = None,
                        WaveLength = None, RegeneratorNode_w = None, RegeneratorNode_p = None, IgnoringNodesIdList = None,
                        SNR_th = None, LaunchPower = None, ModulationType = None, SNR_w = None, SNR_p = None, MandatoryNodesIdList = None):

            self.id = Network.Lightpath.ReferenceId
            
            self.Source = Source
            self.Destination = Destination
            self.WorkingPath = WorkingPath
            self.ProtectionPath = ProtectionPath
            self.RegeneratorNode_w = RegeneratorNode_w
            self.RegeneratorNode_p = RegeneratorNode_p
            self.SNR_th = SNR_th
            self.WaveLength = WaveLength
            self.DemandId = DemandId
            self.Capacity = Capacity
            self.LaunchPower = LaunchPower
            self.ServiceIdList = ServiceIdList
            self.ModulationType = ModulationType
            self.Type = Type
            self.SNR_w = SNR_w
            self.SNR_p = SNR_p
            self.MandatoryNodesIdList = MandatoryNodesIdList
            self.IgnoringNodesIdList = IgnoringNodesIdList
        
        def set_results(self, WorkingPath, ProtectionPath, WaveLength, RegeneratorNode_w, RegeneratorNode_p,
         SNR_th, LaunchPower, ModulationType, SNR_w, SNR_p):

            self.WorkingPath = WorkingPath
            self.ProtectionPath = ProtectionPath
            self.WaveLength = WaveLength
            self.RegeneratorNode_p = RegeneratorNode_p
            self.RegeneratorNode_w = RegeneratorNode_w
            self.SNR_th = SNR_th
            self.LaunchPower = LaunchPower
            self.ModulationType = ModulationType
            self.SNR_w = SNR_w
            self.SNR_p = SNR_p
    
    class Params:
        @classmethod
        def from_json(cls, data):
            instance = cls(merge = data['merge'], alpha = data['alpha'], iterations = data['iterations'],
                           margin = data['margin'], processors = data['processors'], k = data['k'],
                           maxNW = data['maxNW'])
            return instance

        def __init__(self, merge = None, alpha = None, iterations = None, margin = None, processors = None, k = None, maxNW = None):

            self.merge = merge                  
            self.alpha = alpha                  
            self.iterations = iterations        
            self.margin = margin                
            self.processors = processors       
            self.k = k                          
            self.maxNW = maxNW                  


        def set_results(self, merge, alpha, iterations, margin, processors, k, maxNW = None):

            self.merge = merge
            self.alpha = alpha
            self.iterations = iterations
            self.margin = margin
            self.processors = processors
            self.k = k
            self.maxNW = maxNW




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

    n.TrafficMatrix.add_demand("Tehran","Mashhad","X")
    LastId = n.TrafficMatrix.Demand.DemandReferenceId - 1
    n.TrafficMatrix.DemandDict[LastId].add_service("100GE",2)

    n.TrafficMatrix.add_demand("Tehran", "Shiraz", "")
    LastId = n.TrafficMatrix.Demand.DemandReferenceId - 1
    n.TrafficMatrix.DemandDict[LastId].add_service("100GE",2)
    n.TrafficMatrix.DemandDict[LastId].add_service("10GE",2)
    n.TrafficMatrix.DemandDict[LastId].add_service("STM_64",2)

    n.TrafficMatrix.add_demand("Tabriz", "Karaj", "")
    LastId = n.TrafficMatrix.Demand.DemandReferenceId - 1
    n.TrafficMatrix.DemandDict[LastId].add_service("FE",2)
    n.TrafficMatrix.DemandDict[LastId].add_service("1GE",2)
    
    print("DemandDict: ",n.TrafficMatrix.DemandDict)
    print("Demand 1: ",n.TrafficMatrix.DemandDict[1].ServiceDict)
    print("Demand 2: ",n.TrafficMatrix.DemandDict[2].ServiceDict)
    print("Demand 0: ",n.TrafficMatrix.DemandDict[0].ServiceDict)

    n.add_lightpath("Tehran", "Mashhad", "20GE", [1 ,2], "100GE", 2)
    n.put_results(0, [1 , 3 , 7], [1 ,4 ,7], 27, [5], [9], 25, 14, "111", 14, 31)

    print("LightpathDict: ", n.LightPathDict)

    n.put_params(merge= "Yes",
                 alpha= 0.2,
                 iterations= 2,
                 margin= 4,
                 processors= 4,
                 k= 1,
                 maxNW= 50)

    print(f"Params result: {n.ParamsObj.__dict__}")

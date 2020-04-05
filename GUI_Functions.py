from Common_Object_def import Network
from math import ceil
import pickle


def LightPath_Calculation(DemandObj):

    ServiceList =list(DemandObj.ServiceDict.items())

    # Extracting Data from Object

    STM_1_BW = Network.Traffic.Demand.STM_1_Optical.BW
    STM_4_BW = Network.Traffic.Demand.STM_4.BW
    STM_16_BW = Network.Traffic.Demand.STM_16.BW
    FE_BW = Network.Traffic.Demand.FE.BW
    GE_BW = Network.Traffic.Demand.G_1.BW
    STM_64_BW = Network.Traffic.Demand.STM_64

    STM_1_List = list(filter(lambda x : isinstance( x[1] , Network.Traffic.Demand.STM_1_Optical ) , ServiceList))
    STM_1_List = list(map(lambda x : x[0] , STM_1_List ))
    NumSTM_1 = len(STM_1_List)

    STM_4_List = list(filter(lambda x : isinstance( x[1] , Network.Traffic.Demand.STM_4 ) , ServiceList))
    STM_4_List = list(map(lambda x : x[0] , STM_4_List ))
    NumSTM_4 = len(STM_4_List)

    STM_16_List = list(filter(lambda x : isinstance( x[1] , Network.Traffic.Demand.STM_16 ) , ServiceList))
    STM_16_List = list(map(lambda x : x[0] , STM_16_List ))
    NumSTM_16 = len(STM_16_List)

    FE_List = list(filter(lambda x : isinstance( x[1] , Network.Traffic.Demand.FE ) , ServiceList))
    FE_List = list(map(lambda x : x[0] , FE_List ))
    NumFE = len(FE_List)

    GE_List = list(filter(lambda x : isinstance( x[1] , Network.Traffic.Demand.G_1 ) , ServiceList))
    GE_List = list(map(lambda x : x[0] , GE_List ))
    NumGE = len(GE_List)

    STM_64_List = list(filter(lambda x : isinstance( x[1] , Network.Traffic.Demand.STM_64 ) , ServiceList))
    STM_64_List = list(map(lambda x : x[0] , STM_64_List ))
    NumSTM_64 = len(STM_64_List)

    G10_List = list(filter(lambda x : isinstance( x[1] , Network.Traffic.Demand.G_10 ) , ServiceList))
    G10_List = list(map(lambda x : x[0] , G10_List ))
    NumG10 = len(G10_List)

    G100_List = list(filter(lambda x : isinstance( x[1] , Network.Traffic.Demand.G_100 ) , ServiceList))
    G100_List = list(map(lambda x : x[0] , G100_List ))
    NumG100 = len(G100_List)



    #  Number of MP2X Calculation

    TotalRate = (NumSTM_1 * STM_1_BW) + (NumSTM_4 * STM_4_BW) + (NumSTM_16 * STM_16_BW)
    TotalClient = NumSTM_1 + NumSTM_4 + NumSTM_16

    NumLine_Rate = ceil(TotalRate / 10)
    NumLine_Client = ceil(TotalClient / 8)
    NumLinePort = max(NumLine_Client , NumLine_Rate)

    NumMP2X = ceil(NumLinePort / 2)

    # Number of PS6X Calculation

    TotalRate = (NumFE * FE_BW) + (NumGE * GE_BW)
    TotalClient = NumFE + NumGE

    LinePort_Rate = ceil(TotalRate / 10)
    LinePort_Client = ceil(TotalClient / 10)

    NumLinePort = max(LinePort_Client , LinePort_Rate)

    NumPS6X = ceil(NumLinePort / 2)

    # Number Of MP1H Calculation

    NumClientPorts = NumSTM_64 + NumG10

    NumMP1H = ceil(NumClientPorts / 10)

    # Number Of TP1H Calculation

    NumTP1H = NumG100

    








# Test Codes
# making an Object from Network class
n = Network()

# adding a demand to Traffic Matrix
d1 = n.TrafficMatrix.add_demand(1, 'tehran', 'karaj', 'working')

# adding service to demand object
for i in range(9):
    n.TrafficMatrix.DemandDict[1].add_service('STM_1_Optical','x')
for i in range(11):
    n.TrafficMatrix.DemandDict[1].add_service('STM_4','x')
for i in range(7):
    n.TrafficMatrix.DemandDict[1].add_service('STM_16','x')


# calling function for calculating the number of lightpaths and panels
LightPath_Calculation(n.TrafficMatrix.DemandDict[1])

# testing pickle Library for Demand Object 
with open('pickletest.obj' ,'wb') as handle:
    x = pickle.dump(n.TrafficMatrix.DemandDict[1], handle, protocol=pickle.HIGHEST_PROTOCOL)
    handle.close()

with open('pickletest.obj' ,'rb') as handle:
    print(handle)
    x = pickle.load(handle)
    handle.close()

# results after unpickling data
print(type(x))
print(x.ServiceDict.keys())


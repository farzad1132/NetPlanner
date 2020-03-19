from Common_Object_def import Network
import pickle
import copy
from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpStatus

import networkx as nx

import math


def MP2X(Services_lower10):
    prob = LpProblem("grooming", LpMinimize )
    B=10                    #u
    max_port=16
    y=[]
    
    min_number_of_service=3
        
        
        #Services_lower10=[0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 2.5, 2.5, 0.62, 0.62, 0.62, 0.62, 0.62]
        #Services_lower10=[2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5,0.62]

    NO_service_lower10 = len(Services_lower10)
    #print(sum([pair[1] for pair in Services_lower10]))
    #print(math.ceil(sum([pair[1] for pair in Services_lower10])/20))
    NO_Lineport_MP2x=max(math.ceil(NO_service_lower10/8),math.ceil(sum([pair[1] for pair in Services_lower10])/10))    #number of line ports
    max_number_device=math.ceil(NO_Lineport_MP2x/2)
    max_number_device=max_number_device*2
    max_number_device=NO_Lineport_MP2x
        
    for i in range(1,max_number_device+1):
        #y[i]=LpVariable(name='y[i]', cat='Binary')
        y.append(LpVariable(name='y%s'%i, cat='Binary'))
    
    x = {}
    for j in range(1,max_number_device+1):
        for i in range(1,NO_service_lower10+1):
           #x ={ (i, j): LpVariable("x",  cat='Binary')}
           x[(i,j)] = LpVariable("x%s_%s"%(i,j),  cat='Binary')
    
    
    
#    prob += lpSum([x[(i,j)] for j in range(1,NO_service_lower10+1) for i in range(1,max_number_device+1)])
    prob += lpSum([y[i-1] for i in range(1,max_number_device+1)]) 

    for i in range(1,NO_service_lower10+1):
        prob +=lpSum(x[(i,j)] for j in range(1,max_number_device+1) ) ==1,""
    
    
    for j in range(1,max_number_device+1):
        prob +=lpSum(Services_lower10[i-1][1]*x[(i,j)] for i in range(1,NO_service_lower10+1)) <= B*y[j-1],""
        
    
    for j in range(1,max_number_device+1):
        for  i in range(1,NO_service_lower10+1):
            prob +=lpSum(x[(i,j)]) <= y[j-1],""
            
    for j in range(1,max_number_device+1):
        prob +=lpSum(x[(i,j)] for i in range(1,NO_service_lower10+1) ) <=max_port,""
    
            
    
     
    prob.writeLP("grooming.lp")
    prob.solve()
    
    #print("Status:", LpStatus[prob.status])
    
    #for j in range(1,max_number_device+1):
        
    '''for v in prob.variables():
        print (v.name, "=", v.varValue)'''
    '''for j in range(1,max_number_device+1):
        print("******   ",y[j-1],"=",y[j-1].value(),"     *********    ")
        for i in range(1,NO_service_lower10+1):
            print(x[(i,j)],"=",x.get(i,j))'''
    ans = prob.variables()
    Result = {}
    for j in range(max_number_device):
        Result[ans[-1 - j].name] = {}
    #    yy={}
    for i in range( len(ans) - max_number_device ):
        itemName = ans[i].name
        itemValue = ans[i].varValue
        if len(itemName) == 5:
            PanelNum = itemName[4]
            ServiceNum = itemName[1:-2]
        else:
            PanelNum = itemName[3]
            ServiceNum = itemName[1:-2]
    
        key_panel = 'y' + PanelNum
        Result[key_panel][itemName] = (itemValue * Services_lower10[int(ServiceNum) - 1][0],itemValue * Services_lower10[int(ServiceNum) - 1][1])
    #print(Result)
    
    #for j in range(1,max_number_device+1):
    #    if y[j-1].value()==1:
    #        h=0
    #        for i in range(1,NO_service_lower10+1):
    ##            print('**',x[(i,j)].value())
    #            if x[(i,j)].value()==1:
    #                h=h+1
    ##                print('h=',h)
    #        if h>= min_number_of_service:
    #            print(j,y[j-1])                        #????
        
    Output=[]
    
    for key, value in Result.items():
        y=[]
        for inner_key,inner_value in value.items():
            if inner_value[1] != 0:
                y.append((int (inner_value[0]),inner_value[1]))
        Output.append(y)
#    dele=[]    
#    for i in range(0, len(Output)):
#        if (len(Output[i])==0):
#            dele.append(i)
#            
#    print('dsdsss')
#    print(Output)
#    print('dsdsss')
    return Output




def grooming_fun( n, MP1H_Threshold, MP2X_Threshold=None):

        service_lower10_SDH=[]
        service_lower10_E=[]
        service_lower100=[]
        remaining_service_lower10=[]
        MP2x_list=[]                                      #(DemandId,Service)
        output_100=[]
        groom_out10_list=[]
        remain_lower100=[]
        for i in n.TrafficMatrix.DemandDict:
            y=[]
            z=[]
            x=[]
            output_10=[] 
            for j in n.TrafficMatrix.DemandDict[i].ServiceDict:
                if ((n.TrafficMatrix.DemandDict[i].ServiceDict[j].Type == "STM_1_Optical") or (n.TrafficMatrix.DemandDict[i].ServiceDict[j].Type == "STM_4") or (n.TrafficMatrix.DemandDict[i].ServiceDict[j].Type == "STM_16")):
                    y.append((n.TrafficMatrix.DemandDict[i].ServiceDict[j].Id,n.TrafficMatrix.DemandDict[i].ServiceDict[j].BW))
                elif ((n.TrafficMatrix.DemandDict[i].ServiceDict[j].Type == "FE") or (n.TrafficMatrix.DemandDict[i].ServiceDict[j].Type == "1GE")):
                    x.append((n.TrafficMatrix.DemandDict[i].ServiceDict[j].Id,n.TrafficMatrix.DemandDict[i].ServiceDict[j].BW))
                elif (n.TrafficMatrix.DemandDict[i].ServiceDict[j].BW == 10):
                    z.append((n.TrafficMatrix.DemandDict[i].ServiceDict[j].Id,n.TrafficMatrix.DemandDict[i].ServiceDict[j].BW))
                else:
                    n.add_lightpath(n.TrafficMatrix.DemandDict[i].Source, n.TrafficMatrix.DemandDict[i].Destination, 100, [n.TrafficMatrix.DemandDict[i].ServiceDict[j].Id], 100, i)
            if y:
                service_lower10_SDH.append((i,y))
                output_10.append((i,MP2X(y)))
                listofs=[]
                cap=0
                hhhh=[]
                for num in range(0,len(output_10[0][1])):
                    listofs=[]
                    cap=0
                    for nu in range(0,len(output_10[0][1][num])):
                        listofs.append(output_10[0][1][num][nu][0])
                        cap = cap + output_10[0][1][num][nu][1]
                    n.TrafficMatrix.DemandDict[i].add_service(ServiceType= "Groom_out10" ,Sla= 2, Capacity=cap, ServiceIdList=listofs)    
                    LastId = n.TrafficMatrix.Demand.ServiceReferencedId - 1
                    ffff=[(LastId,10)]
                    hhhh.append((LastId,cap,len(listofs)))
                    service_lower100.append((i,ffff))
                groom_out10_list.append((i,hhhh))
#                print(groom_out10_list)
            if x:
                service_lower10_E.append((i,x))
            
            if z:
                service_lower100.append((i,z))
         
 
        
        for i in range(0,len(groom_out10_list)):
            nooo=[]
            for j in range(0,len(groom_out10_list[i][1])):
                for k in range(0,len(groom_out10_list[i][1])):
                    if ((k not in nooo) and (j not in nooo) and (j!=k) and (groom_out10_list[i][1][j][2] + groom_out10_list[i][1][k][2]) <=16):
                        MP2x_list.append((groom_out10_list[i][0],(groom_out10_list[i][1][j][0],groom_out10_list[i][1][k][0])))
                        nooo.append(j)
                        nooo.append(k)
            for m in range(0,len(groom_out10_list[i][1])):
                if m not in nooo:
                    remaining_service_lower10.append((groom_out10_list[i][0],groom_out10_list[i][1][m][0]))  
                    
                    
        for i in range(0,len(service_lower100)):
            NO_LP= math.ceil(len(service_lower100[i][1])/10)
            for j in range(0,NO_LP):
                list_of_service=[]
                cap=0
                for k in range(j*10,(j+1)*10):
                    if (k < len(service_lower100[i][1])):
                        list_of_service.append(service_lower100[i][1][k][0])
                        cap=cap+service_lower100[i][1][k][1]

                if cap ==10:
                    typee="10GE"
                else:
                    typee="100GE"
                if cap < MP1H_Threshold:
                    remain_lower100.append((i,list_of_service))
                else:
                    n.add_lightpath(n.TrafficMatrix.DemandDict[service_lower100[i][0]].Source, n.TrafficMatrix.DemandDict[service_lower100[i][0]].Destination, cap, list_of_service, typee, service_lower100[i][0])    
     
        return remain_lower100,MP2x_list,remaining_service_lower10
        #  remain_lower100            (the services which are not assigned tolightpath)  (DemandId,[ServiceId])
        #  MP2x_list                  (MP2X with 2 output)                               (DemandId,[ServiceId(groomout10),ServiceId(groomout10)])
        #  remaining_service_lower10  (MP2X with 1 output)                               (DemandId,ServiceId(groomout10))
    
    
    
    
    











if __name__ == "__main__":


    """ LastId = 0
    n.TrafficMatrix.DemandDict[LastId].add_service("1GE",2)
    n.TrafficMatrix.DemandDict[LastId].add_service("STM_16",2)
    n.TrafficMatrix.DemandDict[LastId].add_service("STM_16",2)
    n.TrafficMatrix.DemandDict[LastId].add_service("STM_16",2)
    n.TrafficMatrix.DemandDict[LastId].add_service("STM_16",2)
    n.TrafficMatrix.DemandDict[LastId].add_service("STM_16",2)
    n.TrafficMatrix.DemandDict[LastId].add_service("STM_16",2)
    n.TrafficMatrix.DemandDict[LastId].add_service("STM_16",2)
    n.TrafficMatrix.DemandDict[LastId].add_service("STM_4",2)
    n.TrafficMatrix.DemandDict[LastId].add_service("STM_4",2)
    n.TrafficMatrix.DemandDict[LastId].add_service("STM_4",2)
    n.TrafficMatrix.DemandDict[LastId].add_service("STM_4",2)
    n.TrafficMatrix.DemandDict[LastId].add_service("STM_4",2)
    n.TrafficMatrix.DemandDict[LastId].add_service("STM_4",2)

    n.TrafficMatrix.DemandDict[1].add_service("STM_16",2)
    n.TrafficMatrix.DemandDict[1].add_service("STM_16",2)
    n.TrafficMatrix.DemandDict[1].add_service("STM_16",2)
    n.TrafficMatrix.DemandDict[1].add_service("STM_16",2)
    n.TrafficMatrix.DemandDict[1].add_service("STM_16",2)
    n.TrafficMatrix.DemandDict[1].add_service("STM_16",2)
    n.TrafficMatrix.DemandDict[1].add_service("STM_16",2)
    n.TrafficMatrix.DemandDict[1].add_service("STM_16",2)
    n.TrafficMatrix.DemandDict[1].add_service("STM_4",2)
    n.TrafficMatrix.DemandDict[1].add_service("STM_4",2)
    ans = grooming_fun(n,70) """
    pass
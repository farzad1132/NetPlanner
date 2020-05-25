
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
#    max_number_device=NO_Lineport_MP2x
#    if NO_service_lower10 ==81:
#        print("max=",max_number_device)
#        print("**",max_number_device)
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
#    prob += lpSum([y[i-1] for i in range(1,max_number_device+1)])
#     for j in range(1,max_number_device+1):
#        prob +=lpSum(Services_lower10[i-1][1]*x[(i,j)] for i in range(1,NO_service_lower10+1))
    
    
    for i in range(1,NO_service_lower10+1):
        prob +=lpSum(x[(i,j)] for j in range(1,max_number_device+1) ) ==1,""
    
    
    for j in range(1,max_number_device+1):
        prob +=lpSum(Services_lower10[i-1][1]*x[(i,j)] for i in range(1,NO_service_lower10+1)) <= B*y[j-1],""
        
    
    for j in range(1,max_number_device+1):
        for  i in range(1,NO_service_lower10+1):
            prob +=lpSum(x[(i,j)]) <= y[j-1],""
            
    for j in range(1,max_number_device+1):
        prob +=lpSum(x[(i,j)] for i in range(1,NO_service_lower10+1) ) <=max_port,""
    
            
    
     
    #prob.writeLP("grooming.lp")
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
        
        find_underscore = itemName.index("_")
        ServiceNum = itemName[1:find_underscore]
        PanelNum = itemName[(find_underscore+1):]
    
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
        if y:
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
        remain_lower100_2=[]
        remaining_service_lower10=[]
        MP2x_list=[]   
        MP2x_Dict={}                                 #(DemandId,Service)
        output_100=[]
        remain_lower100_dict={}
        remaining_service_lower10_dict={}
        groom_out10_list=[]
        remain_lower100=[]
        for i in n.TrafficMatrix.DemandDict:
            y=[]
            z=[]
            x=[]
            output_10=[] 
            for j in n.TrafficMatrix.DemandDict[i].ServiceDict:
#                if ((n.TrafficMatrix.DemandDict[i].ServiceDict[j].Type == "STM_1_Optical") or (n.TrafficMatrix.DemandDict[i].ServiceDict[j].Type == "STM_4") or (n.TrafficMatrix.DemandDict[i].ServiceDict[j].Type == "STM_16")):
                if (n.TrafficMatrix.DemandDict[i].ServiceDict[j].BW < 10):
                    y.append((n.TrafficMatrix.DemandDict[i].ServiceDict[j].Id,n.TrafficMatrix.DemandDict[i].ServiceDict[j].BW))
                elif (n.TrafficMatrix.DemandDict[i].ServiceDict[j].BW == 10):
                    z.append((n.TrafficMatrix.DemandDict[i].ServiceDict[j].Id,n.TrafficMatrix.DemandDict[i].ServiceDict[j].BW))
                else:
                    n.add_lightpath(n.TrafficMatrix.DemandDict[i].Source, n.TrafficMatrix.DemandDict[i].Destination, 100, [n.TrafficMatrix.DemandDict[i].ServiceDict[j].Id], 100, i,ClusterNum=0)
                    LastId = n.Lightpath.ReferenceId -1
#                    print(len(n.LightPathDict),"**")
                    n.TrafficMatrix.DemandDict[i].ServiceDict[j].LightPathId=LastId
#                    print(LastId,"***")
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
#                    n.TrafficMatrix.DemandDict[i].add_service(ServiceType= "Groom_out10" ,Sla= 2, Capacity=cap, ServiceIdList=listofs)    
                    GroomOutId = n.TrafficMatrix.Generate_GroomOutId()
                    n.TrafficMatrix.add_groom_out_10(GroomOutId= GroomOutId, Source=n.TrafficMatrix.DemandDict[i].Source, Destination=n.TrafficMatrix.DemandDict[i].Destination, DemandId=i, Capacity=cap, ServiceIdList=listofs)
                    LastId = GroomOutId
                    ffff=[(LastId,10)]
                    hhhh.append((LastId,cap,len(listofs)))
                    z.append((LastId,cap))
#                    service_lower100.append((i,ffff))
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
                        MP2x_Dict.update({groom_out10_list[i][0]:(groom_out10_list[i][1][j][0],groom_out10_list[i][1][k][0])})
                        nooo.append(j)
                        nooo.append(k)
            for m in range(0,len(groom_out10_list[i][1])):
                if m not in nooo:
                    remaining_service_lower10.append((groom_out10_list[i][0],groom_out10_list[i][1][m][0])) 
                    remaining_service_lower10_dict.update({groom_out10_list[i][0]:groom_out10_list[i][1][m][0]})
                    
           
        for i in range(0,len(service_lower100)):
            NO_LP= math.ceil(len(service_lower100[i][1])/10)
            for j in range(0,NO_LP):
                list_of_service=[]
                list_of_service2=[]
                cap=0
                for k in range(j*10,(j+1)*10):
                    if (k < len(service_lower100[i][1])):
                        list_of_service.append(service_lower100[i][1][k][0])
                        list_of_service2.append((service_lower100[i][1][k][0],service_lower100[i][1][k][1]))
                        cap=cap+service_lower100[i][1][k][1]
                if cap ==10:
                    typee="10GE"
                else:
                    typee="100G"
                if cap < MP1H_Threshold:
                    remain_lower100.append((service_lower100[i][0],list_of_service))
                    remain_lower100_2.append((service_lower100[i][0],list_of_service2))
                    remain_lower100_dict.update({service_lower100[i][0]:list_of_service})
                else:
                    n.add_lightpath(n.TrafficMatrix.DemandDict[service_lower100[i][0]].Source, n.TrafficMatrix.DemandDict[service_lower100[i][0]].Destination, Capacity=cap, ServiceIdList=list_of_service, Type=typee, DemandId=service_lower100[i][0],ClusterNum=0)    
                    LastId = n.Lightpath.ReferenceId -1
#                    print(LastId)
                    for idd in list_of_service:
                        if idd in n.TrafficMatrix.DemandDict[service_lower100[i][0]].ServiceDict:
                           n.TrafficMatrix.DemandDict[service_lower100[i][0]].ServiceDict[idd].LightPathId= LastId
                        if (service_lower100[i][0],idd) in n.TrafficMatrix.GroomOut10Dict:
                            n.TrafficMatrix.GroomOut10Dict[(service_lower100[i][0],idd)].LightPathId= LastId
                            for sid in n.TrafficMatrix.GroomOut10Dict[(service_lower100[i][0],idd)].ServiceIdList:
                                n.TrafficMatrix.DemandDict[n.TrafficMatrix.GroomOut10Dict[(service_lower100[i][0],idd)].DemandId].ServiceDict[sid].LightPathId= LastId
#        print(remain_lower100_2)  
#        print("***",n.TrafficMatrix.DemandDict[0].ServiceDict)
#        print("***",n.TrafficMatrix.DemandDict[0].Source)
#        print("***",n.TrafficMatrix.DemandDict[0].Destination)
                    
        
        remain_lower100_2_newV=[] 
        def changing_both_inC(Demandid,servId,BW):
            
#            for k in range(1,len(n.PhysicalTopology.ClusterDict)+1):
            for (k,vv) in n.PhysicalTopology.ClusterDict.items():
                if n.TrafficMatrix.DemandDict[Demandid].Source == n.PhysicalTopology.ClusterDict[k].GatewayId :
#                    for z in range(1,len(n.PhysicalTopology.ClusterDict)+1): 
                    for (z,vvv) in n.PhysicalTopology.ClusterDict.items():
                       if z!=k and n.TrafficMatrix.DemandDict[Demandid].Destination == n.PhysicalTopology.ClusterDict[z].GatewayId :
                           ff=0
#                           if(len(remain_lower100_2_newV)!=0):
                           for h in range(0,len(remain_lower100_2_newV)):
                               if (Demandid == remain_lower100_2_newV[h][0] ):
                                   remain_lower100_2_newV[h][1].append((servId,BW)) 
                                   ff=1
                           if ff==0:
                              remain_lower100_2_newV.append((Demandid,[(servId,BW)]))
#                           else:
#                               remain_lower100_2_newV.append((Demandid,[(servId,BW)]))
                       elif z!=k and n.TrafficMatrix.DemandDict[Demandid].Destination in n.PhysicalTopology.ClusterDict[z].SubNodesId :
                           newdes=n.PhysicalTopology.ClusterDict[z].GatewayId
                           orgdes=n.TrafficMatrix.DemandDict[Demandid].Destination
                           orgsrc=n.TrafficMatrix.DemandDict[Demandid].Source
                           typee=n.TrafficMatrix.DemandDict[Demandid].ServiceDict[servId].Type
                           i1=0
                           i2=0
                           for ii in n.TrafficMatrix.DemandDict:
                               if n.TrafficMatrix.DemandDict[ii].Source == n.TrafficMatrix.DemandDict[Demandid].Source and n.TrafficMatrix.DemandDict[ii].Destination == newdes:
                                   n.TrafficMatrix.DemandDict[ii].add_service(ServiceId=servId,ServiceType=typee,Sla=2,OriginalSource=orgsrc,OriginalDestination=orgdes)
                                   ff=0
                                   i1=1
                                   for h in range(0,len(remain_lower100_2_newV)):
                                       if (ii == remain_lower100_2_newV[h][0] ):
                                           remain_lower100_2_newV[h][1].append((servId,BW)) 
                                           ff=1
                                   if ff==0:
                                        remain_lower100_2_newV.append((ii,[(servId,BW)]))
                               elif n.TrafficMatrix.DemandDict[ii].Source == newdes and n.TrafficMatrix.DemandDict[ii].Destination == n.TrafficMatrix.DemandDict[Demandid].Destination:
                                   n.TrafficMatrix.DemandDict[ii].add_service(ServiceId=servId,ServiceType=typee,Sla=2,OriginalSource=orgsrc,OriginalDestination=orgdes)
                                   ff=0
                                   i2=1
                                   for h in range(0,len(remain_lower100_2_newV)):
                                       if (ii == remain_lower100_2_newV[h][0] ):
                                           remain_lower100_2_newV[h][1].append((servId,BW)) 
                                           ff=1
                                   if ff==0:
                                        remain_lower100_2_newV.append((ii,[(servId,BW)]))
                           if i1==0:
                               n.TrafficMatrix.add_demand(n.TrafficMatrix.DemandDict[Demandid].Source,newdes,"X")
                               LastId = n.TrafficMatrix.Demand.DemandReferenceId - 1
                               n.TrafficMatrix.DemandDict[LastId].add_service(servId,typee,2,OriginalSource=orgsrc,OriginalDestination=orgdes)
                               remain_lower100_2_newV.append((LastId,[(servId,BW)]))
                           if i2==0:
                               n.TrafficMatrix.add_demand(newdes,n.TrafficMatrix.DemandDict[Demandid].Destination,"X")
                               LastId = n.TrafficMatrix.Demand.DemandReferenceId - 1
                               n.TrafficMatrix.DemandDict[LastId].add_service(servId,typee,2,OriginalSource=orgsrc,OriginalDestination=orgdes)
                               remain_lower100_2_newV.append((LastId,[(servId,BW)]))
                           n.TrafficMatrix.DemandDict[Demandid].ServiceDict.pop(servId)
                       elif z==k and n.TrafficMatrix.DemandDict[Demandid].Destination in n.PhysicalTopology.ClusterDict[z].SubNodesId :
                           ff=0
                           for h in range(0,len(remain_lower100_2_newV)):
                               if (Demandid == remain_lower100_2_newV[h][0] ):
                                   remain_lower100_2_newV[h][1].append((servId,BW)) 
                                   ff=1
                           if ff==0:
                                remain_lower100_2_newV.append((Demandid,[(servId,BW)]))
                elif n.TrafficMatrix.DemandDict[Demandid].Source in  n.PhysicalTopology.ClusterDict[k].SubNodesId :
#                    for z in range(1,len(n.PhysicalTopology.ClusterDict)+1):
                    for (z,vvv) in n.PhysicalTopology.ClusterDict.items():
                        if z==k and (n.TrafficMatrix.DemandDict[Demandid].Destination in n.PhysicalTopology.ClusterDict[z].SubNodesId or n.TrafficMatrix.DemandDict[Demandid].Destination == n.PhysicalTopology.ClusterDict[z].GatewayId):
                            ff=0
                            for h in range(0,len(remain_lower100_2_newV)):
                                if (Demandid == remain_lower100_2_newV[h][0] ):
                                    remain_lower100_2_newV[h][1].append((servId,BW)) 
                                    ff=1
                            if ff==0:
                               remain_lower100_2_newV.append((Demandid,[(servId,BW)])) 
                        elif z!=k and n.TrafficMatrix.DemandDict[Demandid].Destination in n.PhysicalTopology.ClusterDict[z].SubNodesId:
                            i1=0
                            i2=0
                            i3=0
                            for i in n.TrafficMatrix.DemandDict:
                                if n.TrafficMatrix.DemandDict[i].Source==n.TrafficMatrix.DemandDict[Demandid].Source and n.TrafficMatrix.DemandDict[i].Destination==n.PhysicalTopology.ClusterDict[k].GatewayId:
                                    newdes=n.PhysicalTopology.ClusterDict[k].GatewayId
                                    orgdes=n.TrafficMatrix.DemandDict[Demandid].Destination
                                    orgsrc=n.TrafficMatrix.DemandDict[Demandid].Source
                                    typee=n.TrafficMatrix.DemandDict[Demandid].ServiceDict[servId].Type
                                    n.TrafficMatrix.DemandDict[i].add_service(ServiceId=servId,ServiceType=typee,Sla=2,OriginalSource=orgsrc,OriginalDestination=orgdes)
                                    ff=0
                                    i1=1
                                    for h in range(0,len(remain_lower100_2_newV)):
                                       if (i == remain_lower100_2_newV[h][0] ):
                                           remain_lower100_2_newV[h][1].append((servId,BW)) 
                                           ff=1
                                    if ff==0:
                                        remain_lower100_2_newV.append((i,[(servId,BW)]))
                                elif n.TrafficMatrix.DemandDict[i].Source==n.PhysicalTopology.ClusterDict[k].GatewayId and n.TrafficMatrix.DemandDict[i].Destination==n.PhysicalTopology.ClusterDict[z].GatewayId:
                                    orgdes=n.TrafficMatrix.DemandDict[Demandid].Destination
                                    orgsrc=n.TrafficMatrix.DemandDict[Demandid].Source
                                    typee=n.TrafficMatrix.DemandDict[Demandid].ServiceDict[servId].Type
                                    n.TrafficMatrix.DemandDict[i].add_service(ServiceId=servId,ServiceType=typee,Sla=2,OriginalSource=orgsrc,OriginalDestination=orgdes)
                                    ff=0
                                    i2=1
                                    for h in range(0,len(remain_lower100_2_newV)):
                                       if (i == remain_lower100_2_newV[h][0] ):
                                           remain_lower100_2_newV[h][1].append((servId,BW)) 
                                           ff=1
                                    if ff==0:
                                        remain_lower100_2_newV.append((i,[(servId,BW)]))
                                elif n.TrafficMatrix.DemandDict[i].Source==n.PhysicalTopology.ClusterDict[z].GatewayId and n.TrafficMatrix.DemandDict[i].Destination==n.TrafficMatrix.DemandDict[Demandid].Destination:
                                    orgdes=n.TrafficMatrix.DemandDict[Demandid].Destination
                                    orgsrc=n.TrafficMatrix.DemandDict[Demandid].Source
                                    typee=n.TrafficMatrix.DemandDict[Demandid].ServiceDict[servId].Type
                                    n.TrafficMatrix.DemandDict[i].add_service(ServiceId=servId,ServiceType=typee,Sla=2,OriginalSource=orgsrc,OriginalDestination=orgdes)
                                    ff=0
                                    i3=1
                                    for h in range(0,len(remain_lower100_2_newV)):
                                       if (i == remain_lower100_2_newV[h][0] ):
                                           remain_lower100_2_newV[h][1].append((servId,BW)) 
                                           ff=1
                                    if ff==0:
                                        remain_lower100_2_newV.append((i,[(servId,BW)]))
                            if i1==0:
                                n.TrafficMatrix.add_demand(n.TrafficMatrix.DemandDict[Demandid].Source,n.PhysicalTopology.ClusterDict[k].GatewayId,"X")
                                LastId = n.TrafficMatrix.Demand.DemandReferenceId - 1
                                n.TrafficMatrix.DemandDict[LastId].add_service(servId,typee,2,OriginalSource=orgsrc,OriginalDestination=orgdes)
                                remain_lower100_2_newV.append((LastId,[(servId,BW)]))
                            if i2==0:
                                n.TrafficMatrix.add_demand(n.PhysicalTopology.ClusterDict[k].GatewayId,n.PhysicalTopology.ClusterDict[z].GatewayId,"X")
                                LastId = n.TrafficMatrix.Demand.DemandReferenceId - 1
                                n.TrafficMatrix.DemandDict[LastId].add_service(servId,typee,2,OriginalSource=orgsrc,OriginalDestination=orgdes)
                                remain_lower100_2_newV.append((LastId,[(servId,BW)]))
                            if i3==0:
                                n.TrafficMatrix.add_demand(n.PhysicalTopology.ClusterDict[z].GatewayId,n.TrafficMatrix.DemandDict[Demandid].Destination,"X")
                                LastId = n.TrafficMatrix.Demand.DemandReferenceId - 1
                                n.TrafficMatrix.DemandDict[LastId].add_service(servId,typee,2,OriginalSource=orgsrc,OriginalDestination=orgdes)
                                remain_lower100_2_newV.append((LastId,[(servId,BW)]))
                            n.TrafficMatrix.DemandDict[Demandid].ServiceDict.pop(servId)
                        elif z!=k and n.TrafficMatrix.DemandDict[Demandid].Destination == n.PhysicalTopology.ClusterDict[z].GatewayId:
                            i1=0
                            i2=0
                            for i in n.TrafficMatrix.DemandDict:
                                if n.TrafficMatrix.DemandDict[i].Source==n.TrafficMatrix.DemandDict[Demandid].Source and n.TrafficMatrix.DemandDict[i].Destination==n.PhysicalTopology.ClusterDict[k].GatewayId:
                                    newdes=n.PhysicalTopology.ClusterDict[k].GatewayId
                                    orgdes=n.TrafficMatrix.DemandDict[Demandid].Destination
                                    orgsrc=n.TrafficMatrix.DemandDict[Demandid].Source
                                    typee=n.TrafficMatrix.DemandDict[Demandid].ServiceDict[servId].Type
                                    n.TrafficMatrix.DemandDict[i].add_service(ServiceId=servId,ServiceType=typee,Sla=2,OriginalSource=orgsrc,OriginalDestination=orgdes)
                                    ff=0
                                    i1=1
                                    for h in range(0,len(remain_lower100_2_newV)):
                                       if (i == remain_lower100_2_newV[h][0] ):
                                           remain_lower100_2_newV[h][1].append((servId,BW)) 
                                           ff=1
                                    if ff==0:
                                        remain_lower100_2_newV.append((i,[(servId,BW)]))
                                elif n.TrafficMatrix.DemandDict[i].Source==n.PhysicalTopology.ClusterDict[k].GatewayId and n.TrafficMatrix.DemandDict[i].Destination==n.PhysicalTopology.ClusterDict[z].GatewayId:
                                    orgdes=n.TrafficMatrix.DemandDict[Demandid].Destination
                                    orgsrc=n.TrafficMatrix.DemandDict[Demandid].Source
                                    typee=n.TrafficMatrix.DemandDict[Demandid].ServiceDict[servId].Type
                                    n.TrafficMatrix.DemandDict[i].add_service(ServiceId=servId,ServiceType=typee,Sla=2,OriginalSource=orgsrc,OriginalDestination=orgdes)
                                    ff=0
                                    i2=1
                                    for h in range(0,len(remain_lower100_2_newV)):
                                       if (i == remain_lower100_2_newV[h][0] ):
                                           remain_lower100_2_newV[h][1].append((servId,BW)) 
                                           ff=1
                                    if ff==0:
                                        remain_lower100_2_newV.append((i,[(servId,BW)]))
                            if i1==0:
                                n.TrafficMatrix.add_demand(n.TrafficMatrix.DemandDict[Demandid].Source,n.PhysicalTopology.ClusterDict[k].GatewayId,"X")
                                LastId = n.TrafficMatrix.Demand.DemandReferenceId - 1
                                n.TrafficMatrix.DemandDict[LastId].add_service(servId,typee,2,OriginalSource=orgsrc,OriginalDestination=orgdes)
                                remain_lower100_2_newV.append((LastId,[(servId,BW)]))
                            if i2==0:
                                n.TrafficMatrix.add_demand(n.PhysicalTopology.ClusterDict[k].GatewayId,n.PhysicalTopology.ClusterDict[z].GatewayId,"X")
                                LastId = n.TrafficMatrix.Demand.DemandReferenceId - 1
                                n.TrafficMatrix.DemandDict[LastId].add_service(servId,typee,2,OriginalSource=orgsrc,OriginalDestination=orgdes)
                                remain_lower100_2_newV.append((LastId,[(servId,BW)]))
                            n.TrafficMatrix.DemandDict[Demandid].ServiceDict.pop(servId)
                                #                elif remain_lower100_2[i][1][j][0] in n.TrafficMatrix.GroomOut10Dict:
                 
            
        def changing_onlysrc_inC(Demandid,servId,BW):

#            for k in range(1,len(n.PhysicalTopology.ClusterDict)+1):
            for (k,vv) in n.PhysicalTopology.ClusterDict.items():
                if n.TrafficMatrix.DemandDict[Demandid].Source == n.PhysicalTopology.ClusterDict[k].GatewayId :
                    ff=0
                    for h in range(0,len(remain_lower100_2_newV)):
                        if (Demandid == remain_lower100_2_newV[h][0] ):
                            remain_lower100_2_newV[h][1].append((servId,BW)) 
                            ff=1
                    if ff==0:
                       remain_lower100_2_newV.append((Demandid,[(servId,BW)]))
                elif n.TrafficMatrix.DemandDict[Demandid].Source in n.PhysicalTopology.ClusterDict[k].SubNodesId :
                    newdes=n.PhysicalTopology.ClusterDict[k].GatewayId
                    orgdes=n.TrafficMatrix.DemandDict[Demandid].Destination
                    orgsrc=n.TrafficMatrix.DemandDict[Demandid].Source
                    typee=n.TrafficMatrix.DemandDict[Demandid].ServiceDict[servId].Type
                    i1=0
                    i2=0
                    for ii in n.TrafficMatrix.DemandDict:
                       if n.TrafficMatrix.DemandDict[ii].Source == n.TrafficMatrix.DemandDict[Demandid].Source and n.TrafficMatrix.DemandDict[ii].Destination == newdes:
                           n.TrafficMatrix.DemandDict[ii].add_service(ServiceId=servId,ServiceType=typee,Sla=2,OriginalSource=orgsrc,OriginalDestination=orgdes)
                           ff=0
                           i1=1
                           print(n.TrafficMatrix.DemandDict[ii].ServiceDict[servId].OriginalSource,n.TrafficMatrix.DemandDict[ii].ServiceDict[servId].OriginalDestination,ii,"---------")
                           for h in range(0,len(remain_lower100_2_newV)):
                               if (i == remain_lower100_2_newV[h][0] ):
                                   remain_lower100_2_newV[h][1].append((servId,BW)) 
                                   ff=1
                           if ff==0:
                                remain_lower100_2_newV.append((ii,[(servId,BW)]))
                       elif n.TrafficMatrix.DemandDict[ii].Source == newdes and n.TrafficMatrix.DemandDict[ii].Destination == n.TrafficMatrix.DemandDict[Demandid].Destination:
                           n.TrafficMatrix.DemandDict[ii].add_service(ServiceId=servId,ServiceType=typee,Sla=2,OriginalSource=orgsrc,OriginalDestination=orgdes)
                           ff=0
                           i2=1
                           for h in range(0,len(remain_lower100_2_newV)):
                               if (i == remain_lower100_2_newV[h][0] ):
                                   remain_lower100_2_newV[h][1].append((servId,BW)) 
                                   ff=1
                           if ff==0:
                                remain_lower100_2_newV.append((ii,[(servId,BW)]))
                    if i1==0:
                       n.TrafficMatrix.add_demand(n.TrafficMatrix.DemandDict[Demandid].Source,newdes,"X")
                       LastId = n.TrafficMatrix.Demand.DemandReferenceId - 1
                       n.TrafficMatrix.DemandDict[LastId].add_service(servId,typee,2,OriginalSource=orgsrc,OriginalDestination=orgdes)
                       remain_lower100_2_newV.append((LastId,[(servId,BW)]))
                    if i2==0:
                        n.TrafficMatrix.add_demand(newdes,n.TrafficMatrix.DemandDict[Demandid].Destination,"X")
                        LastId = n.TrafficMatrix.Demand.DemandReferenceId - 1
                        n.TrafficMatrix.DemandDict[LastId].add_service(servId,typee,2,OriginalSource=orgsrc,OriginalDestination=orgdes)
                        remain_lower100_2_newV.append((LastId,[(servId,BW)]))
                    n.TrafficMatrix.DemandDict[Demandid].ServiceDict.pop(servId)
                    
                    
                    
         
            
        def changing_onlydes_inC(Demandid,servId,BW):
            
#            for k in range(1,len(n.PhysicalTopology.ClusterDict)+1):
            for (k,vv) in n.PhysicalTopology.ClusterDict.items():
                if n.TrafficMatrix.DemandDict[Demandid].Destination == n.PhysicalTopology.ClusterDict[k].GatewayId :
                    ff=0
                    for h in range(0,len(remain_lower100_2_newV)):
                        if (Demandid == remain_lower100_2_newV[h][0] ):
                            remain_lower100_2_newV[h][1].append((servId,BW)) 
                            ff=1
                    if ff==0:
                       remain_lower100_2_newV.append((Demandid,[(servId,BW)]))
                elif n.TrafficMatrix.DemandDict[Demandid].Destination in n.PhysicalTopology.ClusterDict[k].SubNodesId :
                    newdes=n.PhysicalTopology.ClusterDict[k].GatewayId
                    orgdes=n.TrafficMatrix.DemandDict[Demandid].Destination
                    orgsrc=n.TrafficMatrix.DemandDict[Demandid].Source
                    typee=n.TrafficMatrix.DemandDict[Demandid].ServiceDict[servId].Type
                    i1=0
                    i2=0
                    for ii in n.TrafficMatrix.DemandDict:
                       if n.TrafficMatrix.DemandDict[ii].Source == n.TrafficMatrix.DemandDict[Demandid].Source and n.TrafficMatrix.DemandDict[ii].Destination == newdes:
                           n.TrafficMatrix.DemandDict[ii].add_service(ServiceId=servId,ServiceType=typee,Sla=2,OriginalSource=orgsrc,OriginalDestination=orgdes)
                           ff=0
                           i1=1
                           for h in range(0,len(remain_lower100_2_newV)):
                               if (i == remain_lower100_2_newV[h][0] ):
                                   remain_lower100_2_newV[h][1].append((servId,BW)) 
                                   ff=1
                           if ff==0:
                                remain_lower100_2_newV.append((ii,[(servId,BW)]))
                       elif n.TrafficMatrix.DemandDict[ii].Source == newdes and n.TrafficMatrix.DemandDict[ii].Destination == n.TrafficMatrix.DemandDict[Demandid].Destination:
                           n.TrafficMatrix.DemandDict[ii].add_service(ServiceId=servId,ServiceType=typee,Sla=2,OriginalSource=orgsrc,OriginalDestination=orgdes)
                           ff=0
                           i2=1
                           for h in range(0,len(remain_lower100_2_newV)):
                               if (i == remain_lower100_2_newV[h][0] ):
                                   remain_lower100_2_newV[h][1].append((servId,BW)) 
                                   ff=1
                           if ff==0:
                                remain_lower100_2_newV.append((ii,[(servId,BW)]))
                    if i1==0:
                       n.TrafficMatrix.add_demand(n.TrafficMatrix.DemandDict[Demandid].Source,newdes,"X")
                       LastId = n.TrafficMatrix.Demand.DemandReferenceId - 1
                       n.TrafficMatrix.DemandDict[LastId].add_service(servId,typee,2,OriginalSource=orgsrc,OriginalDestination=orgdes)
                       remain_lower100_2_newV.append((LastId,[(servId,BW)]))
                    if i2==0:
                        n.TrafficMatrix.add_demand(newdes,n.TrafficMatrix.DemandDict[Demandid].Destination,"X")
                        LastId = n.TrafficMatrix.Demand.DemandReferenceId - 1
                        n.TrafficMatrix.DemandDict[LastId].add_service(servId,typee,2,OriginalSource=orgsrc,OriginalDestination=orgdes)
                        remain_lower100_2_newV.append((LastId,[(servId,BW)]))
                    n.TrafficMatrix.DemandDict[Demandid].ServiceDict.pop(servId)
            
            
            



        def changing_both_inC_groom10(Demandid,servId,BW): 
           
#           for k in range(1,len(n.PhysicalTopology.ClusterDict)+1):
           for (k,vv) in n.PhysicalTopology.ClusterDict.items():
               if n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Source == n.PhysicalTopology.ClusterDict[k].GatewayId:
#                   for z in range(1,len(n.PhysicalTopology.ClusterDict)+1):
                   for (z,vvv) in n.PhysicalTopology.ClusterDict.items():
                       if z!=k and n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Destination == n.PhysicalTopology.ClusterDict[z].GatewayId :
                           ff=0
                           for h in range(0,len(remain_lower100_2_newV)):
                               if (Demandid == remain_lower100_2_newV[h][0] ):
                                   remain_lower100_2_newV[h][1].append((servId,BW)) 
                                   ff=1
                           if ff==0:
                              remain_lower100_2_newV.append((Demandid,[(servId,BW)]))
                       elif z==k and n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Destination in n.PhysicalTopology.ClusterDict[z].SubNodesId :
                           ff=0
                           for h in range(0,len(remain_lower100_2_newV)):
                               if (Demandid == remain_lower100_2_newV[h][0] ):
                                   remain_lower100_2_newV[h][1].append((servId,BW)) 
                                   ff=1
                           if ff==0:
                              remain_lower100_2_newV.append((Demandid,[(servId,BW)]))
                       elif z!=k and n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Destination in n.PhysicalTopology.ClusterDict[z].SubNodesId :
                           newdes=n.PhysicalTopology.ClusterDict[z].GatewayId
                           orgdes=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Destination
                           orgsrc=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Source
#                           typee=n.TrafficMatrix.DemandDict[Demandid].ServiceDict[servId].Type
                           i1=0
                           i2=0
                           for did in n.TrafficMatrix.DemandDict:
                               if n.TrafficMatrix.DemandDict[did].Source == n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Source  and n.TrafficMatrix.DemandDict[did].Destination == newdes:
                                   n.TrafficMatrix.add_groom_out_10(GroomOutId=servId, Source=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Source, Destination=newdes,DemandId=did,Capacity=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Capacity, ServiceIdList=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].ServiceIdList)
                                   ff=0
                                   i1=1
                                   for h in range(0,len(remain_lower100_2_newV)):
                                       if (did == remain_lower100_2_newV[h][0] ):
                                           remain_lower100_2_newV[h][1].append((servId,BW)) 
                                           ff=1
                                   if ff==0:
                                      remain_lower100_2_newV.append((did,[(servId,BW)]))
                                   for sid in n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].ServiceIdList:
                                       n.TrafficMatrix.DemandDict[did].add_service(sid,n.TrafficMatrix.DemandDict[Demandid].ServiceDict[sid].Type,2,OriginalSource=orgsrc,OriginalDestination=orgdes)
                               elif n.TrafficMatrix.DemandDict[did].Source == newdes  and n.TrafficMatrix.DemandDict[did].Destination == n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Destination:
                                   n.TrafficMatrix.add_groom_out_10(GroomOutId=servId, Source=newdes, Destination=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Destination,DemandId=did,Capacity=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Capacity, ServiceIdList=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].ServiceIdList)
                                   ff=0
                                   i2=1
                                   for h in range(0,len(remain_lower100_2_newV)):
                                       if (did == remain_lower100_2_newV[h][0] ):
                                           remain_lower100_2_newV[h][1].append((servId,BW)) 
                                           ff=1
                                   if ff==0:
                                      remain_lower100_2_newV.append((did,[(servId,BW)]))
                                   for sid in n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].ServiceIdList:
                                       n.TrafficMatrix.DemandDict[did].add_service(sid,n.TrafficMatrix.DemandDict[Demandid].ServiceDict[sid].Type,2,OriginalSource=orgsrc,OriginalDestination=orgdes)
                           if i1==0:
                               n.TrafficMatrix.add_demand(n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Source,newdes,"X")
                               LastId = n.TrafficMatrix.Demand.DemandReferenceId - 1
                               n.TrafficMatrix.add_groom_out_10(GroomOutId=servId, Source=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Source, Destination=newdes,DemandId=LastId,Capacity=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Capacity, ServiceIdList=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].ServiceIdList)
                               remain_lower100_2_newV.append((LastId,[(servId,BW)]))
                               for sid in n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].ServiceIdList:
                                   n.TrafficMatrix.DemandDict[LastId].add_service(sid,n.TrafficMatrix.DemandDict[Demandid].ServiceDict[sid].Type,2,OriginalSource=orgsrc,OriginalDestination=orgdes)
                           if i2==0:
                               n.TrafficMatrix.add_demand(newdes,n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Destination,"X")
                               LastId = n.TrafficMatrix.Demand.DemandReferenceId - 1
                               n.TrafficMatrix.add_groom_out_10(GroomOutId=servId, Source=newdes, Destination=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Destination,DemandId=LastId,Capacity=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Capacity, ServiceIdList=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].ServiceIdList)
                               remain_lower100_2_newV.append((LastId,[(servId,BW)]))
                               for sid in n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].ServiceIdList:
                                   n.TrafficMatrix.DemandDict[LastId].add_service(sid,n.TrafficMatrix.DemandDict[Demandid].ServiceDict[sid].Type,2,OriginalSource=orgsrc,OriginalDestination=orgdes) 
#                           for sid in n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].ServiceIdList:
#                              n.TrafficMatrix.DemandDict[Demandid].ServiceDict.pop(sid)
#                           n.TrafficMatrix.delete_groom_out_10(Demandid,servId)
               elif n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Source in n.PhysicalTopology.ClusterDict[k].SubNodesId:
#                   for z in range(1,len(n.PhysicalTopology.ClusterDict)+1):
                   for (z,vvv) in n.PhysicalTopology.ClusterDict.items():
                       if z==k and n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Destination == n.PhysicalTopology.ClusterDict[z].GatewayId :
                           ff=0
                           for h in range(0,len(remain_lower100_2_newV)):
                               if (Demandid == remain_lower100_2_newV[h][0] ):
                                   remain_lower100_2_newV[h][1].append((servId,BW)) 
                                   ff=1
                           if ff==0:
                              remain_lower100_2_newV.append((Demandid,[(servId,BW)]))
                       elif z!=k and n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Destination == n.PhysicalTopology.ClusterDict[z].GatewayId :
                           newdes=n.PhysicalTopology.ClusterDict[k].GatewayId
                           orgdes=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Destination
                           orgsrc=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Source
                           i1=0
                           i2=0
                           for did in n.TrafficMatrix.DemandDict:
                               if n.TrafficMatrix.DemandDict[did].Source == n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Source  and n.TrafficMatrix.DemandDict[did].Destination == newdes:
                                   n.TrafficMatrix.add_groom_out_10(GroomOutId=servId, Source=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Source, Destination=newdes,DemandId=did,Capacity=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Capacity, ServiceIdList=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].ServiceIdList)
                                   ff=0
                                   i1=1
                                   for h in range(0,len(remain_lower100_2_newV)):
                                       if (did == remain_lower100_2_newV[h][0] ):
                                           remain_lower100_2_newV[h][1].append((servId,BW)) 
                                           ff=1
                                   if ff==0:
                                      remain_lower100_2_newV.append((did,[(servId,BW)]))
                                   for sid in n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].ServiceIdList:
                                       n.TrafficMatrix.DemandDict[did].add_service(sid,n.TrafficMatrix.DemandDict[Demandid].ServiceDict[sid].Type,2,OriginalSource=orgsrc,OriginalDestination=orgdes)
                               elif n.TrafficMatrix.DemandDict[did].Source == newdes  and n.TrafficMatrix.DemandDict[did].Destination == n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Destination:
                                   n.TrafficMatrix.add_groom_out_10(GroomOutId=servId, Source=newdes, Destination=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Destination,DemandId=did,Capacity=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Capacity, ServiceIdList=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].ServiceIdList)
                                   ff=0
                                   i2=1
                                   for h in range(0,len(remain_lower100_2_newV)):
                                       if (did == remain_lower100_2_newV[h][0] ):
                                           remain_lower100_2_newV[h][1].append((servId,BW)) 
                                           ff=1
                                   if ff==0:
                                      remain_lower100_2_newV.append((did,[(servId,BW)]))
                                   for sid in n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].ServiceIdList:
                                       n.TrafficMatrix.DemandDict[did].add_service(sid,n.TrafficMatrix.DemandDict[Demandid].ServiceDict[sid].Type,2,OriginalSource=orgsrc,OriginalDestination=orgdes)
                           if i1==0:
                               n.TrafficMatrix.add_demand(n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Source,newdes,"X")
                               LastId = n.TrafficMatrix.Demand.DemandReferenceId - 1
                               n.TrafficMatrix.add_groom_out_10(GroomOutId=servId, Source=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Source, Destination=newdes,DemandId=LastId,Capacity=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Capacity, ServiceIdList=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].ServiceIdList)
                               remain_lower100_2_newV.append((LastId,[(servId,BW)]))
                               for sid in n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].ServiceIdList:
                                   n.TrafficMatrix.DemandDict[LastId].add_service(sid,n.TrafficMatrix.DemandDict[Demandid].ServiceDict[sid].Type,2,OriginalSource=orgsrc,OriginalDestination=orgdes)
                           if i2==0:
                               n.TrafficMatrix.add_demand(newdes,n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Destination,"X")
                               LastId = n.TrafficMatrix.Demand.DemandReferenceId - 1
                               n.TrafficMatrix.add_groom_out_10(GroomOutId=servId, Source=newdes, Destination=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Destination,DemandId=LastId,Capacity=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Capacity, ServiceIdList=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].ServiceIdList)
                               remain_lower100_2_newV.append((LastId,[(servId,BW)]))
                               for sid in n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].ServiceIdList:
                                   n.TrafficMatrix.DemandDict[LastId].add_service(sid,n.TrafficMatrix.DemandDict[Demandid].ServiceDict[sid].Type,2,OriginalSource=orgsrc,OriginalDestination=orgdes) 
#                           for sid in n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].ServiceIdList:
#                              n.TrafficMatrix.DemandDict[Demandid].ServiceDict.pop(sid)
#                           n.TrafficMatrix.delete_groom_out_10(Demandid,servId)
                       elif z==k and n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Destination in n.PhysicalTopology.ClusterDict[z].SubNodesId :
                           ff=0
                           for h in range(0,len(remain_lower100_2_newV)):
                               if (Demandid == remain_lower100_2_newV[h][0] ):
                                   remain_lower100_2_newV[h][1].append((servId,BW)) 
                                   ff=1
                           if ff==0:
                              remain_lower100_2_newV.append((Demandid,[(servId,BW)]))
                       elif z!=k and n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Destination in n.PhysicalTopology.ClusterDict[z].SubNodesId :
                           orgdes=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Destination
                           orgsrc=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Source
                           i1=0
                           i2=0
                           i3=0
                           for did in n.TrafficMatrix.DemandDict:
                               if n.TrafficMatrix.DemandDict[did].Source == n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Source  and n.TrafficMatrix.DemandDict[did].Destination == n.PhysicalTopology.ClusterDict[k].GatewayId:
                                   n.TrafficMatrix.add_groom_out_10(GroomOutId=servId, Source=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Source, Destination=n.PhysicalTopology.ClusterDict[k].GatewayId,DemandId=did,Capacity=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Capacity, ServiceIdList=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].ServiceIdList)
                                   ff=0
                                   i1=1
                                   for h in range(0,len(remain_lower100_2_newV)):
                                       if (did == remain_lower100_2_newV[h][0] ):
                                           remain_lower100_2_newV[h][1].append((servId,BW)) 
                                           ff=1
                                   if ff==0:
                                      remain_lower100_2_newV.append((did,[(servId,BW)]))
                                   for sid in n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].ServiceIdList:
                                       n.TrafficMatrix.DemandDict[did].add_service(sid,n.TrafficMatrix.DemandDict[Demandid].ServiceDict[sid].Type,2,OriginalSource=orgsrc,OriginalDestination=orgdes)
                               elif n.TrafficMatrix.DemandDict[did].Source == n.PhysicalTopology.ClusterDict[k].GatewayId  and n.TrafficMatrix.DemandDict[did].Destination == n.PhysicalTopology.ClusterDict[z].GatewayId:
                                   n.TrafficMatrix.add_groom_out_10(GroomOutId=servId, Source=n.PhysicalTopology.ClusterDict[k].GatewayId, Destination=n.PhysicalTopology.ClusterDict[z].GatewayId,DemandId=did,Capacity=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Capacity, ServiceIdList=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].ServiceIdList)
                                   ff=0
                                   i2=1
                                   for h in range(0,len(remain_lower100_2_newV)):
                                       if (did == remain_lower100_2_newV[h][0] ):
                                           remain_lower100_2_newV[h][1].append((servId,BW)) 
                                           ff=1
                                   if ff==0:
                                      remain_lower100_2_newV.append((did,[(servId,BW)]))
                                   for sid in n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].ServiceIdList:
                                       n.TrafficMatrix.DemandDict[did].add_service(sid,n.TrafficMatrix.DemandDict[Demandid].ServiceDict[sid].Type,2,OriginalSource=orgsrc,OriginalDestination=orgdes)
                               elif n.TrafficMatrix.DemandDict[did].Source == n.PhysicalTopology.ClusterDict[z].GatewayId  and n.TrafficMatrix.DemandDict[did].Destination == n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Destination:
                                   n.TrafficMatrix.add_groom_out_10(GroomOutId=servId, Source=n.PhysicalTopology.ClusterDict[z].GatewayId, Destination=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Destination,DemandId=did,Capacity=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Capacity, ServiceIdList=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].ServiceIdList)
                                   ff=0
                                   i3=1
                                   for h in range(0,len(remain_lower100_2_newV)):
                                       if (did == remain_lower100_2_newV[h][0] ):
                                           remain_lower100_2_newV[h][1].append((servId,BW)) 
                                           ff=1
                                   if ff==0:
                                      remain_lower100_2_newV.append((did,[(servId,BW)]))
                                   for sid in n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].ServiceIdList:
                                       n.TrafficMatrix.DemandDict[did].add_service(sid,n.TrafficMatrix.DemandDict[Demandid].ServiceDict[sid].Type,2,OriginalSource=orgsrc,OriginalDestination=orgdes)
                           if i1==0:
                               n.TrafficMatrix.add_demand(n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Source,n.PhysicalTopology.ClusterDict[k].GatewayId,"X")
                               LastId = n.TrafficMatrix.Demand.DemandReferenceId - 1
                               n.TrafficMatrix.add_groom_out_10(GroomOutId=servId, Source=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Source, Destination=n.PhysicalTopology.ClusterDict[k].GatewayId,DemandId=LastId,Capacity=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Capacity, ServiceIdList=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].ServiceIdList)
                               remain_lower100_2_newV.append((LastId,[(servId,BW)]))
                               for sid in n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].ServiceIdList:
                                   n.TrafficMatrix.DemandDict[LastId].add_service(sid,n.TrafficMatrix.DemandDict[Demandid].ServiceDict[sid].Type,2,OriginalSource=orgsrc,OriginalDestination=orgdes)
                           if i2==0:
                               n.TrafficMatrix.add_demand(n.PhysicalTopology.ClusterDict[k].GatewayId,n.PhysicalTopology.ClusterDict[z].GatewayId,"X")
                               LastId = n.TrafficMatrix.Demand.DemandReferenceId - 1
                               n.TrafficMatrix.add_groom_out_10(GroomOutId=servId, Source=n.PhysicalTopology.ClusterDict[k].GatewayId, Destination=n.PhysicalTopology.ClusterDict[z].GatewayId,DemandId=LastId,Capacity=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Capacity, ServiceIdList=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].ServiceIdList)
                               remain_lower100_2_newV.append((LastId,[(servId,BW)]))
                               for sid in n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].ServiceIdList:
                                   n.TrafficMatrix.DemandDict[LastId].add_service(sid,n.TrafficMatrix.DemandDict[Demandid].ServiceDict[sid].Type,2,OriginalSource=orgsrc,OriginalDestination=orgdes) 
                           if i3==0:
                               n.TrafficMatrix.add_demand(n.PhysicalTopology.ClusterDict[z].GatewayId,n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Destination,"X")
                               LastId = n.TrafficMatrix.Demand.DemandReferenceId - 1
                               n.TrafficMatrix.add_groom_out_10(GroomOutId=servId, Source=n.PhysicalTopology.ClusterDict[z].GatewayId, Destination=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Destination,DemandId=LastId,Capacity=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Capacity, ServiceIdList=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].ServiceIdList)
                               remain_lower100_2_newV.append((LastId,[(servId,BW)]))
                               for sid in n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].ServiceIdList:
                                   n.TrafficMatrix.DemandDict[LastId].add_service(sid,n.TrafficMatrix.DemandDict[Demandid].ServiceDict[sid].Type,2,OriginalSource=orgsrc,OriginalDestination=orgdes) 
           for sid in n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].ServiceIdList:
              n.TrafficMatrix.DemandDict[Demandid].ServiceDict.pop(sid)
           n.TrafficMatrix.delete_groom_out_10(servId,Demandid)
                           
                           
                           
                           
                           


        def changing_onlysrc_inC_groom10(Demandid,servId,BW): 
           
#            for k in range(1,len(n.PhysicalTopology.ClusterDict)+1):
            for (k,vv) in n.PhysicalTopology.ClusterDict.items():
                if n.TrafficMatrix.DemandDict[Demandid].Source == n.PhysicalTopology.ClusterDict[k].GatewayId :
                    ff=0
                    for h in range(0,len(remain_lower100_2_newV)):
                        if (Demandid == remain_lower100_2_newV[h][0] ):
                            remain_lower100_2_newV[h][1].append((servId,BW)) 
                            ff=1
                    if ff==0:
                       remain_lower100_2_newV.append((Demandid,[(servId,BW)]))
                elif n.TrafficMatrix.DemandDict[Demandid].Source in n.PhysicalTopology.ClusterDict[k].SubNodesId :
                    newdes=n.PhysicalTopology.ClusterDict[k].GatewayId
                    orgdes=n.TrafficMatrix.DemandDict[Demandid].Destination
                    orgsrc=n.TrafficMatrix.DemandDict[Demandid].Source
                    i1=0
                    i2=0
                    for did in n.TrafficMatrix.DemandDict:
                        if n.TrafficMatrix.DemandDict[did].Source == n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Source and n.TrafficMatrix.DemandDict[did].Destination == newdes:
                            n.TrafficMatrix.add_groom_out_10(GroomOutId=servId, Source=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Source, Destination=newdes,DemandId=did,Capacity=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Capacity, ServiceIdList=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].ServiceIdList)
                            ff=0
                            i1=1
                            for h in range(0,len(remain_lower100_2_newV)):
                                if (did == remain_lower100_2_newV[h][0] ):
                                    remain_lower100_2_newV[h][1].append((servId,BW)) 
                                    ff=1
                            if ff==0:
                               remain_lower100_2_newV.append((did,[(servId,BW)]))
                            for sid in n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].ServiceIdList:
                                n.TrafficMatrix.DemandDict[did].add_service(sid,n.TrafficMatrix.DemandDict[Demandid].ServiceDict[sid].Type,2,OriginalSource=orgsrc,OriginalDestination=orgdes)
                        elif n.TrafficMatrix.DemandDict[did].Source == newdes and n.TrafficMatrix.DemandDict[did].Destination == n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Destination:
                            n.TrafficMatrix.add_groom_out_10(GroomOutId=servId, Source=newdes, Destination=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Destination,DemandId=did,Capacity=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Capacity, ServiceIdList=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].ServiceIdList) 
                            ff=0
                            i2=1
                            for h in range(0,len(remain_lower100_2_newV)):
                                if (did == remain_lower100_2_newV[h][0] ):
                                    remain_lower100_2_newV[h][1].append((servId,BW)) 
                                    ff=1
                            if ff==0:
                               remain_lower100_2_newV.append((did,[(servId,BW)]))
                            for sid in n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].ServiceIdList:
                                n.TrafficMatrix.DemandDict[did].add_service(sid,n.TrafficMatrix.DemandDict[Demandid].ServiceDict[sid].Type,2,OriginalSource=orgsrc,OriginalDestination=orgdes)
                    if i1==0:
                       n.TrafficMatrix.add_demand(n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Source,n.PhysicalTopology.ClusterDict[k].GatewayId,"X")
                       LastId = n.TrafficMatrix.Demand.DemandReferenceId - 1
                       n.TrafficMatrix.add_groom_out_10(GroomOutId=servId, Source=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Source, Destination=n.PhysicalTopology.ClusterDict[k].GatewayId,DemandId=LastId,Capacity=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Capacity, ServiceIdList=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].ServiceIdList)
                       remain_lower100_2_newV.append((LastId,[(servId,BW)]))
                       for sid in n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].ServiceIdList:
                           n.TrafficMatrix.DemandDict[LastId].add_service(sid,n.TrafficMatrix.DemandDict[Demandid].ServiceDict[sid].Type,2,OriginalSource=orgsrc,OriginalDestination=orgdes) 
                    if i2==0:
                       n.TrafficMatrix.add_demand(n.PhysicalTopology.ClusterDict[k].GatewayId,n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Destination,"X")
                       LastId = n.TrafficMatrix.Demand.DemandReferenceId - 1
                       n.TrafficMatrix.add_groom_out_10(GroomOutId=servId, Source=n.PhysicalTopology.ClusterDict[k].GatewayId, Destination=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Destination,DemandId=LastId,Capacity=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Capacity, ServiceIdList=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].ServiceIdList)
                       remain_lower100_2_newV.append((LastId,[(servId,BW)]))
                       for sid in n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].ServiceIdList:
                           n.TrafficMatrix.DemandDict[LastId].add_service(sid,n.TrafficMatrix.DemandDict[Demandid].ServiceDict[sid].Type,2,OriginalSource=orgsrc,OriginalDestination=orgdes) 
                    for sid in n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].ServiceIdList:
                        n.TrafficMatrix.DemandDict[Demandid].ServiceDict.pop(sid)
                    n.TrafficMatrix.delete_groom_out_10(servId, Demandid)




        def changing_onlydes_inC_groom10(Demandid,servId,BW): 
           
#            for k in range(1,len(n.PhysicalTopology.ClusterDict)+1):
            for (k,vv) in n.PhysicalTopology.ClusterDict.items():
                if n.TrafficMatrix.DemandDict[Demandid].Destination == n.PhysicalTopology.ClusterDict[k].GatewayId :
                    ff=0
                    for h in range(0,len(remain_lower100_2_newV)):
                        if (Demandid == remain_lower100_2_newV[h][0] ):
                            remain_lower100_2_newV[h][1].append((servId,BW)) 
                            ff=1
                    if ff==0:
                       remain_lower100_2_newV.append((Demandid,[(servId,BW)]))
                elif n.TrafficMatrix.DemandDict[Demandid].Destination in n.PhysicalTopology.ClusterDict[k].SubNodesId :
                    newdes=n.PhysicalTopology.ClusterDict[k].GatewayId
                    orgdes=n.TrafficMatrix.DemandDict[Demandid].Destination
                    orgsrc=n.TrafficMatrix.DemandDict[Demandid].Source
                    i1=0
                    i2=0
                    for did in n.TrafficMatrix.DemandDict:
                        if n.TrafficMatrix.DemandDict[did].Source == n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Source and n.TrafficMatrix.DemandDict[did].Destination == newdes:
                            n.TrafficMatrix.add_groom_out_10(GroomOutId=servId, Source=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Source, Destination=newdes,DemandId=did,Capacity=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Capacity, ServiceIdList=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].ServiceIdList)
                            ff=0
                            i1=1
                            for h in range(0,len(remain_lower100_2_newV)):
                                if (did == remain_lower100_2_newV[h][0] ):
                                    remain_lower100_2_newV[h][1].append((servId,BW)) 
                                    ff=1
                            if ff==0:
                               remain_lower100_2_newV.append((did,[(servId,BW)]))
                            for sid in n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].ServiceIdList:
                                n.TrafficMatrix.DemandDict[did].add_service(sid,n.TrafficMatrix.DemandDict[Demandid].ServiceDict[sid].Type,2,OriginalSource=orgsrc,OriginalDestination=orgdes)
                        elif n.TrafficMatrix.DemandDict[did].Source == newdes and n.TrafficMatrix.DemandDict[did].Destination == n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Destination:
                            n.TrafficMatrix.add_groom_out_10(GroomOutId=servId, Source=newdes, Destination=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Destination,DemandId=did,Capacity=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Capacity, ServiceIdList=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].ServiceIdList) 
                            ff=0
                            i2=1
                            for h in range(0,len(remain_lower100_2_newV)):
                                if (did == remain_lower100_2_newV[h][0] ):
                                    remain_lower100_2_newV[h][1].append((servId,BW)) 
                                    ff=1
                            if ff==0:
                               remain_lower100_2_newV.append((did,[(servId,BW)]))
                            for sid in n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].ServiceIdList:
                                n.TrafficMatrix.DemandDict[did].add_service(sid,n.TrafficMatrix.DemandDict[Demandid].ServiceDict[sid].Type,2,OriginalSource=orgsrc,OriginalDestination=orgdes)
                    if i1==0:
                       n.TrafficMatrix.add_demand(n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Source,n.PhysicalTopology.ClusterDict[k].GatewayId,"X")
                       LastId = n.TrafficMatrix.Demand.DemandReferenceId - 1
                       n.TrafficMatrix.add_groom_out_10(GroomOutId=servId, Source=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Source, Destination=n.PhysicalTopology.ClusterDict[k].GatewayId,DemandId=LastId,Capacity=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Capacity, ServiceIdList=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].ServiceIdList)
                       remain_lower100_2_newV.append((LastId,[(servId,BW)]))
                       for sid in n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].ServiceIdList:
                           n.TrafficMatrix.DemandDict[LastId].add_service(sid,n.TrafficMatrix.DemandDict[Demandid].ServiceDict[sid].Type,2,OriginalSource=orgsrc,OriginalDestination=orgdes) 
                    if i2==0:
                       n.TrafficMatrix.add_demand(n.PhysicalTopology.ClusterDict[k].GatewayId,n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Destination,"X")
                       LastId = n.TrafficMatrix.Demand.DemandReferenceId - 1
                       n.TrafficMatrix.add_groom_out_10(GroomOutId=servId, Source=n.PhysicalTopology.ClusterDict[k].GatewayId, Destination=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Destination,DemandId=LastId,Capacity=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].Capacity, ServiceIdList=n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].ServiceIdList)
                       remain_lower100_2_newV.append((LastId,[(servId,BW)]))
                       for sid in n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].ServiceIdList:
                           n.TrafficMatrix.DemandDict[LastId].add_service(sid,n.TrafficMatrix.DemandDict[Demandid].ServiceDict[sid].Type,2,OriginalSource=orgsrc,OriginalDestination=orgdes) 
                    for sid in n.TrafficMatrix.GroomOut10Dict[(Demandid,servId)].ServiceIdList:
                        n.TrafficMatrix.DemandDict[Demandid].ServiceDict.pop(sid)
                    n.TrafficMatrix.delete_groom_out_10(servId, Demandid)
                           
                           
                           
                           
                  
        id_in_cluster=[]
        for (i,vv) in n.PhysicalTopology.ClusterDict.items():
            id_in_cluster.append(n.PhysicalTopology.ClusterDict[i].GatewayId)
            for j in range(0,len(n.PhysicalTopology.ClusterDict[i].SubNodesId)):
                id_in_cluster.append(n.PhysicalTopology.ClusterDict[i].SubNodesId[j])
#        print(id_in_cluster)
            
        for i in range(0,len(remain_lower100_2)):
            for j in range(0,len(remain_lower100_2[i][1])):
                if remain_lower100_2[i][1][j][0] in n.TrafficMatrix.DemandDict[remain_lower100_2[i][0]].ServiceDict:
                    if n.TrafficMatrix.DemandDict[remain_lower100_2[i][0]].Source in id_in_cluster:
                        if n.TrafficMatrix.DemandDict[remain_lower100_2[i][0]].Destination in id_in_cluster :
                            changing_both_inC(remain_lower100_2[i][0],remain_lower100_2[i][1][j][0],remain_lower100_2[i][1][j][1])
                        else:
                            changing_onlysrc_inC(remain_lower100_2[i][0],remain_lower100_2[i][1][j][0],remain_lower100_2[i][1][j][1])
                    elif n.TrafficMatrix.DemandDict[remain_lower100_2[i][0]].Source not in id_in_cluster:
                        if n.TrafficMatrix.DemandDict[remain_lower100_2[i][0]].Destination in id_in_cluster :
                            changing_onlydes_inC(remain_lower100_2[i][0],remain_lower100_2[i][1][j][0],remain_lower100_2[i][1][j][1])
                        else:
                            ff=0
                            for h in range(0,len(remain_lower100_2_newV)):
                               if (remain_lower100_2[i][0] == remain_lower100_2_newV[h][0] ):
                                   remain_lower100_2_newV[h][1].append((remain_lower100_2[i][1][j][0],remain_lower100_2[i][1][j][1])) 
                                   ff=1
                            if ff==0:
                                remain_lower100_2_newV.append((remain_lower100_2[i][0],[(remain_lower100_2[i][1][j][0],remain_lower100_2[i][1][j][1])]))
                elif (remain_lower100_2[i][0],remain_lower100_2[i][1][j][0]) in n.TrafficMatrix.GroomOut10Dict:
#                    for k in n.TrafficMatrix.GroomOut10Dict[(remain_lower100_2[i][0],remain_lower100_2[i][1][j][0])].ServiceIdList:
                    if n.TrafficMatrix.DemandDict[remain_lower100_2[i][0]].Source in id_in_cluster:
                        if n.TrafficMatrix.DemandDict[remain_lower100_2[i][0]].Destination in id_in_cluster :
                            changing_both_inC_groom10(remain_lower100_2[i][0],remain_lower100_2[i][1][j][0],remain_lower100_2[i][1][j][1])
                        else:
                            changing_onlysrc_inC_groom10(remain_lower100_2[i][0],remain_lower100_2[i][1][j][0],remain_lower100_2[i][1][j][1])
                    elif n.TrafficMatrix.DemandDict[remain_lower100_2[i][0]].Source not in id_in_cluster:
                        if n.TrafficMatrix.DemandDict[remain_lower100_2[i][0]].Destination in id_in_cluster :
                            changing_onlydes_inC_groom10(remain_lower100_2[i][0],remain_lower100_2[i][1][j][0],remain_lower100_2[i][1][j][1])
                        else:
                            ff=0
                            for h in range(0,len(remain_lower100_2_newV)):
                                if (remain_lower100_2[i][0] == remain_lower100_2_newV[h][0] ):
                                    remain_lower100_2_newV[h][1].append((remain_lower100_2[i][1][j][0],remain_lower100_2[i][1][j][1])) 
                                    ff=1
                            if ff==0:
                                remain_lower100_2_newV.append((remain_lower100_2[i][0],[(remain_lower100_2[i][1][j][0],remain_lower100_2[i][1][j][1])]))

            
#        print("**")
#        print(remain_lower100_2_newV)
#        print("**")
#        print(remain_lower100_2)
        
#        remain_lower100_2_newV
#        n.TrafficMatrix.GroomOut10Dict.clear()
#        n.LightPathDict.clear()
        for i in range(0,len(remain_lower100_2_newV)):
            for j in range(0,len(remain_lower100_2_newV[i][1])):
                if (remain_lower100_2_newV[i][0],remain_lower100_2_newV[i][1][j][0]) in n.TrafficMatrix.GroomOut10Dict:
                    n.TrafficMatrix.delete_groom_out_10(remain_lower100_2_newV[i][1][j][0], remain_lower100_2_newV[i][0])

        lll=len(n.LightPathDict)
#        print (groom_out10_list)
        if (len(n.TrafficMatrix.GroomOut10Dict)!=0):
            for i in range(0,len(groom_out10_list)):
                for j in range(0,len(groom_out10_list[i][1])):
                    if (groom_out10_list[i][0],groom_out10_list[i][1][j][0]) in n.TrafficMatrix.GroomOut10Dict:
                        n.TrafficMatrix.delete_groom_out_10(groom_out10_list[i][1][j][0], groom_out10_list[i][0])
                        
        """ for i in range(0,lll+1):
            if len(n.LightPathDict)!=0:
                n.del_lightpath(0) """
        for key in list(n.LightPathDict.keys()):
            n.del_lightpath(key)
        
        

        service_lower10_SDH=[]
        service_lower10_E=[]
        service_lower100=[]
        remain_lower100_2=[]
        remaining_service_lower10=[]
        MP2x_list=[]   
        MP2x_Dict={}                                 #(DemandId,Service)
        output_100=[]
        remain_lower100_dict={}
        remaining_service_lower10_dict={}
        groom_out10_list=[]
        remain_lower100=[]
        print(MP2x_Dict)
        for i in n.TrafficMatrix.DemandDict:
            y=[]
            z=[]
            x=[]
            output_10=[] 
            for j in n.TrafficMatrix.DemandDict[i].ServiceDict:
#                if ((n.TrafficMatrix.DemandDict[i].ServiceDict[j].Type == "STM_1_Optical") or (n.TrafficMatrix.DemandDict[i].ServiceDict[j].Type == "STM_4") or (n.TrafficMatrix.DemandDict[i].ServiceDict[j].Type == "STM_16")):
                if (n.TrafficMatrix.DemandDict[i].ServiceDict[j].BW < 10):
                    y.append((n.TrafficMatrix.DemandDict[i].ServiceDict[j].Id,n.TrafficMatrix.DemandDict[i].ServiceDict[j].BW))
                elif (n.TrafficMatrix.DemandDict[i].ServiceDict[j].BW == 10):
                    z.append((n.TrafficMatrix.DemandDict[i].ServiceDict[j].Id,n.TrafficMatrix.DemandDict[i].ServiceDict[j].BW))
                else:
                    n.add_lightpath(n.TrafficMatrix.DemandDict[i].Source, n.TrafficMatrix.DemandDict[i].Destination, 100, [n.TrafficMatrix.DemandDict[i].ServiceDict[j].Id], "Coherent", i,ClusterNum=0)
                    LastId = n.Lightpath.ReferenceId -1
#                    print(len(n.LightPathDict),"**")
                    n.TrafficMatrix.DemandDict[i].ServiceDict[j].LightPathId=LastId
#                    print(LastId,"***")
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
#                    n.TrafficMatrix.DemandDict[i].add_service(ServiceType= "Groom_out10" ,Sla= 2, Capacity=cap, ServiceIdList=listofs)    
                    GroomOutId = n.TrafficMatrix.Generate_GroomOutId()
                    n.TrafficMatrix.add_groom_out_10(GroomOutId= GroomOutId, Source=n.TrafficMatrix.DemandDict[i].Source, Destination=n.TrafficMatrix.DemandDict[i].Destination, DemandId=i, Capacity=cap, ServiceIdList=listofs)
                    LastId = GroomOutId
                    ffff=[(LastId,10)]
                    hhhh.append((LastId,cap,len(listofs)))
                    z.append((LastId,cap))
#                    service_lower100.append((i,ffff))
                groom_out10_list.append((i,hhhh))
#                print(groom_out10_list)
            if x:
                service_lower10_E.append((i,x))
            
            if z:
                service_lower100.append((i,z))
         
 
#        print(groom_out10_list)
        for i in range(0,len(groom_out10_list)):
            nooo=[]
            for j in range(0,len(groom_out10_list[i][1])):
                
                for k in range(0,len(groom_out10_list[i][1])):
                    if ((k not in nooo) and (j not in nooo) and (j!=k) and (groom_out10_list[i][1][j][2] + groom_out10_list[i][1][k][2]) <=16):
                        MP2x_list.append((groom_out10_list[i][0],(groom_out10_list[i][1][j][0],groom_out10_list[i][1][k][0])))
                        if groom_out10_list[i][0] in MP2x_Dict.keys():
#                            MP2x_Dict.update({groom_out10_list[i][0]:[MP2x_Dict[groom_out10_list[i][0]],(groom_out10_list[i][1][j][0],groom_out10_list[i][1][k][0])]})
                            MP2x_Dict[groom_out10_list[i][0]].append((groom_out10_list[i][1][j][0],groom_out10_list[i][1][k][0]))
                        else:
                            MP2x_Dict.update({groom_out10_list[i][0]:[(groom_out10_list[i][1][j][0],groom_out10_list[i][1][k][0])]})
                        nooo.append(j)
                        nooo.append(k)
                
            for m in range(0,len(groom_out10_list[i][1])):
                if m not in nooo:
                    remaining_service_lower10.append((groom_out10_list[i][0],groom_out10_list[i][1][m][0])) 
                    if groom_out10_list[i][0] in remaining_service_lower10_dict.keys():
                        remaining_service_lower10_dict[groom_out10_list[i][0]].append(groom_out10_list[i][1][m][0])
                    else:
                        remaining_service_lower10_dict.update({groom_out10_list[i][0]:[groom_out10_list[i][1][m][0]]})  
                    
           
        for i in range(0,len(service_lower100)):
            NO_LP= math.ceil(len(service_lower100[i][1])/10)
            orsr=n.TrafficMatrix.DemandDict[service_lower100[i][0]].Source
            ords=n.TrafficMatrix.DemandDict[service_lower100[i][0]].Destination
            cls_num=0
            for k in n.PhysicalTopology.ClusterDict:
                if (n.PhysicalTopology.ClusterDict[k].GatewayId == orsr and  ords in n.PhysicalTopology.ClusterDict[k].SubNodesId) or (n.PhysicalTopology.ClusterDict[k].GatewayId == ords and  orsr in n.PhysicalTopology.ClusterDict[k].SubNodesId) or (ords in n.PhysicalTopology.ClusterDict[k].SubNodesId and ords in n.PhysicalTopology.ClusterDict[k].SubNodesId):
                    cls_num=k
            for j in range(0,NO_LP):
                list_of_service=[]
                list_of_service2=[]
                cap=0
                for k in range(j*10,(j+1)*10):
                    if (k < len(service_lower100[i][1])):
                        list_of_service.append(service_lower100[i][1][k][0])
                        list_of_service2.append((service_lower100[i][1][k][0],service_lower100[i][1][k][1]))
                        cap=cap+service_lower100[i][1][k][1]
                if cap >= MP1H_Threshold:
                    typee="100GE" 
                else:
                    typee="NonCoherent"
                if cap < MP1H_Threshold:
                    remain_lower100.append((service_lower100[i][0],list_of_service))
                    remain_lower100_2.append((service_lower100[i][0],list_of_service2))
                    remain_lower100_dict.update({service_lower100[i][0]:list_of_service})
#                    n.add_lightpath(n.TrafficMatrix.DemandDict[service_lower100[i][0]].Source, n.TrafficMatrix.DemandDict[service_lower100[i][0]].Destination, Capacity=cap, ServiceIdList=list_of_service, Type=typee, DemandId=service_lower100[i][0],ClusterNum=cls_num)    
#                    LastId = n.Lightpath.ReferenceId -1
##                    print(LastId)
#                    for idd in list_of_service:
#                        if idd in n.TrafficMatrix.DemandDict[service_lower100[i][0]].ServiceDict:
#                           n.TrafficMatrix.DemandDict[service_lower100[i][0]].ServiceDict[idd].LightPathId= LastId
#                        if (service_lower100[i][0],idd) in n.TrafficMatrix.GroomOut10Dict:
#                            n.TrafficMatrix.GroomOut10Dict[(service_lower100[i][0],idd)].LightPathId= LastId

                        
                else:
                    n.add_lightpath(n.TrafficMatrix.DemandDict[service_lower100[i][0]].Source, n.TrafficMatrix.DemandDict[service_lower100[i][0]].Destination, Capacity=cap, ServiceIdList=list_of_service, Type=typee, DemandId=service_lower100[i][0],ClusterNum=0)    
                    LastId = n.Lightpath.ReferenceId -1
#                    print(LastId)
                    for idd in list_of_service:
                        if idd in n.TrafficMatrix.DemandDict[service_lower100[i][0]].ServiceDict:
                           n.TrafficMatrix.DemandDict[service_lower100[i][0]].ServiceDict[idd].LightPathId= LastId
                        if (service_lower100[i][0],idd) in n.TrafficMatrix.GroomOut10Dict:
                            n.TrafficMatrix.GroomOut10Dict[(service_lower100[i][0],idd)].LightPathId= LastId
                            for sid in n.TrafficMatrix.GroomOut10Dict[(service_lower100[i][0],idd)].ServiceIdList:
                                n.TrafficMatrix.DemandDict[n.TrafficMatrix.GroomOut10Dict[(service_lower100[i][0],idd)].DemandId].ServiceDict[sid].LightPathId= LastId




        for i in  list(n.TrafficMatrix.DemandDict.keys()):
            if len(n.TrafficMatrix.DemandDict[i].ServiceDict)==0:  
                n.TrafficMatrix.del_demand(i)                











        return n, (remain_lower100_dict,MP2x_Dict,remaining_service_lower10_dict)
        #  remain_lower100            (the services which are not assigned to lightpath)  (DemandId,[ServiceId])
        #  MP2x_list                  (MP2X with 2 output)                               (DemandId,[ServiceId(groomout10),ServiceId(groomout10)])
        #  remaining_service_lower10  (MP2X with 1 output)                               (DemandId,ServiceId(groomout10))
    
    
    
    
    


    


















if __name__ == "__main__":

    with open('NetWorkObj.obj', 'rb') as handle:
        n = pickle.load(handle)                   
    handle.close()

    x = 0
    for key, value in n.TrafficMatrix.DemandDict.items():
        for key1, value1 in value.ServiceDict.items():
            if key1 > x :
                x = key1
    
    n.Traffic.Demand.ServiceIdReference = x
    n.Traffic.Demand.DemandReferenceId = x

    with open('NetworkObj_2.obj', 'rb') as handle:
        n2 = pickle.load(handle)                   
    handle.close()

    x = 0
    for key, value in n2.TrafficMatrix.DemandDict.items():
        for key1, value1 in value.ServiceDict.items():
            if key1 > x :
                x = key1

    n2.Traffic.Demand.ServiceIdReference = x
    n2.Traffic.Demand.DemandReferenceId = x

    
    # to see bug 1 run code bellow
    ans = grooming_fun(n,10)

    # to see bug 2 run code bellow
#    ans = grooming_fun(n2, 0)
    
    #Clustering(n)
    #n.add_groom_out_100(Source=1,Destination=2,Capacity=40,ServiceIdList=[1,2],Type=40,DemandId=3)
    print("successful")
    


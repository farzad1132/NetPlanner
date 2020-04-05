from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import sys
import os
from data import *



class MP2D_panel_L(QWidget):

    def __init__(self,Panel_ID,nodename):

        self.id = Panel_ID
        self.nodename = nodename

        super(MP2D_panel_L, self).__init__()
        self.setFixedSize(109, 810)

        self.label_1 = QLabel(self)
        self.label_1.setPixmap(QPixmap(os.path.join("MP2D_panel", "1.png")))
        self.label_1.setFixedSize(37, 62)
        self.label_1.move(3, 3)

        self.label_2 = QLabel(self)
        self.label_2.setPixmap(QPixmap(os.path.join("MP2D_panel", "2.png")))
        self.label_2.setFixedSize(37, 62)
        self.label_2.move(3, 745)

        self.label_title = QLabel(self)
        self.label_title.setPixmap(QPixmap(os.path.join("MP2D_panel", "mp2d_title.png")))
        self.label_title.setFixedSize(20, 91)
        self.label_title.move(85, 3)

        # self.label_button1 = QLabel(self)
        # self.label_button1.setPixmap(QPixmap(os.path.join("MP2D_panel", "button.png")))
        # self.label_button1.setFixedSize(5, 5)
        # self.label_button1.move(95, 30)
        #
        # self.label_ACT = QLabel(self)
        # self.label_ACT.setPixmap(QPixmap(os.path.join("MP2D_panel", "ACT.png")))
        # self.label_ACT.setFixedSize(15, 7)
        # self.label_ACT.move(72, 30)
        #
        # self.label_button2 = QLabel(self)
        # self.label_button2.setPixmap(QPixmap(os.path.join("MP2D_panel", "button.png")))
        # self.label_button2.setFixedSize(5, 5)
        # self.label_button2.move(95, 42)
        #
        # self.label_FAIL = QLabel(self)
        # self.label_FAIL.setPixmap(QPixmap(os.path.join("MP2D_panel", "FAIL.png")))
        # self.label_FAIL.setFixedSize(15, 6)
        # self.label_FAIL.move(72, 42)
        #
        # self.label_button3 = QLabel(self)
        # self.label_button3.setPixmap(QPixmap(os.path.join("MP2D_panel", "button.png")))
        # self.label_button3.setFixedSize(5, 5)
        # self.label_button3.move(95, 54)
        #
        # self.label_WP = QLabel(self)
        # self.label_WP.setPixmap(QPixmap(os.path.join("MP2D_panel", "wp.png")))
        # self.label_WP.setFixedSize(12, 6)
        # self.label_WP.move(72, 54)

        

        self.label_N1 = QLabel(self)
        self.label_N1.setPixmap(QPixmap(os.path.join("MP2D_panel", "N1.png")))
        self.label_N1.setFixedSize(4, 8)
        self.label_N1.move(30, 340)

        # self.label_ACT1 = QLabel(self)
        # self.label_ACT1.setPixmap(QPixmap(os.path.join("MP2D_panel", "ACT.png")))
        # self.label_ACT1.setFixedSize(15, 7)
        # self.label_ACT1.move(85, 330)
        #
        # self.label_button4 = QLabel(self)
        # self.label_button4.setPixmap(QPixmap(os.path.join("MP2D_panel", "button.png")))
        # self.label_button4.setFixedSize(5, 5)
        # self.label_button4.move(73, 331)
        #
        # self.label_SF1 = QLabel(self)
        # self.label_SF1.setPixmap(QPixmap(os.path.join("MP2D_panel", "SF.png")))
        # self.label_SF1.setFixedSize(8, 7)
        # self.label_SF1.move(85, 342)
        #
        # self.label_button5 = QLabel(self)
        # self.label_button5.setPixmap(QPixmap(os.path.join("MP2D_panel", "button.png")))
        # self.label_button5.setFixedSize(5, 5)
        # self.label_button5.move(73, 343)

        

        self.label_N2 = QLabel(self)
        self.label_N2.setPixmap(QPixmap(os.path.join("MP2D_panel", "N2.png")))
        self.label_N2.setFixedSize(5, 8)
        self.label_N2.move(30, 411)

        # self.label_ACT2 = QLabel(self)
        # self.label_ACT2.setPixmap(QPixmap(os.path.join("MP2D_panel", "ACT.png")))
        # self.label_ACT2.setFixedSize(15, 7)
        # self.label_ACT2.move(85, 395)
        #
        # self.label_button6 = QLabel(self)
        # self.label_button6.setPixmap(QPixmap(os.path.join("MP2D_panel", "button.png")))
        # self.label_button6.setFixedSize(5, 5)
        # self.label_button6.move(73, 396)
        #
        # self.label_SF2 = QLabel(self)
        # self.label_SF2.setPixmap(QPixmap(os.path.join("MP2D_panel", "SF.png")))
        # self.label_SF2.setFixedSize(8, 7)
        # self.label_SF2.move(85, 407)
        #
        # self.label_button7 = QLabel(self)
        # self.label_button7.setPixmap(QPixmap(os.path.join("MP2D_panel", "button.png")))
        # self.label_button7.setFixedSize(5, 5)
        # self.label_button7.move(73, 408)

        self.label_line = QLabel(self)
        self.label_line.setPixmap(QPixmap(os.path.join("MP2D_panel", "line.png")))
        self.label_line.setFixedSize(47, 150)
        self.label_line.move(32, 470)

        self.label_client2 = customlabel(self,self.nodename,self.id,"Client2",self.label_line)
        self.label_client2.setPixmap(QPixmap(os.path.join("MP2D_panel", "client.png")))
        self.label_client2.setFixedSize(36, 61)
        self.label_client2.move(38, 381)

        self.label_client1 = customlabel(self,self.nodename,self.id,"Client",self.label_line)
        self.label_client1.setPixmap(QPixmap(os.path.join("MP2D_panel", "client.png")))
        self.label_client1.setFixedSize(36, 61)
        self.label_client1.move(38, 310)

        # self.label_ACT3 = QLabel(self)
        # self.label_ACT3.setPixmap(QPixmap(os.path.join("MP2D_panel", "ACT.png")))
        # self.label_ACT3.setFixedSize(15, 7)
        # self.label_ACT3.move(85, 527)
        #
        # self.label_button8 = QLabel(self)
        # self.label_button8.setPixmap(QPixmap(os.path.join("MP2D_panel", "button.png")))
        # self.label_button8.setFixedSize(5, 5)
        # self.label_button8.move(73, 528)
        #
        # self.label_SF3 = QLabel(self)
        # self.label_SF3.setPixmap(QPixmap(os.path.join("MP2D_panel", "SF.png")))
        # self.label_SF3.setFixedSize(8, 7)
        # self.label_SF3.move(85, 539)
        #
        # self.label_button9 = QLabel(self)
        # self.label_button9.setPixmap(QPixmap(os.path.join("MP2D_panel", "button.png")))
        # self.label_button9.setFixedSize(5, 5)
        # self.label_button9.move(73, 540)

        self.label_CNS = QLabel(self)
        self.label_CNS.setPixmap(QPixmap(os.path.join("MP2D_panel", "CNS.png")))
        self.label_CNS.setFixedSize(16, 28)
        self.label_CNS.move(32, 627)

        self.label_CNS_title = QLabel(self)
        self.label_CNS_title.setPixmap(QPixmap(os.path.join("MP2D_panel", "CNS_title.png")))
        self.label_CNS_title.setFixedSize(19, 8)
        self.label_CNS_title.move(51, 637)

        # self.label_CH = QLabel(self)
        # self.label_CH.setPixmap(QPixmap(os.path.join("MP2D_panel", "CH.png")))
        # self.label_CH.setFixedSize(47, 31)
        # self.label_CH.move(60, 470)
        #
        # self.label_CH_title = QLabel(self)
        # self.label_CH_title.setPixmap(QPixmap(os.path.join("MP2D_panel", "CH_title.png")))
        # self.label_CH_title.setFixedSize(12, 7)
        # self.label_CH_title.move(60, 460)

        self.setAcceptDrops(True)

    def contextMenuEvent(self, event):
        from BLANK_panel.BLANK_panel import BLANK_panel
        ContextMenu = QMenu(self)
        CloseAction = ContextMenu.addAction("Close Panel")
            
        action = ContextMenu.exec_(self.mapToGlobal(event.pos()))

        if action == CloseAction:
            if len(self.id) == 4:
                    uppernum = str(int(self.id) + 1)
            else:
                panelnum = self.id[2]
                uppanelnum = str(int(panelnum) + 1)
                uppernum = self.id[0] + self.id[1] + uppanelnum

            Data[self.id].setWidget(BLANK_panel(self.id ,  self.nodename))
            Data[uppernum].setWidget(BLANK_panel(self.id ,  self.nodename))
            if Data["Nodes"][self.nodename]["Panels"][self.id]["Sockets"]["Line"] == 2:
                self.countdown_fun(self.nodename,"100GE",2)
                self.modify_linelist(self.nodename,-1)
            if Data["Nodes"][self.nodename]["Panels"][self.id]["Sockets"]["Line"] == 1:
                self.countdown_fun(self.nodename,"100GE",1)

            Data["Nodes"][self.nodename]["Panels"].pop(str(self.id))
            Data["Nodes"][self.nodename]["Panels"].pop(str(uppernum))

    def countdown_fun(self,nodename,header,value):
        degree = self.id[1]
        Data["Nodes"][nodename]["Client_Services"]["data"][degree][header] += value
        Data["ClientList"].clear()
        for service in list(Data["Nodes"][nodename]["Client_Services"]["data"][degree].keys()):
            if Data["Nodes"][nodename]["Client_Services"]["data"][degree][service] !=0 :
                Data["ClientList"].addItem(str(Data["Nodes"][nodename]["Client_Services"]["data"][degree][service])+" * "+service)
    
    def modify_linelist(self,nodename,value):
        degree = self.id[1]
        Data["Nodes"][nodename]["Line_Services"][degree]["2*OTU4"] += value
        Data["LineList"].clear()
        for service in list(Data["Nodes"][nodename]["Line_Services"][degree].keys()):
            if Data["Nodes"][nodename]["Line_Services"][degree][service] != 0:
                Data["LineList"].addItem(str(Data["Nodes"][nodename]["Line_Services"][degree][service]) + " * "+service)

# remember to replace default label with custom label
# 

class customlabel(QLabel):
    def __init__(self,parent,nodename,ID,text,line_var):
        super().__init__(parent)
        self.nodename = nodename
        self.line = line_var
        self.id = ID
        self.text = text
        self.setAcceptDrops(True)
    
    def dragEnterEvent(self, event):
        e = event.mimeData()
        model = QStandardItemModel()
        model.dropMimeData(event.mimeData(), Qt.CopyAction, 0,0, QModelIndex())
        dragtext = model.item(0,0).text()
        print(dragtext)
        servicetype = dragtext.split("*")[1]
        servicetype = servicetype.strip()
        if servicetype == "100GE":
            self.setPixmap(QPixmap(os.path.join("MP2D_panel", "client_green.png")))
            #self.line.setPixmap(self.setPixmap(QPixmap(os.path.join("MP2D_panel", "line_green.png"))))
            
        else:
            self.setPixmap(QPixmap(os.path.join("MP2D_panel", "client_red.png")))
        event.accept()

        super(customlabel,self).dragEnterEvent(event)
    

    def dragLeaveEvent(self, event):
        self.setPixmap(QPixmap(os.path.join("MP2D_panel", "client.png")))

    def dropEvent(self, event):
        event.accept()
        e = event.mimeData()
        model = QStandardItemModel()
        model.dropMimeData(event.mimeData(), Qt.CopyAction, 0,0, QModelIndex())
        dragtext = model.item(0,0).text()
        servicetype = dragtext.split("*")[1]
        servicetype = servicetype.strip()
        if servicetype == "100GE":
            Data["Nodes"][self.nodename]["Panels"][self.id]["Sockets"][self.text] = "green"
            Data["Nodes"][self.nodename]["Panels"][self.id]["Sockets"]["Line"] += 1
            self.countdown_fun(self.nodename,"100GE",-1)
            if Data["Nodes"][self.nodename]["Panels"][self.id]["Sockets"]["Line"] == 2:
                self.modify_linelist(self.nodename,+1)
                # TODO: doing sth with line socket ( changing its color to green )
                Data[self.id].widget().label_line.setPixmap(QPixmap(os.path.join("MP2D_panel", "line_green.png")))

            # TODO: be Careful !!!!!
            self.setAcceptDrops(False)  
        else:
            #Data["Nodes"][self.nodename]["Panels"][self.id]["Sockets"][self.text] = "red"
            self.setPixmap(QPixmap(os.path.join("MP2D_panel", "client.png")))
            # TODO: changing color

    def contextMenuEvent(self, event):
        ContextMenu = QMenu(self)
        ClearAction = ContextMenu.addAction("..Clear Socket..")
        
        action = ContextMenu.exec_(self.mapToGlobal(event.pos()))

        if action == ClearAction:
            if Data["Nodes"][self.nodename]["Panels"][self.id]["Sockets"][self.text] == "green":
                self.setPixmap(QPixmap(os.path.join("MP2D_panel", "client.png")))
                Data["Nodes"][self.nodename]["Panels"][self.id]["Sockets"][self.text] = None
                Data["Nodes"][self.nodename]["Panels"][self.id]["Sockets"]["Line"] -= 1
                self.countdown_fun(self.nodename,"100GE",1)
                self.setAcceptDrops(True)
                if Data["Nodes"][self.nodename]["Panels"][self.id]["Sockets"]["Line"] == 1:
                    self.modify_linelist(self.nodename,-1)
                    # TODO: doing sth with line socket ( changing its color to default )
                    Data[self.id].widget().label_line.setPixmap(QPixmap(os.path.join("MP2D_panel", "line.png")))
                    

            elif Data["Nodes"][self.nodename]["Panels"][self.id]["Sockets"][self.text] == "red":
                Data["Nodes"][self.nodename]["Panels"][self.id]["Sockets"][self.text] = None
                self.setPixmap(QPixmap(os.path.join("MP2D_panel", "client.png")))

    def countdown_fun(self,nodename,header,value):
        degree = self.id[1]
        Data["Nodes"][nodename]["Client_Services"]["data"][degree][header] += value
        Data["ClientList"].clear()
        for service in list(Data["Nodes"][nodename]["Client_Services"]["data"][degree].keys()):
            if Data["Nodes"][nodename]["Client_Services"]["data"][degree][service] !=0 :
                Data["ClientList"].addItem(str(Data["Nodes"][nodename]["Client_Services"]["data"][degree][service])+" * "+service)
    
    def modify_linelist(self,nodename,value):
        degree = self.id[1]
        Data["Nodes"][nodename]["Line_Services"][degree]["2*OTU4"] += value
        Data["LineList"].clear()
        for service in list(Data["Nodes"][nodename]["Line_Services"][degree].keys()):
            if Data["Nodes"][nodename]["Line_Services"][degree][service] != 0:
                Data["LineList"].addItem(str(Data["Nodes"][nodename]["Line_Services"][degree][service]) + " * "+service)
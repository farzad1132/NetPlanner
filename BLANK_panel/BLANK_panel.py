from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import sys
import os
from Node_View_Data import Panel_Data
from data import Data
from SC_panel_final.SC_panel import SC_panel
from BAF3_panel.BAF3_panel import BAF3_panel
from LAF3_panel.LAF3_panel import LAF3_panel
from PAF3_panel.PAF3_panel import PAF3_panel
from MP2X_panel.MP2X_panel import MP2X_panel
from MP2D_panel.MP2D_panel_L import MP2D_panel_L
from MP2D_panel.MP2D_panel_R import MP2D_panel_R
from TP2X_panel.TP2X_panel import TP2X_panel


class BLANK_panel(QWidget):

    def __init__(self,Panel_ID,nodename):

        super(BLANK_panel, self).__init__()
        self.id = str(Panel_ID)
        self.nodename = nodename
        width = 109
        height = 810

        self.setMinimumSize(width,height)


        self.label_BLANK = QLabel(self)
        self.label_BLANK.setPixmap(QPixmap(os.path.join("BLANK_panel", "BLANK.png")))
        self.label_BLANK.setFixedSize(98, 810)
        self.label_BLANK.move(0, 0)

        self.setStyleSheet("border: 3px solid black")

        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        
        #TODO: update this
        DoublePanels = ["MP2D","MP2X","TPAX","MPBD","MPAD","RG1H"]

        model = QStandardItemModel()
        model.dropMimeData(event.mimeData(), Qt.CopyAction, 0,0, QModelIndex())
        text = model.item(0,0).text()

        if DoublePanels.count(text) != 0:
            if len(self.id) == 4:
                uppernum = str(int(self.id) + 1)
            else:
                panelnum = self.id[2]
                uppanelnum = str(int(panelnum) + 1)
                uppernum = self.id[0] + self.id[1] + uppanelnum


            if Data["Nodes"][self.nodename]["Panels"].get(uppernum,0) == 0:
                event.accept()
        else:
            event.accept()

        
        super(BLANK_panel,self).dragEnterEvent(event)

    def dragMoveEvent(self, event):
        event.accept()
        super(BLANK_panel,self).dragMoveEvent(event)

    def dropEvent(self, event):
        event.accept()
        model = QStandardItemModel()
        model.dropMimeData(event.mimeData(), Qt.CopyAction, 0,0, QModelIndex())
        text = model.item(0,0).text()
        #self.label.setText(text)

        # TODO: Take Care of this very soon

        if text == "SC":
            Panel_Data[self.id].setWidget(SC_panel(self.id,self.nodename))
            Data["Nodes"][self.nodename]["Panels"][str(self.id)] = {"Name":"SC"}
        elif text == "BAF3":
            Panel_Data[self.id].setWidget(BAF3_panel(self.id,self.nodename))
            Data["Nodes"][self.nodename]["Panels"][str(self.id)] =  {"Name":"BAF3"}
        elif text == "LAF3":
            Panel_Data[self.id].setWidget(LAF3_panel(self.id,self.nodename))
            Data["Nodes"][self.nodename]["Panels"][str(self.id)] = {"Name":"LAF3"}
        elif text == "PAF3":
            Panel_Data[self.id].setWidget(PAF3_panel(self.id,self.nodename))
            Data["Nodes"][self.nodename]["Panels"][str(self.id)] = {"Name":"PAF3"}
        elif text == "MP2X":
            Panel_Data[self.id].setWidget(MP2X_panel(self.id,self.nodename))
            Data["Nodes"][self.nodename]["Panels"][str(self.id)] =  {"Name":"MP2X"}
        elif text == "MP2D":
            
            Panel_Data[self.id].setWidget(MP2D_panel_L(self.id,self.nodename))
            Data["Nodes"][self.nodename]["Panels"][str(self.id)] = {"Name":"MP2D","Position":"L","Sockets":{"Client1":None,"Client2":None,"Line":0}}
            if len(self.id) == 4:
                uppernum = str(int(self.id) + 1)
            else:
                panelnum = self.id[2]
                uppanelnum = str(int(panelnum) + 1)
                uppernum = self.id[0] + self.id[1] + uppanelnum

            Panel_Data[uppernum].setWidget(MP2D_panel_R(self.id,self.nodename))
            Data["Nodes"][self.nodename]["Panels"][uppernum] = {"Name":"MP2D","Position":"R"}

            # change above format into bellow format


            '''Data["Nodes"][self.nodename]["Panels"][str(self.id)] = {}
            dic = {}
            dic.update(MP2D)
            Data["Nodes"][self.nodename]["Panels"][str(self.id)].update(dic)'''

        elif text == "TP2X":
            Panel_Data[self.id].setWidget(TP2X_panel(self.id,self.nodename))
            Data["Nodes"][self.nodename]["Panels"][str(self.id)] = {"Name":"TP2X"} # this is uncompleted
        
        super(BLANK_panel,self).dropEvent(event)


from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import sys
import os
from Node_View_Data import Panel_Data
from data import Data


class SC_panel(QWidget):

    def __init__(self,Panel_ID,nodename):

        super(SC_panel, self).__init__()
        self.id = str(Panel_ID)
        self.nodename = nodename
        self.setFixedSize(109, 810)

        self.label_SC_1 = QLabel(self)
        self.label_SC_1.setPixmap(QPixmap(os.path.join("SC_panel_final","SC_1.png")))
        self.label_SC_1.setFixedSize(36, 61)
        self.label_SC_1.move(3, 3)

        self.label_SC_2 = QLabel(self)
        self.label_SC_2.setPixmap(QPixmap(os.path.join("SC_panel_final","SC_2.png")))
        self.label_SC_2.setFixedSize(36, 61)
        self.label_SC_2.move(3, 747)

        self.label_SC_title = QLabel(self)
        self.label_SC_title.setPixmap(QPixmap(os.path.join("SC_panel_final","SC_title.png")))
        self.label_SC_title.setFixedSize(12, 43)
        self.label_SC_title.move(90, 13)

        self.label_SC_ACT = QLabel(self)
        self.label_SC_ACT.setPixmap(QPixmap(os.path.join("SC_panel_final","SC_ACT.png")))
        self.label_SC_ACT.setFixedSize(34, 12)
        self.label_SC_ACT.move(55, 100)

        self.label_SC_FAIL = QLabel(self)
        self.label_SC_FAIL.setPixmap(QPixmap(os.path.join("SC_panel_final","SC_FAIL.png")))
        self.label_SC_FAIL.setFixedSize(34, 12)
        self.label_SC_FAIL.move(55, 120)

        self.label_SC_CRIT = QLabel(self)
        self.label_SC_CRIT.setPixmap(QPixmap(os.path.join("SC_panel_final","SC_CRIT.png")))
        self.label_SC_CRIT.setFixedSize(35, 12)
        self.label_SC_CRIT.move(55, 140)

        self.label_SC_MAJ = QLabel(self)
        self.label_SC_MAJ.setPixmap(QPixmap(os.path.join("SC_panel_final","SC_MAJ.png")))
        self.label_SC_MAJ.setFixedSize(35, 11)
        self.label_SC_MAJ.move(55, 160)

        self.label_SC_MIN = QLabel(self)
        self.label_SC_MIN.setPixmap(QPixmap(os.path.join("SC_panel_final","SC_MIN.png")))
        self.label_SC_MIN.setFixedSize(35, 11)
        self.label_SC_MIN.move(55, 180)

        self.label_SC_INTER = QLabel(self)
        self.label_SC_INTER.setPixmap(QPixmap(os.path.join("SC_panel_final","SC_INTER.png")))
        self.label_SC_INTER.setFixedSize(43, 11)
        self.label_SC_INTER.move(55, 200)

        self.label_SC_INTRA = QLabel(self)
        self.label_SC_INTRA.setPixmap(QPixmap(os.path.join("SC_panel_final","SC_INTRA.png")))
        self.label_SC_INTRA.setFixedSize(45, 11)
        self.label_SC_INTRA.move(55, 220)

        self.label_SC_CNS = QLabel(self)
        self.label_SC_CNS.setPixmap(QPixmap(os.path.join("SC_panel_final","SC_CNS.png")))
        self.label_SC_CNS.setFixedSize(20, 8)
        self.label_SC_CNS.move(19, 95)

        self.label_SC_CNS_BT = QLabel(self)
        self.label_SC_CNS_BT.setPixmap(QPixmap(os.path.join("SC_panel_final","SC_CNS_BT.png")))
        self.label_SC_CNS_BT.setFixedSize(17, 30)
        self.label_SC_CNS_BT.move(20, 110)

        self.label_SC_RST = QLabel(self)
        self.label_SC_RST.setPixmap(QPixmap(os.path.join("SC_panel_final","SC_RST.png")))
        self.label_SC_RST.setFixedSize(32, 12)
        self.label_SC_RST.move(55, 350)

        self.label_SC_LEDT = QLabel(self)
        self.label_SC_LEDT.setPixmap(QPixmap(os.path.join("SC_panel_final","SC_LEDT.png")))
        self.label_SC_LEDT.setFixedSize(38, 12)
        self.label_SC_LEDT.move(55, 420)

        self.label_SC_ACO = QLabel(self)
        self.label_SC_ACO.setPixmap(QPixmap(os.path.join("SC_panel_final","SC_ACO.png")))
        self.label_SC_ACO.setFixedSize(37, 12)
        self.label_SC_ACO.move(55, 490)


        self.setAcceptDrops(True)

    def contextMenuEvent(self, event):
        from BLANK_panel.BLANK_panel import BLANK_panel
        ContextMenu = QMenu(self)
        CloseAction = ContextMenu.addAction("Close Panel")
        
        action = ContextMenu.exec_(self.mapToGlobal(event.pos()))

        if action == CloseAction:
            Panel_Data[self.id].setWidget(BLANK_panel(self.id ,  self.nodename))

        Data["Nodes"][self.nodename]["Panels"].pop(str(self.id))




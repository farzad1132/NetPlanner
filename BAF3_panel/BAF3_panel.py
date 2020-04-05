from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import sys
import os
from Node_View_Data import Panel_Data
from data import Data

class BAF3_panel(QWidget):

    def __init__(self,Panel_ID,nodename):

        super(BAF3_panel, self).__init__()
        self.id = str(Panel_ID)
        self.nodename = nodename
        self.setMinimumSize(109, 810)
        self.label_BAF3_1 = QLabel(self)
        self.label_BAF3_1.setPixmap(QPixmap(os.path.join("BAF3_panel","BAF3_1.png")))
        self.label_BAF3_1.setFixedSize(37, 61)
        self.label_BAF3_1.move(3, 3)

        self.label_BAF3_2 = QLabel(self)
        self.label_BAF3_2.setPixmap(QPixmap(os.path.join("BAF3_panel","BAF3_2.png")))
        self.label_BAF3_2.setFixedSize(37, 60)
        self.label_BAF3_2.move(3, 747)

        self.label_BAF3_title = QLabel(self)
        self.label_BAF3_title.setPixmap(QPixmap(os.path.join("BAF3_panel","BAF3_title.png")))
        self.label_BAF3_title.setFixedSize(17, 96)
        self.label_BAF3_title.move(82, 5)

        self.label_BAF3_ACT = QLabel(self)
        self.label_BAF3_ACT.setPixmap(QPixmap(os.path.join("BAF3_panel","BAF3_ACT.png")))
        self.label_BAF3_ACT.setFixedSize(20, 19)
        self.label_BAF3_ACT.move(63, 128)

        self.label_BAF3_FAIL = QLabel(self)
        self.label_BAF3_FAIL.setPixmap(QPixmap(os.path.join("BAF3_panel","BAF3_FAIL.png")))
        self.label_BAF3_FAIL.setFixedSize(20, 8)
        self.label_BAF3_FAIL.move(63, 150)

        self.label_BAF3_SF = QLabel(self)
        self.label_BAF3_SF.setPixmap(QPixmap(os.path.join("BAF3_panel","BAF3_SF.png")))
        self.label_BAF3_SF.setFixedSize(10, 9)
        self.label_BAF3_SF.move(63, 167)

        self.label_BAF3_CNS = QLabel(self)
        self.label_BAF3_CNS.setPixmap(QPixmap(os.path.join("BAF3_panel","BAF3_CNS.png")))
        self.label_BAF3_CNS.setFixedSize(16, 28)
        self.label_BAF3_CNS.move(20, 140)

        self.label_BAF3_CNS_title = QLabel(self)
        self.label_BAF3_CNS_title.setPixmap(QPixmap(os.path.join("BAF3_panel","BAF3_CNS_title.png")))
        self.label_BAF3_CNS_title.setFixedSize(19, 8)
        self.label_BAF3_CNS_title.move(18, 131)

        self.label_BAF3_button1 = QLabel(self)
        self.label_BAF3_button1.setPixmap(QPixmap(os.path.join("BAF3_panel","BAF3_button.png")))
        self.label_BAF3_button1.setFixedSize(12, 12)
        self.label_BAF3_button1.move(48, 132)

        self.label_BAF3_button2 = QLabel(self)
        self.label_BAF3_button2.setPixmap(QPixmap(os.path.join("BAF3_panel","BAF3_button.png")))
        self.label_BAF3_button2.setFixedSize(12, 12)
        self.label_BAF3_button2.move(48, 149)

        self.label_BAF3_button3 = QLabel(self)
        self.label_BAF3_button3.setPixmap(QPixmap(os.path.join("BAF3_panel","BAF3_button.png")))
        self.label_BAF3_button3.setFixedSize(12, 12)
        self.label_BAF3_button3.move(48, 166)

        self.label_BAF3_S_IN_title = QLabel(self)
        self.label_BAF3_S_IN_title.setPixmap(QPixmap(os.path.join("BAF3_panel","BAF3_S_IN_title.png")))
        self.label_BAF3_S_IN_title.setFixedSize(19, 8)
        self.label_BAF3_S_IN_title.move(23, 331)

        self.label_BAF3_S_IN = QLabel(self)
        self.label_BAF3_S_IN.setPixmap(QPixmap(os.path.join("BAF3_panel","BAF3_S_IN.png")))
        self.label_BAF3_S_IN.setFixedSize(35, 24)
        self.label_BAF3_S_IN.move(18, 341)

        self.label_BAF3_OSC_IN_title = QLabel(self)
        self.label_BAF3_OSC_IN_title.setPixmap(QPixmap(os.path.join("BAF3_panel","BAF3_OSC_IN_title.png")))
        self.label_BAF3_OSC_IN_title.setFixedSize(34, 9)
        self.label_BAF3_OSC_IN_title.move(19, 391)

        self.label_BAF3_OSC_IN = QLabel(self)
        self.label_BAF3_OSC_IN.setPixmap(QPixmap(os.path.join("BAF3_panel","BAF3_OSC_IN.png")))
        self.label_BAF3_OSC_IN.setFixedSize(35, 24)
        self.label_BAF3_OSC_IN.move(18, 365)

        self.label_BAF3_S_OUT_title = QLabel(self)
        self.label_BAF3_S_OUT_title.setPixmap(QPixmap(os.path.join("BAF3_panel","BAF3_S_OUT_title.png")))
        self.label_BAF3_S_OUT_title.setFixedSize(30, 8)
        self.label_BAF3_S_OUT_title.move(22, 487)

        self.label_BAF3_S_OUT = QLabel(self)
        self.label_BAF3_S_OUT.setPixmap(QPixmap(os.path.join("BAF3_panel","BAF3_S_OUT.png")))
        self.label_BAF3_S_OUT.setFixedSize(35, 24)
        self.label_BAF3_S_OUT.move(18, 461)

        self.label_BAF3_MON_title = QLabel(self)
        self.label_BAF3_MON_title.setPixmap(QPixmap(os.path.join("BAF3_panel","BAF3_MON_title.png")))
        self.label_BAF3_MON_title.setFixedSize(25, 8)
        self.label_BAF3_MON_title.move(22, 427)

        self.label_BAF3_MON = QLabel(self)
        self.label_BAF3_MON.setPixmap(QPixmap(os.path.join("BAF3_panel","BAF3_MON.png")))
        self.label_BAF3_MON.setFixedSize(35, 24)
        self.label_BAF3_MON.move(18, 437)

        self.setAcceptDrops(True)

    def contextMenuEvent(self, event):
        from BLANK_panel.BLANK_panel import BLANK_panel
        ContextMenu = QMenu(self)
        CloseAction = ContextMenu.addAction("Close Panel")
        
        action = ContextMenu.exec_(self.mapToGlobal(event.pos()))

        if action == CloseAction:
            Panel_Data[self.id].setWidget(BLANK_panel(self.id,self.nodename))
            Data["Nodes"][self.nodename]["Panels"].pop(str(self.id))

    
            
if __name__ == "__main__":
    app = QApplication([])
    window = BAF3_panel(111)
    window.show()

    sys.exit(app.exec_())




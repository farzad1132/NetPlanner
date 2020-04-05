from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import sys
import os
from Node_View_Data import Panel_Data
from SC_panel_final.SC_panel import SC_panel
from BAF3_panel.BAF3_panel import BAF3_panel
from LAF3_panel.LAF3_panel import LAF3_panel
from PAF3_panel.PAF3_panel import PAF3_panel
from MP2X_panel.MP2X_panel import MP2X_panel


class BLANK_panel(QWidget):

    def __init__(self,Panel_ID):

        super(BLANK_panel, self).__init__()
        self.id = str(Panel_ID)
        width = int (Panel_Data["width"] / 17.6 )
        height = int(Panel_Data["height"] / 1.235)

        self.setMinimumSize(width,height)


        self.label_BLANK = QLabel(self)
        self.label_BLANK.setPixmap(QPixmap(os.path.join("BLANK_panel", "BLANK.png")))
        self.label_BLANK.setFixedSize(98, 810)
        self.label_BLANK.move(0, 0)

        self.setAcceptDrops(True)
    def dragEnterEvent(self, event):
        event.accept()
        super(paneldemo,self).dragEnterEvent(event)

    def dragMoveEvent(self, event):
        event.accept()
        super(paneldemo,self).dragMoveEvent(event)

    def dropEvent(self, event):
        event.accept()
        model = QStandardItemModel()
        model.dropMimeData(event.mimeData(), Qt.CopyAction, 0,0, QModelIndex())
        text = model.item(0,0).text()
        #self.label.setText(text)

        # TODO: Take Care of this very soon

        if text == "SC":
            Panel_Data[self.id].setWidget(SC_panel(self.id))
        elif text == "BAF3":
            Panel_Data[self.id].setWidget(BAF3_panel(self.id))
        elif text == "LAF3":
            Panel_Data[self.id].setWidget(LAF3_panel(self.id))
        elif text == "PAF3":
            Panel_Data[self.id].setWidget(PAF3_panel(self.id))
        elif text == "MP2X":
            Panel_Data[self.id].setWidget(MP2X_panel(self.id))
        super(paneldemo,self).dropEvent(event)


if __name__ == "__main__":

    app = QApplication([])
    window = BLANK_panel()
    window.show()
    sys.exit(app.exec_())



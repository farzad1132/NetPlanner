from PySide2.QtWidgets import QTableWidget, QMenu

class Custom_table(QTableWidget):
    def __init__(self, parent):
        super().__init__(parent)
    
    def contextMenuEvent(self, event):
        gp = event.globalPos()
        menu = QMenu(self)
        delete_act = menu.addAction("Delete This Row")
        action = menu.exec_(gp)
        vp_pos = self.viewport().mapFromGlobal(gp)
        row = self.rowAt(vp_pos.y())

        if action == delete_act:
            print(row + 1)
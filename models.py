from PySide2.QtWidgets import QTableWidget, QMenu
from data import Data

class Custom_table(QTableWidget):
    def __init__(self, parent, Name):
        super().__init__(parent)
        self.Name = Name
    
    def contextMenuEvent(self, event):
        gp = event.globalPos()
        menu = QMenu(self)
        delete_act = menu.addAction("Delete This Row")
        action = menu.exec_(gp)
        vp_pos = self.viewport().mapFromGlobal(gp)
        row = self.rowAt(vp_pos.y())

        if action == delete_act:
            print(f"row with id =  {Data['General']['DataSection']['0'][row]} deleted")
            for i in range(9):
                if row in Data["General"]["DataSection"][str(i)]:
                    Data["General"]["DataSection"][str(i)].pop(row)
            
            for service in Data["ui"].all_headers:
                for header in Data[service]["Headers"]:
                    header = header.strip()
                    if row in Data[service]["DataSection"][header]:
                        Data[service]["DataSection"][header].pop(row)

            self.removeRow(row)

            if self.Name == "GTM":
                Data["ui"].Traffic_matrix.removeRow(row)
            else:
                Data["ui"].General_TM.removeRow(row)

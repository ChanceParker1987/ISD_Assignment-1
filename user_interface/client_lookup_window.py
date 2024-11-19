from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
from PySide6.QtCore import Qt

from ui_superclasses.lookup_window import LookupWindow
from user_interface.account_details_window import AccountDetailsWindow
from user_interface.manage_data import load_data
from user_interface.manage_data import update_data
from bank_account.bank_account import BankAccount

class ClientLookupWindow(LookupWindow):
    pass
        
"""
self.client_number_edit.textChanged.connect(self.__on_text_changed)
  
    @Slot()
    def __on_text_changed(self):
        self.account_table.setRowCount(0)
"""
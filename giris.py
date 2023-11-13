import sys
from tinydb import TinyDB, Query
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QComboBox, QTableWidgetItem
from girisUi import Ui_Form
from main import MyMainWindow

class sign(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.db = TinyDB("giris.json")
        self.setupUi(self)
        self.giris.clicked.connect(self.sign_in)
        self.kayit.clicked.connect(self.register)

    def sign_in(self, item):
        sirketAdi = self.sirketAdiLine.text()
        Sifre = self.sifreLine.text()
        check = self.db.get((Query().Sifre == Sifre) & (Query().sirketadi == sirketAdi))
        if check:
            self.window = QtWidgets.QMainWindow()
            self.ui = MyMainWindow()
            self.ui.setupUi(self.window)
            self.window.show()
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid company name or password")
    
    def register(self):
        sirket_adi = self.sirketAdiLine.text()
        sifre = self.sifreLine.text()
        self.db.insert({
            "sirketadi": sirket_adi,
            "Sifre": sifre
        })
        QMessageBox.information(self, "sucess", "Your registeration was completed")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = sign()
    window.show()
    sys.exit(app.exec_())
import sys
from tinydb import TinyDB, Query
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QComboBox, QTableWidgetItem, QListWidgetItem
from ui import Ui_Form

class MyMainWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.db = TinyDB("data.json")
        #self.girisdb = TinyDB("giris.json")
        self.userQuery = Query()
        self.Ekle.clicked.connect(self.inputs)
        self.Olustur.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page))
        self.Liste.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))
        self.tabloGorumumbtn.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.tabloGorunum))
        self.tabloGorumumbtn.clicked.connect(self.showTable)
        self.listeGorumumbtn.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.listeGorunum))
        self.listeGorumumbtn.clicked.connect(self.loadList)
        self.listWidget.itemClicked.connect(self.clickList)
        self.tableWidget.itemClicked.connect(self.clickTable)
        self.silbtn.clicked.connect(self.deleteItem)
        self.aramaLine.textChanged.connect(self.search)
        
        #self.toplamGiris = 3
        #self.mevcutGiris = self.girisdb.count(self.userQuery.islem == "giris")
        #if self.mevcutGiris < self.toplamGiris:
            #QMessageBox.warning(self, "toplam giriş hakkı", f"{self.toplamGiris - self.mevcutGiris} giriş hakkınız kaldı.")
            #self.girisdb.insert({"islem": "giris"})
        #else:
            #QMessageBox.warning(self, "Giriş hakkı", "Toplam giriş hakkınız dolmuştur, Veriler siliniyor...")
            #self.db.truncate()
            #self.girisdb.truncate()
        
    
    def inputs(self):
        stok_kodu = self.lineEdit.text()
        stok_adi = self.lineEdit_2.text()
        raf_no = self.lineEdit_3.text()
        alt_raf_no = self.lineEdit_4.text()
        min_stok = self.lineEdit_5.text()
        max_stok = self.lineEdit_6.text()
        stok_grubu = self.comboBox.currentText()
        stok_tipi = self.comboBox_2.currentText()
        
        self.db.insert({
            "Stok_Kodu": stok_kodu,
            "Stok_Adi": stok_adi,
            "Raf_No": raf_no,
            "Alt_Raf_No": alt_raf_no,
            "Minimum_Stok": min_stok,
            "Maximum_Stok": max_stok,
            "Stok_Grubu": stok_grubu,
            "Stok_Tipi": stok_tipi
        })
    
    def loadList(self):
        self.listWidget.clear()
        inList = self.db.all()
        for List in inList:
            self.listWidget.addItem(List["Stok_Adi"])

        font = self.listWidget.font()
        font.setPointSize(20)  # Change the number to adjust font size
        self.listWidget.setFont(font)
    def clickList(self, item):
        secilen_isim = item.text()
        materyal = self.db.get(Query().Stok_Adi == secilen_isim)
        if materyal:
            self.lineEdit_7.setText(materyal["Stok_Kodu"])
            self.lineEdit_8.setText(materyal["Stok_Adi"])
            self.lineEdit_9.setText(materyal["Raf_No"])
            self.lineEdit_10.setText(materyal["Alt_Raf_No"])
            self.lineEdit_11.setText(materyal["Minimum_Stok"])
            self.lineEdit_12.setText(materyal["Maximum_Stok"])
            self.comboBox_4.setCurrentText(materyal["Stok_Grubu"])
            self.comboBox_3.setCurrentText(materyal["Stok_Tipi"])
        else:
            QMessageBox.warning(self, "Öğe bulunamadı", f"{secilen_isim} Bulunamadı")

    def showTable(self):
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
        inList = self.db.all()
        for row, data in enumerate(inList):
            self.tableWidget.insertRow(row)
            for col, value in enumerate(data.values()):
                item = QTableWidgetItem(str(value))
                self.tableWidget.setItem(row, col, item)

    def clickTable(self, item):
        row = item.row()
        stok_adi = self.tableWidget.item(row, 1).text()
        materyal = self.db.get(Query().Stok_Adi == stok_adi)
        if materyal:
            self.lineEdit_7.setText(materyal["Stok_Kodu"])
            self.lineEdit_8.setText(materyal["Stok_Adi"])
            self.lineEdit_9.setText(materyal["Raf_No"])
            self.lineEdit_10.setText(materyal["Alt_Raf_No"])
            self.lineEdit_11.setText(materyal["Minimum_Stok"])
            self.lineEdit_12.setText(materyal["Maximum_Stok"])
            self.comboBox_4.setCurrentText(materyal["Stok_Grubu"])
            self.comboBox_3.setCurrentText(materyal["Stok_Tipi"])
        else:
            QMessageBox.warning(self, "Öğe bulunamadı", f"{stok_adi} Bulunamadı")

    def deleteItem(self):
        current_row = self.tableWidget.currentRow()
        current_item = self.listWidget.currentItem()
        if current_row != -1:
            stok_adi = self.tableWidget.item(current_row, 1).text()
            materyal = self.db.get(Query().Stok_Adi == stok_adi)
            if materyal:
                self.db.remove(doc_ids=[materyal.doc_id])
            else:
                QMessageBox.warning(self, "Öğe bulunamadı", f"{stok_adi} Bulunamadı")
        
        elif current_item:
            stok_adi = current_item.text()
            materyal = self.db.get(Query().Stok_Adi == stok_adi)

            if materyal:
                self.db.remove(doc_ids=[materyal.doc_id])
                
            else:
                QMessageBox.warning(self, "Öğe bulunamadı", f"{stok_adi} Bulunamadı")
        else:
            QMessageBox.warning(self, "Öğe seçilmedi", "Lütfen silinecek öğeyi seçin")
    def search(self):
        keyword = self.aramaLine.text().strip()
        if keyword:
            results = self.db.search(
                (Query().Stok_Kodu.search(keyword)) |
                (Query().Stok_Adi.search(keyword)) |
                (Query().Raf_No.search(keyword)) |
                (Query().Alt_Raf_No.search(keyword)) |
                (Query().Stok_Grubu.search(keyword)) |
                (Query().Stok_Tipi.search(keyword))
            )
            self.showSearchResults(results)
        else:
            self.showTable()

    def showSearchResults(self, results):
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
        self.listWidget.clear()

        for row, data in enumerate(results):
            self.tableWidget.insertRow(row)
            for col, value in enumerate(data.values()):
                item = QTableWidgetItem(str(value))
                self.tableWidget.setItem(row, col, item)
        for data in results:
            list_item = QListWidgetItem(data["Stok_Adi"])
            self.listWidget.addItem(list_item)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())

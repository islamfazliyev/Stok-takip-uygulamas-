# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'giris.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 436)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 411))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.sirketAdi = QtWidgets.QLabel(self.frame)
        self.sirketAdi.setGeometry(QtCore.QRect(150, 20, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sirketAdi.setFont(font)
        self.sirketAdi.setAlignment(QtCore.Qt.AlignCenter)
        self.sirketAdi.setObjectName("sirketAdi")
        self.giris = QtWidgets.QPushButton(self.frame)
        self.giris.setGeometry(QtCore.QRect(140, 180, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.giris.setFont(font)
        self.giris.setToolTipDuration(1)
        self.giris.setObjectName("giris")
        self.sirketAdiLine = QtWidgets.QLineEdit(self.frame)
        self.sirketAdiLine.setGeometry(QtCore.QRect(50, 50, 301, 31))
        self.sirketAdiLine.setObjectName("sirketAdiLine")
        self.sifre = QtWidgets.QLabel(self.frame)
        self.sifre.setGeometry(QtCore.QRect(150, 90, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sifre.setFont(font)
        self.sifre.setAlignment(QtCore.Qt.AlignCenter)
        self.sifre.setObjectName("sifre")
        self.sifreLine = QtWidgets.QLineEdit(self.frame)
        self.sifreLine.setGeometry(QtCore.QRect(50, 120, 301, 31))
        self.sifreLine.setObjectName("sifreLine")
        self.kayit = QtWidgets.QPushButton(self.frame)
        self.kayit.setGeometry(QtCore.QRect(140, 240, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.kayit.setFont(font)
        self.kayit.setToolTipDuration(1)
        self.kayit.setObjectName("kayit")
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.sirketAdi.setText(_translate("Form", "Şirket Adı:"))
        self.giris.setText(_translate("Form", "Giriş Yap"))
        self.sifre.setText(_translate("Form", "Şifre:"))
        self.kayit.setText(_translate("Form", "Kaydol"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

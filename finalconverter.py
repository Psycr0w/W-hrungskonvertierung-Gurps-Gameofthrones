# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\converter.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import argparse
import math

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(424, 254)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 40, 261, 41))
        self.textEdit.setObjectName("textEdit")

        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(283, 50, 55, 17))
        self.radioButton.setObjectName("radioButton")

        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(9, 92, 410, 121))
        self.textEdit_2.setObjectName("textEdit_2")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(344, 47, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(clicked)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 424, 21))
        self.menubar.setObjectName("menubar")

        self.menuW_hrungskonvertierung = QtWidgets.QMenu(self.menubar)
        self.menuW_hrungskonvertierung.setObjectName("menuW_hrungskonvertierung")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuW_hrungskonvertierung.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.radioButton.setText(_translate("MainWindow", "Monde"))
        self.pushButton.setText(_translate("MainWindow", "Konvertieren"))
        self.menuW_hrungskonvertierung.setTitle(_translate("MainWindow", "Währungskonvertierung"))


def clicked():
    try:
        gurpsdollar = int(ui.textEdit.toPlainText())

        drachendiv = 23520
        mondediv = 784
        hirschendiv = 112
        sternediv = 16
        groschendiv = 8
        halbgroschendiv = 4
        penniesdiv = 2

        monde = 0
        monddolar = 0

        drachen = math.floor(gurpsdollar / drachendiv)
        drachendollar = drachen * drachendiv


        if ui.radioButton.isChecked():
            monde = math.floor((gurpsdollar - drachendollar) / mondediv)
            monddolar = monde * mondediv


        hirschen = math.floor((gurpsdollar - drachendollar - monddolar) / hirschendiv)
        hirschdollar = hirschen * hirschendiv
        sterne = math.floor((gurpsdollar - drachendollar - monddolar - hirschdollar) / sternediv)
        sterndollar = sterne * sternediv
        groschen = math.floor((gurpsdollar - drachendollar  - monddolar - hirschdollar - sterndollar) / groschendiv)
        groschendollar = groschen * groschendiv
        halbgroschen = math.floor((gurpsdollar - drachendollar  - monddolar - hirschdollar - sterndollar - groschendollar) / halbgroschendiv)
        halbgroschendollar = halbgroschen * halbgroschendiv
        pennies = math.floor((gurpsdollar - drachendollar  - monddolar - hirschdollar - sterndollar - groschendollar - halbgroschendollar) / penniesdiv)
        penniesdollar = pennies * penniesdiv
        halbpennies = gurpsdollar - drachendollar  - monddolar - hirschdollar - sterndollar - groschendollar - halbgroschendollar - penniesdollar

        currency =["Drachen", "Monde", "Hirschen", "Sterne", "Groschen", "Halbgroschen", "Pennies", "Halbpennies"]

        value = [drachen,monde,hirschen,sterne,groschen,halbgroschen,pennies,halbpennies]

        array = []

        for i in range(0,len(currency)):
            if value[i] != 0:
            
                val = value[i]
                cur = currency[i]
                array.append(f"{val} {cur}")


        stringer = " , ".join(array)
        ui.textEdit_2.setText(stringer)
    except:
        print("An error occurred")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setWindowTitle("Converter")
    MainWindow.show()
    sys.exit(app.exec_())
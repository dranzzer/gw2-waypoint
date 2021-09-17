from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(227, 208)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.search_en = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.search_en.setGeometry(QtCore.QRect(0, 0, 141, 21))
        self.search_en.setObjectName("search_en")
        self.search_bt = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.test())
        self.search_bt.setGeometry(QtCore.QRect(140, 0, 81, 23))
        self.search_bt.setObjectName("search_bt")
        self.result = QtWidgets.QListView(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(0, 20, 221, 161))
        self.result.setObjectName("result")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def test(self):
        print("BOOOM!")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.search_en.setPlainText(_translate("MainWindow", "asdasdasd"))
        self.search_bt.setText(_translate("MainWindow", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

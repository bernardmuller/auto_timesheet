# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newSubmit.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SubmitWindow(object):
    def setupUi(self, SubmitWindow):
        SubmitWindow.setObjectName("SubmitWindow")
        SubmitWindow.resize(300, 180)
        self.centralwidget = QtWidgets.QWidget(SubmitWindow)
        self.centralwidget.setObjectName("centralwidget")
        SubmitWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SubmitWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 21))
        self.menubar.setObjectName("menubar")
        SubmitWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SubmitWindow)
        self.statusbar.setObjectName("statusbar")
        SubmitWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SubmitWindow)
        QtCore.QMetaObject.connectSlotsByName(SubmitWindow)

    def retranslateUi(self, SubmitWindow):
        _translate = QtCore.QCoreApplication.translate
        SubmitWindow.setWindowTitle(_translate("SubmitWindow", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SubmitWindow = QtWidgets.QMainWindow()
    ui = Ui_SubmitWindow()
    ui.setupUi(SubmitWindow)
    SubmitWindow.show()
    sys.exit(app.exec_())

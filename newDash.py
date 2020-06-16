import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

class Ui_DashWindow(object):

    switch_window = QtCore.pyqtSignal()
    iconFile = resource_path('icon/CNRlogo.ico')

    def setupUi(self, DashWindow):
        app.setStyle('Fusion')
        DashWindow.setObjectName("DashWindow")
        DashWindow.resize(300, 180)
        self.centralwidget = QtWidgets.QWidget(DashWindow)
        self.centralwidget.setObjectName("centralwidget")
        DashWindow.setCentralWidget(self.centralwidget)

        # App window
        DashWindow.setGeometry(300, 300, 300, 180)
        DashWindow.setStyleSheet("background-color: White;")
        DashWindow.setWindowTitle("Auto Timesheet")
        DashWindow.setFixedSize(300, 180)
        self.center()

        app.setStyle('Fusion')
        self.iconFile = resource_path('icon/CNRlogo.ico')

        # Init QSystemTrayIcon
        self.tray_icon = QSystemTrayIcon(QIcon(self.iconFile))
        self.tray_icon.show()

        # Tray menu
        show_action = QAction("Show", DashWindow)
        quit_action = QAction("Exit", DashWindow)
        hide_action = QAction("Hide", DashWindow)
        show_action.triggered.connect(DashWindow.show)
        hide_action.triggered.connect(DashWindow.hide)
        quit_action.triggered.connect(app.quit)

        tray_menu = QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(hide_action)
        tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

        # Widgets

        self.titlelabel = QtWidgets.QLabel(DashWindow)
        self.titlelabel.setGeometry(QtCore.QRect(50, 10, 200, 40))
        self.titlelabel.setText("")
        self.titlelabel.setPixmap(QtGui.QPixmap(resource_path('icon/CNRtitle.png')))
        self.titlelabel.setScaledContents(True)
        self.titlelabel.setObjectName("titlelabel")

        self.Label = QtWidgets.QLabel(DashWindow)
        self.Label.move(70, 60)
        self.Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Label.setText("Next Submission at: (time) ")
        self.Label.setFont(QFont("calibri", 11))
        self.Label.adjustSize()

        self.submitButton = QtWidgets.QPushButton(DashWindow)
        self.submitButton.setText("Submit Now")
        self.submitButton.move(105, 100)
        self.submitButton.clicked.connect(self.submit_clicked)
        self.submitButton.setFont(QFont("Calibri", 11))
        self.submitButton.setStyleSheet("QPushButton::hover"
                                        "{"
                                        "background-color : lightgrey;"
                                        "}")

        self.statusbar = QtWidgets.QStatusBar(DashWindow)
        self.statusbar.setObjectName("statusbar")
        DashWindow.setStatusBar(self.statusbar)
        self.statusbar.setFont(QFont('Calibri', 8))
        self.statusbar.showMessage("Status bar working...")

        self.retranslateUi(DashWindow)
        QtCore.QMetaObject.connectSlotsByName(DashWindow)

    def submit_clicked(self):
        pass

    def back_clicked(self):
        pass

    def center(self):
        qr = DashWindow.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        DashWindow.move(qr.topLeft())

    def closeEvent(self, event):
        event.ignore()
        DashWindow.hide()
        self.tray_icon.showMessage(
            "Auto Timesheet",
            "Application was minimized to Tray",
            QIcon(self.iconFile),
            2000
        )

    def retranslateUi(self, DashWindow):
        _translate = QtCore.QCoreApplication.translate
        DashWindow.setWindowTitle(_translate("DashWindow", "Auto Timesheet"))


class Ui_SubmitWindow(object):

    switch_window = QtCore.pyqtSignal()
    iconFile = resource_path('icon/CNRlogo.ico')

    def setupUi(self, SubmitWindow):
        SubmitWindow.setObjectName("SubmitWindow")
        SubmitWindow.resize(300, 180)

        self.centralwidget = QtWidgets.QWidget(SubmitWindow)
        self.centralwidget.setObjectName("centralwidget")
        SubmitWindow.setCentralWidget(self.centralwidget)

        # App window
        self.setGeometry(300, 300, 300, 180)
        self.setStyleSheet("background-color: White;")
        self.setWindowTitle("Auto Timesheet")
        self.setFixedSize(300, 180)
        self.center()

        # Widgets
        self.Promptlabel = QtWidgets.QLabel(self)
        self.Promptlabel.setGeometry(QtCore.QRect(50, 10, 200, 40))
        self.Promptlabel.move(70, 20)
        self.Promptlabel.setText("Today's work description:")
        self.Promptlabel.setObjectName("Promptlabel")
        self.Promptlabel.setFont(QFont("calibri", 13))
        self.Promptlabel.adjustSize()

        self.line = QLineEdit(self)
        self.line.move(25, 50)
        self.line.resize(250, 28)

        self.submitButton = QtWidgets.QPushButton(self)
        self.submitButton.setText("Submit")
        self.submitButton.move(107, 100)
        self.submitButton.clicked.connect(self.submit_clicked)
        self.submitButton.setFont(QFont("Calibri", 11))
        self.submitButton.setStyleSheet("QPushButton::hover"
                                        "{"
                                        "background-color : lightgrey;"
                                        "}")

        self.timeButton = QtWidgets.QPushButton(self)
        self.timeButton.setText("Back")
        self.timeButton.move(107, 130)
        self.timeButton.clicked.connect(self.back_clicked)
        self.timeButton.setFont(QFont("Calibri", 11))
        self.timeButton.setStyleSheet("QPushButton::hover"
                                      "{"
                                      "background-color : lightgrey;"
                                      "}")


        self.menubar = QtWidgets.QMenuBar(SubmitWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 21))
        self.menubar.setObjectName("menubar")
        SubmitWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(SubmitWindow)
        self.statusbar.setObjectName("statusbar")
        SubmitWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SubmitWindow)
        QtCore.QMetaObject.connectSlotsByName(SubmitWindow)

    def submit_clicked(self):
        self.line.setPlaceholderText("Coming soon...")
        pass

    def back_clicked(self):
        self.switch_window.emit()
        pass

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def retranslateUi(self, SubmitWindow):
        _translate = QtCore.QCoreApplication.translate
        SubmitWindow.setWindowTitle(_translate("SubmitWindow", "MainWindow"))

class Controller:

    def __init__(self):
        self.dashWindow = Ui_DashWindow()
        self.submitWindow = Ui_SubmitWindow()
        dash = self.dashWindow.setupUi(DashWindow)
        submit = self.submitWindow.setupUi()


    def show_dash(self):
        #self.dash = Dash()
        self.dash.switch_window.connect(self.show_submit)
        self.submit.hide()
        self.dash.show()

    def show_submit(self):
        #self.submit = MainWindow()
        self.submit.switch_window.connect(self.show_dash)
        self.dash.hide()
        self.submit.show()



if __name__ == "__main__":
    import sys
    iconFile = resource_path('icon/CNRlogo.ico')
    app = QtWidgets.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    app.setWindowIcon(QIcon(iconFile))
    controller = Controller()
    DashWindow = QtWidgets.QMainWindow()
    #ui = Ui_DashWindow()
    #ui.setupUi(DashWindow)
    #DashWindow.show()
    controller.show_dash()
    sys.exit(app.exec_())

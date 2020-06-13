import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QAction, QApplication, QLabel, QMainWindow, QMenu, QStyle, QSystemTrayIcon, QDesktopWidget, \
    QLineEdit
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


class MainWindow(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal()
    iconFile = resource_path('icon/CNRlogo.ico')

    def __init__(self):
        global app
        QtWidgets.QWidget.__init__(self)
        app.setStyle('Fusion')

        # Init QSystemTrayIcon
        self.tray_icon = QSystemTrayIcon(QIcon(self.iconFile))
        self.tray_icon.show()

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
        self.Promptlabel.setText("Enter work description:")
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


        self.name = QtWidgets.QLabel(self)
        self.name.setGeometry(QtCore.QRect(50, 10, 200, 40))
        self.name.move(240, 165)
        self.name.setText("made by grizzly")
        self.name.setObjectName("Promptlabel")
        self.name.setFont(QFont("calibri", 6))
        self.name.adjustSize()

    def submit_clicked(self):
        self.line.setPlaceholderText("Coming soon...")
        pass


    def back_clicked(self):
        self.switch_window.emit()
        pass


    def closeEvent(self, event):
        event.ignore()
        self.hide()
        self.tray_icon.showMessage(
            "Auto Timesheet",
            "Application was minimized to Tray",
            QIcon(self.iconFile),
            2000
        )

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


class WindowTwo(QtWidgets.QWidget):

    def __init__(self, text):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Window Two')

        layout = QtWidgets.QGridLayout()

        self.label = QtWidgets.QLabel(text)
        layout.addWidget(self.label)

        self.button = QtWidgets.QPushButton('Close')
        self.button.clicked.connect(self.close)

        layout.addWidget(self.button)

        self.setLayout(layout)


class Dash(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal()
    iconFile = resource_path('icon/CNRlogo.ico')

    def __init__(self):
        global app
        QtWidgets.QWidget.__init__(self)
        app.setStyle('Fusion')
        self.iconFile = resource_path('icon/CNRlogo.ico')

        # Init QSystemTrayIcon
        self.tray_icon = QSystemTrayIcon(QIcon(self.iconFile))
        self.tray_icon.show()

        # Tray menu
        show_action = QAction("Show", self)
        quit_action = QAction("Exit", self)
        hide_action = QAction("Hide", self)
        show_action.triggered.connect(self.show)
        hide_action.triggered.connect(self.hide)
        quit_action.triggered.connect(app.quit)

        tray_menu = QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(hide_action)
        tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

        # App window
        self.setGeometry(300, 300, 300, 180)
        self.setStyleSheet("background-color: White;")
        self.setWindowTitle("Auto Timesheet")
        self.setFixedSize(300, 180)
        self.center()

        # Widgets

        self.titlelabel = QtWidgets.QLabel(self)
        self.titlelabel.setGeometry(QtCore.QRect(50, 10, 200, 40))
        self.titlelabel.setText("")
        self.titlelabel.setPixmap(QtGui.QPixmap(resource_path('icon/CNRtitle.png')))
        self.titlelabel.setScaledContents(True)
        self.titlelabel.setObjectName("titlelabel")

        self.Label = QtWidgets.QLabel(self)
        self.Label.move(70, 60)
        self.Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Label.setText("Next Submission at: (time) ")
        self.Label.setFont(QFont("calibri", 11))
        self.Label.adjustSize()

        self.submitButton = QtWidgets.QPushButton(self)
        self.submitButton.setText("Submit Now")
        self.submitButton.move(105, 100)
        self.submitButton.clicked.connect(self.submit_clicked)
        self.submitButton.setFont(QFont("Calibri", 11))
        self.submitButton.setStyleSheet("QPushButton::hover"
                                        "{"
                                        "background-color : lightgrey;"
                                        "}")

        # self.timeButton = QtWidgets.QPushButton(self)
        # self.timeButton.setText("Set Time")
        # self.timeButton.move(107.5, 130)
        # self.timeButton.clicked.connect(self.time_clicked)
        # self.timeButton.setFont(QFont("Calibri", 11))


        self.name = QtWidgets.QLabel(self)
        self.name.setGeometry(QtCore.QRect(50, 10, 200, 40))
        self.name.move(240, 165)
        self.name.setText("made by grizzly")
        self.name.setObjectName("Promptlabel")
        self.name.setFont(QFont("calibri", 6))
        self.name.adjustSize()

    def submit_clicked(self):
        self.switch_window.emit()

    def closeEvent(self, event):
        event.ignore()
        self.hide()
        self.tray_icon.showMessage(
            "Auto Timesheet",
            "Application was minimized to Tray",
            QIcon(self.iconFile),
            2000
        )

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


class Controller:

    def __init__(self):
        self.dash = Dash()
        self.submit = MainWindow()


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

    def show_window_two(self, text):
        self.window_two = WindowTwo(text)
        self.window.close()
        self.window_two.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    controller = Controller()
    app.setWindowIcon(QIcon(iconFile))
    controller.show_dash()
    sys.exit(app.exec_())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    iconFile = resource_path('icon/CNRlogo.ico')
    main()

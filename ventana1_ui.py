# Form implementation generated from reading ui file '.\ventana1.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 500)
        MainWindow.setMinimumSize(QtCore.QSize(700, 500))
        MainWindow.setMaximumSize(QtCore.QSize(700, 500))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("QWidget#centralwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.126, y1:0.0572727, x2:0.626429, y2:0.671, stop:0 rgba(197, 1, 225, 255), stop:1 rgba(255, 153, 204, 255));}\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 40, 131, 71))
        self.label.setMinimumSize(QtCore.QSize(131, 71))
        self.label.setMaximumSize(QtCore.QSize(131, 71))
        self.label.setStyleSheet("font: 36pt \"Times New Roman\";\n"
"color: black;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icono/logoNext.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(260, 130, 211, 41))
        self.label_2.setStyleSheet("font: 16pt \"Monospac821 BT\";\n"
"color: white;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 210, 101, 21))
        self.label_3.setStyleSheet("font: 16pt \"Monospac821 BT\";\n"
"color: white;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(120, 270, 151, 21))
        self.label_4.setStyleSheet("font: 16pt \"Monospac821 BT\";\n"
"color: white;")
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(280, 270, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setTabletTracking(False)
        self.lineEdit_3.setToolTipDuration(-1)
        self.lineEdit_3.setStyleSheet("border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(218, 11, 255, 255), stop:0.994505 rgba(229, 74, 144, 255));")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(280, 210, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor))
        self.lineEdit_4.setTabletTracking(False)
        self.lineEdit_4.setStyleSheet("border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(218, 11, 255, 255), stop:0.994505 rgba(229, 74, 144, 255));")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(570, 430, 111, 31))
        self.pushButton_2.setStyleSheet("font: 700 11pt \"Segoe UI Variable Display\";\n"
"background-color: rgb(130, 15, 200);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 350, 191, 41))
        self.pushButton.setStyleSheet("border-radius:15;\n"
"font: 14pt  \"Monospac821 BT\";\n"
"background-color: rgb(156, 245, 247);\n"
"color: black;")
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(260, 310, 231, 16))
        self.label_5.setStyleSheet("font: 11pt \"Swis721 Cn BT\";\n"
"color: red;")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 33))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Ingresar usuario"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">Usuario:</p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">Contraseña:</p></body></html>"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", " **********"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", " Name or Nickname"))
        self.pushButton_2.setText(_translate("MainWindow", "Salir"))
        self.pushButton.setText(_translate("MainWindow", "Ingresar"))
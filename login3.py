import sys
from resources_rc import *
from PySide6 import QtWidgets
from PyQt6 import QtCore, QtWidgets
from PyQt6.uic import loadUi
from PySide6.QtUiTools import QUiLoader

# Crear la aplicación
app = QtWidgets.QApplication(sys.argv)

# Cargar archivos .ui con QUiLoader
loader = QUiLoader()
login = loader.load("ventana1.ui", None)
entrar = loader.load("ventana2.ui", None)
error = loader.load("ventana3.ui", None)

# Funciones de navegación
def gui_login():
    name = login.findChild(QtWidgets.QLineEdit, "lineEdit_4").text()
    password = login.findChild(QtWidgets.QLineEdit, "lineEdit_3").text()
    if len(name) == 0 or len(password) == 0:
        login.findChild(QtWidgets.QLabel, "label_5").setText("Ingrese todos los datos")
    elif name == "Erubiel" and password == "12345":
        gui_entrar()
    else:
        gui_error()

def gui_entrar():
    login.hide()
    entrar.show()

def gui_error():
    login.hide()
    error.show()

def regresar_entrar():
    entrar.hide()
    login.show()

def regresar_error():
    error.hide()
    login.show()

# Configurar conexiones de los botones
#login.findChild(QtWidgets.QPushButton, "pushButton").clicked.connect(gui_login)
#entrar.findChild(QtWidgets.QPushButton, "pushButton").clicked.connect(regresar_entrar)
#error.findChild(QtWidgets.QPushButton, "pushButton").clicked.connect(regresar_error)
login.pushButton.clicked.connect(gui_login)
entrar.pushButton.clicked.connect(regresar_entrar)
error.pushButton.clicked.connect(regresar_error)

# Mostrar la ventana inicial y ejecutar la aplicación
login.show()
app.exec()

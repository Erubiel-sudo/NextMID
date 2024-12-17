from PyQt6 import QtWidgets, uic
import resource_rc

#inciar la aplicacion 
app = QtWidgets.QApplication([])

#cargar archivos .ui
login = uic.loadUi("ventana1.ui")
entrar = uic.loadUi("ventana2.ui")
error = uic.loadUi("ventana3.ui")


def gui_login():
    name = login.lineEdit_4.text()
    password = login.lineEdit_3.text()
    if len(name)==0 or len(password)==0:
        login.label_5.setText("Ingrese todos los datos")
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
    login.label_5.setText("")
    login.show()

def regresar_error():
    error.hide()
    login.label_5.setText("")
    login.show()

def salir():
    app.exit()

#BOTONES

login.pushButton.clicked.connect(gui_login)
login.pushButton_2.clicked.connect(salir)

entrar.pushButton.clicked.connect(regresar_entrar)
entrar.pushButton_2.clicked.connect(salir)

error.pushButton.clicked.connect(regresar_error)
error.pushButton_2.clicked.connect(salir)



#ejecutable
login.show()
app.exec()


#convertir los recursos a un archivo ejecutable
#resource.qrc -o resources_rc.py 

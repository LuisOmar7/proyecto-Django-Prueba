# Variables globales
clave = ""
nombre = ""
monto = 0.0


#Funcion de crear la cuenta
def crearCuenta():
    global clave, nombre, monto
    clave = input("Ingrese la clave de la cuenta: ")
    nombre = input("Ingrese el nombre del cliente: ")
    monto = float(input("Ingrese el monto inicial: "))


#Funcion que muestra los datos
def imprimirDatos():
    print('\nDatos de la cuenta')
    print("Clave:", clave)
    print("Nombre:", nombre)
    print("Monto:", monto)


#Funcion para retirar
def retirar(rmonto):
    global monto
    if rmonto > monto:
        print("No puedes retirar mas del dinero que tienes en tu cuenta")
    else:
        monto -= rmonto
        print("Saldo actualizado: ", monto)


#Funcion para depositar
def depositar(dmonto):
    global monto
    monto += dmonto
    print("Saldo actualizado: ", monto)
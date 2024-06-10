from practica.Principios.Funciones import crearCuenta, imprimirDatos, retirar, depositar

#Funcion que contiene el menu
def menu():
    while True:
        print("\nOpciones:")
        print("1. Información de la cuenta")
        print("2. Retirar")
        print("3. Depositar")
        print("4. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == '1':
            imprimirDatos()

        elif opcion == '2':
            monto = float(input("Ingrese el monto a retirar: "))
            retirar(monto)

        elif opcion == '3':
            monto = float(input("Ingrese el deposito: "))
            depositar(monto)
            
        elif opcion == '4':
            print("Hasta pronto")
            break

        else:
            print("No existe esa opcion")


#Funcion que llama a las demas
def general():
    crearCuenta()
    menu()


#Ejecuta el archivo
if _name_ == "_main_":
    general()
import Nomina as nom

class Principal:
    def imprimirMenu(self):
        i=True
        print('\nRegistrar un trabajador\n')
        trab1=nom.Nomina()
        nombre=input('Nombre del empleado: ')
        salario=input('Salario: ')
        trab1.registrarEmpleado(float(salario), nombre)

        print('\nRegistrar nuevo trabajador\n')
        trab2=nom.Nomina()
        nombre=input('Nombre del empleado: ')
        salario=input('Salario: ')
        trab2.registrarEmpleado(float(salario), nombre)

        while i==True:
            print('\n1. Nomina trabajador 1 \n2. Nomina trabajador 2 \n3. Salir')
            opcion = int(input(''))

            if (opcion==1):
                print('\n1. Solicitar Préstamo \n2. Calcular Salario')
                opcion2 = int(input(''))
                if(opcion2==1):
                    trab1.asignarPrestamo()
                elif(opcion2==2):
                    trab1.pagarNomina()

            elif(opcion==2):
                print('\n1. Solicitar Préstamo \n2. Calcular Salario')
                opcion3 = int(input(''))
                if(opcion3==1):
                    trab2.asignarPrestamo()
                elif(opcion3==2):
                    trab2.pagarNomina()
            else:
                i=False

obj=Principal()
obj.imprimirMenu()
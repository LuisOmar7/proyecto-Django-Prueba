class Nomina:
    prestamo=0
    pago=0

    def registrarEmpleado(self, salario, nombre):
        self.salario=salario
        self.nombre=nombre
    
    def asignarPrestamo(self):
        self.prestamo+=float(input('Ingresa el monto del prestamo: '))
        self.pago=self.prestamo*0.10
        print('Tus pagos seran de: ' + str(self.pago))

    def pagarNomina(self):
        if(self.prestamo==0):
            print('Empleado: ' + self.nombre + '\n Salario: ' + str(self.salario))
        else:
            self.prestamo-=self.pago
            print('Empleado: ' + self.nombre + '\nSalario: ' + str(self.salario - self.pago)
                   + '\nDeuda pendiente: ' + str(self.prestamo))
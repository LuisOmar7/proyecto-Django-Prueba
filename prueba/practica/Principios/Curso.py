class Curso:
    cuatrimestre='Mayo-Agosto'

    def __init__(self, n):
        self.nombre=n

curso1=Curso('Desarrollo web')
curso2=Curso('Matematicas')
print('\n Curso 1 \n Cuatrimestre: ' + curso1.cuatrimestre + 'Nombre: ' + curso1.nombre)
print('\n Curso 2 \n Cuatrimestre: ' + curso2.cuatrimestre + 'Nombre: ' + curso2.nombre)
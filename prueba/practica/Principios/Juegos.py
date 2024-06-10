import random

class Juego:
    jugadas=['Piedra', 'Papel', 'Tijera']
    juegos=dict()

    def __init__(self):
        while(True):
            print('\n PIEDRA, PAPEL O TIJERAS\n')

            opc=input('Ingresar una opcion: \n1) Jugar \n2) Ver resultados \n3) Salir')
            if(int(opc)==1):
                self.jugar()
            elif(int(opc)==2):
                self.imprimirJuegos()
            elif(int(opc)==3):
                quit()

    def jugar(self):
        maquina=self.jugadas[random.randint(0,2)]
        jugador=input('Nombre del jugador: ')

        opcion=input('Ingresa una opcion: (Piedra, Papel o Tijeras)')
        if(maquina==opcion):
            ganador='Empate'
        elif(maquina=='Piedra' and opcion=='Tijeras'):
            ganador='Maquina'
        elif(maquina=='Papel' and opcion=='Piedra'):
            ganador='Maquina'
        elif(maquina=='Tijeras' and opcion=='Papel'):
            ganador='Maquina'
        elif(maquina=='Piedra' and opcion=='Papel'):
            ganador='Jugador'
        elif(maquina=='Papel' and opcion=='Tijeras'):
            ganador='Jugador'
        elif(maquina=='Tijeras' and opcion=='Piedra'):
            ganador='Jugador'
        else:
            ganador='Juego anulado'

    
        print('\nRESULTADOS')
        print('Jugador: ' + jugador + '\nTirada: '+ opcion+'\nMaquina: ' + maquina + '\nGanador: '+ ganador)

        resultados=[]
        resultados.append(jugador)
        resultados.append(opcion)
        resultados.append(maquina)
        resultados.append(ganador)
        self.juegos[len(self.juegos)]=resultados

    def imprimirJuegos(self):
        for i in range(0, len(self.juegos)):
            arr=self.juegos[i]
            print('\nJugador: ' + arr[0] + '\nTiradas: ' + arr[1] + '\nMaquina: '+ arr[2] + '\nGanador: ' + arr[3])
Juego()
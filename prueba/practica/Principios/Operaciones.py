contratos=0
rechazados=0
otros=0 #No contestan o cuelgan la llamada

def registrarllamada(numero, contrato=True, status="Terminada"):
    global contratos, rechazados, otros
    if status=="Terminada" and contrato==True:
        contratos+=1
    elif status=="Terminada" and contrato==False:
        rechazados+=1
    elif status=='Sin respuesta':
        otros+=1
    return 'Resultados: \n Contratos Logrados:' + str(contratos) + ' Contratos rechazados:' + str(rechazados) + ' Otros: ' + str(otros)


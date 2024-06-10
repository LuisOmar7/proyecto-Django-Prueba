''' 
costo=[15.9, 10, 7.90]
print(costo[0])
costo[0]=20
print(costo[0])
costo.remove(20)
print(costo[0])
'''

costos=[]
for i in range(0,5):
    monto=int(input('Dame una cantidad: '))
    costos.append(monto)
print('Los datos registrados son: ')
for i in range(0,5):
    print(costos[i])

costos.insert(0,12)
print('Los datos registrados tras insert son: ')
for i in range(0,6):
    print(costos[i])

print('Los datos registrados tras la inserccion multiple son: ')
costos=costos+[11.50,22,30.5]
for i in range(0, len(costos)):
    print(costos[i])
constEscenario = '''
-----------------------------
|         ESCENARIO         |
-----------------------------
'''
constEntradas='''
    [1,2,3,4,5,6,7,8,9,10],
    [11,12,13,14,15,16,17,18,19,20],
    [21,22,23,24,25,26,27,28,29,30],
    [31,32,33,34,35,36,37,38,39,40],
    [41,42,43,44,45,46,47,48,49,50],
    [51,52,53,54,55,56,57,58,59,60],
    [61,62,63,64,65,66,67,68,69,70],
    [71,7,73,74,75,76,77,78,79,80],
    [81,82,83,84,85,86,87,88,89,90],
    [91,92,93,94,95,96,97,98,99,100]
'''
matrizEntradas = [
    [1,2,3,4,5,6,7,8,9,10],
    [11,12,13,14,15,16,17,18,19,20],
    [21,22,23,24,25,26,27,28,29,30],
    [31,32,33,34,35,36,37,38,39,40],
    [41,42,43,44,45,46,47,48,49,50],
    [51,52,53,54,55,56,57,58,59,60],
    [61,62,63,64,65,66,67,68,69,70],
    [71,7,73,74,75,76,77,78,79,80],
    [81,82,83,84,85,86,87,88,89,90],
    [91,92,93,94,95,96,97,98,99,100]]

listaEntradas = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,7,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100
]

listaRutEnt = listaEntradas

listaRut = []

constPrecios = '''
Platinum $120.000 (Asientos del 1 al 20)
Gold $80.000 (Asientos del 21 al 50)
Silver $50.000 (Asientos del 51 al 100)
'''
contGold = 0
contPlat = 0
contSilver = 0

#Comprar entradas
def comprar():
    cant=0
    #while cantidad
    while True:
        try:
            cant = int(input('Cuantas entradas desea comprar? (1-3): '))
            if cant>=1 and cant<=3:
                for i in range(cant):
                    print(constEscenario)
                    print(constEntradas)
                    try:
                        ubi = int(input('Ingrese el asiento que desea: '))
                        if ubi in listaEntradas:
                            try:
                                rut = int(input('Ingrese su rut: '))
                                listaRut.append(rut)
                                for j in range(len(listaEntradas)):
                                    if listaEntradas[j]>=1 and listaEntradas[j]<=20:
                                        contPlat += 1
                                    elif listaEntradas[j]>=21 and listaEntradas[j]<=50:
                                        contGold += 1
                                    elif listaEntradas[j]>=51 and listaEntradas[j]<=51:
                                        contSilver += 1
                                    listaEntradas[j] = 'X'
                                    listaRutEnt[j] = rut
                            except:
                                print('Excepcion en rut')
                    except:
                        print('Excepcion en ubicacion')
                break
            else:
                print('Ingrese una cantidad valida')
        except:
            print('excepcion en cantidad de entradas')


def mostrar():
    print(constEscenario)
    print(matrizEntradas)

def listado():
    listaRut.sort()
    print('ASISTENTES:')
    for i in range(len(listaRut)):
        print(listaRut[i])


totalPlat = contPlat *120000
totalGold = contGold*80000
totalSilver = contSilver*50000
totalCont = contPlat + contSilver + contGold
totalGanancias = totalPlat + totalGold + totalSilver

def ganancias():
    print(f'''
TIPO ENTRADA           CANTIDAD        TOTAL
Platinum    $120000     {contPlat}      {totalPlat}
Gold        $80000      {contGold}      {totalGold}
Silver      $50000      {contSilver}    {totalSilver}
TOTAL                   {totalCont}     {totalGanancias}
    ''')

def salida():
    print('Saliendo del sistema...')
    print('Bárbara Poblete      10/07/2023')

constMenu = '''
1. Comprar entradas
2. Mostrar ubicaciones disponibles
3. Ver listado de asistentes
4. Mostrar ganancias totales
5. Salir
'''

def menu():
    while True:
        try:
            opc = int(input(constMenu))
            if opc == 1:
                comprar()
            elif opc == 2:
                mostrar()
            elif opc == 3:
                listado()
            elif opc == 4:
                ganancias()
            elif opc == 5:
                salida()
                break
        except:
            print('Excepcion en menu')

menu()
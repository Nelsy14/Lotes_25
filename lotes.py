
import os
ls_urbano = []
ls_comercial = []
ls_campestre = []
def fnt_limpiar():
    os.system('cls')

def fnt_agregar():
    
    while True:
        tipo = int(input('Tipo de constuctora: [1]URBANO [2]COMERCIAL [3]CAMPESTRE\n-->  '))
        if 1 <= tipo <= 3:
            break
    constructora = input('Nombre de la constructora: ')
    frente = float(input('Frente: '))
    fondo = float(input('Fondo: '))
    m2 = frente * fondo
    
    #pc= PermisoConstruccion | pTotal = Precio Total
    if tipo == 1:
        m2_precio = 25.000
        pc = 0.45
        pTotal = m2_precio * m2
        pFinal = pTotal * (1-pc)
        pFinal = str(pFinal)+'$'
        R= constructora + ' | Area: ' +  str(m2) +' | Precio final: ' + pFinal+' |'
        ls_urbano.append(R)
    elif tipo == 2:
        m2_precio = 60.000
        pc = 0.75
        pTotal = m2_precio * m2
        pFinal = pTotal * (1-pc)
        pFinal = str(pFinal)+'$'
        R= constructora + ' = Area: ' +  str(m2) +' | Precio final: ' + pFinal+' |'
        ls_comercial.append(R)
    elif tipo == 3:
        m2_precio = 35.000
        pc = 0.15
        pTotal = m2_precio * m2
        pFinal = pTotal * (1-pc)
        pFinal = str(pFinal)+'$'
        R= constructora + ' | Area: ' +  str(m2) +' | Precio final: ' + pFinal+' |'
        ls_campestre.append(R)
    input(f'Registro exitoso \n Precio final = {pFinal} | <ENTER>..')

def fnt_consultar():
    global ls_campestre , ls_comercial , ls_urbano
    while True:
        fnt_limpiar()
        print('<<< MENU DE CONSULTA >>>\n')
        tipo = int(input('Tipo de constructora a consultar\n[1]URBANO\n[2]COMERCIAL\n[3]CAMPESTRE\n[0]Salir\n-->  '))
        
        if tipo == 0:
            break
        elif tipo == 1:
            fnt_limpiar()
            print('<<< MENU DE CONSULTA >>>\n')
            print(f'Lotes urbanos: {ls_urbano}')
            input('Fin de consulta <ENTER>..')
        elif tipo == 2:
            fnt_limpiar()
            print('<<< MENU DE CONSULTA >>>\n')
            print(f'Lotes comercial: {ls_comercial}')
            input('Fin de consulta <ENTER>..')
        elif tipo == 3:
            fnt_limpiar()
            print('<<< MENU DE CONSULTA >>>\n')
            print(f'Lotes campestre: {ls_campestre}')
            input('Fin de consulta <ENTER>..')
        else:
            input('Opcion no valida <ENTER>..')
        
def fnt_selector(op):
    global sw
    if op == '0':
        sw = False
    elif op == '1':
        fnt_agregar()
    elif op == '2':
        fnt_consultar()
sw = True
while sw == True:
    fnt_limpiar()
    op = input('<<< CALCULADOR DE ÁREA >>> \n[0]Salir\n[1]Agregar un nuevo lote\n[2]Mostrar lotes\n--> ')
    fnt_selector(op)

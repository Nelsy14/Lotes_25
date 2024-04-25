
import os

def fnt_limpiar():
    os.system('cls')

def fnt_agregar():
    
    tipo = input ('Tipo de constuctora: [1] URBANO [2] COMERCIAL []')
    constructora = input('Nombre de la constructora: '3)
    frente = float(input('Frente: '))
    fondo = float(input('Fondo: '))
    m2 = frente * fondo
    
    if 
    
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
    op = input('<<< CALCULADOR DE ÁREA >>> \n[0]Salir\n[1]Agregar un nuevo lote\n[2]Mostrar lotes\n')
    fnt_selector(op)
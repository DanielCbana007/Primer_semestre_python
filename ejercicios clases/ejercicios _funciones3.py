import numpy as np
import math

hola = "hola"

print(hola)
parte="po"
parte2="po"
def num(parte,parte2):
    global hola
    hola = parte+parte2
    
print(hola)
#ejercicio 1

"""cantidad_numeros = int(input("¿cuantos numeros desea ingresar?: "))

numeros = np.array([])
def ingresar_numeros(cantidad_numeros):
    for i in range(cantidad_numeros):
        numeros = np.append(numeros, int(input("escriba el numero que desea guardar: ")))
ingresar_numeros()
    
print(f"la media o promedio de los numeros ingresados es de: {np.mean(numeros)}")"""

#ejercicio 2 
"""
num_dia = int(input("ingrese el numero del dia: "))
num_mes = int(input("ingrese el numero del dia: "))
num_year = int(input("ingrese el numero del dia: "))

def imprimir(num_dia, num_mes, num_year):
    print("::::::::::::::::::::::::: FORMATO dd/mm/aaaa :::::::::::::::::::::::::")
    print(f"{num_dia}/{num_mes}/{num_year}")

    print("::::::::::::::::::::::::: FORMATO dd/nombre_mes/aaaa :::::::::::::::::::::::::")
    if num_mes == 1:
        print(f"{num_dia}/Enero/{num_year}")
    elif num_mes == 1:
        print(f"{num_dia}/Febrero/{num_year}")
    elif num_mes == 1:
        print(f"{num_dia}/Marzo/{num_year}")
    elif num_mes == 1:
        print(f"{num_dia}/Abril/{num_year}")
    elif num_mes == 1:
        print(f"{num_dia}/Mayo/{num_year}")
    elif num_mes == 1:
        print(f"{num_dia}/Junio/{num_year}")
    elif num_mes == 1:
        print(f"{num_dia}/Julio/{num_year}")
    elif num_mes == 1:
        print(f"{num_dia}/Agosto/{num_year}")
    elif num_mes == 1:
        print(f"{num_dia}/Septiembre/{num_year}")
    elif num_mes == 1:
        print(f"{num_dia}/Octubre/{num_year}")
    elif num_mes == 1:
        print(f"{num_dia}/Noviembre/{num_year}")
    elif num_mes == 1:
        print(f"{num_dia}/Diciembre/{num_year}")
    else:
        print("el mes ingresado no existe")
        
    print("::::::::::::::::::::::::: AÑO BISIESTO O NO BISIESTO :::::::::::::::::::::::::")
                
    if (num_year % 4):
        if (num_year % 100):
            if (num_year % 400):
                print("El año es bisiesto (tiene 366 días)")
            else:
                print("El año no es bisiesto (tiene 365 días)")
        else:
            print("El año es bisiesto (tiene 366 días)")
    else:
        print("El año no es bisiesto (tiene 365 días)")
        
imprimir()"""

#ejercicio 3

"""r = int(input("ingrese el valor de r: "))
t = int(input("ingrese el valor de r: "))

def x(r,t):
    return r * math.cos(math.radians(t))
def y(r,t):
    return r * math.sin(math.radians(t))
      
print(x(r,t))
print(y(r,t))"""



#ejercicio 4

"""num = int(input("ingrese el numero del cual quiera saber el valor absoluto: "))

def valor_absoluto(num): 
    return abs(num)
    
print(valor_absoluto())
"""

#ejercuicio 5

"""numero = int(input("Ingrese un numero: "))

def convertir_a_romano(numero):

    if numero < 1 or numero > 3000:
        return "El numero debe estar entre 1 y 3000"

    unidades = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    decenas = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    centenas = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    millares = ["", "M", "MM", "MMM"]

    u = numero % 10
    d = int(numero / 10) % 10
    c = int(numero / 100) % 10
    m = int(numero / 1000) % 10

    return millares[m] + centenas[c] + decenas[d] + unidades[u]

print(convertir_a_romano(numero))"""
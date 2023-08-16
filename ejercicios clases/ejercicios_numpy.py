import numpy as np
import math 
import random

#ejercicio 1

"""n = int(input("¿cuantos numeros va a almacenar?: "))
areglo = np.empty(0)
    
for i in range(n):
    valor =int(input("ingresa el numero a guardar: ".format(i+1)))
    areglo = np.append(areglo, valor)
    
print(areglo)"""

#ejercicio 2

areglo = []

for i in range(10):
    num = math.floor(random.random() * (999999 - 1 + 1) + 1)
    areglo = np.append(areglo, num)
    
print(areglo)

#ejercicio 3

"""edades = []

for i in range(5):
    valor_edades =  int(input("Escriba la edad guardar: "))
    edades = np.append(edades,valor_edades)
    promedio = np.mean(edades[i])
    media = np.median(edades[i])
    desviacion_estandar = np.std(edades[i])

print(":::::::::::::::::::::::: EDADES ::::::::::::::::::::::::")
print(edades)
print(":::::::::::::::::::::::: PROMEDIO ::::::::::::::::::::::::")
print(promedio)
print(":::::::::::::::::::::::: MEDIA ::::::::::::::::::::::::")
print(media)
print(":::::::::::::::::::::::: DESVIACION ESTANDAR ::::::::::::::::::::::::")
print(desviacion_estandar)"""

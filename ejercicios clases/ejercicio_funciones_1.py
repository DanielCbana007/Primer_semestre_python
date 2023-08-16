import numpy as np
import math 
import random

#ejercicio 1

"""lanzamientos = []
par = 0
impar = 0

def lanzar_dado_10():
    for i in range(10):
        num = math.floor(random.random() * (6 - 1 + 1) + 1)
        lanzamientos.append(num)

while True:
    decision = int(input("si quiere seguir con el programa dijite 1, si desea terminar con el programa dijite 2: "))
    lanzar_dado_10()
    
    if decision == 1:

        for i in range(10):
            if lanzamientos[i] % 2 == 0:
                par += 1
            else:
                impar += 1
        

        print(f"la frecuencia de numeros pares es de: {par}")
        print(f"la frecuencia de numeros impares es de: {impar}")
        
    elif decision == 2:  
        print("que tenga un buen dia :)")   
        break
    
    else: 
        print("opcion invalida. por favor, ingrese 1 o 2.")"""

#ejercicio 2

"""dado1 = []
dado2 = []
par1 = 0
impar1 = 0
par2 = 0
impar2 = 0
r = 0


def lanzar_dado_10_1():
    for i in range(20):
        num1 = math.floor(random.random() * (6 - 1 + 1) + 1)
        dado1.append(num1)
        
def lanzar_dado_10_2():
    for i in range(20):
        num2 = math.floor(random.random() * (6 - 1 + 1) + 1)
        dado2.append(num2)
        
while True:
    
    decision = int(input("si quiere seguir con el programa dijite 1, si desea terminar con el programa dijite 2: "))
    
    if decision == 1:
        dado1 = []
        dado2 = []
        par1 = 0
        impar1 = 0
        par2 = 0
        impar2 = 0
        r = 0
        
        lanzar_dado_10_1()
        lanzar_dado_10_2()

        for i in range(20):
            if dado1[i] % 2 == 0:
                par1 += 1
            else:
                impar1 += 1             
                
        for i in range(10):
            if dado2[i] % 2 == 0:
                par2 += 1
            else:
                impar2 += 1

        for i in range(20):
            if dado1[i] % 2 == 0 and dado2[i] % 2 == 0:
                r += 1

        print(f"las veces en que la cara de los dados fue un numero par es de: {r}")
    elif decision == 2:
        print("buen dia :)")
        break
    
    else:
        print("opcion invalida. por favor, ingrese 1 o 2.")"""
        
#ejeccio 3

"""dado1 = []
dado2 = []
par1 = 0
impar1 = 0
par2 = 0
impar2 = 0
r = 0


def lanzar_dado_10_1():
    for i in range(20):
        num1 = math.floor(random.random() * (6 - 1 + 1) + 1)
        dado1.append(num1)
        
def lanzar_dado_10_2():
    for i in range(20):
        num2 = math.floor(random.random() * (6 - 1 + 1) + 1)
        dado2.append(num2)
        
while True:
    
    decision = int(input("si quiere seguir con el programa dijite 1, si desea terminar con el programa dijite 2: "))
    
    if decision == 1:
        dado1 = []
        dado2 = []
        par1 = 0
        impar1 = 0
        par2 = 0
        impar2 = 0
        r = 0
        
        lanzar_dado_10_1()
        lanzar_dado_10_2()

        for i in range(10):
            if dado1[i] == dado2[i]:
                r += 1
            else:
                r = r
                
        print(f"las veces en que la cara de los dados fue el mismo numero es de: {r}")
        
    elif decision == 2:
        print("buen dia :)")
        break
    
    else:
        print("opcion invalida. por favor, ingrese 1 o 2.")"""
        
#ejercico 4

"""dado1 = []
dado2 = []
par1 = 0
impar1 = 0
par2 = 0
impar2 = 0
r = 0


def lanzar_dado_10_1():
    for i in range(20):
        num1 = math.floor(random.random() * (6 - 1 + 1) + 1)
        dado1.append(num1)
        
def lanzar_dado_10_2():
    for i in range(20):
        num2 = math.floor(random.random() * (6 - 1 + 1) + 1)
        dado2.append(num2)
        
while True:
    
    decision = int(input("si quiere seguir con el programa dijite 1, si desea terminar con el programa dijite 2: "))
    
    if decision == 1:
        dado1 = []
        dado2 = []
        par1 = 0
        impar1 = 0
        par2 = 0
        impar2 = 0
        r = 0
        
        lanzar_dado_10_1()
        lanzar_dado_10_2()

        for i in range(10):
            if dado1[i] % 2 == 0 and dado2[i] % 2 == 0:
                if dado1[i] == dado2[i]:
                    r += 1
                else:
                    r = r
            else:
                r = r
                
        print(f"las veces en que la cara de los dados fue el mismo numero y el mismo numero es par es de: {r}")
        
    elif decision == 2:
        print("buen dia :)")
        break
    
    else:
        print("opcion invalida. por favor, ingrese 1 o 2.")"""


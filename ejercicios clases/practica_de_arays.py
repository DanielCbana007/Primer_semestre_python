import numpy as np
import time
import  os

#ejercicio 1

"""personas = int(input("¿cuantas personas son?: "))

def nombre():
    return input("escriba el nombre que quiere guardar: ")
    
def estatura():
    return float(input("escriba la estatura que quiere guardar: "))

esteturas = np.array([])
nombres = np.array([])

for i in range(personas):
    nombres = np.append(nombres, nombre())
    
for i in range(personas):
    esteturas = np.append(esteturas, estatura())

print("::::::::::::::::::::::::: NOMBRES :::::::::::::::::::::::::")
print(nombres)
print("::::::::::::::::::::::::: ESTATURAS :::::::::::::::::::::::::")
estaturas_ordenadas = np.sort(esteturas)[::-1] 
print(estaturas_ordenadas)
print("::::::::::::::::::::::::: ESTATURAS INVERSAS :::::::::::::::::::::::::")
estaturas_inversas = np.sort(esteturas)[::1] 
print(estaturas_inversas)"""

#ejercicio 2

"""estudiantes = int(input("¿cuantos estudiantes son?: "))

nombres = []
notas = np.empty((estudiantes,5))
estudiantes_perdieron = []

for i in range(estudiantes):
    nombres.append(input("escriba el nombre que quiere guardar: "))
    
for i in range(estudiantes):
    for j in range(5):
        notas[i][j] = float(input(f"escriba la nota del estudiante {nombres[i]} en orden: "))

time.sleep(3)
os.system("cls")

promedios = np.mean(notas, axis=1)

mayor_promedio = np.amax(promedios)
coordenada = np.where(promedios == mayor_promedio)[0][0]

print("::::::::::::::::::::::::: PROMEDIOS :::::::::::::::::::::::::")
print(promedios)

print("::::::::::::::::::::::::: ESTUDIANTE CON EL MAYOR PROMEDIO :::::::::::::::::::::::::")
print(F"el estudiante {nombres[coordenada]} fue el mayor promedio, con una nota final de {mayor_promedio}")

print("::::::::::::::::::::::::: ESTUDIANTES QUE TIENEN QUE REPETIR MATERIA :::::::::::::::::::::::::")
for i in range(estudiantes):
    if promedios[i] < 3.0:
        estudiantes_perdieron.append(nombres[i])
        print(f"el estudiante {nombres[i]} tiene que repetir la materia")
    elif promedios[i] >= 3.0:
        print(f"el estudiante {nombres[i]} no tiene que repetir la materia")
    else:
        print("error")

print("::::::::::::::::::::::::: ESTUDIANTES QUE PUEDEN REPETIR MATERIA :::::::::::::::::::::::::")
for i in range(estudiantes):
    if promedios[i] < 3.0 and promedios[i] < 2.0:
        print(f"el estudiante {nombres[i]} no puede repetir la materia")
    elif promedios[i] > 3.0 and promedios[i] >= 2.0:
        print(f"el estudiante {nombres[i]} puede repetir la materia")
    elif promedios[i] > 3.0 and promedios[i] >= 2.0:
        print(f"el estudiante {nombres[i]} no tiene que repetir materia")
    else:
        print("error")

print("::::::::::::::::::::::::: ESTUDIANTES QUE APROBARON MATERIA :::::::::::::::::::::::::")
for i in range(estudiantes):
    if promedios[i] < 3.0:
        estudiantes_perdieron.append(nombres[i])
        print(f"el estudiante {nombres[i]} no aprobo la materia")
    elif promedios[i] >= 3.0:
        print(f"el estudiante {nombres[i]} aprobo la materia")
    else:
        print("error")
"""
#ejercicio 3

"""pasientes = int(input("¿cuantos pacientes son?: "))
nombres = np.array([])
pesos = np.empty((pasientes,3))
objetivos = np.array([])

perdieron_peso = 0

for i in range(pasientes):
    nombres = np.append(nombres, input("cual es el nombre del paciente: "))
    for j in range(1):
        pesos[i][0] = input(f"¿cual es el peso del pasiente en su evaluacion numero 1?: ")
        pesos[i][1] = input(f"¿cual es el peso del pasiente en su evaluacion numero 2?: ")
        pesos[i][2] = input(f"¿cual es el peso del pasiente en su evaluacion numero 3?: ")

for i in range(pasientes):
    objetivos = np.append(objetivos, int(input(f"si el objetivo del pasiente {nombres[i]} es subir de peso dijite 1, si su objetivo es bajar de peso dijite 2: ")))

time.sleep(3)       
os.system("cls")
      
print("::::::::::::::::::::::::: PESO PASIENTES :::::::::::::::::::::::::")         
for i in range(pasientes):
    for j in range(1):
        if pesos[i][0] < pesos[i][2]:            
            peso_final =  pesos[i][0] - pesos[i][2]
            print(f"el pasiente {nombres[i]} gano {abs(peso_final)}kg de peso")
            
        elif pesos[i][0] > pesos[i][2]:
            peso_final =  pesos[i][0] - pesos[i][2]
            print(f"el pasiente {nombres[i]} perdido {abs(peso_final)}kg de peso")
        elif pesos[i][0] == pesos[i][2]:
            print("tiene el mismo peso con el cual inicios las evaluaciones")
            
        elif pesos[i][0] < pesos[i][1]:
            perdieron_peso +=1
            print(f"la cantidad de pasientes que perdieron peso entre la evaluacion 1 hasta ña evaluacion 2 son {perdieron_peso}")
        else:
            print("error")
            
time.sleep(6)
os.system("cls")
time.sleep(7)

print("::::::::::::::::::::::::: PASIENTES QUE LOGRARON SU OBJETIVO :::::::::::::::::::::::::")       
for i in range(pasientes):
    for j in range(1):
        if pesos[i][0] < pesos[i][1] or pesos[i][0] < pesos[i][2] and objetivos[i] == 1:       
            print(f"el pasiente {nombres[i]} cumplio su objetivo")
        elif pesos[i][0] > pesos[i][2] and objetivos[i] == 2:       
            print(f"el pasiente {nombres[i]} cumplio su objetivo")
        else:
            print(f"el paciente {nombres[i]} no cumplio su objetivo")
            
time.sleep(6)
os.system("cls")
time.sleep(7)
            
print("::::::::::::::::::::::::: PASIENTES QUE PERDIERON PESO EN LA EVALUACION 2 :::::::::::::::::::::::::")
for i in range(pasientes):
    for j in range(1):
        if pesos[i][0] > pesos[i][1]:       
            print(f"el pasiente {nombres[i]} perdio peso en la segunda evaluacion")
        elif pesos[i][0] <= pesos[i][1]:       
            print(f"el pasiente {nombres[i]} no perdio peso en la segunda evaluacion")
        else:
            print(f"error")"""
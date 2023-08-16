import numpy as np

#ejecicio 1

"""num1 = 4
num2 = 8

def sum():
    return num1 + num2

print(sum())"""

#ejercicio 2

"""palabra = "hola soy una palabra"

def medir():
    return len(palabra)
    
print(medir())"""

#ejercicio 3

tareas = np.array([], dtype=int)
completas = []
contador = 0

def agregar_tareas(tareas):
    cantidad_tareas = int(input("cuantas tareas decea agregar: "))
    for i in range(cantidad_tareas):
        tareas = np.append(tareas, input("agrege su tarea: "))   
    return tareas

def marcar_tareas():
    cantidad_completadas = int(input("¿Cuántas tareas completó?: "))
    recorrido = 0
    completas = []
    
    for i in range(len(tareas)):
        print(f"La tarea {tareas[i]} es la número {i + 1}")
    
    while recorrido < cantidad_completadas:
        decision_completar = int(input("¿Cuál es el número de la tarea que completó? (0 para salir): "))
        
        if decision_completar == 0:
            break
        
        if decision_completar > 0 and decision_completar <= len(tareas):
            tarea_completada = tareas[decision_completar - 1]
            
            if tarea_completada not in completas:
                completas.append(tarea_completada)
                recorrido += 1
            else:
                pass
        else:
            print("El número de tarea es inválido.")
    
    return completas

while True:
    salida_entrada = int(input("si desea continuar con el programa dijite 1, si no quiere continuar con el programa dijite 2: "))
    
    if salida_entrada == 1:
        decision = int(input("para agregar tareas dijite 1, para marcar como completadas las tareas dijite 2, para mostrar las tareas completadas y no completadas dijite 3: "))
        if decision == 1:
            tareas = agregar_tareas(tareas)
            completas = np.zeros(len(tareas), dtype=int)
        elif decision == 2:
            completas = marcar_tareas()
        elif decision == 3:
            for i in range(len(tareas)):
                if tareas[i] in completas:
                    print(f"la tarea {tareas[i]} esta completada")
                else:
                    print(f"l tarea {tareas[i]} no se completo") 
                    
    elif salida_entrada == 2:
        print("buelva pronto :)")
        break
    else:
        print("el valor dijitado es incirecto, por favor dijite 1 0 2")
        
import math 
import random



dado1 = []
dado2 = []
r = 0


def lanzar_dado():
    num1 = math.floor(random.random() * (6 - 1 + 1) + 1)
    dado1.append(num1)
    num2 = math.floor(random.random() * (6 - 1 + 1) + 1)
    dado2.append(num2)

lanzar_dado()

while True:
    decision = int(input("si quiere seguir con el programa dijite 1, si desea terminar con el programa dijite 2: "))
    if decision == 1:
        print(dado1,dado2)
        for i in  range(99999999999999999999999999999999999999999999999999999999999999999999999999999999999):
            if dado1[i] % 2 == 0 and dado2[i] % 2 == 0 and dado1 == dado2:  
                    r += 1 
            elif r == 3:
                    break                            
    elif decision == 2:
        print("buen dia :)")
        break
    
    else:
        print("opcion invalida. por favor, ingrese 1 o 2.")
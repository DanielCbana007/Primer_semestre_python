#ejecicio 1

"""decision = int(input("¿cuantos numeros va a guardar?: "))
num = []

def n ():
    return int(input("escriba el nimero que quiere guardar: "))

for i in range(decision):
    num.append(n())

print(num)"""

#ejercicio 2

"""palabra = input("escriba la palabra a evaluar ")
letras = []

for i in palabra:
    letras.append(i)
    
if palabra == ''.join(letras[::-1]):
    print("es palindoma")
else:
    print("no es palindroma")
    """

#ejercicio 3

"""num = []
num2 = []

def n ():
    return int(input("escriba el nimero que quiere guardar: "))

for i in range(0,5):
    num.append(n())
    num2 = num[::-1]

print(f"{num}\n{ num2}")"""

#ejercicio 4

"""vector1 = []
vector2 = []

def v1 ():
    return int(input("escriba el nimero que quiere guardar en el vector 1: "))

def v2 ():
    return int(input("escriba el nimero que quiere guardar en el vector 2: "))

for i in range(0,5):
    vector1.append(v1())
    
for i in range(0,5):
    vector2.append(v2())

vector3 = [vector1[i] + vector2[i] for i in range(0,5)]
    
print(f"{vector1}\n{vector2}\n{vector3}")"""

#ejercicio 5

"""vector1 = []

def v1 ():
    return int(input("escriba el nimero que quiere guardar en el vector 1: "))

for i in range(0,3):
    vector1.append(v1())

vector2 = [(vector1[i] +20) / 2 for i in range(0,3)]

print(vector2)"""
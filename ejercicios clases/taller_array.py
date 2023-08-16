"""decision = int(input("¿cuantos numeros va a guardar?: "))
num = []

def n ():
    return int(input("escriba el numero que quiere guardar: "))

for i in range(decision):
    num.append(n())

print(num)"""

"""num_a_guardar = int(input("¿cuantos numeros quieres guardar?: "))
numP = []
numI = []

def n ():
    return int(input("escriba el numero que quiere guardar: "))

for i in range(0,num_a_guardar):
    num = n()
    
    if num % 2 == 0:
        numP.append(num)
        
    elif num % 2 == 1:
        numI.append(num)
   
print(f"{numP}\n{numI}")"""

"""num_a_guardar = int(input("¿cuantos numeros quieres guardar?: "))
numeros = []

def n ():
    return int(input("escriba el numero que quiere guardar: "))


for i in range(0,num_a_guardar):
    num = n()
    numeros.append(num)

for i in range(0,num_a_guardar):
    num = numeros[i]
    if num % 2 == 0:
        print(f"{num} impar")
    elif num % 2 == 1:
        print(f"{num} par")"""
        

"""n = int(input("Ingrese la cantidad de personas a ingresar: "))

nombres = []
generos = []
edades = []

for i in range(n):
    nombre = input("Ingrese el nombre de la persona: ")
    genero = input("Ingrese el género de la persona (M/F): ")
    edad = int(input("Ingrese la edad de la persona: "))
    nombres.append(nombre)
    generos.append(genero)
    edades.append(edad)

hombres = generos.count('M')

mujeres_mayores = 0
for i in range(n):
    if generos[i] == 'F' and edades[i] >= 18:
        mujeres_mayores += 1

suma_edades_hombres = 0
for i in range(n):
    if generos[i] == 'M':
        suma_edades_hombres += edades[i]
if hombres > 0:
    promedio_edad_hombres = suma_edades_hombres / hombres
else:
    promedio_edad_hombres = 0

nombre_mujer_mas_joven = ''
edad_mujer_mas_joven = float('inf')
for i in range(n):
    if generos[i] == 'F' and edades[i] < edad_mujer_mas_joven:
        nombre_mujer_mas_joven = nombres[i]
        edad_mujer_mas_joven = edades[i]

print("Cantidad de hombres:", hombres)
print("Cantidad de mujeres mayores de edad:", mujeres_mayores)
print("Promedio de edad de hombres:", promedio_edad_hombres)
if nombre_mujer_mas_joven != '':
    print("Nombre de la mujer más joven:", nombre_mujer_mas_joven)
else:
    print("No hay mujeres en la lista.")"""
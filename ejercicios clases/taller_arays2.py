import numpy as np 
#ejercicio 1

"""# declaramos matriz 3.3 vacia
matriz1 = np.empty((3,3))
matriz2 = np.zeros((3,3))
matriz3 = []

def num():
    return int(input("Ingrese un numero: "))

def llenarMatriz(matriz):
    for i in range(3):
        for j in range(3):
            matriz[i][j] = num()
    return matriz

print("::::::::::::::::::::::::: MATRIZ 1 :::::::::::::::::::::::::")
m1 = llenarMatriz(matriz1)
print("::::::::::::::::::::::::: MATRIZ 2 :::::::::::::::::::::::::")
m2 = llenarMatriz(matriz2)

# recorrer las matrices y sumarlas
for i in range(3):
    for j in range(3):
         m1[i][j] *= m2[i][j]
         matriz3 = m1
print("::::::::::::::::::::::::: MATRIZES :::::::::::::::::::::::::")
print(matriz1)
print(matriz2)
print("::::::::::::::::::::::::: PRODUCTO DE MATRIZES :::::::::::::::::::::::::")
print(matriz3)"""

#ejercicio 2

"""matriz = np.empty((5,5))

def num():
    return int(input("Ingrese un numero: "))


print("::::::::::::::::::::::::: ALMACENAMIENTO DE MATRIZ :::::::::::::::::::::::::")
def llama_matriz():
    for i in range(5):
        for j in range(5):
            matriz[i][j] = num()

llama_matriz()
        
print("::::::::::::::::::::::::: RECORRIDO DE MATRIZ IMVERSA :::::::::::::::::::::::::")
print(matriz)

print("::::::::::::::::::::::::: RECORRIDO DE MATRIZ IMVERSA :::::::::::::::::::::::::")
print(np.flip(matriz))"""

#ejercicio 3

"""m = int(input("¿cuantas filas desea en la matriz?: "))
n = int(input("¿cuantas columnas desea en la matriz?: "))
matriz = np.random.randint(50, 100, size=(m, n))   
numero = int(input("¿que numero desea buscar?: "))   
coordenadas = np.where(matriz == numero)
fila = coordenadas[0][0]
columna = coordenadas[1][0]

print("::::::::::::::::::::::::: POCISION EN LA MATRIZ :::::::::::::::::::::::::")

print(f"el nmero {numero} se encuentra en la fila {fila} y en la columna {columna}")

print("::::::::::::::::::::::::: MATRIZ :::::::::::::::::::::::::")

print(matriz)"""

#ejercicio 4

"""matriz = np.empty((4,5), dtype='U25')

def caracteres():
    return input("escriba un caracter: ")


for i in range(4):
    for j in range(5):
        matriz[i][j] = caracteres()

print("::::::::::::::::::::::::: MATRIZ :::::::::::::::::::::::::")
print(matriz)

matriz_teapuesta =np.transpose(matriz)

print("::::::::::::::::::::::::: MATRIZ TRASPUESTA :::::::::::::::::::::::::")
print(matriz_teapuesta)"""

#ejercicio 5
"""
matriz = np.zeros((5,5))

matriz[0,:] = 1
matriz[-1,:] = 1
matriz[:,0] = 1
matriz[:,-1] = 1

print("::::::::::::::::::::::::: MATRIZ :::::::::::::::::::::::::")
print(matriz)
"""
            
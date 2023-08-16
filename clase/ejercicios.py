# contaminacion 

"""poblacion = int(input("Escriba el numero de la poblacion: "))
contaminacion = ((175000 * 4) * (poblacion * 1000))

with open("contaminacion.txt", mode="w") as contaminaciones:
    contaminaciones.write(f"la poblacion total es de: {poblacion} mil personas\n")
    contaminaciones.write(f"la contaminacion total es de: {contaminacion}m3 por year")

print( "La contaminación es de: " + str(contaminacion / 0.001) + " m3 por ")"""

#contaminacion con funciones 

"""poblacion = int(input("Escriba el numero de la poblacion: "))
def contaminacion(poblacion):
    return (175000 * 4) * (poblacion * 1000)

with open("contaminacion.txt", mode="w") as contaminaciones:
    contaminaciones.write(f"la poblacion total es de: {poblacion} mil personas\n")
    contaminaciones.write(f"la contaminacion total es de: {contaminacion(poblacion)}m3 por year")

print(f"La contaminación es de: {contaminacion(poblacion)} m3 por year")"""

#radian

"""radian = int (input("dijite el radian: "))

def paso1(radian):
    return radian/57.2958

with open("radianes.txt", mode="w") as radianes:
    radianes.write(f"El radian es: {radian}\n")
    radianes.write(f"Los radianes del tiangulo son: {paso1(radian)}\n")

print(f"Los radianes del tiangulo son: {paso1(radian)} radianes")"""

#nota 

"""parcial = int(input("Nota del parcial: "))
final = int(input("Nota del final: "))
seguimiento = int(input("Nota del seguimiento: "))

parcialPorsiento = parcial * 20
finalPorsiento = final * 30
seguimientolPorsiento = seguimiento * 50

algoritmo = ((parcialPorsiento + finalPorsiento + seguimientolPorsiento) / 100)

with open("nota.txt",mode="w") as notas:
    notas.write(f"la nota del parcial es: {parcial}\n")
    notas.write(f"la nota del final es: {final}\n")
    notas.write(f"la nota del seguimiento es: {seguimiento}\n")
    notas.write(f"La nota final es:: {algoritmo}")

print(f"La nota final es: {algoritmo}")"""

#nota con funciones

"""parcial = int(input("Nota del parcial: "))
final = int(input("Nota del final: "))
seguimiento = int(input("Nota del seguimiento: "))

def algoritmo(parcial, final, seguimiento):
    return ((parcial*20) + (final*30) + (seguimiento*50))/100

with open("nota.txt",mode="w") as notas:
    notas.write(f"la nota del parcial es: {parcial}\n")
    notas.write(f"la nota del final es: {final}\n")
    notas.write(f"la nota del seguimiento es: {seguimiento}\n")
    notas.write(f"La nota final es:: {algoritmo(parcial, final, seguimiento)}")

print(f"La nota final es: {algoritmo(parcial, final, seguimiento)}")"""


#año

"""yearActual = 2023
yearDeNacimiento = int(input("¿En que año naciste?: "))
s
operacion = yearActual - yearDeNacimiento

with open("año.txt", mode="w") as years:
    years.write(f"Los años que tienes son: {operacion(yearDeNacimiento)}")

print(operacion)"""

#año con fotmimulas 

"""yearDeNacimiento = int(input("¿En que año naciste?: "))

def operacion(yearDeNacimiento):
    return 2023 - yearDeNacimiento

with open("año.txt", mode="w") as years:
    years.write(f"Los años que tienes son: {operacion(yearDeNacimiento)}")

print(f"Los años que tienes son: {operacion(yearDeNacimiento)}")"""

#Algoritmo de resistencias

"""R1 = int(input("Resistencia r1: "))

R2 = int(input("Resistencia r2: "))

operacionDe_R = 1/((1/R1) + (1/R2))

print(f'La resistencia total es: {operacionDe_R}')"""

#Algoritmo de resistencias con funciones 

"""def operacionDe_R(r1,r2):
    return 1/((1/r1) + (1/r2))

print(operacionDe_R(int(input("Resistencia r1: ")), int(input("Resistencia r2: "))))"""
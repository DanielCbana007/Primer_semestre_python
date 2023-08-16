#variables & listas 

"""a,b,c = 1, 1.2, "soy una cadena 1"
d = e = f = "el bicho siuuuuuuu" 
array = [1, 1.5, "ejejejej"]
"""

#matriz

"""lista = [[1, 1.4, "Soy una cadena"], ["soy una cadena", 3, False]]

print(lista[1] [2])
print(f"{a}\n{b}\n{c}")
print(f"{d}\n{e}\n{f}")"""

#estructuras de control (if), (while)

"""algo = 2

if (algo == 1):
    print("funciona")
elif(algo == 2):
    print("es increible")
else:
    print("no es igual a 1")"""

"""numero_cucharadoas = 5
cuantas_llevaas = 0

while cuantas_llevaas < numero_cucharadoas:
    cuantas_llevaas = cuantas_llevaas + 1
    print(f"se pone una cucharada, la cual es la numero: {str(cuantas_llevaas)}")"""

#Listas, Diccionarios y estructura de control For

"""milist = ["gato", "perro", "rana", "perro"]
milist.append("pato")
milist.remove("perro")
milist.extend(["mariposa", "hormiga", "gusano"])
milist.insert(0,"Cabra")
for animal in milist:
    print(animal)"""

#diccionario

"""midiccionario = {"nombre":"Daniel", "apellido":"Cabana", "edad":17}
midiccionario.update({"nacionalidad": "colombiano"})
clave = midiccionario.keys()
valor = midiccionario.values()
cantidadDeElementos = midiccionario.items()

for clave, valor in cantidadDeElementos:
    print(f"{clave}: {valor}")"""

#funciones 

"""def resta(numero1 = 0, numero2 = 0):
    return(numero1 - numero2)
    # print(f"la suma es ugual a {str(numero1 + numero2)}")

resultado = resta(numero2 = 5, numero1 = 6)

print(str(resultado))"""

"""def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado = resultado + numero
    return resultado

# suma(2,6,3,43,5,6)

resultado = suma(2,6,3,43,5,6)

print(str(resultado))"""

# clases y objetos 

class familia:
    def __init__(self, nom = "Sin nombre"):
        self.nombre = nom

    def hermano(self, suNombre = "Juan David" ):
        print(f"tengo un hemano que se llama {suNombre}")

Mifamilia = familia("Cabana Trejos")
Mifamilia.hermano()
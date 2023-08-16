class colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    NULL = '\033[0m'

#Ejercicio 1 (Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.)

#codigo:

"""print("¡Hola Mundo!")"""

#Ejercicio 2 (Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable.)

"""saludo = "¡Hola Mundo!"

print(saludo)"""

#Ejercicio 3 (Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.)

"""nombre = input("escriba su nomdre: ")

print(f"¡Hola {nombre}")"""

#Ejercicio 4 (Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética ((3+2)/(2*5))**2.)

"""operacion_aridmetica = ((3+2)/(2*5))**2

print(operacion_aridmetica)"""

#Ejercicio 5 (Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.)

"""num_horas_trabajo = int(input("¿cuantas horas trabajó?: "))
costo_hora = int(input("¿cuanto cuesta una hora trabajada?: "))

def paga():
    return num_horas_trabajo*costo_hora

print(f"su paga es de: {paga()}")"""

#(Escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n. La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma: suma = ((n*(n+1))/2))

"""n = int(input(f"{colors.NULL}escriba el numero n: {colors.NULL}"))
contador = 0
numeros = []

suma = ((n*(n+1))/2)

for i in range(n):
    contador += 1
    numeros.append(contador)

suma2 = sum(numeros)

print(f"{colors.RED}------------------------- SUMA NORMAL -------------------------")
print(colors.GREEN,suma)
print(f"{colors.RED}------------------------- SUMA SICLO -------------------------")
print(colors.GREEN,suma2)"""

#Ejercicio 7 (Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.)

"""peso = float(input(f"{colors.NULL}escriba su peso en kg: "))
estatura = float(input(f"{colors.NULL}escriba su estatura: "))

indice_masa_corporal = peso / (estatura**2)

print(f"{colors.RED}------------------------- SU INDICE DE MASA CORPORAL ES DE -------------------------")
print(colors.GREEN, indice_masa_corporal)"""

#Ejercicio 8 (Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.)

"""n = int(input(f"{colors.NULL}escriba del entero1: "))
m = int(input(f"{colors.NULL}escriba del entero2: "))

def cosiente():
    return n//m
    
def resto():
    return n % m

print(f"{colors.RED}------------------------- RESULTADO -------------------------")
print(f"{colors.GREEN}{n} estre {m}, da un cosiente de: {cosiente()} y un resto de: {resto()}")"""

#Ejercicio 9 (Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.)

"""inmvercion = float(input(f"{colors.NULL}el¿que cantidad decea invertir?: "))
interes = int(input(f"{colors.NULL}¿de cuanto es el interes anual?:"))
years = int(input(f"{colors.NULL}cuantos años desea invertir su capital?: "))
ineteres_anual = 0

def capital_obtenido():
    ineteres_anual = inmvercion*(interes / 100 + 1)**years
    return ineteres_anual

print(f"{colors.RED}------------------------- INTERES ANUAL -------------------------")
print(f"{colors.GREEN}el capital obtenido es de: {capital_obtenido():.2f}")
"""
#Ejercicio 10 (Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.)
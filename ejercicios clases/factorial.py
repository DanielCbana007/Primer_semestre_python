import random, math

decision = int(input("para calcular el factorial de un número dado por el usuario dijite 1, para generar 10 números aleatorios dijite 2, para imprimir la tabla del 9 dijite 3, para imprimir los primeros 20 números impares dijite 4, para imprimir los números primos del 1 al 100 dijite 4: "))

if decision == 1:
    # Pedimos al usuario que ingrese un número entero positivo
    numero = int(input("Ingrese un número entero positivo: "))

    # Verificamos que el número ingresado sea positivo
    if numero <= 0:
        print("El número debe ser positivo.")
    else:
        # Inicializamos el factorial y el contador en 1
        factorial = 1
        contador = 1
        # Calculamos el factorial del número
        while contador <= numero:
            factorial *= contador
            contador += 1
        # Mostramos el resultado
        print(f"El factorial de {numero} es {factorial}")
elif decision == 2:
    numero = 0
    while numero < 10:
        numero += 1
        if numero <= 10:
            num_aleatorio = int(random.random() * ((10 - 1) + 1))
        else:
            break
        print(num_aleatorio)

elif decision == 3:

    multiplo = 0
    resultado = 0
    while multiplo < 10:
        multiplo += 1
        resultado += 1 * 9
        if multiplo <= 10:
            print(f"9 multiplicado por {multiplo} es igual a: {resultado}")
        else:
            break
elif decision == 4:

    numero = 0
    while numero < 60:
        numero += 1
        if numero % 3 == 0:
            print(numero)

elif decision == 5:
    numero = 0

    while numero < 100:
        numero += 1
        if numero % 2 == 0:
            print(numero)

else: 
    print("valor no valido")
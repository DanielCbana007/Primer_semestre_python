import math

opcion_global = int(input("que quiere calcular, 1 para area, 2 para volumen, 3 para perimetro: "))

if opcion_global  == 1:
    
    opcion1 = int(input("decida que area quiere encontrar, 1 para triangulo, 2 para rectanculo, 3 para circulo: "))

    if opcion1 == 1:
        valor1 = int(input("Dijite la base del triangulo: "))
        valor2 = int(input("Dijite la altura del triangulo: "))
        operacion = (valor1 * valor2)/2

        print(f"el area de el triangulo es: {operacion}")
    
    elif opcion1 == 2:
        #area triangulo
        valor1 = int(input("Dijite la base del triangulo: "))
        valor2 = int(input("Dijite la altura del triangulo: "))
        operacion = valor1 * valor2

        print(f"el area de el rectangulo es: {operacion}")
    
    elif opcion1 == 3:
        #area triangulo
        radio = int(input("Dijite el radio del circulo: "))
        operacion = math.pi * (radio**2)

        print(f"el area de el circulo es: {operacion}")
    
    else:
        exit ()
elif opcion_global == 2:
    opcion2 = int(input("decida que volumen quiere encontrar, 1 para esfera, 2 para cilinfro, 3 para cubo: "))
    
    if opcion2 == 1:
        #area triangulo
        radio = int(input("Dijite el radio del circulo: "))
        operacion = (4/3) * math.pi * (radio**3)

        print(f"el volumen de la esfera es: {operacion}")

    elif opcion2 == 2:
        #area triangulo
        area = int(input("Dijite el area del cilindro: "))     
        altura = int(input("Dijite la altura del cilindro: "))
        operacion = area * altura
        
        print(f"el volumen del cilindro es: {operacion}")

    elif opcion2 == 3:
        #area triangulo
        altura = int(input("Dijite la altura del cubo: "))
        operacion = altura**3

        print(f"el volumen del cubo es: {operacion}")

    else:
        exit ()
elif opcion_global == 3:
    opcion3 = int(input("decida que perimetro quiere encontrar, 1 para circulo, 2 para cuadrado, 3 para rectangulo: "))

    if opcion3 == 1:
        radio = int(input("Dijite el radio del circulo: "))
        operacion = (2 * math.pi) * radio

        print(f"el volumen del circulo es: {operacion}")

    elif opcion3 == 2:
        altura = int(input("Dijite la altura del cuadrado: "))
        operacion = 4 * altura

        print(f"el volumen del cuadrado es: {operacion}")

    elif opcion3 == 3:
        altura = int(input("Dijite la altura del rectangulo: "))
        base = int(input("Dijite la base del rectangulo: "))
        operacion = 2 * (altura + base)

        print(f"el volumen del rectangulo es: {operacion}")

    else:
        exit ()
else: 
    print(f"no eligio ningun valor")


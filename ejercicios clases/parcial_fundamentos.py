#pido al usuario su nombre
nombre = input("ingrese su nombre: ")

# #muestro al usuario un mensaje que diga: "bienvenido a su cajero electronico (nombre del usuario)"
saludo = print(f"bienvenido a su cajero electronico {nombre}")

#le pregunto al usuario operacion desea realizar
opciones = int(input("si desea ver el saldo de la cuenta escriba 1, si desea Retirar dinero de la cuenta escriba 2, si desea Consignar dinero a la cuenta de la cuenta escriba 3: "))

#Establesco la cantidad del saldo, el carnet es: 140035699
saldo = (99 * 50)+13

#establesco los condicionales  

#si decidio retirar entonces le pregunto cuanto va a retirar y paso al siguiente condicional
if (opciones == 2):
    valor_retiro = int(input("¿cuanto va a retirar?: "))

    #si el valor del retiro es menor que el saldo paso al siguiente condicional
    if (valor_retiro < saldo):

        #si el valor del retiro es multiplo de 10 y es menor que 200000 paso a los siguientes condicionales
        if(valor_retiro % 10 == 0 and valor_retiro < 200000):

            #si el valor es igual a 10000 muestro al usuario: "la cantidad de billetes por denominación que recibirá son un billete de 10000"
            if (valor_retiro == 10000):
                print("la cantidad de billetes por denominación que recibirá son un billete de 10000")

            #si el valor es igual a 20000 muestro al usuario: "la cantidad de billetes por denominación que recibirá son un billete de 20000"
            if (valor_retiro == 20000):
                print("la cantidad de billetes por denominación que recibirá son un billete de 20000")
            
            #si el valor es igual a 30000 muestro al usuario: "la cantidad de billetes por denominación que recibirá son un billete de 10000 y un billete de 20000"
            if (valor_retiro == 30000):
                print("la cantidad de billetes por denominación que recibirá son un billete de 10000 y un billete de 20000")
            
            #si el valor es igual a 40000 muestro al usuario: "la cantidad de billetes por denominación que recibirá son dos billetes de 20000"
            if (valor_retiro == 40000):
                print("la cantidad de billetes por denominación que recibirá son dos billetes de 20000")
            
            #si el valor es igual a 50000 muestro al usuario: "la cantidad de billetes por denominación que recibirá son un billete de 50000"
            if (valor_retiro == 50000):
                print("la cantidad de billetes por denominación que recibirá son un billete de 50000")

            #si el valor es igual a 60000 muestro al usuario:"la cantidad de billetes por denominación que recibirá son un billete de 50000 y un billete de 10000"
            if (valor_retiro == 60000):
                print("la cantidad de billetes por denominación que recibirá son un billete de 50000 y un billete de 10000")

            #si el valor es igual a 70000 muestro al usuario: "la cantidad de billetes por denominación que recibirá son un billete de 50000 y un billete de 20000"
            if (valor_retiro == 70000):
                print("la cantidad de billetes por denominación que recibirá son un billete de 50000 y un billete de 20000")

            #si el valor es igual a 80000 muestro al usuario: "la cantidad de billetes por denominación que recibirá son un billete de 50000, un billete de 20000 y un billete de 10000"+
            if (valor_retiro == 80000):
                print("la cantidad de billetes por denominación que recibirá son un billete de 50000, un billete de 20000 y un billete de 10000")

            #si el valor es igual a 90000 muestro al usuario: "la cantidad de billetes por denominación que recibirá son un billete de 50000 y dos billetes de 20000"
            if (valor_retiro == 90000):
                print("la cantidad de billetes por denominación que recibirá son un billete de 50000 y dos billetes de 20000")

            #si el valor es igual a 100000 muestro al usuario: "la cantidad de billetes por denominación que recibirá son un billete de 100000"
            if (valor_retiro == 100000):
                print("la cantidad de billetes por denominación que recibirá son un billete de 100000")

            #si el valor es igual a 110000 muestro al usuario: "la cantidad de billetes por denominación que recibirá son un billete de 100000 y un billete de 10000"
            if (valor_retiro == 110000):
                print("la cantidad de billetes por denominación que recibirá son un billete de 100000 y un billete de 10000")

            #si el valor es igual a 120000 muestro al usuario: "la cantidad de billetes por denominación que recibirá son un billete de 100000 y un billete de 20000"
            if (valor_retiro == 120000):
                print("la cantidad de billetes por denominación que recibirá son un billete de 100000 y un billete de 20000")

            #si el valor es igual a 130000 muestro al usuario: "la cantidad de billetes por denominación que recibirá son un billete de 100000, un billete de 10000 y un billete de 20000"
            if (valor_retiro == 130000):
                print("la cantidad de billetes por denominación que recibirá son un billete de 100000, un billete de 10000 y un billete de 20000")

            #si el valor es igual a 140000 muestro al usuario: "la cantidad de billetes por denominación que recibirá son un billete de 100000 y dos billetes de 20000"
            if (valor_retiro == 140000):
                print("la cantidad de billetes por denominación que recibirá son un billete de 100000 y dos billetes de 20000") 

            #si el valor es igual a 150000 muestro al usuario: "la cantidad de billetes por denominación que recibirá son un billete de 100000 y un billete de 50000"
            if (valor_retiro == 150000):
                print("la cantidad de billetes por denominación que recibirá son un billete de 100000 y un billete de 50000")

            #si el valor es igual a 160000 muestro al usuario: "la cantidad de billetes por denominación que recibirá son un billete de 100000, un billete de 50000 y un billete de 10000"
            if (valor_retiro == 160000):
                print("la cantidad de billetes por denominación que recibirá son un billete de 100000, un billete de 50000 y un billete de 10000")

            #si el valor es igual a 170000 muestro al usuario: "la cantidad de billetes por denominación que recibirá son un billete de 100000, un billete de 50000 y un billete de 20000"
            if (valor_retiro == 170000):
                print("la cantidad de billetes por denominación que recibirá son un billete de 100000, un billete de 50000 y un billete de 20000")
            
            #si el valor es igual a 180000 muestro al usuario: "la cantidad de billetes por denominación que recibirá son un billete de 100000, un billete de 50000, un billete de 20000 y un billete de 10000"
            if (valor_retiro == 180000):
                print("la cantidad de billetes por denominación que recibirá son un billete de 100000, un billete de 50000, un billete de 20000 y un billete de 10000")

            #si el valor es igual a 190000 muestro al usuario: "la cantidad de billetes por denominación que recibirá son un billete de 100000, un billete de 50000 y dos billetes de 20000"
            if (valor_retiro == 190000):
                print("la cantidad de billetes por denominación que recibirá son un billete de 100000, un billete de 50000 y dos billetes de 20000")

            #si estas condiciones no se cumplen muestro al usuario: no se puede hacer esta operacion"
            else: 
                print("no se puede hacer esta operacion")
        
        #si esta condiciones no se cumplen muestro al usuario: "error"
        else: 
            print ("error")
    #si esta condiciones no se cumplen muestro al usuario: "el retiro es mayor que el saldo"
    else: 
            print ("el retiro es mayor que el saldo")

#si deside consignar                         
elif (opciones == 3):
     
     #le pregunto cuantos billetes y de que denominacion va a consignar
    denominación_10 = int(input("cuantos billetes de 10.000 consignara"))
    denominación_20 = int(input("cuantos billetes de 20.000 consignara"))
    denominación_50 = int(input("cuantos billetes de 50.000 consignara"))
    denominación_100 = int(input("cuantos billetes de 100.000 consignara"))

    #sumo los billetes 
    calculo = denominación_10 + denominación_20 + denominación_50 + denominación_100
    
    #muestro al usuario: "Su saldo actual es de (elresultado del calculo mas el saldo)"
    print(f"Su saldo actual es de {calculo + saldo}")


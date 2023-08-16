while True:
    
    decision = int(input("¿quiere iniciar el menu?, para iniciar escriba 1, para finalizar escriba 2. : "))
        
    if decision == 1:
      
        nacionalidad = input("¿cual es la nacionalidad del libro? : ")
        num_paginas = int(input("si tiene menos de 100 pag dijite 1, si tiene entre 100 y 300 pag dijite 2, si tiene mas de 300 pag dijite 3. : "))

        if nacionalidad == "argentina" and num_paginas == 1:
            numero_pag = int(input("¿cuantas paginas tiene el libro? : "))
            mes = input("¿en que mes estas?: ")
            valor_hoja = 0.36 
            iva = 0.21
            valor_neto_libro = (numero_pag * valor_hoja)/2
            
            if mes == "12" or mes == "1" or mes == "2":
                rebaja = [17.85, "Invierno"]

                print(f"el varo del libro en pesos Argentinos es de: {round(valor_neto_libro,2)}\n el IVA es de: {round((valor_neto_libro)*iva,2)}\n el descuento es de: {round(valor_hoja * rebaja[0],2)}\n el valor final del libro es de: {round(((valor_hoja * rebaja[0])-( valor_neto_libro *iva)*-1),2)}\n la estacion del año es: {rebaja[1]}\nel varo del libro en pesos Colombianos es de: {round(num_paginas * (valor_hoja * 20.76),2)}\n el IVA es de: {round(valor_neto_libro*0.19,2)}\n el descuento es de: {round((valor_hoja * 20.76) * rebaja[0],2)}\n el valor final del libro es de: {round(((valor_hoja * 20.76) * rebaja[0]) - (num_paginas * (valor_hoja * 20.76)),2)}\n la estacion del año es: {rebaja[1]}")

            elif mes == "3" or mes == "4" or mes == "5":
                rebaja = [12.35, "Primavera"]

                print(f"el varo del libro en pesos Argentinos es de: {round(valor_neto_libro,2)}\n el IVA es de: {round((valor_neto_libro)*iva,2)}\n el descuento es de: {round(valor_hoja * rebaja[0],2)}\n el valor final del libro es de: {round(((valor_hoja * rebaja[0])-( valor_neto_libro *iva)*-1),2)}\n la estacion del año es: {rebaja[1]}\nel varo del libro en pesos Colombianos es de: {round(num_paginas * (valor_hoja * 20.76),2)}\n el IVA es de: {round(valor_neto_libro*0.19,2)}\n el descuento es de: {round((valor_hoja * 20.76) * rebaja[0],2)}\n el valor final del libro es de: {round(((valor_hoja * 20.76) * rebaja[0]) - (num_paginas * (valor_hoja * 20.76)),2)}\n la estacion del año es: {rebaja[1]}")
            
            elif mes == "6" or mes == "7" or mes == "8":
                rebaja = [10.05, "Verano"]

                print(f"el varo del libro en pesos Argentinos es de: {round(valor_neto_libro,2)}\n el IVA es de: {round((valor_neto_libro)*iva,2)}\n el descuento es de: {round(valor_hoja * rebaja[0],2)}\n el valor final del libro es de: {round(((valor_hoja * rebaja[0])-( valor_neto_libro *iva)*-1),2)}\n la estacion del año es: {rebaja[1]}\nel varo del libro en pesos Colombianos es de: {round(num_paginas * (valor_hoja * 20.76),2)}\n el IVA es de: {round(valor_neto_libro*0.19,2)}\n el descuento es de: {round((valor_hoja * 20.76) * rebaja[0],2)}\n el valor final del libro es de: {round(((valor_hoja * 20.76) * rebaja[0]) - (num_paginas * (valor_hoja * 20.76)),2)}\n la estacion del año es: {rebaja[1]}")
            
            elif mes == "9" or mes == "10" or mes == "11":
                rebaja = [8.75, "Otoño"]

                print(f"el varo del libro en pesos Argentinos es de: {round(valor_neto_libro,2)}\n el IVA es de: {round((valor_neto_libro)*iva,2)}\n el descuento es de: {round(valor_hoja * rebaja[0],2)}\n el valor final del libro es de: {round(((valor_hoja * rebaja[0])-( valor_neto_libro *iva)*-1),2)}\n la estacion del año es: {rebaja[1]}\nel varo del libro en pesos Colombianos es de: {round(num_paginas * (valor_hoja * 20.76),2)}\n el IVA es de: {round(valor_neto_libro*0.19,2)}\n el descuento es de: {round((valor_hoja * 20.76) * rebaja[0],2)}\n el valor final del libro es de: {round(((valor_hoja * 20.76) * rebaja[0]) - (num_paginas * (valor_hoja * 20.76)),2)}\n la estacion del año es: {rebaja[1]}")

        elif nacionalidad == "argentina" and num_paginas == 2:
            numero_pag = int(input("¿cuantas paginas tiene el libro? : "))
            mes = input("¿en que mes estas?: ")
            valor_hoja =    0.54 
            iva = 21
            valor_neto_libro = (numero_pag * valor_hoja)/2

            if mes == "12" or mes == "1" or mes == "2":
                rebaja = [17.85, "Invierno"]

                print(f"el varo del libro en pesos Argentinos es de: {round(valor_neto_libro,2)}\n el IVA es de: {round((valor_neto_libro)*iva,2)}\n el descuento es de: {round(valor_hoja * rebaja[0],2)}\n el valor final del libro es de: {round(((valor_hoja * rebaja[0])-( valor_neto_libro *iva)*-1),2)}\n la estacion del año es: {rebaja[1]}\nel varo del libro en pesos Colombianos es de: {round(num_paginas * (valor_hoja * 20.76),2)}\n el IVA es de: {round(valor_neto_libro*0.19,2)}\n el descuento es de: {round((valor_hoja * 20.76) * rebaja[0],2)}\n el valor final del libro es de: {round(((valor_hoja * 20.76) * rebaja[0]) - (num_paginas * (valor_hoja * 20.76)),2)}\n la estacion del año es: {rebaja[1]}")

            elif mes == "3" or mes == "4" or mes == "5":
                rebaja = [12.35, "Primavera"]

                print(f"el varo del libro en pesos Argentinos es de: {round(valor_neto_libro,2)}\n el IVA es de: {round((valor_neto_libro)*iva,2)}\n el descuento es de: {round(valor_hoja * rebaja[0],2)}\n el valor final del libro es de: {round(((valor_hoja * rebaja[0])-( valor_neto_libro *iva)*-1),2)}\n la estacion del año es: {rebaja[1]}\nel varo del libro en pesos Colombianos es de: {round(num_paginas * (valor_hoja * 20.76),2)}\n el IVA es de: {round(valor_neto_libro*0.19,2)}\n el descuento es de: {round((valor_hoja * 20.76) * rebaja[0],2)}\n el valor final del libro es de: {round(((valor_hoja * 20.76) * rebaja[0]) - (num_paginas * (valor_hoja * 20.76)),2)}\n la estacion del año es: {rebaja[1]}")
            
            elif "6" or mes == "7" or mes == "8":
                rebaja = [10.05, "Verano"]

                print(f"el varo del libro en pesos Argentinos es de: {round(valor_neto_libro,2)}\n el IVA es de: {round((valor_neto_libro)*iva,2)}\n el descuento es de: {round(valor_hoja * rebaja[0],2)}\n el valor final del libro es de: {round(((valor_hoja * rebaja[0])-( valor_neto_libro *iva)*-1),2)}\n la estacion del año es: {rebaja[1]}\nel varo del libro en pesos Colombianos es de: {round(num_paginas * (valor_hoja * 20.76),2)}\n el IVA es de: {round(valor_neto_libro*0.19,2)}\n el descuento es de: {round((valor_hoja * 20.76) * rebaja[0],2)}\n el valor final del libro es de: {round(((valor_hoja * 20.76) * rebaja[0]) - (num_paginas * (valor_hoja * 20.76)),2)}\n la estacion del año es: {rebaja[1]}")
            
            elif mes == "9" or mes == "10" or mes == "11":
                rebaja = [8.75, "Otoño"]

                print(f"el varo del libro en pesos Argentinos es de: {round(valor_neto_libro,2)}\n el IVA es de: {round((valor_neto_libro)*iva,2)}\n el descuento es de: {round(valor_hoja * rebaja[0],2)}\n el valor final del libro es de: {round(((valor_hoja * rebaja[0])-( valor_neto_libro *iva)*-1),2)}\n la estacion del año es: {rebaja[1]}\nel varo del libro en pesos Colombianos es de: {round(num_paginas * (valor_hoja * 20.76),2)}\n el IVA es de: {round(valor_neto_libro*0.19,2)}\n el descuento es de: {round((valor_hoja * 20.76) * rebaja[0],2)}\n el valor final del libro es de: {round(((valor_hoja * 20.76) * rebaja[0]) - (num_paginas * (valor_hoja * 20.76)),2)}\n la estacion del año es: {rebaja[1]}")
            
        elif nacionalidad == "argentina" and num_paginas == 3:
            numero_pag = int(input("¿cuantas paginas tiene el libro? : "))
            mes = input("¿en que mes estas?: ")
            valor_hoja =    0.98 
            iva = 21
            valor_neto_libro = (numero_pag * valor_hoja)/2

            if mes == "12" or mes == "1" or mes == "2":
                rebaja = [17.85, "Invierno"]

                print(f"el varo del libro en pesos Argentinos es de: {round(valor_neto_libro,2)}\n el IVA es de: {round((valor_neto_libro)*iva,2)}\n el descuento es de: {round(valor_hoja * rebaja[0],2)}\n el valor final del libro es de: {round(((valor_hoja * rebaja[0])-( valor_neto_libro *iva)*-1),2)}\n la estacion del año es: {rebaja[1]}\nel varo del libro en pesos Colombianos es de: {round(num_paginas * (valor_hoja * 20.76),2)}\n el IVA es de: {round(valor_neto_libro*0.19,2)}\n el descuento es de: {round((valor_hoja * 20.76) * rebaja[0],2)}\n el valor final del libro es de: {round(((valor_hoja * 20.76) * rebaja[0]) - (num_paginas * (valor_hoja * 20.76)),2)}\n la estacion del año es: {rebaja[1]}")
            

            elif mes == "3" or mes == "4" or mes == "5":
                rebaja = [12.35, "Primavera"]

                print(f"el varo del libro en pesos Argentinos es de: {round(valor_neto_libro,2)}\n el IVA es de: {round((valor_neto_libro)*iva,2)}\n el descuento es de: {round(valor_hoja * rebaja[0],2)}\n el valor final del libro es de: {round(((valor_hoja * rebaja[0])-( valor_neto_libro *iva)*-1),2)}\n la estacion del año es: {rebaja[1]}\nel varo del libro en pesos Colombianos es de: {round(num_paginas * (valor_hoja * 20.76),2)}\n el IVA es de: {round(valor_neto_libro*0.19,2)}\n el descuento es de: {round((valor_hoja * 20.76) * rebaja[0],2)}\n el valor final del libro es de: {round(((valor_hoja * 20.76) * rebaja[0]) - (num_paginas * (valor_hoja * 20.76)),2)}\n la estacion del año es: {rebaja[1]}")
            
            
            elif "6" or mes == "7" or mes == "8":
                rebaja = [10.05, "Verano"]

                print(f"el varo del libro en pesos Argentinos es de: {round(valor_neto_libro,2)}\n el IVA es de: {round((valor_neto_libro)*iva,2)}\n el descuento es de: {round(valor_hoja * rebaja[0],2)}\n el valor final del libro es de: {round(((valor_hoja * rebaja[0])-( valor_neto_libro *iva)*-1),2)}\n la estacion del año es: {rebaja[1]}\nel varo del libro en pesos Colombianos es de: {round(num_paginas * (valor_hoja * 20.76),2)}\n el IVA es de: {round(valor_neto_libro*0.19,2)}\n el descuento es de: {round((valor_hoja * 20.76) * rebaja[0],2)}\n el valor final del libro es de: {round(((valor_hoja * 20.76) * rebaja[0]) - (num_paginas * (valor_hoja * 20.76)),2)}\n la estacion del año es: {rebaja[1]}")
            
            
            elif mes == "9" or mes == "10" or mes == "11":
                rebaja = [8.75, "Otoño"]

                print(f"el varo del libro en pesos Argentinos es de: {round(valor_neto_libro,2)}\n el IVA es de: {round((valor_neto_libro)*iva,2)}\n el descuento es de: {round(valor_hoja * rebaja[0],2)}\n el valor final del libro es de: {round(((valor_hoja * rebaja[0])-( valor_neto_libro *iva)*-1),2)}\n la estacion del año es: {rebaja[1]}\nel varo del libro en pesos Colombianos es de: {round(num_paginas * (valor_hoja * 20.76),2)}\n el IVA es de: {round(valor_neto_libro*0.19,2)}\n el descuento es de: {round((valor_hoja * 20.76) * rebaja[0],2)}\n el valor final del libro es de: {round(((valor_hoja * 20.76) * rebaja[0]) - (num_paginas * (valor_hoja * 20.76)),2)}\n la estacion del año es: {rebaja[1]}")
            
        elif nacionalidad == "america" and num_paginas == 1:
            numero_pag = int(input("¿cuantas paginas tiene el libro? : "))
            mes = input("¿en que mes estas?: ")
            valor_hoja =    2 
            iva = 9
            valor_neto_libro = (numero_pag * valor_hoja)/2
            
            if mes == "12" or mes == "1" or mes == "2":
                rebaja = [17.85, "Invierno"]

                print(f"el varo del libro en dolar es de: {round(valor_neto_libro,2)}\n el IVA es de: {round((num_paginas * valor_hoja)*iva,2)}\n el descuento es de: {round(valor_hoja * rebaja[0],2)}\n el valor final del libro es de: {(round((valor_hoja * rebaja[0])-((num_paginas * valor_hoja)*iva)*-1),2)}\n la estacion del año es: {rebaja[1]}\nel varo del libro en pesos Colombianos es de: {round(num_paginas * (valor_hoja * 4526.14),2)}\n el IVA es de: {(num_paginas * valor_hoja)*0.19}\n el descuento es de: {round((valor_hoja * 4526.14) * rebaja[0],2)}\n el valor final del libro es de: {round(((valor_hoja * 4526.14) * rebaja[0]) - (num_paginas * (valor_hoja * 4526.14)),2)}\n la estacion del año es: {rebaja[1]}")

            elif mes == "3" or mes == "4" or mes == "5":
                rebaja = [12.35, "Primavera"]

                print(f"el varo del libro en dolar es de: {round(valor_neto_libro,2)}\n el IVA es de: {round((num_paginas * valor_hoja)*iva,2)}\n el descuento es de: {round(valor_hoja * rebaja[0],2)}\n el valor final del libro es de: {(round((valor_hoja * rebaja[0])-((num_paginas * valor_hoja)*iva)*-1),2)}\n la estacion del año es: {rebaja[1]}\nel varo del libro en pesos Colombianos es de: {round(num_paginas * (valor_hoja * 4526.14),2)}\n el IVA es de: {(num_paginas * valor_hoja)*0.19}\n el descuento es de: {round((valor_hoja * 4526.14) * rebaja[0],2)}\n el valor final del libro es de: {round(((valor_hoja * 4526.14) * rebaja[0]) - (num_paginas * (valor_hoja * 4526.14)),2)}\n la estacion del año es: {rebaja[1]}")
            
            elif "6" or mes == "7" or mes == "8":
                rebaja = [10.05, "Verano"]

                print(f"el varo del libro en dolar es de: {round(valor_neto_libro,2)}\n el IVA es de: {round((num_paginas * valor_hoja)*iva,2)}\n el descuento es de: {round(valor_hoja * rebaja[0],2)}\n el valor final del libro es de: {(round((valor_hoja * rebaja[0])-((num_paginas * valor_hoja)*iva)*-1),2)}\n la estacion del año es: {rebaja[1]}\nel varo del libro en pesos Colombianos es de: {round(num_paginas * (valor_hoja * 4526.14),2)}\n el IVA es de: {(num_paginas * valor_hoja)*0.19}\n el descuento es de: {round((valor_hoja * 4526.14) * rebaja[0],2)}\n el valor final del libro es de: {round(((valor_hoja * 4526.14) * rebaja[0]) - (num_paginas * (valor_hoja * 4526.14)),2)}\n la estacion del año es: {rebaja[1]}")
            
            elif mes == "9" or mes == "10" or mes == "11":
                rebaja = [8.75, "Otoño"]

                print(f"el varo del libro en dolar es de: {round(valor_neto_libro,2)}\n el IVA es de: {round((num_paginas * valor_hoja)*iva,2)}\n el descuento es de: {round(valor_hoja * rebaja[0],2)}\n el valor final del libro es de: {(round((valor_hoja * rebaja[0])-((num_paginas * valor_hoja)*iva)*-1),2)}\n la estacion del año es: {rebaja[1]}\nel varo del libro en pesos Colombianos es de: {round(num_paginas * (valor_hoja * 4526.14),2)}\n el IVA es de: {(num_paginas * valor_hoja)*0.19}\n el descuento es de: {round((valor_hoja * 4526.14) * rebaja[0],2)}\n el valor final del libro es de: {round(((valor_hoja * 4526.14) * rebaja[0]) - (num_paginas * (valor_hoja * 4526.14)),2)}\n la estacion del año es: {rebaja[1]}")

        elif nacionalidad == "america" and num_paginas == 2:
            numero_pag = int(input("¿cuantas paginas tiene el libro? : "))
            mes = input("¿en que mes estas?: ")
            valor_hoja =    4
            iva = 9
            valor_neto_libro = (numero_pag * valor_hoja)/2

            if mes == "12" or mes == "1" or mes == "2":
                rebaja = [17.85, "Invierno"]

                print(f"el varo del libro en dolar es de: {round(valor_neto_libro,2)}\n el IVA es de: {round((num_paginas * valor_hoja)*iva,2)}\n el descuento es de: {round(valor_hoja * rebaja[0],2)}\n el valor final del libro es de: {(round((valor_hoja * rebaja[0])-((num_paginas * valor_hoja)*iva)*-1),2)}\n la estacion del año es: {rebaja[1]}\nel varo del libro en pesos Colombianos es de: {round(num_paginas * (valor_hoja * 4526.14),2)}\n el IVA es de: {(num_paginas * valor_hoja)*0.19}\n el descuento es de: {round((valor_hoja * 4526.14) * rebaja[0],2)}\n el valor final del libro es de: {round(((valor_hoja * 4526.14) * rebaja[0]) - (num_paginas * (valor_hoja * 4526.14)),2)}\n la estacion del año es: {rebaja[1]}")

            elif mes == "3" or mes == "4" or mes == "5":
                rebaja = [12.35, "Primavera"]

                print(f"el varo del libro en dolar es de: {round(valor_neto_libro,2)}\n el IVA es de: {round((num_paginas * valor_hoja)*iva,2)}\n el descuento es de: {round(valor_hoja * rebaja[0],2)}\n el valor final del libro es de: {(round((valor_hoja * rebaja[0])-((num_paginas * valor_hoja)*iva)*-1),2)}\n la estacion del año es: {rebaja[1]}\nel varo del libro en pesos Colombianos es de: {round(num_paginas * (valor_hoja * 4526.14),2)}\n el IVA es de: {(num_paginas * valor_hoja)*0.19}\n el descuento es de: {round((valor_hoja * 4526.14) * rebaja[0],2)}\n el valor final del libro es de: {round(((valor_hoja * 4526.14) * rebaja[0]) - (num_paginas * (valor_hoja * 4526.14)),2)}\n la estacion del año es: {rebaja[1]}")
            
            elif "6" or mes == "7" or mes == "8":
                rebaja = [10.05, "Verano"]

                print(f"el varo del libro en dolar es de: {round(valor_neto_libro,2)}\n el IVA es de: {round((num_paginas * valor_hoja)*iva,2)}\n el descuento es de: {round(valor_hoja * rebaja[0],2)}\n el valor final del libro es de: {(round((valor_hoja * rebaja[0])-((num_paginas * valor_hoja)*iva)*-1),2)}\n la estacion del año es: {rebaja[1]}\nel varo del libro en pesos Colombianos es de: {round(num_paginas * (valor_hoja * 4526.14),2)}\n el IVA es de: {(num_paginas * valor_hoja)*0.19}\n el descuento es de: {round((valor_hoja * 4526.14) * rebaja[0],2)}\n el valor final del libro es de: {round(((valor_hoja * 4526.14) * rebaja[0]) - (num_paginas * (valor_hoja * 4526.14)),2)}\n la estacion del año es: {rebaja[1]}")
            
            elif mes == "9" or mes == "10" or mes == "11":
                rebaja = [8.75, "Otoño"]

                print(f"el varo del libro en dolar es de: {round(valor_neto_libro,2)}\n el IVA es de: {round((num_paginas * valor_hoja)*iva,2)}\n el descuento es de: {round(valor_hoja * rebaja[0],2)}\n el valor final del libro es de: {(round((valor_hoja * rebaja[0])-((num_paginas * valor_hoja)*iva)*-1),2)}\n la estacion del año es: {rebaja[1]}\nel varo del libro en pesos Colombianos es de: {round(num_paginas * (valor_hoja * 4526.14),2)}\n el IVA es de: {(num_paginas * valor_hoja)*0.19}\n el descuento es de: {round((valor_hoja * 4526.14) * rebaja[0],2)}\n el valor final del libro es de: {round(((valor_hoja * 4526.14) * rebaja[0]) - (num_paginas * (valor_hoja * 4526.14)),2)}\n la estacion del año es: {rebaja[1]}")

        elif nacionalidad == "america" and num_paginas == 3:
            numero_pag = int(input("¿cuantas paginas tiene el libro? : "))
            mes = input("¿en que mes estas?: ")
            valor_hoja =    6 
            iva = 9
            valor_neto_libro = (numero_pag * valor_hoja)/2

            if mes == "12" or mes == "1" or mes == "2":
                rebaja = [17.85, "Invierno"]

                print(f"el varo del libro en dolar es de: {round(valor_neto_libro,2)}\n el IVA es de: {round((num_paginas * valor_hoja)*iva,2)}\n el descuento es de: {round(valor_hoja * rebaja[0],2)}\n el valor final del libro es de: {(round((valor_hoja * rebaja[0])-((num_paginas * valor_hoja)*iva)*-1),2)}\n la estacion del año es: {rebaja[1]}\nel varo del libro en pesos Colombianos es de: {round(num_paginas * (valor_hoja * 4526.14),2)}\n el IVA es de: {(num_paginas * valor_hoja)*0.19}\n el descuento es de: {round((valor_hoja * 4526.14) * rebaja[0],2)}\n el valor final del libro es de: {round(((valor_hoja * 4526.14) * rebaja[0]) - (num_paginas * (valor_hoja * 4526.14)),2)}\n la estacion del año es: {rebaja[1]}")

            elif mes == "3" or mes == "4" or mes == "5":
                rebaja = [12.35, "Primavera"]

                print(f"el varo del libro en dolar es de: {round(valor_neto_libro,2)}\n el IVA es de: {round((num_paginas * valor_hoja)*iva,2)}\n el descuento es de: {round(valor_hoja * rebaja[0],2)}\n el valor final del libro es de: {(round((valor_hoja * rebaja[0])-((num_paginas * valor_hoja)*iva)*-1),2)}\n la estacion del año es: {rebaja[1]}\nel varo del libro en pesos Colombianos es de: {round(num_paginas * (valor_hoja * 4526.14),2)}\n el IVA es de: {(num_paginas * valor_hoja)*0.19}\n el descuento es de: {round((valor_hoja * 4526.14) * rebaja[0],2)}\n el valor final del libro es de: {round(((valor_hoja * 4526.14) * rebaja[0]) - (num_paginas * (valor_hoja * 4526.14)),2)}\n la estacion del año es: {rebaja[1]}")
            
            elif "6" or mes == "7" or mes == "8":
                rebaja = [10.05, "Verano"]

                print(f"el varo del libro en dolar es de: {round(valor_neto_libro,2)}\n el IVA es de: {round((num_paginas * valor_hoja)*iva,2)}\n el descuento es de: {round(valor_hoja * rebaja[0],2)}\n el valor final del libro es de: {(round((valor_hoja * rebaja[0])-((num_paginas * valor_hoja)*iva)*-1),2)}\n la estacion del año es: {rebaja[1]}\nel varo del libro en pesos Colombianos es de: {round(num_paginas * (valor_hoja * 4526.14),2)}\n el IVA es de: {(num_paginas * valor_hoja)*0.19}\n el descuento es de: {round((valor_hoja * 4526.14) * rebaja[0],2)}\n el valor final del libro es de: {round(((valor_hoja * 4526.14) * rebaja[0]) - (num_paginas * (valor_hoja * 4526.14)),2)}\n la estacion del año es: {rebaja[1]}")

            elif mes == "9" or mes == "10" or mes == "11":
                rebaja = [8.75, "Otoño"]

                print(f"el varo del libro en dolar es de: {round(valor_neto_libro,2)}\n el IVA es de: {round((num_paginas * valor_hoja)*iva,2)}\n el descuento es de: {round(valor_hoja * rebaja[0],2)}\n el valor final del libro es de: {(round((valor_hoja * rebaja[0])-((num_paginas * valor_hoja)*iva)*-1),2)}\n la estacion del año es: {rebaja[1]}\nel varo del libro en pesos Colombianos es de: {round(num_paginas * (valor_hoja * 4526.14),2)}\n el IVA es de: {(num_paginas * valor_hoja)*0.19}\n el descuento es de: {round((valor_hoja * 4526.14) * rebaja[0],2)}\n el valor final del libro es de: {round(((valor_hoja * 4526.14) * rebaja[0]) - (num_paginas * (valor_hoja * 4526.14)),2)}\n la estacion del año es: {rebaja[1]}")

        elif nacionalidad == "europa" and num_paginas == 1:
            numero_pag = int(input("¿cuantas paginas tiene el libro? : "))
            mes = input("¿en que mes estas?: ")
            valor_hoja =    0.4 * 2
            iva = 25
            valor_neto_libro = (numero_pag * valor_hoja)/2

            if mes == "12" or mes == "1" or mes == "2":
                rebaja = [17.85, "Invierno"]

                print(f"el varo del libro en Euro es de: {round(valor_neto_libro,2)}\n el IVA es de: {round((num_paginas * valor_hoja)*iva,2)}\n el descuento es de: {round(valor_hoja * rebaja[0],2)}\n el valor final del libro es de: {round(((valor_hoja * rebaja[0])-((num_paginas * valor_hoja)*iva)*-1),2)}\n la estacion del año es: {rebaja[1]}\nel varo del libro en pesos Colombianos es de: {round(num_paginas * (valor_hoja * 4960.08),2)}\n el IVA es de: {round((num_paginas * valor_hoja)*0.19,2)}\n el descuento es de: {round((valor_hoja * 4960.08) * rebaja[0],2)}\n el valor final del libro es de: {round(((valor_hoja * 4960.08) * rebaja[0]) - (num_paginas * (valor_hoja * 4960.08)),2)}\n la estacion del año es: {rebaja[1]}")

            elif mes == "3" or mes == "4" or mes == "5":
                rebaja = [12.35, "Primavera"]

                print(f"el varo del libro en Euro es de: {round(valor_neto_libro,2)}\n el IVA es de: {round((num_paginas * valor_hoja)*iva,2)}\n el descuento es de: {round(valor_hoja * rebaja[0],2)}\n el valor final del libro es de: {round(((valor_hoja * rebaja[0])-((num_paginas * valor_hoja)*iva)*-1),2)}\n la estacion del año es: {rebaja[1]}\nel varo del libro en pesos Colombianos es de: {round(num_paginas * (valor_hoja * 4960.08),2)}\n el IVA es de: {round((num_paginas * valor_hoja)*0.19,2)}\n el descuento es de: {round((valor_hoja * 4960.08) * rebaja[0],2)}\n el valor final del libro es de: {round(((valor_hoja * 4960.08) * rebaja[0]) - (num_paginas * (valor_hoja * 4960.08)),2)}\n la estacion del año es: {rebaja[1]}")
            
            elif "6" or mes == "7" or mes == "8":
                rebaja = [10.05, "Verano"]

                print(f"el varo del libro en Euro es de: {round(valor_neto_libro,2)}\n el IVA es de: {round((num_paginas * valor_hoja)*iva,2)}\n el descuento es de: {round(valor_hoja * rebaja[0],2)}\n el valor final del libro es de: {round(((valor_hoja * rebaja[0])-((num_paginas * valor_hoja)*iva)*-1),2)}\n la estacion del año es: {rebaja[1]}\nel varo del libro en pesos Colombianos es de: {round(num_paginas * (valor_hoja * 4960.08),2)}\n el IVA es de: {round((num_paginas * valor_hoja)*0.19,2)}\n el descuento es de: {round((valor_hoja * 4960.08) * rebaja[0],2)}\n el valor final del libro es de: {round(((valor_hoja * 4960.08) * rebaja[0]) - (num_paginas * (valor_hoja * 4960.08)),2)}\n la estacion del año es: {rebaja[1]}")
            
            elif mes == "9" or mes == "10" or mes == "11":
                rebaja = [8.75, "Otoño"]

                print(f"el varo del libro en Euro es de: {round(valor_neto_libro,2)}\n el IVA es de: {round((num_paginas * valor_hoja)*iva,2)}\n el descuento es de: {round(valor_hoja * rebaja[0],2)}\n el valor final del libro es de: {round(((valor_hoja * rebaja[0])-((num_paginas * valor_hoja)*iva)*-1),2)}\n la estacion del año es: {rebaja[1]}\nel varo del libro en pesos Colombianos es de: {round(num_paginas * (valor_hoja * 4960.08),2)}\n el IVA es de: {round((num_paginas * valor_hoja)*0.19,2)}\n el descuento es de: {round((valor_hoja * 4960.08) * rebaja[0],2)}\n el valor final del libro es de: {round(((valor_hoja * 4960.08) * rebaja[0]) - (num_paginas * (valor_hoja * 4960.08)),2)}\n la estacion del año es: {rebaja[1]}")

        elif nacionalidad == "europa" and num_paginas == 2:
            numero_pag = int(input("¿cuantas paginas tiene el libro? : "))
            mes = input("¿en que mes estas?: ")
            valor_hoja =    0.8 * 2
            iva = 25
            valor_neto_libro = (numero_pag * valor_hoja)/2

            if mes == "12" or mes == "1" or mes == "2":
                rebaja = [17.85, "Invierno"]

                print(f"el varo del libro en Euro es de: {round(valor_neto_libro,2)}\n el IVA es de: {round((num_paginas * valor_hoja)*iva,2)}\n el descuento es de: {round(valor_hoja * rebaja[0],2)}\n el valor final del libro es de: {round(((valor_hoja * rebaja[0])-((num_paginas * valor_hoja)*iva)*-1),2)}\n la estacion del año es: {rebaja[1]}\nel varo del libro en pesos Colombianos es de: {round(num_paginas * (valor_hoja * 4960.08),2)}\n el IVA es de: {round((num_paginas * valor_hoja)*0.19,2)}\n el descuento es de: {round((valor_hoja * 4960.08) * rebaja[0],2)}\n el valor final del libro es de: {round(((valor_hoja * 4960.08) * rebaja[0]) - (num_paginas * (valor_hoja * 4960.08)),2)}\n la estacion del año es: {rebaja[1]}")

            elif mes == "3" or mes == "4" or mes == "5":
                rebaja = [12.35, "Primavera"]

                print(f"el varo del libro en Euro es de: {round(valor_neto_libro,2)}\n el IVA es de: {round((num_paginas * valor_hoja)*iva,2)}\n el descuento es de: {round(valor_hoja * rebaja[0],2)}\n el valor final del libro es de: {round(((valor_hoja * rebaja[0])-((num_paginas * valor_hoja)*iva)*-1),2)}\n la estacion del año es: {rebaja[1]}\nel varo del libro en pesos Colombianos es de: {round(num_paginas * (valor_hoja * 4960.08),2)}\n el IVA es de: {round((num_paginas * valor_hoja)*0.19,2)}\n el descuento es de: {round((valor_hoja * 4960.08) * rebaja[0],2)}\n el valor final del libro es de: {round(((valor_hoja * 4960.08) * rebaja[0]) - (num_paginas * (valor_hoja * 4960.08)),2)}\n la estacion del año es: {rebaja[1]}")
            
            elif "6" or mes == "7" or mes == "8":
                rebaja = [10.05, "Verano"]

                print(f"el varo del libro en Euro es de: {round(valor_neto_libro,2)}\n el IVA es de: {round((num_paginas * valor_hoja)*iva,2)}\n el descuento es de: {round(valor_hoja * rebaja[0],2)}\n el valor final del libro es de: {round(((valor_hoja * rebaja[0])-((num_paginas * valor_hoja)*iva)*-1),2)}\n la estacion del año es: {rebaja[1]}\nel varo del libro en pesos Colombianos es de: {round(num_paginas * (valor_hoja * 4960.08),2)}\n el IVA es de: {round((num_paginas * valor_hoja)*0.19,2)}\n el descuento es de: {round((valor_hoja * 4960.08) * rebaja[0],2)}\n el valor final del libro es de: {round(((valor_hoja * 4960.08) * rebaja[0]) - (num_paginas * (valor_hoja * 4960.08)),2)}\n la estacion del año es: {rebaja[1]}")
            
            elif mes == "9" or mes == "10" or mes == "11":
                rebaja = [8.75, "Otoño"]

                print(f"el varo del libro en Euro es de: {round(valor_neto_libro,2)}\n el IVA es de: {round((num_paginas * valor_hoja)*iva,2)}\n el descuento es de: {round(valor_hoja * rebaja[0],2)}\n el valor final del libro es de: {round(((valor_hoja * rebaja[0])-((num_paginas * valor_hoja)*iva)*-1),2)}\n la estacion del año es: {rebaja[1]}\nel varo del libro en pesos Colombianos es de: {round(num_paginas * (valor_hoja * 4960.08),2)}\n el IVA es de: {round((num_paginas * valor_hoja)*0.19,2)}\n el descuento es de: {round((valor_hoja * 4960.08) * rebaja[0],2)}\n el valor final del libro es de: {round(((valor_hoja * 4960.08) * rebaja[0]) - (num_paginas * (valor_hoja * 4960.08)),2)}\n la estacion del año es: {rebaja[1]}")

        elif nacionalidad == "europa" and num_paginas == 3:
            numero_pag = int(input("¿cuantas paginas tiene el libro? : "))
            mes = input("¿en que mes estas?: ")
            valor_hoja =    0.10 * 2
            iva = 25
            valor_neto_libro = (numero_pag * valor_hoja)/2

            if mes == "12" or mes == "1" or mes == "2":
                rebaja = [17.85, "Invierno"]

                print(f"el varo del libro en Euro es de: {round(valor_neto_libro,2)}\n el IVA es de: {round((num_paginas * valor_hoja)*iva,2)}\n el descuento es de: {round(valor_hoja * rebaja[0],2)}\n el valor final del libro es de: {round(((valor_hoja * rebaja[0])-((num_paginas * valor_hoja)*iva)*-1),2)}\n la estacion del año es: {rebaja[1]}\nel varo del libro en pesos Colombianos es de: {round(num_paginas * (valor_hoja * 4960.08),2)}\n el IVA es de: {round((num_paginas * valor_hoja)*0.19,2)}\n el descuento es de: {round((valor_hoja * 4960.08) * rebaja[0],2)}\n el valor final del libro es de: {round(((valor_hoja * 4960.08) * rebaja[0]) - (num_paginas * (valor_hoja * 4960.08)),2)}\n la estacion del año es: {rebaja[1]}")

            elif mes == "3" or mes == "4" or mes == "5":
                rebaja = [12.35, "Primavera"]

                print(f"el varo del libro en Euro es de: {round(valor_neto_libro,2)}\n el IVA es de: {round((num_paginas * valor_hoja)*iva,2)}\n el descuento es de: {round(valor_hoja * rebaja[0],2)}\n el valor final del libro es de: {round(((valor_hoja * rebaja[0])-((num_paginas * valor_hoja)*iva)*-1),2)}\n la estacion del año es: {rebaja[1]}\nel varo del libro en pesos Colombianos es de: {round(num_paginas * (valor_hoja * 4960.08),2)}\n el IVA es de: {round((num_paginas * valor_hoja)*0.19,2)}\n el descuento es de: {round((valor_hoja * 4960.08) * rebaja[0],2)}\n el valor final del libro es de: {round(((valor_hoja * 4960.08) * rebaja[0]) - (num_paginas * (valor_hoja * 4960.08)),2)}\n la estacion del año es: {rebaja[1]}")
            
            elif "6" or mes == "7" or mes == "8":
                rebaja = [10.05, "Verano"]

                print(f"el varo del libro en Euro es de: {round(valor_neto_libro,2)}\n el IVA es de: {round((num_paginas * valor_hoja)*iva,2)}\n el descuento es de: {round(valor_hoja * rebaja[0],2)}\n el valor final del libro es de: {round(((valor_hoja * rebaja[0])-((num_paginas * valor_hoja)*iva)*-1),2)}\n la estacion del año es: {rebaja[1]}\nel varo del libro en pesos Colombianos es de: {round(num_paginas * (valor_hoja * 4960.08),2)}\n el IVA es de: {round((num_paginas * valor_hoja)*0.19,2)}\n el descuento es de: {round((valor_hoja * 4960.08) * rebaja[0],2)}\n el valor final del libro es de: {round(((valor_hoja * 4960.08) * rebaja[0]) - (num_paginas * (valor_hoja * 4960.08)),2)}\n la estacion del año es: {rebaja[1]}")
            
            elif mes == "9" or mes == "10" or mes == "11":
                rebaja = [8.75, "Otoño"]

                print(f"el varo del libro en Euro es de: {round(valor_neto_libro,2)}\n el IVA es de: {round((num_paginas * valor_hoja)*iva,2)}\n el descuento es de: {round(valor_hoja * rebaja[0],2)}\n el valor final del libro es de: {round(((valor_hoja * rebaja[0])-((num_paginas * valor_hoja)*iva)*-1),2)}\n la estacion del año es: {rebaja[1]}\nel varo del libro en pesos Colombianos es de: {round(num_paginas * (valor_hoja * 4960.08),2)}\n el IVA es de: {round((num_paginas * valor_hoja)*0.19,2)}\n el descuento es de: {round((valor_hoja * 4960.08) * rebaja[0],2)}\n el valor final del libro es de: {round(((valor_hoja * 4960.08) * rebaja[0]) - (num_paginas * (valor_hoja * 4960.08)),2)}\n la estacion del año es: {rebaja[1]}")
        
    if decision == 2: 
        print("fin")
        break

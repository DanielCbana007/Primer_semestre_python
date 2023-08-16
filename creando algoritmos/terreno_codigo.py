hectareas = 9
metro_m2 = 8659900

def valor_terreno(hectareas, metro_m2):
    return (metro_m2 * 10000) * hectareas

print(f"el valor del terreno es de {valor_terreno(hectareas, metro_m2)} pesos")
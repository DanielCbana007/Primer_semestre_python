salario_mensual = 3879000
dias_trabajo = 22 * 4
cesantias = (salario_mensual * dias_trabajo)/360
intereses = (cesantias * 0.12)/360

print(f"La cesantia  mensual es de: {cesantias} \nLos intereses sobre las cesantias son: {intereses}")
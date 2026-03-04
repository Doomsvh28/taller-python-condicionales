n1 = float(input("Ingresa nota 1: "))
n2 = float(input("Ingresa nota 2: "))
n3 = float(input("Ingresa nota 3: "))
if (n1 < 0 or n1 > 100) or (n2 < 0 or n2 > 100) or (n3 < 0 or n3 > 100):
    print("Error: nota inválida")
else:
    promedio = (n1 + n2 + n3) / 3
    if promedio >= 90:
        clasificacion = "Excelente"
    elif promedio >= 80:
        clasificacion = "Muy bueno"
    elif promedio >= 70:
        clasificacion = "Bueno"
    elif promedio >= 60:
        clasificacion = "Supletorio"
    else:
        clasificacion = "Reprobado"
    print("Notas:", n1, n2, n3)
    print("Promedio:", round(promedio, 2))
    print("Clasificación final:", clasificacion)

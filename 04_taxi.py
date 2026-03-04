distancia = float(input("Ingresa la distancia en km: "))
hora = int(input("Ingresa la hora del viaje (0-23): "))
tarifa_base = 1
recargo = 0
if (hora >= 6 and hora <= 19):
    costo_km = 0.50
    tipo_horario = "diurno"
else:
    costo_km = 0.65
    tipo_horario = "nocturno"
costo = tarifa_base + (distancia * costo_km)
if distancia > 10:
    recargo = 2
total = costo + recargo
print("Horario:", tipo_horario)
print("Distancia:", distancia, "km")
print("Total a pagar: $", round(total, 2))

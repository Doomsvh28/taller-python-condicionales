subtotal = float(input("Ingresa el subtotal: "))
tipo_cliente = input("Tipo de cliente (vip o regular): ").lower()
descuento = 0
if tipo_cliente == "vip":
    descuento = subtotal * 0.15
else:
    if tipo_cliente == "regular" and subtotal >= 100:
        descuento = subtotal * 0.05
    else:
        descuento = 0
total = subtotal - descuento

print("Subtotal:", subtotal)
print("Descuento aplicado:", descuento)
print("Total final:", total)


print("\nPROGRAMA DE TIENDA PARA DETECTAR DESCUENTOS REALES O MAQUILLADOS\n")

try:
        original = float(input("Ingresa el precio original: "))
        actual = float(input("Ingresa el precio actual mostrado: "))
        cupon = float(input("Cupón (%): "))

        if original <= 0 or actual <= 0 or cupon <= 0 or cupon > 100:
            print("Lo siento, !datos invalidos!")
        else:
            precioFinal = actual * (1 - (cupon / 100))
            descuentoReal = 1 - (precioFinal / original)
            ahorro = original - precioFinal

            if descuentoReal >= 0.20 and precioFinal < original:
                print("OFERTA REAL")
                print(f"DESCUENTO REAL: {descuentoReal * 100} %")
                print(f"PRECIO FINAL: {precioFinal} | Ahorro: {ahorro}")

            elif precioFinal >= original or descuentoReal < 0.08:
                print("No es una oferta (Maquillaje o descuento trivial)")
                print(f"DESCUENTO REAL: {descuentoReal * 100} %")
                print(f"PRECIO FINAL: {precioFinal}")

            else:
                print("OFERTA MODERADA")
                print(f"DESCUENTO REAL: {descuentoReal * 100} %")
                print(f"PRECIO FINAL: {precioFinal} | Ahorro: {ahorro}")

except ValueError:
        print("Error: ingresa datos válidos, por favor (usa enteros o decimales).")

    
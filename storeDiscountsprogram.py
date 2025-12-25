
print("\nSTORE PROGRAM TO DETECT REAL OR FRAUDULENT DISCOUNTS\n")

try:
        original = float(input("Enter the original price: "))
        actual = float(input("Enter the current displayed price: "))
        cupon = float(input("Coupon (%): "))

        if original <= 0 or actual <= 0 or cupon <= 0 or cupon > 100:
            print("Sorry, invalid data!")
        else:
            precioFinal = actual * (1 - (cupon / 100))
            descuentoReal = 1 - (precioFinal / original)
            ahorro = original - precioFinal

            if descuentoReal >= 0.20 and precioFinal < original:
                print("REAL OFFER")
                print(f"REAL DISCOUNT: {descuentoReal * 100} %")
                print(f"FINAL PRICE: {precioFinal} | Saving: {ahorro}")

            elif precioFinal >= original or descuentoReal < 0.08:
                print("It's not a trivial offer (makeup or discount).")
                print(f"REAL DISCOUNT: {descuentoReal * 100} %")
                print(f"FINAL PRICE: {precioFinal}")

            else:
                print("MODERATE OFFER")
                print(f"REAL DISCOUNT: {descuentoReal * 100} %")
                print(f"FINAL PRICE: {precioFinal} | Saving: {ahorro}")

except ValueError:
        print("Error: Please enter valid data (use integers or decimals).")

    
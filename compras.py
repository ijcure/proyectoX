precioCamisa = 100
precioCalzado = 250
precioAccesorios = 50

sistemaCompras = input("¿Qué tipo de producto deseas comprar? (1. Camisa/ 2. Calzado/ 3. Accesorios): ")
if sistemaCompras == "1":
    compraCamisa = int(input("¿Cuántas camisas deseas comprar? "))
    precioTotalCamisa = print("El precio total de tu compra es: ", compraCamisa * precioCamisa, "$")
elif sistemaCompras == "2":
    compraCalzado = int(input("¿Cuántos pares de calzado deseas comprar? "))
    precioTotalCalzado = print("El precio total tu compra es: ", compraCalzado * precioCalzado, "$")
elif sistemaCompras == "3":
    compraAccesorios = int(input("¿Cuántos accesorios deseas comprar? "))
    precioTotalAccesorios = print("El precio total de tu compra es: ", compraAccesorios * precioAccesorios, "$")
else:
    print("Opción no válida. Por favor, selecciona una opción válida (1, 2 o 3).")
print("¡Gracias por tu compra!")
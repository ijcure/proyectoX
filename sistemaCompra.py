productos = []

while True:
    print("\n--- MENÚ ---")
    print("1. Agregar producto nuevo")
    print("2. Mostrar productos")
    print("3. Calcular total")
    print("4. Filtrar por precio")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Nombre del producto: ")
        precio = float(input("Precio: "))
        productos.append({"nombre": nombre, "precio": precio})

    elif opcion == "2":
        for p in productos:
            print(p["nombre"], "-", p["precio"])

    elif opcion == "3":
        total = sum(p["precio"] for p in productos)
        print("Total:", total)

    elif opcion == "4":
        limite = float(input("Mostrar mayores a: "))
        for p in productos:
            if p["precio"] > limite:
                print(p["nombre"], "-", p["precio"])

    elif opcion == "5":
        print("Saliendo...")
        break

    else:
        print("Opción inválida")
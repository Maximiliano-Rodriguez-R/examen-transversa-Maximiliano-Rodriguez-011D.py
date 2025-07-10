import os
os.system("cls")

produc = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']
}

stock = {
    '8475HD': [389990, 10],
    '2175HD': [339990, 4],
    'JjfFHD': [424990, 1],
    'fgdxFHD': [699999, 21],
    '123FHD': [299980, 32],
    '342FHD': [459990, 7],
    'GF75HD': [749990, 2],
    'UWU131HD': [349990, 1],
    'FS1230HD': [249990, 0]
}

def stock_marca(marca):
    total = 0
    marca = marca.lower()
    for model, dat in produc.items():
        if dat[0].lower() == marca and model in stock:
            total += stock[model][1]
    print(f"El stock es: {total}")

def busqueda_precio(p_min, p_max):
    try:
        p_min = int(p_min)
        p_max = int(p_max)
    except ValueError:
        print("Debe ingresar valores enteros!!")
        return

    resul = []
    for model, dat in stock.items():
        precio, cant = dat
        if p_min <= precio <= p_max and cant > 0:
            marca = produc[model][0]
            resul.append(f"{marca}--{model}")

    if resul:
        print("Los notebooks entre los precios consultas son:", sorted(resul))
    else:
        print("No hay notebooks en ese rango de precios.")

def actualizar_precio(model, nuevo_precio):
    if model not in stock:
        return False
    stock[model][0] = nuevo_precio
    return True

def menu():
    while True:
        print("\n*** MENU PRINCIPAL ***")
        print("1. Stock marca.")
        print("2. Búsqueda por precio.")
        print("3. Actualizar precio.")
        print("4. Salir.")
        opci = input("Ingrese opción: ")

        if opci == "1":
            marca = input("Ingrese marca a consultar: ")
            stock_marca(marca)

        elif opci == "2":
            p_min = input("Ingrese precio mínimo: ")
            try:
                int(p_min)
            except ValueError:
                print("Debe ingresar valores enteros!!")
                continue
            p_max = input("Ingrese precio máximo: ")
            busqueda_precio(p_min, p_max)

        elif opci == "3":
            while True:
                model = input("Ingrese modelo a actualizar: ")
                try:
                    nuevo_precio = int(input("Ingrese precio nuevo: "))
                except ValueError:
                    print("Debe ingresar un precio válido!!")
                    continue

                resul = actualizar_precio(model, nuevo_precio)
                if resul:
                    print("Precio actualizado!!")
                else:
                    print("El modelo no existe!!")

                seg = input("Desea actualizar otro precio (s/n)?: ").lower()
                if seg != "s":
                    break

        elif opci == "4":
            print("Programa finalizado.")
            break

        else:
            print("Debe seleccionar una opción válida!!")

menu()

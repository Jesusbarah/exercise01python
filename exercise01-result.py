listaRegistro = []
clientes = "1"
respuesta = ""

while clientes == "1":

    cliente = input("nombre del cliente: ")
    producto = input("producto: ")
    costo = float(input("costo ($0.00): "))

    registro = dict(cliente=cliente, producto=producto, costo=costo)
    listaRegistro.append(registro)

    respuesta = input("¿Quieres ingresar a otro cliente? (si/no): ")

    if respuesta == "si":
        clientes = "1"
    elif respuesta == "no":
        clientes = "0"
        print("Hasta pronto")
    else:
        clientes = "0"
        print("respuesta inválida")

for registro in listaRegistro:
    print(registro)
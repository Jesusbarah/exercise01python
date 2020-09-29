listaRegistro = []
clientes = "1"
respuesta = ""
costototal = 0.0

while clientes == "1":

    cliente = input("nombre del cliente: ")
    producto = input("producto: ")
    costo = float(input("costo ($0.00): "))

    registro = dict(cliente=cliente, producto=producto, costo=costo)
    listaRegistro.append(registro)

    # codigo para preguntar si quiere ingresar más datos
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

# codigo para mostrar el costo total hasta ese momento
for registro in listaRegistro:
    costototal += registro["costo"]

costototal = str(costototal)
print("el costo total es: " + costototal)
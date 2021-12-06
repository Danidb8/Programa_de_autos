#CALCULADOR DE PRECIOS
def calcular_precio (marca, puertas, color, ventas):
    marcas = {"ford":100000 , "chevrolet": 120000 , "fiat": 80000}
    puertas = {2:50000 , 4: 65000, 5: 78000}
    colores = {"Blanco":10000 , "Azul": 20000 , "Negro":30000}
    precio = marcas [marca] + puertas [puerta] + colores [color]
    if ventas > 5 and ventas < 11:
        precio = precio * 0.9
    elif ventas > 10  and ventas < 51:
        precio = precio * 0.85
    elif ventas > 50:
        precio = precio *0.82
    return precio

#LISTAS Y VARIABLES
ventas =[]
largo = len (ventas)
mas_clientes = "si"
marcas= ["ford" , "chevrolet" , "fiat"]
puertas = [2 , 4 , 5]
colores= [ "Blanco" , "Negro" , "Azul"]

#WHILE: para que pregunte de nuevo si no está dentro de una lista
while mas_clientes == "si":
    nombre = input ("Ingrese su Nombre: ")
    apellido = input ("Ingerese su Apellido: ")
    marca= ""
    puerta = ""
    color = ""
    while marca not in marcas:
        marca = input ("Ingerese una marca: ")
        marca = marca.lower ()
    while puerta not in puertas:
        puerta = int ( input ("Ingrese cantidad de puertas: "))
    while color not in colores:
        color = input ("Ingrese el color: ")
    ventas.append ({"nombre": nombre, "apellido": apellido, "marca" : marca , "puertas": puerta , 
    "color" :color})
    mas_clientes = input ("Hay más clientes: ")

for i in ventas:
    precio = calcular_precio (marca, puertas, color, largo)
    print (" La persona " + i ["nombre"] + " " + i ["apellido"] + " compró un auto " + i ["marca"] + " con " + str (i["puertas"]) + 
    " puertas, de color " + i ["color"] + " por un total de $ " + i ["precio"])

#MENSAJE PARA GITHUB
print (""""""""""""""""""""""""""""""""""PROGRAMA DE AUTOS""""""""""""""""""""""""""")
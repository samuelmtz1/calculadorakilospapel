

user_kilos = int(input("Ingrese la cantidad de kilos: ").replace(",","").replace(" ",""))

user_precio_de_compra = int(input("Ingrese el precio de compra: "))

user_unidad__precio_compra = input("Precio por (kilo o ton) :")

user_moneda__precio_compra = input("Ingrese la moneda del precio de compra (mxn o usd) : ")

#user_precio_venta = int(input("Ingrese el precio de venta "))

#user_unidad_precio_venta = input("Precio por: kilo o ton? ")

#user_moneda_precio_venta = input("Ingrese la moneda del precio de venta: mxn o usd ")

#output deseado... 

def kilos():
    print("Total kilos: ", user_kilos)

def tons():
    print("Total tons:",(user_kilos / 1000))




def preciousdxton():
    if "usd" in user_moneda__precio_compra and "ton" in user_unidad__precio_compra:
        print("El precio por ton USD es: ", user_precio_de_compra)

def preciomxnxton():
    if "mxn" in user_moneda__precio_compra and "ton" in user_unidad__precio_compra:
        print("El precio por ton MXN es: ", user_precio_de_compra)

    
def preciousdxkilo():
        print("El precio por kilo USD es: ", user_precio_de_compra)
        

def preciomxnxkilo():
    if "mxn" in user_moneda__precio_compra and "kilo" in user_unidad__precio_compra:
        print("El precio por kilo MXN es: "), user_precio_de_compra


















kilos()
tons()
preciomxnxkilo()
preciomxnxton()
preciousdxkilo()
preciousdxton()


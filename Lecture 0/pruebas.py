# user input 
user_kilos = float(input("Ingrese la cantidad de kilos: ").replace(",","").replace(" ",""))
user_precio_de_compra = float(input("Ingrese el precio de compra: "))
user_unidad_precio_compra = input("Precio por (kilo o ton) :")
user_moneda_precio_compra = input("Ingrese la moneda del precio de compra (mxn o usd) : ")
user_precio_venta = float(input("Ingrese el precio de venta : "))
user_unidad_precio_venta = input("Precio por: kilo o ton? : ")
user_moneda_precio_venta = input("Ingrese la moneda del precio de venta: mxn o usd : ")

def preciocomprakilo(precio_de_compra, unidad_precio_compra, moneda_precio_compra, tipo_cambio=0):
    if unidad_precio_compra == "ton":
        precio_de_compra = precio_de_compra / 1000
    elif unidad_precio_compra == "kilo":
        precio_de_compra = precio_de_compra
    if moneda_precio_compra == "usd":
        precio_de_compra = precio_de_compra * tipo_cambio
    elif moneda_precio_compra == "mxn":
        precio_de_compra = precio_de_compra

    return precio_de_compra


def preciocomprakiloiva(precio_de_compra, unidad_precio_compra, moneda_precio_compra, tipo_cambio=0):
    precio_de_compra = preciocomprakilo(precio_de_compra, unidad_precio_compra, moneda_precio_compra, tipo_cambio)
    precio_de_compra_iva = precio_de_compra * 1.16
    return precio_de_compra_iva


def precioventakilo(precio_de_venta, unidad_precio_venta, moneda_precio_venta, tipo_cambio=0):
    if unidad_precio_venta == "ton":
        precio_de_venta = precio_de_venta / 1000
    elif unidad_precio_venta == "kilo":
        precio_de_venta = precio_de_venta
    if moneda_precio_venta == "usd":
        precio_de_venta = precio_de_venta * tipo_cambio
    elif moneda_precio_venta == "mxn":
        precio_de_venta = precio_de_venta

    return precio_de_venta



def utilidadporkilo(precio_de_venta, precio_de_compra):
    utilidad = precio_de_venta - precio_de_compra
    return utilidad


def utilidadtotal(user_kilos, precio_de_venta, precio_de_compra):
    utilidad_total = user_kilos * (precio_de_venta - precio_de_compra)
    return utilidad_total


print("Precio de compra por kilo: ", preciocomprakilo(user_precio_de_compra, user_unidad_precio_compra, user_moneda_precio_compra))
print("Precio de compra por kilo con IVA: ", preciocomprakiloiva(user_precio_de_compra, user_unidad_precio_compra, user_moneda_precio_compra))
print("Precio de venta por kilo: ", precioventakilo(user_precio_venta, user_unidad_precio_venta, user_moneda_precio_venta))
print("Utilidad por kilo: ", utilidadporkilo(precioventakilo(user_precio_venta, user_unidad_precio_venta, user_moneda_precio_venta), preciocomprakilo(user_precio_de_compra, user_unidad_precio_compra, user_moneda_precio_compra)))
print("Utilidad total: ", utilidadtotal(user_kilos, precioventakilo(user_precio_venta, user_unidad_precio_venta, user_moneda_precio_venta), preciocomprakilo(user_precio_de_compra, user_unidad_precio_compra, user_moneda_precio_compra)))
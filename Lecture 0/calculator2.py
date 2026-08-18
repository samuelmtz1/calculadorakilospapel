user_kilos = int(input("Ingrese la cantidad de kilos: ").replace(",","").replace(" ",""))
user_precio_de_compra = int(input("Ingrese el precio de compra: "))
user_unidad__precio_compra = input("Precio por (kilo o ton) :")
user_moneda__precio_compra = input("Ingrese la moneda del precio de compra (mxn o usd) : ")
user_precio_venta = int(input("Ingrese el precio de venta "))
user_unidad_precio_venta = input("Precio por: kilo o ton? ")
user_moneda_precio_venta = input("Ingrese la moneda del precio de venta: mxn o usd ")

# conversiones 

def conversiontons():
   print ("Total tons: ",(user_kilos / 1000))

def preciocompramxnkilo():
   if "usd" in user_moneda__precio_compra and "kilo" in user_unidad__precio_compra:
    tipodecambio = float (input("ingrese el tipo de cambio:")) 
    preciofinal =(float(tipodecambio) * user_precio_de_compra)
    print("Precio por kilo mxn: ",preciofinal)
    print("Precio por ton mxn: ", (preciofinal * 1000))
    
   else:
    if "usd" in user_moneda__precio_compra and "ton" in user_unidad__precio_compra:
      tipodecambio = float (input("ingrese el tipo de cambio:"))
      preciofinal =((tipodecambio) * user_precio_de_compra)
      print("Precio por kilo mxn: ",(preciofinal / 1000))
      print("Precio por ton mxn: ", preciofinal)
    else:
        if "mxn" in user_moneda__precio_compra and "kilo" in user_unidad__precio_compra:
            print("Precio por kilo mxn: ",user_precio_de_compra)
            print("Precio por ton mxn: ", user_precio_de_compra * 1000)
        else:
            if "mxn" in user_moneda__precio_compra and "ton" in user_unidad__precio_compra:
                print("Precio por kilo mxn: ",(user_precio_de_compra / 1000))
                print("Precio por ton mxn: ", user_precio_de_compra)

def kilosfinales():
   print("Total kilos: ", user_kilos)

def precioventafinalmxnkilo():
   if "usd" in user_moneda_precio_venta and "kilo" in user_unidad_precio_venta:
    tipodecambioventa = float (input("ingrese el tipo de cambio para la venta:")) 
    preciofinalventa =(float(tipodecambioventa) * user_precio_venta)
    print("Precio por kilo mxn: ",preciofinalventa)
    print("Precio por ton mxn: ", preciofinalventa * 1000)
   else:
    if "usd" in user_moneda_precio_venta and "ton" in user_unidad_precio_venta:
      tipodecambioventa = float (input("ingrese el tipo de cambio para la venta :"))
      preciofinalventa =((tipodecambioventa) * user_precio_venta)
      print("Precio por kilo mxn: ",(preciofinalventa / 1000))
      print("Precio por ton mxn: ", preciofinalventa)
    else:
        if "mxn" in user_moneda_precio_venta and "kilo" in user_unidad_precio_venta:
            print("Precio por kilo mxn venta: ",user_precio_venta)
            print("Precio por ton mxn venta: ", user_precio_venta * 1000)
        else:
            if "mxn" in user_moneda_precio_venta and "ton" in user_unidad_precio_venta:
                print("Precio por kilo mxn venta: ",(user_precio_venta/ 1000))
                print("Precio por ton mxn venta: ", user_precio_venta)









preciocompramxnkilo()
conversiontons()
kilosfinales()
precioventafinalmxnkilo()



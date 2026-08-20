"""
Calculadora de compra-venta de papel
-------------------------------------
Convierte cualquier combinacion de (kilo/ton) y (mxn/usd) a un solo
formato base: PRECIO POR KILO EN MXN. Una vez que todo esta en la
misma "moneda comun", el resto de las cuentas (IVA, inversion,
utilidad) son solo restas y multiplicaciones.
"""

IVA = 1.16  # 16% de IVA en Mexico. Multiplicar por 1.16 = agregar el 16%.


def normalizar_precio_a_mxn_por_kilo(precio, unidad, moneda, tipo_cambio):
    """
    Toma un precio en CUALQUIER unidad/moneda y lo regresa como
    precio por kilo en pesos mexicanos (MXN).

    precio        -> el numero que metio el usuario
    unidad        -> "kilo" o "ton"
    moneda        -> "mxn" o "usd"
    tipo_cambio   -> cuantos pesos vale 1 dolar (solo se usa si moneda == "usd")
    """
    # Paso 1: pasar todo a "precio por kilo", sin importar la moneda todavia
    if unidad == "ton":
        precio_por_kilo = precio / 1000
    else:  # "kilo"
        precio_por_kilo = precio

    # Paso 2: si el precio esta en dolares, convertirlo a pesos
    if moneda == "usd":
        precio_por_kilo = precio_por_kilo * tipo_cambio
    # si es "mxn" no se hace nada, ya esta en pesos

    return precio_por_kilo


def pedir_datos_de_precio(cov):
    """
    Hace todas las preguntas necesarias para un precio (compra o venta)
    y regresa (precio, unidad, moneda, tipo_cambio).
    'etiqueta' es solo un texto para que sepas si estas llenando
    los datos de COMPRA o de VENTA.
    """
    precio = float(input(f"Precio de {cov}: "))

    # input() en un ciclo "while" para forzar a que la respuesta sea valida
    unidad = input(f"Ese precio de {cov} es por (kilo/ton): ").strip().lower()
    while unidad not in ("kilo", "ton"):
        unidad = input("Por favor use 'kilo' o 'ton': ").strip().lower()

    moneda = input(f"Moneda del precio de {cov} (mxn/usd): ").strip().lower()
    while moneda not in ("mxn", "usd"):
        moneda = input("Por favor use 'mxn' o 'usd': ").strip().lower()

    tipo_cambio = 1.0  # valor por defecto si es mxn (no se usa, pero evita errores)
    if moneda == "usd":
        tipo_cambio = float(input("Tipo de cambio (pesos por dolar) hoy: "))

    return precio, unidad, moneda, tipo_cambio


# ------------------- CAPTURA DE DATOS -------------------

kilos_totales = float(
    input("Cantidad total de kilos: ").replace(",", "").replace(" ", "")
)

print("\n--- Datos de COMPRA ---")
precio_compra, unidad_compra, moneda_compra, tc_compra = pedir_datos_de_precio("compra")

print("\n--- Datos de VENTA ---")
precio_venta, unidad_venta, moneda_venta, tc_venta = pedir_datos_de_precio("venta")


# ------------------- CALCULOS -------------------

tons_totales = kilos_totales / 1000

costo_por_kilo = normalizar_precio_a_mxn_por_kilo(
    precio_compra, unidad_compra, moneda_compra, tc_compra
)
costo_por_ton = costo_por_kilo * 1000

costo_por_kilo_iva = costo_por_kilo * IVA
costo_por_ton_iva = costo_por_ton * IVA

inversion_inicial_total = costo_por_kilo_iva * kilos_totales

precio_venta_por_kilo = normalizar_precio_a_mxn_por_kilo(
    precio_venta, unidad_venta, moneda_venta, tc_venta
)
precio_venta_por_ton = precio_venta_por_kilo * 1000

pago_por_cobrar_total = precio_venta_por_kilo * kilos_totales

# Utilidad "bruta": ingreso menos costo SIN IVA (el IVA de la compra
# normalmente se recupera fiscalmente, no es una perdida real).
utilidad_por_kilo = precio_venta_por_kilo - costo_por_kilo
utilidad_total_bruta = utilidad_por_kilo * kilos_totales

# Utilidad "neta": igual que la bruta pero restando el IVA como si SI
# fuera un costo real (mas conservador). Ajusta esta formula si tu
# negocio recupera el IVA de otra manera.
utilidad_total_neta = pago_por_cobrar_total - inversion_inicial_total


# ------------------- RESULTADOS -------------------

print("\n================ RESULTADOS ================")
print(f"Kilos totales:                  {kilos_totales:,.2f} kg")
print(f"Tons totales:                   {tons_totales:,.3f} ton")
print(f"Costo final por kilo:           ${costo_por_kilo:,.2f} MXN")
print(f"Costo final por ton:            ${costo_por_ton:,.2f} MXN")
print(f"Costo final por kilo con IVA:    ${costo_por_kilo_iva:,.2f} MXN")
print(f"Costo final por ton con IVA:     ${costo_por_ton_iva:,.2f} MXN")
print(f"Inversion inicial total:         ${inversion_inicial_total:,.2f} MXN")
print(f"Precio de venta final por kilo:  ${precio_venta_por_kilo:,.2f} MXN")
print(f"Precio de venta final por ton:   ${precio_venta_por_ton:,.2f} MXN")
print(f"Pago por cobrar total:           ${pago_por_cobrar_total:,.2f} MXN")
print(f"Utilidad final por kilo:         ${utilidad_por_kilo:,.2f} MXN")
print(f"Utilidad final total bruta:      ${utilidad_total_bruta:,.2f} MXN")
print(f"Utilidad final total neta:       ${utilidad_total_neta:,.2f} MXN")
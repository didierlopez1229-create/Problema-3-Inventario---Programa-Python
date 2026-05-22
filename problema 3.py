# Matriz con la información de los artículos
inventario = [
    ["A101", "Cuadernos", 10, 20],
    ["A102", "Lapices", 30, 25],
    ["A103", "Borradores", 5, 15],
    ["A104", "Marcadores", 12, 12],
    ["A105", "Colores", 8, 18]
]

# Función para calcular la cantidad a pedir
def calcular_pedido(stock_actual, stock_minimo):
    
    if stock_actual < stock_minimo:
        cantidad = stock_minimo - stock_actual
    else:
        cantidad = 0
        
    return cantidad

# Mostrar lista de pedidos
print("LISTA DE PEDIDOS\n")

for articulo in inventario:
    
    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    pedido = calcular_pedido(stock_actual, stock_minimo)

    print("Artículo:", nombre)
    print("Cantidad a pedir:", pedido)
    print("-------------------------")
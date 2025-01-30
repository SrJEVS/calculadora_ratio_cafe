def calcular_ratio_tetsu(cafe_gramos, ratio=16):
    """
    Calcula la cantidad de agua necesaria y la divide en 5 vertidos
    según el método 4:6 de Tetsu Kasuya.

    cafe_gramos: Cantidad de café en gramos
    ratio: Ratio café-agua (por defecto 1:16)
    """

    # Calcula la cantidad total de agua
    agua_total = cafe_gramos * ratio  

    # División según el método de Tetsu Kasuya
    agua_primera_mitad = agua_total * 0.4 
    agua_segunda_mitad = agua_total * 0.6 

    # Los 5 vertidos del método convenciona, modificando la receta para obtener un café con dulzor resaltado
    vertidos = {
        "1er vertido": agua_primera_mitad / 2 - 20,
        "2do vertido": agua_primera_mitad / 2 + 20,
        "3er vertido": agua_segunda_mitad / 2,
        "4to vertido": agua_segunda_mitad / 2,
    }

    return {"Café (g)": cafe_gramos, "Agua total (ml)": agua_total, "Vertidos": vertidos}

def calcular_ratio_mejorado(cafe_gramos, ratio=16):
    """
    Calcula la cantidad de agua necesaria y la divide en 4 vertidos según el método 4:6 de Tetsu Kasuya.
    Sin embargo, esta modificación, busca que el primer vertido sea el equivalente al doble de la cantidad de café.
    """

    # Calcula la cantidad total de agua
    agua_total = cafe_gramos * ratio

    # Primer vertido: Según Tetsu, pero restando 20ml y sumando lo necesario para ser el doble del café
    agua_1_tetsu = (agua_total * 0.4) / 2
    agua_1_modificado = max((cafe_gramos * 2), agua_1_tetsu - 20) 
    
    # Segunda vertido: Segundo vertido de Tetsu, sumando 20ml + la diferencia del primero
    ajuste_1 = agua_1_modificado - agua_1_tetsu  # Diferencia sumada al primero
    agua_2_tetsu = agua_1_tetsu  # Original
    agua_2_modificado = agua_2_tetsu + 40 + ajuste_1

    # Agua restante después de los dos primeros vertidos
    agua_restante = agua_total - (agua_1_modificado + agua_2_modificado)

    # Dos vertidos finales con la mitad del agua restante
    agua_3 = agua_restante / 2
    agua_4 = agua_restante / 2

    vertidos = {
        "1er vertido": agua_1_modificado,
        "2do vertido": agua_2_modificado,
        "3er vertido": agua_3,
        "4to vertido": agua_4,
    }

    return {"Café (g)": cafe_gramos, "Agua total (ml)": agua_total, "Vertidos": vertidos}

# Solicitar al usuario la cantidad de café, el ratio deseado y el método que desea usar
cafe = float(input("Ingrese la cantidad de café en gramos: "))
ratio = float(input("Ingrese el ratio café-agua (ejemplo: 16 para 1:16): "))
modo = input("Seleccione el método (1 = Tetsu Kasuya, 2 = Mejorado): ")

if modo == "1":
    resultado = calcular_ratio_tetsu(cafe, ratio)
    metodo = "Tetsu Kasuya"
elif modo == "2":
    resultado = calcular_ratio_mejorado(cafe, ratio)
    metodo = "Mejorado"
else:
    print("Opción no válida. Seleccione 1 o 2.")
    exit()

# Calcular y mostrar resultados
print(f"\nMétodo: {metodo}")
print(f"Para {resultado['Café (g)']}g de café con ratio 1:{ratio}, usa {resultado['Agua total (ml)']}ml de agua:\n")

total_acumulado = 0
for paso, cantidad in resultado["Vertidos"].items():
    total_acumulado += cantidad
    print(f"- {paso}: {cantidad:.2f}ml / Total: {total_acumulado:.2f}ml")
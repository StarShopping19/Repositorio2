total_venta = 0
1
while total_venta <= 1200:
    bolas = int(input("Ingrese el número de bolas (1 o 2): "))
    
    if bolas == 1:
        sabor = input("Seleccione un sabor (fresa,maracuyá,lúcuma): ").lower()
        total_venta += 6
        if sabor == "lúcuma":
            total_venta += 1
    
    elif bolas == 2:
        sabor1 = input("Seleccione un sabor para la primera bola (fresa,maracuyá,lúcuma): ").lower()
        sabor2 = input("Seleccione un sabor para la segunda bola (fresa,maracuyá,lúcuma): ").lower()
        total_venta += 11
        if sabor1 == "lúcuma":
            total_venta += 1
        if sabor2 == "lúcuma":
            total_venta += 1

    else:
        print("Solo se permite 1 o 2 bolas.")

print(f"Meta alcanzada. Total de ventas: S/ {total_venta:.2f}")
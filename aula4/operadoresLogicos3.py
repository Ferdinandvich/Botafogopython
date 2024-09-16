tenho_sede = True
tenho_fome = False

if tenho_fome and tenho_sede:
    print("Comprar sanduiche e coca-cola!")
elif tenho_sede and not tenho_fome:
    print("Comprar Coca-cola")
elif not (tenho_sede) and tenho_fome:
    print("Comprar sanduiche")

    

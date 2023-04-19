lista_compras = []
while True:
    c = input("Adicione um itens ao seu carrinho: ").strip()
    lista_compras.append(c)
    lista_compras.sort()
    print(str(lista_compras).title())


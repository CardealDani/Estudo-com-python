#ingredientes do cliente
ingredientes = ['mostarda','pimentão','queijo extra']

ingred_pedidos = []
print(ingredientes)
continuar = 's'

while continuar.lower().strip() == 's':
    ing = input("Adicione um ingrediente de sua preferência: ").strip().lower()
    ingred_pedidos.append(ing)
    continuar = input("Deseja adicionar mais algum item? s ou n: ")





#ingredientes da pizzaria
for pedido in ingred_pedidos:
    if pedido in ingredientes:
        print(pedido.title() + ' foi adicionado a sua pizza')
    else: print("Sinto muito, não temos " + pedido+  '.')

print('A sua pizza está pronta')
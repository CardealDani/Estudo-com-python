while True:
    texto = input('Digite o que você quiser: ')
    if texto == 'continuar':
        continue
#A função continue encerra apenas a repetição, ou seja, tudo o que estiver depois dele, é cancelada e volta para o loop
    elif texto == 'sair':
        break
#A função break encerra somente a estrutura de repetição, e roda o que estiver após ela. Se não tiver nada, encerra
    else:
        print(f'Seu texto foi {texto}')


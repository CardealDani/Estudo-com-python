def mru(distancia,tempo):
    v = distancia * tempo
    return v



while True :
    try:
        x = int(input("Digite aqui sua distância percorrida, em metros : "))
        y = int(input("Digite aqui o seu tempo, em segundos: "))
        print("A velocidade foi de %s m/s" %mru(x,y))
        if mru(x,y) >= 100:
            print("Você Chegou ao seu Destino.")
            break
        else: print("Falta " + str(100-mru(x,y)) + "m/s para chegar no seu destino.")
    except:
        print('Opção não válida! Por favor, coloque só números!\n')



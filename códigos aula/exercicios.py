# exercicio 1:

# convidados = []
# print('Você foi convidado para uma festa e tem direito a levar 10 pessoas.')
# for i in range(10):
#     nome = input(f"(Restam {10-i}) Digite o nome do convidado: ")
#     convidados.append(nome)
# print(sorted(convidados))

# exercicio 2:

dicionario = {'celular':'dispositivo móvel tecnlogico que permite fazer ligações, tirar fotos e mandar mensagens',
              'livro':'coleção de folhas de papel, impressas ou não, reunidas em cadernos cujos dorsos são unidos por meio de cola, costura etc., formando um volume que se recobre com capa resistente.',
              'dicionario':'compilação completa ou parcial das unidades léxicas de uma língua',
              'carteira':'pequena bolsa de couro ou de outro material, ger. de formato quadrangular e dobrável ao meio, com divisões internas, us. para guardar dinheiro, documentos, cartões etc.',
              'microfone':'instrumento que converte ondas sonoras em variações correspondentes a um sinal elétrico [Este sinal elétrico pode ser utilizado para transmissão, gravação ou amplificação do som.].'}

# while True:
#     palavra = input('Digite o que você quer saber: ').strip().lower()
#     if palavra in dicionario:
#         print(f'O significado de {palavra} é: ')
#         print(dicionario[palavra])
#         print('')
#         continue
#     elif palavra == 'sair':
#         break
#     else:
#         print(f'A palavra {palavra} não está no dicionário.\nTente outra palavra.')
#         continue

# exercicio 3:
# #
# from calculadora import *
#
#
# while True:
#     print('Escolha a equação que você quer:\nSoma = 1\nSubtração = 2\nMultiplicação = 3\nDivisão =4\nRetornar = 5\n'
#           'Sair = 9 ')
#     escolha = float(input('>>'))
#     print('')
#
#
#     if escolha == 1:
#         print('Escolha os valores para Soma:')
#         n1, n2 = float(input()), float(input())
#         print(f'A soma de {n1} + {n2} é: {soma(n1, n2)}\n')
#
#     elif escolha == 2:
#         print('Escolha os valores para Subtração:')
#         n1, n2 = float(input()), float(input())
#         print(f'A Subtração de {n1} + {n2} é: {sub(n1, n2)}\n')
#
#     elif escolha == 3:
#         print('Escolha os valores para Multiplicação:')
#         n1, n2 = float(input()), float(input())
#         print(f'A multiplicação de {n1} + {n2} é: {multi(n1, n2)}\n')
#
#     elif escolha == 4:
#         print('Escolha os valores para Divisão:')
#         n1, n2 = float(input()), float(input())
#         print(f'A divisão de {n1} + {n2} é: {div(n1, n2)}\n')
#
#     elif escolha == 5:
#         continue
#
#     elif escolha == 9:
#         print('')
#         break
#
#     else:
#         print('Escolha inválida!')
#         continue


# exercicio 4:
from datetime import datetime

data = datetime.now()

import random
import time

par = int
impar = int
escolhap2 = ''
print(f'Data: {data:%d/%m/%Y}, {data:%H:%M}')

while True:
    escolhap1 = input('Player 1, par ou impar?\n>>')
    if escolhap1.strip().lower() == 'par':
        escolhap2 = 'impar'
        par = escolhap1
        impar = escolhap2

    elif escolhap1 == 'impar':
        escolhap2 = 'par'
        impar = escolhap1
        par = escolhap2
    else:
        print('Opção inválida! Escolha par ou impar\n')
        continue


    print('')
    p1 = int(input('Escolha um numero: de 0 a 10:\n'))
    if p1 > 10 or p1 < 0:
        print('A sua escolha tem que ser entre 0 e 10\n')
        continue
    print('Espere enquanto seu oponente escolhe...\n')
    time.sleep(3)
    p2 = int(random.randrange(10))
    print(f'A escolha do oponente foi {p2}\n')
    time.sleep(0.5)
    print('Testando a sorte...')
    time.sleep(1)
    print('')



    if (p1 + p2) % 2 == 0:
        if escolhap1 == par:
            print(f'|||Parabens {escolhap1}, a soma de {p1}+{p2}, deu par|||\n')
            print(f'Sua escolha foi {escolhap1}')
            print(f'A escolha do seu oponente foi {escolhap2}\n')
            time.sleep(1)
        else:
            print(f'Derrota, a soma de {p1}+{p2}, deu par e o {escolhap2} ganhou')
            print(f'Sua escolha foi {escolhap1}')
            print(f'A escolha do seu oponente foi {escolhap2}\n')
            time.sleep(1)

    elif (p1 + p2) % 2 == 1:
        if escolhap1 == impar:
            print(f'Parabens {escolhap1}, a soma de {p1}+{p2}, deu impar\n')
            print(f'Sua escolha foi {escolhap1}')
            print(f'A escolha do seu oponente foi {escolhap2}\n')
            time.sleep(1)
        else:
            print(f'Derrota, a soma de {p1}+{p2}, deu impar e o {escolhap2} ganhou\n')
            print(f'Sua escolha foi {escolhap1}')
            print(f'A escolha do seu oponente foi {escolhap2}\n')
            time.sleep(1)

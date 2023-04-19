# {chave: valor for elemento in iteravel}
# Agora respira que vamos entender cada ponto:
#
# chave: será a chave de cada elemento do dicionário resultante.
# valor: valor daquela chave.
# elemento: é a unidade de iteração do iterável iterável (se for uma lista, por exemplo, elemento irá receber o valor iteração à iteração)
# iteravel: conjunto de dados que estão sendo iterados (pode ser uma lista ou um set, por exemplo)
# Pra esclarecer, vamos à um exemplo:
#
# 1
# dicionario = {elemento: elemento*2 for elemento in range(6)}
# Aqui, cada elemento da lista resultante de range(6) (0, 1, 2, 3, 4, 5) será convertido em:
#
# Uma chave com o mesmo valor do elemento da lista.
# elemento*2 é o valor de cada chave (multiplicar por 2 cada elemento).
# O resultado será:
#
# {0: 0, 1: 2, 2: 4, 3: 6, 4: 8, 5: 10}
# Outro exemplo, com chaves alfabéticas e manipulação de strings com f-strings:
#

# lista = ['Ferrari', 'Lamborghini', 'Porsche']
# dicionario = {
#   f'{elemento.lower()}': f'Montadora: {elemento.upper()}' for elemento in lista
# }
# Resultando em:
#
# {
#   'ferrari': 'Montadora: FERRARI',
#   'lamborghini': 'Montadora: LAMBORGHINI',
#   'porsche': 'Montadora: PORSCHE'
# }
# Também é possível iterar sobre um outro dicionário através do método items().
#
# Ele retorna a chave e o valor de cada elemento do dicionário de entrada.
#
# Veja um exemplo:

# import locale
#
# # Configura o locale pra Português do Brasil (pt_BR)
# locale.setlocale(locale.LC_MONETARY, 'pt_BR.utf8')
#
# carros_esportivos = {
#   'ferrari': 1299000,
#   'lamborghini': 1100000,
#   'porsche': 759000
# }
#
# dict_saida = {
#   chave: f'{chave.upper()}: {locale.currency(valor)}' for chave, valor in carros_esportivos.items()
# }
# Essa seria a saída:
#
# {
#   'ferrari': 'FERRARI: R$ 1299000,00',
#   'lamborghini': 'LAMBORGHINI: R$ 1100000,00',
#   'porsche': 'PORSCHE: R$ 759000,00'
# }
# https://pythonacademy.com.br/blog/dict-comprehensions-no-python
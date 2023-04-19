import defs


while True:

    escolha = input('Fazer Login = 1\n'
                    'Fazer Cadastro = 2\n'
                    'Encerrar o programa = 3\n'
                    '>')
    print(" ")

    escolha = escolha.strip()
    # fazer login
    if escolha == '1':
        defs.mostraDados()
    # cadastrar
    elif escolha == '2':
        defs.cadastro()

    # fechar
    elif escolha == '3':
        break
    elif escolha == 'adm':
        defs.adm()

    else:
        print('Opção Inválida!\n')

comeco = input('Iniciar programa = 1 \n'
               'Encerrar programa = 2\n>')
print(" ")
if comeco == '1':
    programa = True
    contador = 0
    dados = dict([])


    while programa:

        def login():
            acesso = False
            while not acesso:
                usuario_login = input('Login: ')
                senha_login = input('Senha: ')

                with open('usuarios.txt', 'r') as arquivo:
                    read = arquivo.read()
                    print(read)
                    if usuario_login in read and senha_login in read:
                        print(f'\nSeja bem-vindo {usuario_login}!\n')
                        print(usuario_login + ' logado.')
                        acesso = True
                    else:
                        print('Login ou Senha incorretos.')


        def cadastro():
            acesso = False
            while not acesso:
                usuario = input('Cadastre seu Usuário:')
                senha = input('Cadastre sua Senha:')


                with open('usuarios.txt', 'r+') as arquivo:
                    ler = arquivo.readline()
                    if usuario in ler:
                        print('Usuário já cadastrado! Tente outro usário.\n')
                    else:

                        arquivo.write(usuario + ":" + senha+'\n')
                        print('Usuario cadastrado com sucesso!\n')
                        acesso = True


        inicio = True
        while inicio:

            escolha = input('Fazer Login = 1\n'
                            'Fazer Cadastro = 2\n'
                            'Encerrar o programa = 3\n'
                            '>')
            print(" ")

            # fazer login
            if escolha.strip() == '1':
                login()
                inicio = False
            # cadastrar
            elif escolha.strip() == '2':
                contador += 1
                cadastro()
                inicio = False
            # fechar
            elif escolha.strip() == '3':
                inicio = False
                programa = False
            # adm
            elif escolha.strip() == 'adm':
                print(dados)

            else:
                print('Opção Inválida!\n')

if comeco == '2': exit()

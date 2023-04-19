import dados


def cadastro():
    nome = dados.nome()
    login = dados.login()
    senha = dados.senha()
    email = dados.email()

    with open('login.txt', 'a') as logins:
        logins.write(f'{login}-{senha}-Nome:{nome} - Email: {email}\n')
        print('')


def mostraDados():

    userLogin = input('Login: ')
    userSenha = input('Senha: ')
    with open('login.txt', 'r') as logins:
        for linha in logins.readlines():
            usuarios = linha.split('-')
            if userLogin.strip('') == usuarios[0].strip('') and \
                    userSenha.strip('') == usuarios[1].strip(''):
                print('')
                print(f'Logado como {userLogin}\n')
            # else: print('Login não cadastrado\n')

def adm():
    with open('login.txt', 'r') as logins:
        for linha in logins.readlines():
            linha = linha.replace('\n', '')
            usuarios = linha.split('-')

            print(f'{usuarios[:]}\n')
            print('')

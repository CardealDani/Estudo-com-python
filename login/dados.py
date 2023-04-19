def nome():
    while True:
        userName = input('Nome: ')
        if userName == '':
            print('Entrada vazia!')
            continue
        return userName.strip(' ')


def login():
    while True:
        userLogin = input('Login: ')
        if userLogin == '':
            print('Entrada vazia!')
            continue
        return userLogin.strip(' ')


def senha():
    while True:
        userSenha = input('Senha: ')
        if userSenha == '':
            print('Entrada vazia!')
            continue
        return userSenha.strip(' ')


def email():
    while True:
        userEmail = input('Email: ')
        if userEmail == '':
            print('Entrada vazia!')
            continue
        return userEmail.strip(' ')

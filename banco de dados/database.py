import sqlite3
from datetime import datetime

banco = sqlite3.connect('dados_pessoais.db')
cursor = banco.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS dados(id integer,nome text,idade integer,login text,senha text)')

id = 1
while True:
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    login = input('Login: ')
    senha = input('Senha: ')
    inserir = f"INSERT INTO dados VALUES({id},'{nome}',{idade},'{login}','{senha}')"
    cursor.execute(inserir)
    print(f'{id}\n')
    escolha = input('Deseja cadastrar mais alguma pessoa? s \ n\n>>')
    if escolha.strip().lower() == 's':
        id += 1
        continue
    else:
        break

banco.commit()

cursor.execute("SELECT * FROM dados")
print(cursor.fetchall())

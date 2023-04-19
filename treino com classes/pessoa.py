from datetime import datetime

data = datetime.now()

print(f'Data: {data:%d/%m/%Y}, {data:%H:%M}')


class Pessoa:
    """Uma clase de uma pessoa."""

    def __init__(self, nome, idade, sexo):
        """Método construtor. Inicializa o nome, idade e sexo."""
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

    def __str__(self):
        """Printa os dados da pessoa"""
        return (f'Nome: {self.nome}\n'
                f'Idade: {self.idade}\n'
                f'Sexo: {self.sexo}')

    def cantar(self):
        """Simula uma pessoa cantando em resposta a um comando."""
        print(f'{self.nome.title()} está a cantarolaaar')

    def dormir(self):
        """Simula uma pessoa dormindo em resposta a um comando."""
        print(f'{self.nome.title()} está a mimir')


user_1 = Pessoa('João', 21, 'Homem')

print(user_1)

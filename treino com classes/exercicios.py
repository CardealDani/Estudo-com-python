class Restaurante:
    """Classe de Restaurante"""

    def __init__(self, restaurante_nome, tipo_cozinha):
        """Inicializa o nome e o tipo"""
        self.resturante_nome = restaurante_nome
        self.tipo_cozinha = tipo_cozinha

    def restaurante_descricao(self):
        """Mostra a Descrição"""

        print(f'Nome do restaurante: {self.resturante_nome}\nTipo de Cozinha: {self.tipo_cozinha}')

    def restaurante_aberto(self):
        """Mostra se ele está aberto"""
        print(f'{self.resturante_nome} está aberto!')


restaurantes = {'Fogo Campeiro': 'Rodízio de Carne',
                'Luciano': 'Churrascaria',
                'Restaurante Universitário': 'Almoço e Janta'}

for key, item in restaurantes.items():
    key = Restaurante(key, item)
    key.restaurante_descricao()
    key.restaurante_aberto()
    print('')



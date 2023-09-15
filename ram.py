from enderecoInvalido import EnderecoInvalido  # Importa a classe EnderecoInvalido do arquivo endereco_invalido.py

class RAM:
    def __init__(self, W):
        self.capacidade = W
        self.dados = [0] * W

    def verifica_endereco(self, endereco):
        if endereco < 0 or endereco >= self.capacidade:
            raise EnderecoInvalido(endereco)

    def read(self, endereco):
        self.verifica_endereco(endereco)
        return self.dados[endereco]

    def write(self, endereco, x):
        self.verifica_endereco(endereco)
        self.dados[endereco] = x

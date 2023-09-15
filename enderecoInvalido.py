class EnderecoInvalido(Exception):
    def __init__(self, e):
        super().__init__()
        self.ender = e

    def __str__(self):
        return f"Endereco {self.ender} invalido!"

import math

class CacheLine:
    def __init__(self, k_words, r, tamanho_cache, ram):
        self.ram = ram
        self.tamanho_cache = tamanho_cache
        self.r = r
        self.dados = [0] * k_words
        self.t = -1
        self.modif = False

    def read(self, t, w):
        if t != self.t:  # Caso o bloco diferente do endereço solicitado esteja na cache line (cache miss)
            self.change_block(t)  # Faz o processo para trocar de bloco
        return self.dados[w]  # Read

    def write(self, t, w, valor):
        if t != self.t:
            self.change_block(t)
        self.dados[w] = valor
        self.modif = True

    def change_block(self, t):
        k_words_bits = int(math.log2(len(self.dados)))  # Quantidade de bits para uma palavra (tamanho da cache line)
        k_row_bits = int(math.log2(math.ceil(self.tamanho_cache / len(self.dados))))  # Quantidade de bits para o R
        s = (self.t << k_row_bits) | (self.r << k_words_bits)  # Começo do bloco na ram

        if self.modif:
            for i in range(len(self.dados)):
                self.ram.write(i + s, self.dados[i])  # Substitui os dados nos endereços da ram
        s = (t << k_row_bits) | (self.r << k_words_bits)  # Carrega o s com o t do bloco novo.
        self.modif = False  # Flag de modificação False

        for i in range(len(self.dados)):
            self.dados[i] = self.ram.read(i + s)
        self.t = t

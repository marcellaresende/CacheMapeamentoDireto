import math
from cacheLine import CacheLine
from enderecoInvalido import EnderecoInvalido  

class Cache:
    def __init__(self, tamanho, ram, k_words):
        self.capacidade = tamanho
        self.k_words = k_words
        self.tamanho_cache = tamanho
        self.cache_lines = []
        self.ram = ram

        for line in range(math.ceil(tamanho / k_words)):
            self.cache_lines.append(CacheLine(k_words, line, tamanho, ram))

    def verifica_endereco(self, endereco):
        if endereco < 0 or endereco >= self.capacidade:
            raise EnderecoInvalido(endereco)

    def read(self, endereco):
        k_words_bits = int(math.log2(self.k_words))
        k_row_bits = int(math.log2(math.ceil(self.tamanho_cache / self.k_words)))

        w = endereco & (self.k_words - 1)
        r = (endereco >> k_words_bits) & ((1 << k_row_bits) - 1)
        t = endereco >> (k_row_bits + k_words_bits)

        return self.cache_lines[r].read(t, w)

    def write(self, endereco, valor):
        k_words_bits = int(math.log2(self.k_words))
        k_row_bits = int(math.log2(math.ceil(self.tamanho_cache / self.k_words)))

        w = endereco & (self.k_words - 1)
        r = (endereco >> k_words_bits) & ((1 << k_row_bits) - 1)
        t = endereco >> (k_row_bits + k_words_bits)

        self.cache_lines[r].write(t, w, valor)

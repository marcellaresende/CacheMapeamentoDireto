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
            self.cache_lines.append(CacheLine(k_words, line, tamanho, ram))# Preenche a cache com as cache lines correspondentes

    def verifica_endereco(self, endereco):
        if endereco < 0 or endereco >= self.capacidade:
            raise EnderecoInvalido(endereco)# Valida se o endereço ultrapassa a capacidade da memoria

    def read(self, endereco):
        k_words_bits = int(math.log2(self.k_words))# Define o número de palavras (blocos) na cache line
        k_row_bits = int(math.log2(math.ceil(self.tamanho_cache / self.k_words)))# Define o número de linhas com formam a cache

        w = endereco & (self.k_words - 1) # Essa operação extrai os menores bits (k_words_bits) do endereço, que indicam o posicionamento da palavra (bloco) dentro de uma linha de cache.

        r = (endereco >> k_words_bits) & ((1 << k_row_bits) - 1)# Extrai os bits de k_row_bits no endereço, que são usados para indicar o indice da linha onde está o endereço de memória.
                                                                # O QUE ESTÁ SENDO FEITO!!!!!!!
                                                                # 1º Desloca o endereço para mais a direita em k_words_bits posições
                                                                # 2º operação bit a bit AND é aplicada entre o resultado do 1º e ((1 << k_row_bits) - 1) para extrair os próximos k_row_bits no endereço

        t = endereco >> (k_row_bits + k_words_bits)# Restante do endereço indica a tag de busca em uma cache

        return self.cache_lines[r].read(t, w)# Lê o endereco da linha r e espaço w

    def write(self, endereco, valor):
        k_words_bits = int(math.log2(self.k_words))
        k_row_bits = int(math.log2(math.ceil(self.tamanho_cache / self.k_words)))

        w = endereco & (self.k_words - 1) # Essa operação extrai os menores bits (k_words_bits) do endereço, que indicam o posicionamento da palavra (bloco) dentro de uma linha de cache.
        r = (endereco >> k_words_bits) & ((1 << k_row_bits) - 1)#  Extrai os bits de k_row_bits no endereço, que são usados para indicar o indice do endereço em uma linha específica na cache
        t = endereco >> (k_row_bits + k_words_bits)# Restante do endereço indica a tag de busca em uma cache

        self.cache_lines[r].write(t, w, valor)# Escreve na cache line no endereco da linha r e espaço w

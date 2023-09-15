from es import Es
from ram import RAM
from cache import Cache
from cpu import CPU
from enderecoInvalido import EnderecoInvalido

print("Mapeamento Direto\n")

# Cria componentes da arquitetura
es = Es(print)
ram = RAM(8 * 1024 * 1024)
cache = Cache(4 * 1024, ram, 64)
cpu = CPU(es, cache)

try:
    # Carrega "programa" na memória
    inicio = 10

    ram.write(inicio, 118)
    ram.write(inicio + 1, 130)

    # Executa o programa
    cpu.run(inicio)

except EnderecoInvalido as e:
    print("Erro:", e)

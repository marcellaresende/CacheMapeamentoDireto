class CPU:
    def __init__(self, es, mem):
        self.PC = 0  # program counter
        self.regA = 0  # registrador A
        self.regB = 0  # registrador B
        self.regC = 0  # registrador C
        self.mem = mem
        self.es = es

    def run(self, ender):
        self.PC = ender

        # Lê "programa" da memória
        self.regA = self.mem.read(self.PC)
        self.PC += 1
        self.regB = self.mem.read(self.PC)
        self.PC += 1

        # Roda o programa
        self.regC = 1  # Contador
        while self.regA <= self.regB:
            self.mem.write(self.regA, self.regC)
            self.es.output("> " + str(self.regA) + " -> " + str(self.regC) + "\n")
            self.regC += 1
            self.regA += 1

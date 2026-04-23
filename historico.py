class Historico:
    def __init__(self):
        self.operacoes = []

    def adicionar(self, tipo, valor):
        self.operacoes.append(f"{tipo}: R$ {valor}")

    def mostrar(self):
        for op in self.operacoes:
            print(op)

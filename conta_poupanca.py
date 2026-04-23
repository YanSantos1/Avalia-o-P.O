from contas.conta import Conta

class ContaPoupanca(Conta):
    def sacar(self, valor):
        limite = 500
        if valor > limite:
            print("Limite de saque excedido!")
        elif valor <= self.get_saldo():
            self._Conta__saldo -= valor
            self.historico.adicionar("Saque CP", valor)
            print("Saque realizado!")
        else:
            print("Saldo insuficiente!")

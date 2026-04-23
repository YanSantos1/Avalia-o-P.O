from contas.conta import Conta

class ContaCorrente(Conta):
    def sacar(self, valor):
        if valor <= self.get_saldo():
            self._Conta__saldo -= valor
            self.historico.adicionar("Saque CC", valor)
            print("Saque realizado!")
        else:
            print("Saldo insuficiente!")

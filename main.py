from clientes.cliente import Cliente
from contas.conta_corrente import ContaCorrente
from contas.conta_poupanca import ContaPoupanca
from sistema.banco import Banco


banco = Banco()

while True:
    print("\n1 - Criar Conta")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Saldo")
    print("5 - Histórico")
    print("0 - Sair")

    op = input("Escolha: ")

    if op == "1":
        nome = input("Nome: ")
        tipo = input("1-CC 2-CP: ")
        cliente = Cliente(nome)
        numero = len(banco.contas) + 1

        if tipo == "1":
            conta = ContaCorrente(numero, cliente)
        else:
            conta = ContaPoupanca(numero, cliente)

        banco.adicionar_conta(conta)
        print("Conta criada!")

    elif op == "2":
        num = int(input("Conta: "))
        valor = float(input("Valor: "))
        banco.contas[num-1].depositar(valor)

    elif op == "3":
        num = int(input("Conta: "))
        valor = float(input("Valor: "))
        banco.contas[num-1].sacar(valor)

    elif op == "4":
        num = int(input("Conta: "))
        print("Saldo:", banco.contas[num-1].get_saldo())

    elif op == "5":
        num = int(input("Conta: "))
        banco.contas[num-1].historico.mostrar()

    elif op == "0":
        break

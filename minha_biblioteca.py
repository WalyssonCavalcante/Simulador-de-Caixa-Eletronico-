def exibir_menu():
    print("\n=== Caixa Eletrônico ===")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Ver saldo")
    print("4 - Sair")
    return int(input("Escolha uma opção: "))

def depositar(saldo, valor):
    if valor > 0:
        saldo += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso!")
    else:
        print("Valor inválido!")
    return saldo

def sacar(saldo, valor):
    if valor <= 0:
        print("Valor inválido!")
    elif valor > saldo:
        print("Saldo insuficiente!")
    else:
        saldo -= valor
        print(f"Saque de R${valor:.2f} realizado com sucesso!")
    return saldo

def ver_saldo(saldo):
    print(f"Saldo atual: R${saldo:.2f}")

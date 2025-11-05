from minha_biblioteca import sacar, depositar, ver_saldo, exibir_menu

def main():
    saldo = 1000.0
    while True:
        opcao = exibir_menu()
        
        if opcao == 1:
            valor = float(input("Digite o valor do depósito: "))
            saldo = depositar(saldo, valor)
        elif opcao == 2:
            valor = float(input("Digite o valor do saque: "))
            saldo = sacar(saldo, valor)
        elif opcao == 3:
            ver_saldo(saldo)
        elif opcao == 4:
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()

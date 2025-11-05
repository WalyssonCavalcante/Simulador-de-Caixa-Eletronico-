# 💰 Simulador de Caixa Eletrônico

Um projeto desenvolvido em **Python** com foco em **lógica de programação e modularização**, simulando as operações básicas de um caixa eletrônico.  
Este sistema permite realizar **depósitos, saques e consultas de saldo**, utilizando uma **biblioteca personalizada** com funções reutilizáveis.

---

## 📘 Objetivo do Projeto

Este projeto foi desenvolvido como parte da disciplina **Lógica de Programação**, com o propósito de:
- Aplicar o conceito de **modularização**;
- Praticar **criação e reutilização de funções**;
- Exercitar a **organização e clareza do código**.

---

## 🧩 Estrutura do Projeto

📂 Simulador-Caixa-Eletronico
├── main.py # Módulo principal (fluxo do programa)
├── minha_biblioteca.py # Biblioteca personalizada com as funções
└── README.md # Documentação do projeto


---

## ⚙️ Funcionalidades

- 💵 **Depositar:** adiciona valores ao saldo da conta.  
- 💸 **Sacar:** realiza saques respeitando o saldo disponível.  
- 📊 **Ver Saldo:** exibe o saldo atual.  
- 🚪 **Sair:** encerra o sistema de forma segura.

---

## 🧠 Funções da Biblioteca

| Função | Descrição |
|--------|------------|
| `exibir_menu()` | Mostra o menu principal e retorna a opção escolhida. |
| `depositar(saldo, valor)` | Realiza um depósito e retorna o saldo atualizado. |
| `sacar(saldo, valor)` | Realiza um saque se houver saldo suficiente. |
| `ver_saldo(saldo)` | Exibe o saldo atual formatado em reais. |

---

## 💻 Exemplo de Execução

```python
from minha_biblioteca import sacar, depositar, ver_saldo, exibir_menu

def main():
    saldo = 1000.0  # saldo inicial da conta
    
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
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
```
## 🚀 Como Executar o Projeto


### ⚙️ Passos para execução

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/WalyssonCavalcante/Simulador-de-Caixa-Eletronico-.git
    ```
2. **Acesse a pasta do projeto:**
   ```bash
   cd Simulador-Caixa-Eletronico
   ```
3.**Execute o programa principal:**
  ```bash
   python main.py
  ```

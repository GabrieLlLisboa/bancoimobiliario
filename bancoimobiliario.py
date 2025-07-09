
# Imports
import time

# Variáveis

resposta = ""
deposito = 0
opcao = ""
saldo = 0
limite_saque = 500

menu = """
[1] Depositar
[2] Sacar
[3] Saldo
[4] Sair

=> """
# Código


while True:
    opcao = input(menu)

    if opcao == "1":
        deposito = int(input("Digite o depósito que você deseja fazer:"))
        saldo += deposito
        print("Seu saldo após este depósito é de:", saldo)

    elif opcao == "2":
        print("Seu saldo é de:", saldo)
        sacar = float(input("Quanto você deseja sacar?"))
        saldo -= sacar
        print("Agora você tem:", saldo)

    elif opcao == "3":
        print("Seu saldo é de:", saldo)
        resposta = input("Deseja sair?")
        if resposta.lower() == "sair":
            print(menu)

    elif opcao == "4":
        print("Obrigado por usar nosso sistema!")
        print("Saindo em 3 segundos.")
        time.sleep(3)
        break
import os

saldo =0
saque=0

extrato="-----------Extrato------------"

qtde_saques=0
LIMITE=500

menu = """
############## MENU ################
1. Depositar
2. Sacar
3. Extrato
4. Limpar
5. Sair
####################################
"""

op = 0

while True:

    print(menu)
    op = int(input("Digite uma opção:"))
    if op == 1:
        dep = float(input("Informe o valor do depósito:"))
        if dep <= 0:
            print("Valor inválido!")
        else:
            saldo += dep
            extrato=extrato+"\nDepósito: R$ " + str(dep)
    elif op == 2:
        saq = float(input("Informe o valor do saque:"))
        if saq <= 0 or saq > LIMITE or saq > saldo:
            print("Valor inválido!")
        else:
            if qtde_saques > 3:
                print("Número de saques excedido!")
            else:
                saldo -= saq
                extrato=extrato+"\nSaque...: R$ " + str(saq)
                qtde_saques += 1
    elif op == 3:
        print(extrato)
        print("Saldo...: R$ " + str(saldo))
        print("-------------------------------")
    elif op == 4:
        os.system('clear')
    elif op == 5:
        break
    else:
        print("Opção inválida!")

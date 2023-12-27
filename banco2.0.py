saldo = 0
saque = 0
numero_saques = 0
LIMITE = 500
LIMITE_SAQUES = 3
AGENCIA = "0001"
conta = 0
usuarios = {}
contas = {}

menu = """
############## MENU ################
1. Depositar
2. Sacar
3. Extrato
4. Criar Usuário
5. Criar Conta Corrente
6. Listar Usuários
7. Listar Contas
8. Sair
####################################
"""
extrato="---------------Extrato---------------"

op = 0


def depositar(saldo, valor, extrato, /):
    if valor <= 0:
        print("Valor inválido!")
    else:
        saldo += valor
        extrato=extrato+"\nDepósito: R$ " + str(valor)
    return [saldo, extrato]


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor <= 0 or valor > limite or valor > saldo:
        print("Valor inválido!")
    else:
        if numero_saques == limite_saques:
            print("Número de saques excedido!")
        else:
            saldo -= valor
            extrato = extrato + "\nSaque...: R$ " + str(valor)
            numero_saques += 1
    return [saldo, extrato, numero_saques]


def visualizar_extrato(saldo, *, extrato):
    print("\n" + extrato)
    print("\nSaldo...: R$ " + str(saldo))
    print("-------------------------------------")


def criar_usuario(*, cpf, nome, data_nascimento, endereco):
    usuarios[cpf] = [nome, data_nascimento, endereco]
    return usuarios


def criar_conta(*, agencia, conta, usuario):
    contas[conta] = [agencia, usuario]
    return contas


def listar_usuarios(lista):
    print("\n-------------------------------- Lista de Usuários --------------------------------")
    for chave, valor in lista.items():
        print(f'CPF: {chave}, Nome: {valor[0]}, Nascido em: {valor[1]}')
        print(f'..............Endereço: {valor[2]}')
    print("\n-----------------------------------------------------------------------------------")


def listar_contas(lista):
    print("\n-------------------------------- Lista de Contas ----------------------------------")
    for chave, valor in lista.items():
        print(f'Agência: {valor[0]}, Conta: {chave}, Titular: {valor[1]}')
    print("\n-----------------------------------------------------------------------------------")


while True:
    print(menu)
    op = int(input("Digite uma opção: "))
    if op == 1:
        print("############################### DEPÓSITO ###############################")
        valor = float(input("Digite o valor do depósito:"))
        retorno = depositar(saldo, valor, extrato)
        saldo = retorno[0]
        extrato = retorno[1]
    elif op == 2:
        print("############################### SAQUE ###############################")
        valor = float(input("Digite o valor do saque:"))
        retorno = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=LIMITE, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)
        saldo = retorno[0]
        extrato = retorno[1]
        numero_saques = retorno[2]
        print(saldo)
        print(numero_saques)
    elif op == 3:
        visualizar_extrato(saldo, extrato=extrato)
    elif op == 4:
        print("######################### CADASTRAR USUÁRIO #########################")
        cpf = input("CPF do usuário (apenas números): ")
        while not isinstance(cpf, int) and not len(cpf)==11:
            cpf = input("CPF do usuário (apenas números): ")    
        nome = input("NOME do usuário: ")
        data_nascimento = input("Data de Nascimento (dd/mm/aaaa): ")
        endereco = input("Endereço (logradouro,num,bairro,cidade/uf): ")
        usuarios = criar_usuario(cpf=cpf, nome=nome, data_nascimento=data_nascimento, endereco=endereco)
    elif op == 5:
        print("##################### CADASTRAR CONTA CORRENTE #####################")
        agencia = AGENCIA
        conta = conta + 1
        usuario = input("CPF do Titular da Conta: ")
        while not usuario in usuarios:
            usuario = input("CPF do Titular da Conta: ")
        contas = criar_conta(agencia=agencia, conta=conta, usuario=usuario)
    elif op == 6:  
        listar_usuarios(usuarios)
    elif op == 7:  
        listar_contas(contas)
    elif op == 8:
        break
    else:
        print("Opção inválida")

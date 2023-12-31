from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime, date


class Cliente:
    
    def __init__(self, endereco) -> None:
        self._endereco = endereco
        
    def realizar_transacao(self, conta, transacao):
        pass
    
    
class Historico:
    
    def __init__(self) -> None:
        self._transacoes = []
        
    def adicionar_transacao(self, transacao):
        self._transacoes.append(transacao)
        
       
class PessoaFisica(Cliente):
    
    def __init__(self, cpf, nome, data_nascimento, endereco) -> None:
        super().__init__(endereco) 
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento
    
    def __str__(self) -> str:
        return f"""
            CPF : {self._cpf}
            Nome: {self._nome}
            Data de Nascimento: {self._data_nascimento}
            """

   
class Conta:
    
    def __init__(self, numero, cliente) -> None:
        self._saldo = 0 
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
    
    @property
    def saldo(self):
        return self._saldo
    
    def nova_conta(self, cliente, numero):
        pass
    
    def sacar(self, valor):
        """ num_saques=0
        for historico in self._historico._transacoes:
            if historico._tipo == "Saque":
                num_saques += 1

        contacorrente = ContaCorrente()
        if valor <= 0 or num_saques > contacorrente.limite_saques or valor > contacorrente.limite:
            return False
        else:
            self._saldo -= valor
            self._historico.adicionar_transacao(saque) """
        return True
    
    def depositar(self, valor):
        if valor <= 0:
            return False
        else:
            self._saldo += valor
            self._historico.adicionar_transacao(deposito)
            return True
        
    def __str__(self) -> str:
        
        extrato ="------------------------------------------------------------------------------"
        extrato += f"\nCONTA: {self._numero}, AGENCIA: {self._agencia}"
        extrato += f"\nTitular: {self._cliente._nome}"
        
        for historico in self._historico._transacoes:
            extrato += f"\n{historico._tipo}: {historico._valor}"
        
        extrato += f"\nSaldo: {self.saldo}"
        
        return extrato
    
    
class ContaCorrente(Conta):
    
    def __init__(self, limite=500.0, limite_saques=3):
        self.limite = limite
        self.limite_saques = limite_saques
        
        
class Transacao(ABC):
    
    @classmethod
    def registrar(conta):
        pass
    
    
class Deposito(Transacao):
    
    def __init__(self, valor) -> None:
        self._valor = valor
        self._tipo = "Deposito"
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        if conta.depositar(self.valor):
            print(f"Depósito de R$ {self.valor} realizado com sucesso!")


class Saque(Transacao):
    def __init__(self, valor) -> None:
        self._valor = valor
        self._tipo = "Saque"
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        if conta.sacar(self.valor):
            historico = Historico()
            historico.adicionar_transacao(self)


class Banco:
    
    def __init__(self) -> None:
        self._clientes = []
        self._contas = []

    def adicionar_cliente(self, cliente):
        self._clientes.append(cliente)
        
    def adicionar_conta(self, conta):
        self._contas.append(conta)
        
    def valida_cpf(self, cpf):
        if len(cpf) == 11:
            if cpf.isnumeric:
                return True
            else:
                print("Informe apenas números!")
        else:
            print("CPF deve conter 11 números!")
        return False
    
    def buscar_cliente(self, cpf):
        for cliente in self._clientes:
            if cliente._cpf == cpf:
                return cliente
        return print("Cliente não cadastrado!")

    def buscar_conta(self, cpf):
        minhas_contas = []
        for conta in self._contas:
            if conta._cliente._cpf == cpf:
                minhas_contas.append(conta)
        return minhas_contas 


menu = """
############## MENU ################
1. Depositar
2. Sacar
3. Extrato
4. Cadastrar Cliente
5. Cadastrar Conta Corrente
6. Listar Usuários
7. Listar Contas
8. Sair
####################################
"""

pf1 = PessoaFisica("11111111111", "João Miguel Alves", date, "rua A, 11, Centro, Aurora-CE")
banco = Banco()
banco.adicionar_cliente(pf1)
conta1 = Conta(1, pf1)
banco.adicionar_conta(conta1)

while True:
    
    print(menu)
    
    op = int(input("Digite uma opção: "))
    
    if op == 1:
               
        print("\n########################### DEPÓSITO ###########################\n")
        
        cpf = input("Informe seu CPF: ")
        
        while not banco.valida_cpf(cpf):
            cpf = input("Informe seu CPF: ")
        
        pessoa = banco.buscar_cliente(cpf)
        
        contas = banco.buscar_conta(cpf)
        
        quant_contas = len(contas)
                
        for conta in contas:
            print(conta)
               
            if quant_contas == 0:
                print("Cliente não possui conta!")
            elif quant_contas == 1:
                conta = contas[0]
                indice = 1
            else:
                indice = int(input("Escolha a Conta (1-Primeira, 2-Segunda,): "))   
                while indice > quant_contas:
                    indice = int(input("Escolha a Conta (1-Primeira, 2-Segunda,): "))
                conta = contas[indice - 1] 
        
        valor = float(input("\nDigite o valor do depósito: R$ "))
        deposito = Deposito(valor)
        deposito.registrar(conta)
        print("\n",contas[indice - 1])
        
    elif op == 2:
        """ print("############################### SAQUE ###############################")
        valor = float(input("Digite o valor do saque:"))
        retorno = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=LIMITE, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)
        saldo = retorno[0]
        extrato = retorno[1]
        numero_saques = retorno[2]
        print(saldo)
        print(numero_saques) """
    elif op == 3:
        """ visualizar_extrato(saldo, extrato=extrato) """
    elif op == 4:
        """ print("######################### CADASTRAR USUÁRIO #########################")
        cpf = input("CPF do usuário (apenas números): ")
        while not isinstance(cpf, int) and not len(cpf)==11:
            cpf = input("CPF do usuário (apenas números): ")    
        nome = input("NOME do usuário: ")
        data_nascimento = input("Data de Nascimento (dd/mm/aaaa): ")
        endereco = input("Endereço (logradouro,num,bairro,cidade/uf): ")
        usuarios = criar_usuario(cpf=cpf, nome=nome, data_nascimento=data_nascimento, endereco=endereco) """
    elif op == 5:
        """ print("##################### CADASTRAR CONTA CORRENTE #####################")
        agencia = AGENCIA
        conta = conta + 1
        usuario = input("CPF do Titular da Conta: ")
        while not usuario in usuarios:
            usuario = input("CPF do Titular da Conta: ")
        contas = criar_conta(agencia=agencia, conta=conta, usuario=usuario) """
    elif op == 6:  
        """ listar_usuarios(usuarios) """
    elif op == 7:  
        cpf = int(input("Informe o CPF para consultar suas contas: "))
    elif op == 8:
        break
    else:
        print("Opção inválida")
        
        
        
""" strdata = "18/05/1982"
data = datetime.strptime(strdata, "%d/%m/%Y")        

pf1 = PessoaFisica("11111111111", "João Miguel Alves", data, "rua A, 11, Centro, Aurora-CE")   
   
conta1 = Conta(1, pf1)
conta2 = Conta(2, pf1)

pf1.adicionar_conta(conta1)
pf1.adicionar_conta(conta2)

pf2 = PessoaFisica("22222222222", "Antonio Miguel Alves", data, "rua B, 11, Centro, Aurora-CE")
conta3 = Conta(3, pf2)
pf2.adicionar_conta(conta3)

deposito = Deposito(100.0)
deposito.registrar(conta1)

deposito = Deposito(200.0)
deposito.registrar(conta1)
print(conta1)

saque = Saque(100.0)
saque.registrar(conta1)

print(conta1) """

""" print("----------------------------------")
print(f"Contas de : {pf1._nome}")
for conta in pf1._contas:
    print(conta)
print("----------------------------------") """

"""print(f"Contas de : {pf2._nome}")    
for conta in pf2._contas:
    print(conta)  
print("----------------------------------") """
            
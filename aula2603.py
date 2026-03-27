# Primeiro menu em Python
print("Qual seu CPF? Sem pontos ou traços")
CPF = int(input())
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("Banco Exxemplo")
print("Usuário: Bia")
print("CPF:",CPF)
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("~Selecione uma opção:") 
print("1- Saldo") 
print("2- Extratos (Últimos 5 dias)")  
print("3- Emprétimos")
opção = int(input())
if opção == 1:
    print("~Saldo:00,01")
elif opção == 2:
    print("~Extratos: Você não fez nenhuma movimentação nos útimos dias.")
elif opção == 3:
    print("~Empréstimos: Não são possíveis no momento.")
elif opção <=0:
    print("~Opção inválida")
elif opção >3:
    print("~Opção inválida")


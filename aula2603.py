# Primeiro menu em Python
cliente = input("Qual seu CPF?")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("Banco Exxemplo")
print("Usuário: Bia")
print("CPF:",cliente)
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("Selecione uma opção: 1- Saldo / 2- Extratos (Últimos 5 dias) / 3- Emprétimos")
opção = int(input())
if opção == 1:
    print("Saldo:00,01")
elif opção == 2:
    print("Extratos: Você não fez nenhuma movimentação nos útimos dias.")
elif opção == 3:
    print("Empréstimos: Não são possíveis no momento.")
elif opção <=0:
    print("Opção inválida")
elif opção >3:
    print("Opção inválida")




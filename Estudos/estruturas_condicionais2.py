saque = int(input("Valor de saque: "))
saldo_conta_banco = 2000
cheque_especial = 350
conta_normal = False
conta_estudante = False

if conta_normal:
    if saque <= saldo_conta_banco:
        print("Saque realizado com sucesso!")
    elif saque == (saldo_conta_banco + cheque_especial):
        print("Saque realizado com uso do cheque especial")
    else:
         print("Não foi possivel realizar o saque!")
elif conta_estudante:
    if saque <= saldo_conta_banco:
        print("Saque realizado com sucesso da sua conta de estudante!")
else:
    print("Sistema não reconheceu seu tipo de conta, entre em contato com o seu gerente.")
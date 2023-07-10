def habilitacao(idade_minima):
    idade = 18
    idade_especial = 17

    if idade_minima >= idade:
        print("Você pode tirar sua habilitação")
    
    elif idade_minima == idade_especial:
        print("Como você não atingiu a idade para praticar as aulas praticas, você ainda pode fazer a teorica.")

    else:
        print("Você ainda não pode tirar sua habilitação")


habilitacao(idade_minima= int(input("Informe sua idade: ")))

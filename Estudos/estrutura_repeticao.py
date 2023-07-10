texto = input("informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
  print()

  opcao = -1

  while opcao != 0:
      
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

  if opcao == 1:
        print('Sacando...')

  elif opcao == 2:
        print("exibindo o extrato...")
  else:
      print("obrigado por usar nosso sistema bancario, até logo!")
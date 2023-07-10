nome = input("qual o seu nome: ")
idade = int(input("qual a sua idade: "))
profissao = input("qual a sua profissão: ")
linguagem = input("qual linguagem de programação: ")

#Old Style
print ("\nOlá. me chamo %s, Eu tenho %d ano(s) de idade, trabalho como %s e estou matriculado no curso de %s" %(nome,idade,profissao,linguagem))


# Format
print("\nOlá. me chamo {0}, Eu tenho {1} ano(s) de idade, trabalho como {2} e estou matriculado no curso de {3}".format(nome, idade,profissao, linguagem))

#f-string
print(f"\nOlá. me chamo {nome}, Eu tenho {idade} ano(s) de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}")

name = "Lucas Henrique"
print(name[::-1])
print(name[:])
print(name[:6])
print(name[7:])
print(name[10:5])
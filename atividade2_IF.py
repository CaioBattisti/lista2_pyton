#faça um programa que receba um nota de aluno e se for superior ou igual a 7 apareça mensagem que ele esta aprovado,
#se for inferior a 5 ele esta nao "aprovado/reprovado direto" e se estiver entre 5 e 7 apareça mensagem "nao aprovado/recuperação"
nota = int(input("digite a nota:"))
if nota >=7:
    print("aprovado!")
else:
    if nota >=5:
        print("nao aprovado/recuperação")
        print("nao aprovado/reprovado direto")
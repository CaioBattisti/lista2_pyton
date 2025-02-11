#faça um programa que receba um nota de aluno e se for superior ou igual a 7 apareça mensagem que ele esta aprovado,
#se for inferior a 5 ele esta nao "aprovado/reprovado direto" e se estiver entre 5 e 7 apareça mensagem "nao aprovado/recuperação"
num1 = int(input("digite a nota:"))
if num1 >=7:
    print("aluno aprovado!")
else:
    if num1 >=5:
        print("aluno em recuperação!")
    else:
        print("aluno reprovado!")
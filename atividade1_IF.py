#faça um programa que o usuario digite um numero e diga seu numero e diga se o numero e superior a 20,inferir a 10 ou se esta entre 10 e 20
num1 = int(input("digite um numero:"))
if num1 > 20:
    print("seu numero e superior a 20!")
elif num1 < 10:
    print("seu numero e menor que 10!")
else:
    print("o numero esta entre 10 e 20!")
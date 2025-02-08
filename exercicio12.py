#escreva um programa que pergunte o valor total da conta em seguida pergunte quantos clientes tem,divida a entre os clientes e exiba o quanto cada cliente deve pagar segida da mensagem "cada cliente deve pagar:"valor
conta =int(input("qual o valor total da conta?"))
clientes =int(input("qual o numero de clientes?"))
divisao = conta / clientes
print("cada cliente deve pagar:",divisao)
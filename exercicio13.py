#escreva um programa que solicite um determinado numero de dias,em seguida exiba o quanto esses dias equivalem em horas minutos e segundos
dias = int(input("quantos dias?"))
horas = dias * 24
minutos = horas * 60
segundos = horas * minutos * 60
print("o dias equivalem a:",horas,"horas",minutos,"minutos",segundos,"segundos")
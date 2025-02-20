#excluindo da lista usando .pop obs:mais deixa o valor
lucro_jun ={"janeiro":1,"fevereiro":2,"marco":3}
lucro_2tri ={"abril":4,"maio":5,"junho":6}
lucro_jun=lucro_2tri.pop("junho")
print(lucro_2tri)
print(lucro_jun)
#REMOVENDO TDOS OS DADOS DE UM DICIONARIO:usando .clear obs:apaga todos os dados
lucro_2tri.clear()
print(lucro_2tri)
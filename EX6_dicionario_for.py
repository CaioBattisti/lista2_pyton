vendas_tecnologia = {'iphone':'1500','sansung galaxy':'12000','Tv samsung':'10000','ps5':'14300'}
#demonsrando for
for chave in vendas_tecnologia:
    print(chave)#ele nao diz o valor
    print("o produto {} vendeu {} unidades.".format(chave,vendas_tecnologia[chave]))#diz o valor
#metodo .itens:
for item in vendas_tecnologia.items():
    print(item)
#metodo unpacking:
for produto,vendas in vendas_tecnologia.items():
    print("{}: {} de unidades.".format(produto,vendas))
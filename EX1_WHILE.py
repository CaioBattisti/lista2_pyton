venda =input("registe um produto. Para cancelar o registro de um novo produto basta apertar enter sem digitar nada: ")
vendas = []
#crie aqui o programa
while venda != "":
    vendas.append(venda)
    venda =input("registre um produto. para cancelar o registro de um novo produto, basta apertar enter sem digitar nada: ")
print("registros finalizados. As vendas cadastradas foram: {}".format(vendas))
meta = 20000
vendas =int(input(digite a venda:))

if vendas < meta:
    print("não ganhou bônus")
elif vendas > (meta*2):
    print("ganhou {} de bônus".format(bonus))
else:
    bonus = 0.03 * vendas
    print("ganhou {} de bônus".format(bonus))
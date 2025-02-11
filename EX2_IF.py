meta = 20000
vendas = 1000

if vendas < meta:
    print("não ganhou bônus")
elif vendas > (meta*2):
    bonus = 0.07 * vendas
    print("ganhou {} de bônus".format(bonus))
else:
    bonus = 0.03 * vendas
    print("ganhou {} de bônus".format(bonus))
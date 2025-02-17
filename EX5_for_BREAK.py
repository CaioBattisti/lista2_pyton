pessoas_presentes = ['john snow','jesse pinkman','aria stark','tyrion','lannister']
#quero saber se uma pessoa espeifica esta presente .
chamada = 'aria stark'
for pessoa in pessoas_presentes:
    if pessoa == chamada:
        print('{} esta presente.'.format(chamada))
        break
    else:
        print("so um print para mostrar que o for passou por essa pessoa: "+str(pessoa))
        continue
        print("so para mostrar que isso nao vai ser printado")
        print("deu para entender ne?")
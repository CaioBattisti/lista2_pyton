#transforma apenas a primeira letra de uma string em maiscula.
nome = "caio"
print(nome.capitalize(),"\n")

#transorma todas as letras em minusculas.
nome = "CAIO"
print(nome.casefold(),"\n")

#conta um numero de vezes que um caractere especifico aparece na string.
nome = "CaioLuizBattisti@gmail.com"
print(nome.count('i'),"\n")

#retorna true (verdadeiro) ou false (falso) para um teste se a string com uma string especifica.
nome = "CaioLuizBattisti@gmail.com"
print(nome.endswith('gmail.com'),"\n")

#esncontra a posição do termo procurado, lembre-se que se começa com ZERO.
nome = "CaioLuizBattisti@gmail.com"
print(nome.find('@'),"\n")

#verifica se o texto e todo feito com letras.
nome = "Caio"
print(nome.isalpha(),"\n")

#verifica se o texto e feito com numeros.
nome = "123"
print(nome.isnumeric(),"\n")

#substitue um caractere escolhido por outro.
nome = "Caio"
print(nome.replace('o','u'),"\n")

#separa o texto string baseado em algum caractere indicado
nome = "CaioLuizBattisti @ gmail.com"
print(nome.split('@'),"\n") 
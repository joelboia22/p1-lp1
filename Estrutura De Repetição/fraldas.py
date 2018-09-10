soma = 0
while (True):
    idade = int(input('digite a idade: '))
    if (idade <= 2):
        soma += 270
    else:
        soma += 180

    saida = input('tem mais criança: ')
    if saida == 'não' or saida == 'Não' or saida == 'NÃO':
        break

var_aux = int(soma/100)
if soma%100 != 0:
    var_aux += 1

print(var_aux)
print((var_aux * 100)-soma)

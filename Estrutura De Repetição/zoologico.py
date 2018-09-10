cont = 0
media_tigres = 0
cont1 = 0
cont2 = 0

while True:
    animal = input('digite o animal: ')
    peso = float(input('digite o peso: '))
    pais = input('digite o pais de origem: ')

    if animal == 'tigre':
        cont += 1
        media_tigres += peso
        media_tigres = media_tigres / cont
    elif animal == 'cobra' and pais == 'venezuela':
        cont1 += 1
    elif animal == 'macaco':
        cont2 += 1

    saida = input('Deseja continuar:? ')
    if saida == 'parar' or saida == 'Parar' or saida == 'PARAR':
        break

print(cont2)
print(media_tigres)
print(cont1)
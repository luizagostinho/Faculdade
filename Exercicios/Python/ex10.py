print('Bem vindo ao Cinema!')
print('1 - De 0 a 3 - Grátis')
print('2 - De 3 a 12 - R$ 15,00')
print('3 - 12 ou + - R$ 30,00')


total = 0
dinheiro = 0
while True:
    idade = int(input('Qual a sua idade?'))
    if idade == 0:
       break

    total += 1



    if idade < 3:
        ingresso = 0
    elif idade > 12:
        ingresso = 30
    else:
        ingresso = 15

    dinheiro += ingresso 

media = idade / total
print(f'Total de ingressos vendidos: {total}, total arrecadado: R$ {dinheiro}')




print('Escolha oque deseja comprar: ')
print('1 - Maça')
print('2 - Banana')
print('3 - Laranja')    

produto = int(input('Qual a sua escolha? '))
qtd = int(input('Quantas unidades? '))

if (produto == 1):
    valor = qtd * 2.3
    print(f'Você comprou {qtd} maçãs, totalizando R$ {valor}')
else:
    if (produto == 2):
        valor = qtd * 1.5
        print(f'Você comprou {qtd} bananas, totalizando R$ {valor}')
    else:
        if (produto == 3):
            valor = qtd * 2.0
            print(f'Você comprou {qtd} laranjas, totalizando R$ {valor}')
        else:
            print(f'Produto inexistente! Escolha entre 1, 2 ou 3.')

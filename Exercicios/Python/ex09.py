print('LANCHONETE')
print('1 - Coxinha - R$ 5,00')
print('2 - Pastel - R$ 7,00')
print('3 - Café - R$ 4,00')
print('4 - Suco - R$ 6,00')
print('5 - SAIR')

total = 0
while True:
    op = int(input('Digite o numero do produto: '))
    qtd = int(input('Digite a quantidade do produto: '))

    if (op == 1):
        total = total + qtd * 5.00
    elif (op == 2):
        total = total + qtd * 7.00
    elif (op == 3):
        total = total + qtd * 4.00
    elif (op == 4):
        total = total + qtd * 6.00
    elif (op == 5):
        break
    else:
        print('Produto inválido!')

print(f'O total da compra é R$ {total}')


        

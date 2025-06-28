
print('Seja bem-vindo, Luiz Fernando!')


print('Qual o valor do pedido?')
valor = float(input('R$ ')) #recebe o valor do pedido

parcelas = int(input('Numero de parcelas: ')) #Recebe o numero de parcelas

if parcelas < 4:
	juros = 0
elif parcelas >= 4 and parcelas < 6:
	juros = 4
elif parcelas >= 6 and parcelas < 9:
	juros = 8
elif parcelas >= 9 and parcelas < 13:
	juros = 16
elif parcelas >= 13:
	juros = 32 #Base de juros conforme o enunciado
else:
	juros = 0

valor_com_juros = valor * (1 + juros / 100)
print(f'O valor da parcela é de R$ {valor_com_juros / parcelas:.2f}') #Valor já com juros, dividido pelo numero de parcelas

print(f'O valor total do pedido é de R$ {valor_com_juros:.2f}') #Valor total do pedido já com juros

print('Obrigado pela preferência!') #Mensagem de agradecimento
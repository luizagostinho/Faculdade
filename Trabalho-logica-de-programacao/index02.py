print('------ Seja bem-vindo a Loja da Marmita, Luiz Fernando! ------')

print('------------------ MENU DE PEDIDOS ---------------------------')

print('--- | Tamanho  | Bife Acebolado (BA) | Filé de Frango (FF) | --- ')
print('--- |    P     |      R$ 16,00       |     R$ 15,00        | --- ')
print('--- |    M     |      R$ 18,00       |     R$ 17,00        | --- ')
print('--- |    G     |      R$ 22,00       |     R$ 21,00        | --- ')
print('-------------------------------------------------------------')


total_pedido = 0  # Inicializa o total do pedido
soma = 0  # Inicializa a variável soma para o valor do pedido

while True: # Loop para fazer pedidos
    sabor = input('Qual o sabor da sua Marmita? (BA/FF): ')
    if sabor == "BA" or sabor == "FF":
        tamanho = input('Qual o tamanho da sua Marmita? (P/M/G): ')
        if tamanho == 'P' or tamanho == 'M' or tamanho == 'G':



            # Aqui o cliente pode adicionar o processamento do pedido.
        
         pedido = sabor + tamanho


        if sabor == 'BA':
            if tamanho == 'P':
                soma = 16.00
                print('Você escolheu Bife Acebolado no tamanho P: R$ 16,00')
            elif tamanho == 'M':
                soma = 18.00
                print('Você escolheu Bife Acebolado no tamanho M: R$ 18,00')
            elif tamanho == 'G':
                soma = 22.00
                print('Você escolheu Bife Acebolado no tamanho G: R$ 22,00')
        elif sabor == 'FF':
            if tamanho == 'P':
                soma = 15.00
                print('Você escolheu Filé de Frango no tamanho P: R$ 15,00')
            elif tamanho == 'M':
                soma = 17.00
                print('Você escolheu Filé de Frango no tamanho M: R$ 17,00')
            elif tamanho == 'G':
                soma = 21.00
                print('Você escolheu Filé de Frango no tamanho G: R$ 21,00')

        total_pedido += soma  # Adiciona o valor do pedido ao total
        print('Pedido realizado com sucesso!')

        mais = input('Deseja pedir mais alguma coisa? (S/N): ') # Pergunta se o cliente deseja fazer mais pedidos.
        if mais.upper() != 'S':
            print('Finalizando o pedido...')
            print(f'Valor total: R$ {total_pedido}')
            print('Obrigado por escolher a Loja da Marmita, Luiz Fernando!')
            print('Volte sempre!')
            break
    else:
        print('Tamanho inválido. Por favor, escolha P, M ou G.')
else:
    print('Sabor inválido. Por favor, escolha BA (Bife Acebolado) ou FF (Filé de Frango).')


print("Bem vindo a Fábrica de Camisetas do Luiz Fernando")

# Função para escolher o modelo da camiseta
def escolha_modelo():
    while True:
        print("Entre com o modelo desejado")
        print("MCS - Manga Curta Simples")
        print("MLS - Manga Longa Simples")
        print("MCE - Manga Curta Estampada")
        print("MLE - Manga Longa Estampada")
        modelo = input("->").upper()

        if modelo == "MCS":
            return 1.80, modelo
        elif modelo == "MLS":
            return 2.10, modelo
        elif modelo == "MCE":
            return 2.90, modelo
        elif modelo == "MLE":
            return 3.20, modelo
        else:
            print("Escolha inválida, entre com o modelo novamente")

# Função para obter e validar o número de camisetas
def num_camisetas():
    while True:
        try:
            quantidade = int(input("Entre com o número de camisetas: "))
            if quantidade > 20000:
                print("Não aceitamos tantas camisetas de uma vez.")
                print("Por favor, entre com o número de camisetas novamente.")
                continue
            elif quantidade >= 2000:
                return quantidade * 0.88, quantidade  # 12% desconto
            elif quantidade >= 200:
                return quantidade * 0.93, quantidade  # 7% desconto
            elif quantidade >= 20:
                return quantidade * 0.95, quantidade  # 5% desconto
            elif quantidade > 0:
                return quantidade, quantidade  # Sem desconto
            else:
                print("Número inválido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

# Função para escolher o frete
def frete():
    while True:
        print("Escolha o tipo de frete:")
        print("1 - Frete por transportadora - R$ 100.00")
        print("2 - Frete por Sedex - R$ 200.00")
        print("0 - Retirar pedido na fábrica - R$ 0.00")
        opcao = input("->")
        if opcao == "1":
            return 100
        elif opcao == "2":
            return 200
        elif opcao == "0":
            return 0
        else:
            print("Opção inválida. Tente novamente.")

# (main)

preco_unitario, modelo_escolhido = escolha_modelo()

# Quantidade com desconto
quantidade_com_desconto, quantidade_original = num_camisetas()

# Escolha do frete
valor_frete = frete()

# Cálculo do total
total = (preco_unitario * quantidade_com_desconto) + valor_frete

# Exibição do total formatado
print(f"Total: R$ {total:.2f} (Modelo: {preco_unitario:.2f} * Quantidade(com desconto): {int(quantidade_com_desconto)} + frete: {valor_frete:.2f})")








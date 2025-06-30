def valida_int (pergunta, min, max):
    x = int(input(pergunta))
    while((x < min) or (x > max)):
        x = int(input(pergunta))
        return x
    
def existeArquivo(arquivo):
    try:
        a = open(arquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')
        a.close()
    except:
        print('Erro na criação do arquivo.')
    else:
        print(f'Arquivo {nomeArquivo} criado com sucesso!')

def cadastrarJogo(nomeArquivo, nomeJogo, nomeVideoGame):
    try:
        a = open(nomeArquivo, 'at')
    except:
        print('Erro ao abrir arquivo.')
    else:
        a.write(f'{nomeJogo};{nomeVideoGame}\n')
    finally:
        a.close()

def listarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
    except:
        print('Erro ao ler arquivo')
    else:
        print(a.read())
    finally:
        a.close()



# programa prncipal

arquivo = 'games.txt'
if existeArquivo(arquivo):
    print('Arquivo localizado no computador.')
else:
    print('Arquivo inexistente')
    criarArquivo(arquivo)

while True:
    print('MENU')
    print('1 - Cadastrar novo item.')
    print('2 - Listar os cadastros.')
    print('SAIR')

    op = valida_int('Escolha a opção desejada: ', 1, 3)
    if (op == 1): #novo item
        print('Opção de cadastrar novo item selecionada...\n')
        nomeJogo = input('Nome do Jogo: ')
        nomeVideoGame = input('Nome do Vieo Game: ')
        cadastrarJogo(arquivo, nomeJogo, nomeVideoGame )
    
    elif (op == 2): # Listar
        print('Opção de listar selecionada...\n')

    elif (op == 3):
        print('Encerrando o programa...')
        break


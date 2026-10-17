import os

cadastro_produtos = []

def limpa_tela():
    os.system("cls" if os.name == "nt" else "clear")

def volta_menu():
    input('\nTecle ENTER para voltar ao menu principal')

def menu():
    print('***   SISTEMA DE CADASTRAMENTO DE PRODUTOS   ***\n')
    print('1. Cadastrar produto')
    print('2. Listar produtos')
    print('3. Consultar produto')
    print('4. Alterar o preço do produto')
    print('5. Excluir produto')
    print('6. Sair')

def cadastrar_produto(lista):
    try:
        nome_produto = input('Informe o nome do produto: ')
        preco_produto = float(input('Informe o preço do produto: '))
        estoque_produto = int(input('Informe a quantidade em estoque: '))
        dados_produto = {'nome':nome_produto, 'preco':preco_produto, 'estoque':estoque_produto}
        lista.append(dados_produto)
        print('\nProduto cadastrado com sucesso')
    except ValueError:
        print('Entrada invalida')    
    
def listar_produtos(lista):
    for dados in lista:
        print(f'{dados['nome']} - {dados['preco']} - {dados['estoque']}')
       
def consultar_produto(lista):
    produto_consulta = input('Informe o produto para consulta na lista: ')
    for produto in lista:
        if produto['nome'] == produto_consulta:
            print(f'O produto {produto_consulta} consta na lista')
            break
    else:
        print(f'O produto {produto_consulta} não consta na lista')    

def alterar_preco(lista):
    try:
        altera_produto = input('Informe o produto para alteração do preço: ')
        novo_preco = float(input('Informe o novo preço do produto: '))
        for produto in lista:
            if produto['nome'] == altera_produto:
                produto['preco'] = novo_preco
                print('Preço do produto alterado com sucesso')
                break
        else:
            print(f'O produto {altera_produto} não consta na lista')    
    except ValueError:
        print('Entrada invalida')
             
def excluir_produto(lista): 
    produto_exclusao =  input('Informe o produto para excluir da lista: ')  
    for produto in lista:
        if produto['nome'] == produto_exclusao:
            lista.remove(produto)
            print(f'O produto {produto_exclusao} foi excluído da lista')
            break
    else:
        print(f'O produto {produto_exclusao} não consta na lista')

while True:
    limpa_tela()
    menu()
    opcao = input('\nEscolha a opção desejada: ' )

    if opcao == '1':
        cadastrar_produto(cadastro_produtos)
        volta_menu()
    elif opcao == '2':
        listar_produtos(cadastro_produtos)
        volta_menu()
    elif opcao == '3':
        consultar_produto(cadastro_produtos)
        volta_menu()
    elif opcao == '4':
        alterar_preco(cadastro_produtos)
        volta_menu()
    elif opcao == '5':
        excluir_produto(cadastro_produtos)
        volta_menu()
    elif opcao == '6':
        print('Programa encerrado!')    
        break
    else:
        print('Opção invalida')
        volta_menu()


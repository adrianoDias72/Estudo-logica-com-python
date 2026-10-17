import os

# Variável que cria o cadastro de alunos.
cadastro_alunos = []

# Função que limpa a tela ao executar o Menu.
def limpa_tela():
    os.system("cls" if os.name == "nt" else "clear")

# Função que pausa a execuração até que se tecle ENTER. Últil para manter as informações na tela.
def pausa():
    input('\nTecle ENTER para continuar')

# Função que cria o Menu principal do programa.
def menu():
    print('=' * 50)
    print('   PROGRAMA PARA CONTROLE DE NOTAS DOS ALUNOS') 
    print('=' * 50)   
    print('1. Cadastrar aluno')
    print('2. Listar alunos')
    print('3. Consultar aluno')
    print('4. Adicionar nota')
    print('5. Calcular média')
    print('0. Sair')
    print('=' * 50)

# Função que cadadastras os alunos na lista, fazendo as verificações de entrada vazia e inválida.
def cadastrar_aluno(lista):
    nome_aluno = input('\nInforme o nome do aluno: ').strip().lower()
    if nome_aluno == '':
        print('\nEntrada vazia')
        pausa()
    else:    
        while True:
            try:
                nota_1 = float(input('Informe a primeira nota: '))
                nota_2 = float(input('Informe a segunda nota: '))
                nota_3 = float(input('Informe a terceira nota: '))
                
            except ValueError:
                print('\nEntrada invalida')
                pausa()
                continue

            if 0 <= nota_1 <= 10 and 0 <= nota_2 <=10 and 0 <= nota_3 <= 10:    
                dados_alunos = {'nome':nome_aluno, 'notas':[nota_1,nota_2,nota_3]}
                lista.append(dados_alunos)
                print('\nAluno cadastrado com sucesso')
                pausa()
                break
            else:
                print('Informe as notas entre 0 e 10')

# Função que lista os alunos, verificando se a lista está vazia.
def listar_alunos(lista):
    if not lista:
        print('\nA lista está vazia')
        pausa()
    else:    
        for aluno in lista:
            print(f'Nome do aluno: {aluno['nome']} | Notas: {aluno['notas']}')
        pausa()    
        
# Função para consultar se um aluno consta na lista.
def consultar_aluno(lista):
    pesquisa_aluno = input('\nInforme um nome de aluno para consulta: ').strip().lower()
    if pesquisa_aluno == '':
        print('Entrada vazia')
        pausa()
    else:
        for aluno in lista:
            if aluno['nome'] == pesquisa_aluno:
                print(f'Nome do aluno: {aluno['nome']} | Notas: {aluno['notas']}')
                pausa()
                break
        else:
            print('Aluno não consta na lista')            
            pausa()

# Função para adicionar uma nota no cadastro do aluno.
def adicionar_nota(lista):
    pesquisa_aluno = input('\nInforme o nome do aluno para acrescentar uma nota: ').strip().lower()
    if pesquisa_aluno == '':
            print('Entrada vazia')
            pausa()
    else:
        for aluno in lista:
            if aluno['nome'] == pesquisa_aluno:
                while True:
                    try:
                        nova_nota = float(input('Informe a nota: '))
                        if 0 <= nova_nota <= 10:
                            aluno['notas'].append(nova_nota)
                            print('\nNota cadastrada com sucesso')
                            pausa()
                            break
                        else:
                            print('Informe uma nota entre 0 e 10')
                    except ValueError:
                        print('Entrada invalida')
                        continue
                break            
        else:
            print('Aluno não encontrado')
            pausa()         

# Função para calcular a média de um aluno informado.
def calcular_media(lista):
    aluno_media = input('\nInforme o nome do aluno para calculo da média: ').strip().lower()
    if aluno_media == '':
        print('Entrada invalida')
        pausa()
    else:
        for aluno in lista:
            if aluno['nome'] == aluno_media:
                if len(aluno['notas']) == 0:
                    print('\nNão é possível calcular a média, a lista está vazia')
                    pausa()
                    break
                else:    
                    media = sum(aluno['notas']) / len(aluno['notas'])    
                    print(f'A media do aluno {aluno_media} é: {media:.2f}')
                    pausa()
                    break
        else: 
            print('O aluno não consta na lista')
            pausa()    

# Laço que mantem a execução do programa executando cada opção escolhida.
while True:
    limpa_tela()
    menu()

    opcao = input('Escolha a opção desejada: ')

    if opcao == '1':
        cadastrar_aluno(cadastro_alunos)
    elif opcao == '2':
        listar_alunos(cadastro_alunos)
    elif opcao == '3':
        consultar_aluno(cadastro_alunos)
    elif opcao == '4':
        adicionar_nota(cadastro_alunos)
    elif opcao == '5':                
        calcular_media(cadastro_alunos)
    elif opcao == '0':
        print('Programa encerrado!')
        break    
    else:
        print('Opção invalida!')
        pausa()


        


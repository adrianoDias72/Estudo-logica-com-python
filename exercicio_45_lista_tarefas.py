import os

lista_tarefas = []

def limpa_tela():
    os.system("cls" if os.name == "nt" else "clear")

def retorna_menu():
    input('\nTecle ENTER para retornar ao menu')

def menu():
    print('=' * 40)
    print('   PROGRAMA PARA CONTROLE DE TAREFAS') 
    print('=' * 40)   
    print('1. Adicionar tarefa')
    print('2. Listar tarefas')
    print('3. Concluir tarefa')
    print('4. Excluir tarefa')
    print('0. Sair')
    print('=' * 40)

def adicionar_tarefa(lista):
    tarefa = input('Descreva a tarefa a realizar: ').strip().lower()
    if tarefa == '':
        print('Tarefa vazia')
        retorna_menu()
    else:    
        dados_tarefa = {'descricao':tarefa, 'concluida': False}
        lista.append(dados_tarefa)
        print('Tarefa incluída com sucesso!')
        retorna_menu()
    
def listar_tarefas(lista):
    if not lista:
        print('A lista está vazia')
        retorna_menu()
    else:    
        for tarefa in lista:
            status = '[x]' if tarefa['concluida'] else '[ ]'
            print(f'{status} {tarefa['descricao']}')
        retorna_menu()

def concluir_tarefa(lista):
    tarefa_concluida = input('Informe a tarefa que foi concluída: ').strip().lower()
    for tarefa in lista:
        if tarefa['descricao'] == tarefa_concluida:
            tarefa['concluida'] = True
            print('Tarefa concluída com sucesso!')
            break 
    else:
        print('Tarefa inexistente')       
    retorna_menu()        
    
def excluir_tarefa(lista):
    tarefa_excluida = input('Informe a tarefa a ser excluída: ').strip().lower()
    for tarefa in lista:
        if tarefa['descricao'] == tarefa_excluida:
            lista.remove(tarefa)
            print('Tarefa excluída')
            break
    else:
        print('Tarefa inexistente')
    retorna_menu()    

while True:
    limpa_tela()
    menu()
    
    opcao = input('\nEscolha uma opção: ')

    if opcao == '1':
        adicionar_tarefa(lista_tarefas)
    elif opcao == '2':
        listar_tarefas(lista_tarefas) 
    elif opcao == '3':
        concluir_tarefa(lista_tarefas)
    elif opcao == '4':
        excluir_tarefa(lista_tarefas)        
    elif opcao == '0':
        print('Programa encerrado')
        break
    else:
        print('Opção invalida')
        retorna_menu()

    

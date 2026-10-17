def menu():
    print('***  𝓒𝓪𝓵𝓬𝓾𝓵𝓪𝓻𝓭𝓸𝓻𝓪 𝓑𝓪𝓼𝓲𝓬𝓪  ***')
    print('1. Somar')
    print('2. Subtrair')
    print('3. Multiplicar')
    print('4. Dividir')
    print('5. Sair')

def solicita_numeros():
    numero1 = float(input('Digite o primero número: '))
    numero2 = float(input('Digite o segundo número: '))
    return numero1, numero2
    
def somar():
    numero1, numero2 = solicita_numeros()
    resultado = numero1 + numero2
    return resultado

def subtracao():
    numero1, numero2 = solicita_numeros()
    resultado = numero1 - numero2
    return resultado

def multiplicacao():
     numero1, numero2 = solicita_numeros()
     resultado = numero1 * numero2
     return resultado

def divisao():
    numero1, numero2 = solicita_numeros()
    if numero2 == 0:
        return('Não é possivel fazer divisão por zero')
    else:
        resultado = numero1 / numero2
        return resultado
               
while True:
    menu()
    
    opcao = input('Seleciona a operação: ')

    if opcao == '1':
        resultado = somar()
        print(resultado)
    elif opcao == '2':
        resultado = subtracao()
        print(resultado)
    elif opcao == '3':
        resultado = multiplicacao()
        print(resultado) 
    elif opcao == '4':
        resultado = divisao()
        print(resultado)
    elif opcao == '5':
        print('Calculadora encerrada')
        break
    else:
        print('Opção invalida')        
    
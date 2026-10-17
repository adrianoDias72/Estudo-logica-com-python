import os

def limpa_tela():
    input('Tecle ENTER para nova conversão')
    os.system("cls" if os.name == "nt" else "clear")

def menu():
    print('***   CONVERSOR DE TEMPERATURA   ***')
    print('1. Celsius → Fahrenheit')
    print('2. Fahrenheit → Celsius')
    print('3. Celsius → Kelvin')
    print('4. Kelvin → Celsius')
    print('5. Sair')

def solicita_temperatura():
    temperatura = float(input('Informe a temperatura para conversão: '))
    return temperatura

def celsius_fahrenheit():
    celsius = solicita_temperatura()
    conversao = (celsius * (9/5)) + 32
    return conversao

def fahrenheit_celsius():
    fahrenheit = solicita_temperatura()
    conversao = (fahrenheit - 32) * (5 / 9)
    return conversao

def celsius_kelvin():
    celsius = solicita_temperatura()
    conversao = celsius + 273.15
    return conversao

def kelvin_celsius():
    kelvin = solicita_temperatura()
    conversao = kelvin - 273.15
    return conversao

while True:
    
    menu()

    opcao = input('Selecione a conversão que deseja: ')

    if opcao == '1':
        resultado = celsius_fahrenheit()
        print(resultado)
        limpa_tela()
    elif opcao == '2':
        resultado = fahrenheit_celsius()
        print(resultado)
        limpa_tela()
    elif opcao == '3':
        resultado = celsius_kelvin()
        print(resultado)
        limpa_tela()
    elif opcao == '4':
        resultado = kelvin_celsius()
        print(resultado)
        limpa_tela()
    elif opcao == '5':
        print('Aplicação encerrada')
        break   
    else:
        print('Opção invalida')                
        limpa_tela()
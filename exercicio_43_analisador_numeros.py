lista_numeros = []
quantidade_numeros = int(input('Informe a quantidade de número da lista: '))
while quantidade_numeros <= 0:
    quantidade_numeros = int(input('A lista não pode estar vazia, informe a quantidade de númeos:'))


for i in range(0, quantidade_numeros):
    numero = int(input(f'Informe o numero {i+1}: '))
    lista_numeros.append(numero)

def maior_numero(lista):
    maior_numero = lista[0]
    for i in lista:
        if i > maior_numero:
            maior_numero = i
    return maior_numero    

def menor_numero(lista):
    menor_numero = lista[0]
    for i in lista:
        if menor_numero > i:
            menor_numero = i
    return menor_numero    

def somar(lista):
    soma = 0
    for i in lista:
        soma += i
    return soma    

def calculo_media(lista):
    if len(lista) == 0:
        print('Não é possível calcular a media, lista vazia')
    else:    
        media = somar(lista) / len(lista)
        return media

def quantidade_pares_impares(lista):
    pares = 0
    impares = 0
    for i in lista:
        if i % 2 == 0:
            pares += 1
        else:
            impares += 1    
    return pares, impares        

maior = maior_numero(lista_numeros)
menor = menor_numero(lista_numeros)
soma = somar(lista_numeros)
media = calculo_media(lista_numeros)
par, impar = quantidade_pares_impares(lista_numeros)

print(f'Analisando a sua lista podemos dizer que o maior numero é o {maior}, o menor é o {menor}, a soma dos numeros é {soma}, a media é {media} e existem {par} números pares é {impar} números impares')

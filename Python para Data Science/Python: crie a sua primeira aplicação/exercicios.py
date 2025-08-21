import os

def exercicio_1():
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        print('O número é par')
    else:
        print('O número é ímpar')

def exercicio_2():
    idade = int(input('Digite sua idade: '))
    if idade >= 0 and idade <= 12:
        print('Você é uma criança')
    elif idade >= 13 and idade <= 18:
        print('Você é um adolescente')
    elif idade > 18:
        print('Você é um adulto')
    else:
        print('Idade inválida')

def exercicio_3():
    nome_usuario = input('Digite seu nome de usuário: ')
    senha = input('Digite sua senha: ')
    if nome_usuario == 'admin' and senha == '123456':
        print('Acesso permitido')
    else:
        print('Acesso negado')

def exercicio_4():
    x = int(input('Digite o valor de x: '))
    y = int(input('Digite o valor de y: '))
    if x > 0 and y > 0:
        print('O ponto está no primeiro quadrante')
    elif x < 0 and y > 0:
        print('O ponto está no segundo quadrante')
    elif x < 0 and y < 0:
        print('O ponto está no terceiro quadrante')
    elif x > 0 and y < 0:
        print('O ponto está no quarto quadrante')
    else:
        print('O ponto está localizado no eixo ou origem')

def exercicio_5():
    projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]
    for projeto in projetos:
        if projeto:
            print(f"Projeto: {projeto}")
        else:
            print("Projeto não disponível.")

def exercicio_extra_1():
    nome = input('Digite seu nome: ')
    idade = input('Digite sua idade: ')
    print(f'Meu nome é {nome} e tenho {idade} anos.')

def exercicio_extra_2():
    print('A\nL\nU\nR\nA')

def exercicio_extra_3():
    pi = 3.14159
    pi_arredondado = round(pi, 2)
    print(f'O valor arredondado de pi é: {pi_arredondado}')




lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''
2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.
'''
def exercicio_extra_4():
    for numero in lista_numeros:
        print(numero)


'''
3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
'''
def exercicio_extra_5():

    soma_impares = 0

    for numero in lista_numeros:
        if numero % 2 != 0:
            soma_impares += numero

    print(f'A soma dos números ímpares de 1 a 10 é: {soma_impares}')



'''
4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
'''
#Começa em 10, termina em 0, vai de -1 em -1
for numero in range (10, 0, -1):
    print(numero)


'''
5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.
'''

numero = int(input('Digite um número: '))

for i in range(1, 11):
    print(f'{numero} x {i} = {numero * i}')

'''
6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.
'''

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

soma_numeros = 0

for numero in lista_numeros:
    try:
        soma_numeros += numero
    except:
        print('Erro ao somar os números')

print(f'A soma de todos os números da lista é: {soma_numeros}')

'''
7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.
'''

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

try:
    media_numeros = sum(lista_numeros) / len(lista_numeros)
except ZeroDivisionError:
    print('Erro ao calcular a média')

print(f'A média dos números da lista é: {media_numeros}')


'''
1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.

2 - Utilizando o dicionário criado no item 1:

Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
Adicione um campo de profissão para essa pessoa;
Remova um item do dicionário.
3 - Crie um dicionário que relacione os números de 1 a 5 aos seus respectivos quadrados.

4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.

5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.
'''


# exercicio_1()
# exercicio_2()
# exercicio_3()
# exercicio_4()
# exercicio_5()

# Extras:
# exercicio_extra_1()
# exercicio_extra_2()
# exercicio_extra_3()

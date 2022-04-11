import numpy as np

# 01. Ler dois números inteiros, executar e mostrar o resultado das seguintes operações: adição, subtração, multiplicação e divisão.
def ex1():
    numero1 = int(input('Digite o primeiro número: '))
    numero2 = int(input('Digite o segundo número: '))

    adicao = numero1 + numero2
    subtracao = numero1 - numero2
    multiplicacao = numero1 * numero2
    divisao = numero1 / numero2

    print(f'Adição: {adicao}')
    print(f'Subtração: {subtracao}')
    print(f'Multiplicação: {multiplicacao}')
    print(f'Divisão: {round(divisao, 2)}')


# 02. Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem, utilizando um automóvel que faz 12 Km por litro. Para obter o cálculo, o usuário deve fornecer o tempo gasto na viagem e a velocidade média durante ela. Desta forma, será possível obter a distância percorrida com a fórmula DISTANCIA = TEMPO * VELOCIDADE. Tendo o valor da distância, basta calcular a quantidade de litros de combustível utilizada na viagem, com a fórmula: LITROS_USADOS = DISTANCIA / 12. O programa deve apresentar os valores da velocidade média, tempo gasto na viagem, a distância percorrida e a quantidade de litros utilizada na viagem.
def ex2():
    tempo = float(input('Digite o tempo gasto na viagem: '))
    velocidade = float(input('Digite a velocidade média: '))

    distancia = tempo * velocidade
    litros_usados = distancia / 12

    print(f'Velocidade média: {velocidade}')
    print(f'Tempo gasto na viagem: {tempo}')
    print(f'Distância percorrida: {distancia}')
    print(f'Quantidade de litros: {round(litros_usados,1)}')


# 03. Leia a idade do usuário e classifique-o em:
#   - Criança – 0 a 12 anos
#   - Adolescente – 13 a 17 anos
#   - Adulto – acima de 18 anos
#   - Se o usuário digitar um número negativo, mostrar a mensagem que a idade é inválida.
def ex3():
    idade = int(input('Digite a idade: '))

    if idade < 0:
        print('idade inválida')
    elif idade <= 12:
        print('criança')
    elif idade <= 17:
        print('adolescente')
    else:
        print('adulto')


# 04. Imprimir a tabuada de um número lido.
def ex4():
    num = int(input('Tabuada do número: '))

    for count in range(1, 11):
        print(f'{num} x {count} = {num * count}')


# 05. (lista) Crie uma estrutura de repetição para fazer a leitura de 5 números inteiros e os armazene dentro de uma lista. Após a leitura, crie outra estrutura de repetição para somar todos os valores digitados.
def ex5():
    lista = []

    for i in range(5):
        valor = int(input('Digite valor: '))
        lista.append(valor)

    soma = 0
    for i in range(len(lista)):
        soma += lista[i]

    print(soma)

    # Convertendo para o formato numpy para ter acesso a varios recursos matemáticos (soma, media, etc)
    print(np.array(lista).sum())


# 06. (dict) Crie um dicionário para armazenar o nome e a nota de 3 alunos, fazendo a leitura dos valores por meio de uma estrutura de repetição. Depois, crie uma nova estrutura de repetição para somar todas as notas e retornar a média
def ex6():
    #contatos = {'teste': '1234-5678'}
    alunos = {}

    for i in range(3):
        nome = input('Digite nome: ')
        nota = float(input('Digite nota: '))
        alunos[nome] = nota

    print(alunos)

    soma = 0
    for nota in alunos.values():
        soma += nota

    print(f'Média = {round(soma/len(alunos),2)}')


# 07. (matriz) Dada a matriz abaixo, construa uma estrutura de repetição para percorrer e somar todos os elementos da matriz
# matriz = np.array([[3, 4, 1],
#                   [3, 1, 5]])
def ex7():
    matriz = np.array([[3, 4, 1], [3, 1, 5]])

    soma = 0
    for i in range(matriz.shape[0]):
        for j in range(matriz.shape[1]):
            soma += matriz[i][j]

    print(f'Soma = {soma}')


if __name__ == '__main__':

    opcoes = {1: ex1, 2: ex2, 3: ex3, 4: ex4, 5: ex5, 6: ex6, 7: ex7}

    while True:
        exemplo = int(input('Digite o exemplo a ser executado: '))
        if exemplo in opcoes:  # Verifica se o valor digitado está no dict opcoes
            opcoes.get(exemplo)(
            )  # A função get() retorna o valor referente a chave, fazendo uma chamada a função.
            break  # Depois de executar a função termina o programa. Se comentada essa linha, fica no loop.
        else:
            print('Valor inválido. Tente novamente!'
                  )  # Caso a opção seja inválida.

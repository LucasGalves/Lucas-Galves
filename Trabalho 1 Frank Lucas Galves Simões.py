""" Trabalho de Lógica Discreta feita pelo aluno Lucas Galves Simões, da turma 2B """

"""O programa que você desenvolverá irá receber como entrada um arquivo de texto (.txt)
contendo vários conjuntos de dados e várias operações. Estas operações e dados estarão representadas
em um arquivo de textos contendo apenas os dados referentes as operações que devem ser realizadas
segundo a seguinte regra fixa: a primeira linha do arquivo de texto de entrada conterá o número de
operações que estão descritas no arquivo, este número de operações será um inteiro; as linhas
seguintes seguirão sempre o mesmo padrão de três linhas: a primeira linha apresenta o código da
operação (U para união, I para interseção, D para diferença e C produto cartesiano), a segunda e
terceira linhas conterão os elementos dos conjuntos separados por virgulas.
    A resposta do seu programa deverá conter a operação realizada, descrita por extenso, os dados 
dos conjuntos identificados, e o resultado da operação. No caso da união a linha de saída deverá conter 
a informação e a formatação mostrada a seguir:    
União: conjunto 1 {3,5,67,7}, conjunto 2 {1,2,3,4}. Resultado: {3,5,67,7,1,2,4}"""


def criando_matriz(txt):
    mat_temp_1 = txt.split('\n')

    mat = []
    for l in range(len(mat_temp_1)):
        mat_temp_2 = mat_temp_1[l].split(', ')

        mat.append(mat_temp_2)

    return mat


def transform(lista):
    txt = "{" + lista[0]

    for i in range(1, len(lista) - 1):
        txt = f"{txt}, " + lista[i]

    txt = f"{txt}, {lista[-1]}" + "}"

    return txt


def uniao(A, B):
    print(f"União: conjunto 1 {transform(A)}, conjunto 2 {transform(B)}.", end="")
    uni = A

    for i in range(len(B)):
        if B[i] in A:
            pass
        else:
            uni.append(B[i])

    print(f" Resultado: {transform(uni)}")


def intersecao(A, B):
    print(f"Interseção: conjunto 1 {transform(A)}, conjunto 2 {transform(B)}.", end="")
    inter = []

    if len(B) > len(A):
        for i in range(len(B)):
            if B[i] in A:
                inter.append(B[i])
    else:
        for i in range(len(A)):
            if A[i] in B:
                inter.append(A[i])

    print(f" Resultado: {transform(inter)}")


def diferenca(A, B):
    print(f"Diferença: conjunto 1 {transform(A)}, conjunto 2 {transform(B)}.", end="")
    dif = []

    for i in range(len(A)):
        if A[i] in B:
            pass
        else:
            dif.append(A[i])

    print(f" Resultado: {transform(dif)}")


def cartesiano(A, B):
    print(f"Plano Cartesiano: conjunto 1 {transform(A)}, conjunto 2 {transform(B)}.", end="")
    plano = []

    for i in range(len(A)):
        for j in range(len(B)):
            data = f"({A[i]},{B[j]})"
            plano.append(data)

    print(f" Resultado: {transform(plano)}")


arquivo = open("Trabalho 3 Frank", "r")  # Aqui escolhe qual arquivo ler
desafio = arquivo.read()
arquivo.close()

mat = criando_matriz(desafio)

operacoes = int(mat[0][0])
i = 1
l = 1
while i != operacoes + 1:
    if mat[l][0] == "U":
        x, y = mat[l+1], mat[l+2]
        uniao(x, y)
        l += 3
        i += 1

    elif mat[l][0] == "I":
        x, y = mat[l+1], mat[l+2]
        intersecao(x, y)
        l += 3
        i += 1

    elif mat[l][0] == "D":
        x, y = mat[l+1], mat[l+2]
        diferenca(x, y)
        l += 3
        i += 1

    elif mat[l][0] == "C":
        x, y = mat[l+1], mat[l+2]
        cartesiano(x, y)
        l += 3
        i += 1

    else:
        print("error 404")
        i += 1
        l += 3

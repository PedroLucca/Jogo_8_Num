import numpy as np
from busca_a import busca_a

def lerTabuleiro():
    estado_inicial = []
    num = open("numeros.txt", "r")
    for line in num:
        linha = []
        elementos = line.split(",")
        for num in elementos:
            num = num.rstrip("\n")
            linha.append(num)
        estado_inicial.append(linha)

    return estado_inicial

#Recebe estado inicial
estado_inicial = lerTabuleiro()

#Algoritmo A*
alg_a = busca_a(np.array(estado_inicial))
alg_a.executar()









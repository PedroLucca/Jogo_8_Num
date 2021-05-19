import numpy as np
from busca_prof import profundidade
from busca_l import BF
from guloso import guloso
from busca_a import busca_a


print("--- JOGO DOS 8 NUMEROS ---\n")
print("Digite os números que compoem o estado inicial(Digite 0 para representar o estado vazio) :")
initial_state = np.zeros(9)
print("Insira os números: \n")
for i in range(9):
    estado = int(input("Insira o valor " + str(i+1) + ":"))
    initial_state[i] = np.array(estado)
initial_array = np.reshape(initial_state,(3,3))

#Recebe estado inicial
print("\n")
estado_inicial = initial_array
print("Estado inicial:\n")
print(estado_inicial)
print("\n")

#Busca cega por Largura
alg_L = BF(np.array(estado_inicial))
alg_L.executar()

#Busca cega por profundidade
alg_P = profundidade(np.array(estado_inicial))
alg_P.executar()

#Algoritmo A*
alg_A = busca_a(np.array(estado_inicial))
alg_A.executar()

#Algoritmo Guloso
alg_G = guloso(np.array(estado_inicial))
alg_G.executar()










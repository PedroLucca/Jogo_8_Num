import sys
import numpy as np
from node import Node
import time

class profundidade:
    def __init__(self, estado_inicial):
        self.tabuleiro  = estado_inicial
        self.objetivo = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
        self.n = 3
        self.g = 0
        #Expressao f = h

    def calcular_h(self, node):
        h = 0
        for i in range(0, self.n):
            for j in range(0, self.n):
                if node[i][j] != 0:
                      if node[i][j] != self.objetivo[i][j]:
                        h += 1
        return h

    def verificar_visitado(self, node):
        for v in self.visitados:
            if np.array_equal(v.data, node):
                return False

        return True

    def calcular_dados(self):
        prof_max = 0
        for node in self.visitados:
            if node.level > prof_max:
                prof_max = node.level
        return prof_max

    def executar(self):
        self.pilha = []
        self.visitados = []
        self.num_nos = 1

        resultado = open("resultado_profundidade.txt", "w")
        resultado.write("Algoritmo Busca por profundidade:\n")
        inicio = time.time()
        escrever = open("resultado_profundidade.txt", "r")
        print("Realizando busca profundidade...")
        self.pilha.append(Node(self.tabuleiro, 0, 0))
        while True:
            cur = self.pilha[0]
            #print(cur)
            conteudo = escrever.readlines()
            #conteudo.append("N = " + str(self.g) + "\n")
            conteudo.append(str(cur.data))
            if self.calcular_h(cur.data) == 0:
                self.visitados.append(cur)
                fim = time.time()
                prof_max = self.calcular_dados()
                conteudo.append("\n")
                conteudo.append("\n")
                conteudo.append("Custo de tempo: " + str(self.g))
                conteudo.append("\n")
                conteudo.append("Numero de tabuleiros criados: " + str(self.num_nos))
                conteudo.append("\n")
                conteudo.append("Profundidade maxima: " + str(prof_max))
                conteudo.append("\n")
                conteudo.append("Profundidade solucao: " + str(cur.level))
                resultado.writelines(conteudo)
                resultado.close()
                escrever.close()
                print("Resultado profundidade no arquivo: resultado_profundidade!")
                break
            
            #print(cur)
            nodes = cur.gerar_nodes()
            self.nos = []
            for node in nodes:
                if self.verificar_visitado(node.data):
                    self.num_nos += 1
                    self.nos.append(node)
            
            #print(self.pilha)
            #print("\n")
            conteudo.append("\n")
            conteudo.append("    |")
            conteudo.append("\n")
            conteudo.append("    |")
            conteudo.append("\n")
            conteudo.append("    V")
            conteudo.append("\n")
            resultado.writelines(conteudo)
            
            self.visitados.append(self.pilha[0])
            del self.pilha[0]

            self.pilha = self.pilha + self.nos
            #print(self.pilha)
            self.g += 1
            
            #time.sleep(3)
            






    

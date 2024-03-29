import sys
from node import Node
import numpy as np
import time

class busca_a:
    def __init__(self, estado_inicial):
        self.open = []
        self.closed = []
        self.objetivo = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
        self.tabuleiro  = estado_inicial
        self.n = 3
        #Expressao f = g + h


    def calcular_h(self, node):
        h = 0
        for i in range(0, self.n):
            for j in range(0, self.n):
                if node[i][j] != 0:
                      if node[i][j] != self.objetivo[i][j]:
                        h += 1
        return h

    def funcao(self, node):
        f = self.calcular_h(node.data) + node.level
        return f

    def calcular_dados(self):
        prof_max = 0
        for node in self.closed:
            if node.level > prof_max:
                prof_max = node.level
        return prof_max



    def executar(self):
        self.g = 0
        self.num_nos = 1
        resultado = open("resultado_a.txt", "w")
        resultado.write("Algoritmo A*:\n")
        inicio = time.time()
        
        escrever = open("resultado_a.txt", "r")
        inicial = Node(self.tabuleiro, 0, 0)
        inicial.fval = self.funcao(inicial)
        print("Realizando busca A*...")
        self.open.append(inicial)
        while True:
            cur = self.open[0]
            conteudo = escrever.readlines()
            #conteudo.append("F = " + str(cur.level) + "\n")
            conteudo.append(str(cur.data))
            #print(cur.data)
            #print(self.tabuleiro)
            #print("\n")
            if self.calcular_h(cur.data) == 0:
                fim = time.time()
                self.closed.append(cur)
                num_nos = self.num_nos
                prof_max = self.calcular_dados()
                conteudo.append("\n")
                conteudo.append("\n")
                #print(cur.data)
                conteudo.append("Custo de tempo: " + str(self.g))
                conteudo.append("\n")
                conteudo.append("Numero de tabuleiros criados: " + str(num_nos))
                conteudo.append("\n")
                conteudo.append("Profundidade maxima: " + str(prof_max))
                conteudo.append("\n")
                conteudo.append("Profundidade solucao: " + str(cur.level))
                resultado.writelines(conteudo)
                resultado.close()
                escrever.close()
                print("Resultado A* no arquivo: resultado_a!")
                break
            
            for node in cur.gerar_nodes():
                self.num_nos += 1
                node.fval = self.funcao(node)
                self.open.append(node)
            self.closed.append(cur)
            del self.open[0]

            conteudo.append("\n")
            conteudo.append("    |")
            conteudo.append("\n")
            conteudo.append("    |")
            conteudo.append("\n")
            conteudo.append("    V")
            conteudo.append("\n")
            resultado.writelines(conteudo)

            self.open.sort(key = lambda x:x.fval,reverse=False)

            self.g += 1
            #time.sleep(3)
            






    

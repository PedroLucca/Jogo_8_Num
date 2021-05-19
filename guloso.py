import sys
import numpy as np
import time

class guloso:
    def __init__(self, estado_inicial):
        self.tabuleiro  = estado_inicial
        self.objetivo = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
        self.n = 3
        self.g = 0
        #Expressao f = h

    def buscar_vazio(self):
        for i in range(0, self.n):
            for j in range(0, self.n):
                if self.tabuleiro[i][j] == 0:
                    return i, j

    def calcular_h(self, node):
        h = 0
        for i in range(0, self.n):
            for j in range(0, self.n):
                if node[i][j] != 0:
                      if node[i][j] != self.objetivo[i][j]:
                        h += 1
        return h

    def funcao(self, node):
        f = self.calcular_h(node)
        return f

    def mover_vazio(self, node , x_vazio, y_vazio, x_obj, y_obj):
        if x_obj >= 0 and x_obj < self.n and y_obj >= 0 and y_obj < self.n:
            tab_movido = []
            tab_movido = np.copy(node)
            mov = tab_movido[x_obj][y_obj]
            tab_movido[x_obj][y_obj] = tab_movido[x_vazio][y_vazio]
            tab_movido[x_vazio][y_vazio] = mov
            return np.array(tab_movido)
        else:
            return None

    def gerar_nodes(self):
        x_vazio , y_vazio = self.buscar_vazio()
        nodes = []
        movimentos = [[x_vazio,y_vazio-1],[x_vazio,y_vazio+1],[x_vazio-1,y_vazio],[x_vazio+1,y_vazio]]
        for mov in movimentos:
            node = self.mover_vazio(self.tabuleiro, x_vazio, y_vazio, mov[0], mov[1])
            if node is not None:
                nodes.append(node)
        return nodes

    def executar(self):
        self.num_nos = 1
        resultado = open("resultado_guloso.txt", "w")
        resultado.write("Algoritmo Guloso:\n")
        inicio = time.time()
        f = self.funcao(self.tabuleiro)
        escrever = open("resultado_guloso.txt", "r")
        print("Realizando busca gulosa...")
        while True:
            conteudo = escrever.readlines()
            #conteudo.append("G = " + str(self.g) + "\n")
            conteudo.append(str(self.tabuleiro))
            if self.calcular_h(self.tabuleiro) == 0:
                fim = time.time()
                conteudo.append("\n")
                conteudo.append("\n")
                conteudo.append("TCusto de tempo: " + str(self.g))
                conteudo.append("\n")
                conteudo.append("Numero de tabuleiros criados: " + str(self.num_nos))
                conteudo.append("\n")
                conteudo.append("Profundidade maxima/solucao: " + str(self.g))
                resultado.writelines(conteudo)
                resultado.close()
                escrever.close()
                print("Resultado guloso no arquivo: resultado_guloso!")
                break
            nodes = self.gerar_nodes()
            node_index = 0
            i = 0
            f_node = float('inf')
            for node in nodes:
                self.num_nos += 1
                valor = self.funcao(node)
                if valor <= f_node:
                    f_node = valor
                    node_index = i
                i = i + 1
            self.tabuleiro = np.array(nodes[node_index])
            self.g += 1
            conteudo.append("\n")
            conteudo.append("    |")
            conteudo.append("\n")
            conteudo.append("    |")
            conteudo.append("\n")
            conteudo.append("    V")
            conteudo.append("\n")
            resultado.writelines(conteudo)
            #time.sleep(3)
            






    

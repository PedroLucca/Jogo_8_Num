import time
import numpy as np
import copy

class Node:
    def __init__(self, nums, level):
        self.data = nums
        self.level = level
        


class BF:
    def __init__(self, estado_inicial):
        self.initial_array = estado_inicial

        self.goal_node = np.array([[1,2,3],[4,5,6],[7,8,0]])
        self.start_time=time.time()
        self.visited_nodes=[]
        self.visited_nodes.append(self.initial_array)
        self.child_node_number=1
        self.temp_index = []
        self.open = []
        self.movements = 0
        self.nodes = 0
        self.treeDeep = 0
        self.solDeep = 0
        self.nextLevel = 0
        

    

    def find_index(self, puzzle):
        for i in range(3):
            for j in range(3):
                if puzzle[i][j] == 0:
                    return i,j

    def move_left(self, data):
        temp_arr = copy.deepcopy(data)
        i, j = self.find_index(temp_arr)
        if j != 0:
            temp = temp_arr[i, j - 1]
            temp_arr[i, j] = temp
            temp_arr[i, j - 1] = 0
          
            return temp_arr
        else:
            return temp_arr

    def move_right(self, data):
        temp_arr = copy.deepcopy(data)
        i, j = self.find_index(data)
        if j != 2:
            temp = temp_arr[i, j + 1]
            temp_arr[i, j] = temp
            temp_arr[i, j + 1] = 0
           
            return temp_arr
        else:
            return temp_arr

    def move_up(self, data):
        temp_arr = copy.deepcopy(data)
        i, j = self.find_index(data)
        if i != 0:
            temp_arr = np.copy(data)
            temp = temp_arr[i - 1, j]
            temp_arr[i, j] = temp
            temp_arr[i - 1, j] = 0
            
            return temp_arr
        else:
            return temp_arr

    def move_down(self, data):
        temp_arr = copy.deepcopy(data)
        i, j = self.find_index(data)
        if i != 2:
            temp_arr = np.copy(data)
            temp = temp_arr[i + 1, j]
            temp_arr[i, j] = temp
            temp_arr[i + 1, j] = 0
           
            return temp_arr            
        else:
           
            return temp_arr

    def sol(self, ip_node):
        ip_node = self.initial_array
        z = []
        inv = 0
        for i in range(3):
            for j in range(3):
                if (ip_node[i][j]!=0):
                    z.append(ip_node[i][j])            
        for i in range(7):
            j=i+1
            while(j<8):
                if z[i]>z[j]:
                    inv += 1
                j += 1
        if inv % 2:
            
            return 0
        else:
            return 1
    
    def check_and_append(self, p_node, new_node, count):
        stat=False
        q = 1
        
        
        for l in p_node:
            if (l == new_node).all():  
                q = 0
        
        if q == 1:
            self.visited_nodes.append(new_node)
            self.nodes +=1
            stat=True
        return count, stat
    
    def goal_check(self, B):
        status = np.array_equal(B,self.goal_node)
        return status

    def calcular_dados(self):
        prof_max = 0
        for node in self.closed:
            if node.level > prof_max:
                prof_max = node.level
        return prof_max


    def calcular_h(self):
        h = 0
        for i in self.open:
            if i.level > h:
                h = i.level
        return h

    def executar(self):
        inicial = Node(self.initial_array, 0)
        self.open.append(inicial)
        resultado = open("resultado_bf.txt", "w")
        resultado.write("Algoritmo Largura:\n")
        escrever = open("resultado_bf.txt", "r")
        i=0
        
        if (self.sol(self)):

            while (i < self.child_node_number):
                cur = self.open[0]#saber se é isso mesmo
                

                node_list = self.visited_nodes[i]

                for j in self.open:
                    if np.array_equal(j.data, node_list):
                        
                        self.nextLevel = j.level + 1
                

                new_node = self.move_left(node_list)
                
                self.movements += 1

                self.child_node_number, status = self.check_and_append(self.visited_nodes, new_node, self.child_node_number)
                

                if status == True:
                    conteudo = escrever.readlines()
                
                    conteudo.append(str(new_node))
                    conteudo.append("\n")
                    conteudo.append("    |")
                    conteudo.append("\n")
                    conteudo.append("    |")
                    conteudo.append("\n")
                    conteudo.append("    V")
                    conteudo.append("\n")
                    resultado.writelines(conteudo)
                    novoNode = Node(new_node, self.nextLevel)
                    self.open.append(novoNode)
                    
                    self.child_node_number += 1
                    self.temp_index.append(self.child_node_number)
                    

                if self.goal_check(new_node):
                    level = novoNode.level
                    found = True
                    break

                new_node = self.move_up(node_list)
                self.movements += 1

                
                self.child_node_number, status=self.check_and_append(self.visited_nodes, new_node, self.child_node_number)
                
                if status == True:
                    conteudo = escrever.readlines()
            
                    conteudo.append(str(new_node))
                    conteudo.append("\n")
                    conteudo.append("    |")
                    conteudo.append("\n")
                    conteudo.append("    |")
                    conteudo.append("\n")
                    conteudo.append("    V")
                    conteudo.append("\n")
                    resultado.writelines(conteudo)
                    novoNode = Node(new_node, self.nextLevel)
                    self.open.append(novoNode)

                    self.child_node_number += 1
                    self.temp_index.append(self.child_node_number)
                    

                if self.goal_check(new_node):
                    level = novoNode.level
                    found = True       
                    break

                new_node = self.move_right(node_list)
                self.movements += 1

                
                
                self.child_node_number, status = self.check_and_append(self.visited_nodes, new_node, self.child_node_number)
                
                if status == True: 
                    conteudo = escrever.readlines()
                
                    conteudo.append(str(new_node))
                    conteudo.append("\n")
                    conteudo.append("    |")
                    conteudo.append("\n")
                    conteudo.append("    |")
                    conteudo.append("\n")
                    conteudo.append("    V")
                    conteudo.append("\n")
                    resultado.writelines(conteudo)
                    novoNode = Node(new_node, self.nextLevel)
                    self.open.append(novoNode)
                    
                    self.child_node_number += 1
                    self.temp_index.append(self.child_node_number)
                    

                if self.goal_check(new_node):
                    level = novoNode.level
                    found = True
                    break

                new_node = self.move_down(node_list)
                self.movements += 1

                
                
                self.child_node_number, status=self.check_and_append(self.visited_nodes, new_node, self.child_node_number)
                
                if status == True:
                    conteudo = escrever.readlines()
                
                    conteudo.append(str(new_node))
                    conteudo.append("\n")
                    conteudo.append("    |")
                    conteudo.append("\n")
                    conteudo.append("    |")
                    conteudo.append("\n")
                    conteudo.append("    V")
                    conteudo.append("\n")
                    resultado.writelines(conteudo)
                    novoNode = Node(new_node, self.nextLevel)
                    self.open.append(novoNode)
                    
                    self.child_node_number += 1
                    self.temp_index.append(self.child_node_number)
                    

                if self.goal_check(new_node):
                    level = novoNode.level
                    found = True
                    break

                i += 1
        
        conteudo.append("\n")
        conteudo.append("\n")
        conteudo.append("Custo do tempo: " + str(self.nodes))
        conteudo.append("\nNumero de tauleiros Criados " + str(len(self.open)))
        conteudo.append("\nProfundidade do no encontrado: " + str(level))
        conteudo.append("\nProfundidade total: " + str(self.calcular_h()))
        conteudo.append("\n")
        
        resultado.writelines(conteudo)
        resultado.close()
        escrever.close()
        
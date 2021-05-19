import numpy as np

class Node:
    def __init__(self, nums, level, valor_f):
        self.data = nums
        self.level = level
        self.fval = valor_f
        self.n = 3
    
    def buscar_vazio(self):
        for i in range(0, self.n):
            for j in range(0, self.n):
                if self.data[i][j] == 0:
                    return i, j

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
            node = self.mover_vazio(self.data, x_vazio, y_vazio, mov[0], mov[1])
            if node is not None:
                child_node = Node(node, self.level + 1, 0)
                nodes.append(child_node)
        return nodes
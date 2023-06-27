#def BFS(self, graph, v_ini):
#            self.lista = [v_ini]
#            self.distance = []
#            self.anterior = []
#            self.color = []
#            temp = 0
#            for i in range(len(self.list_vertices)):
#                self.color.append("B")
#                self.distance.append(0)
#                self.anterior.append(None)
#            print(self.color)
#            print(self.distance)
#            print(self.anterior)
#            for j in range(len(self.list_vertices)):
#                for k in range(len(self.list_vertices) - 1):
#                    print(graph.list_vertices[j] , graph.list_vertices[k])
#                    try:
#                        self.list_arestas.index((graph.list_vertices[j] , graph.list_vertices[k]))
#                        if  self.lista[j] != self.list_vertices[k] and self.list_vertices[k] != "C":
#                            if self.lista.count(self.list_vertices[k]) != True:
#                                self.lista.append(self.list_vertices[k])
#                            self.color[j] = "C"
#                            print("Vertice 2:" , self.list_vertices[k])
#                            print("Vertice 1:",self.list_vertices[j])
#                            if self.anterior[k] == None and k >= 1:
#                                print("AQUI")
#                                self.anterior[k] = self.list_vertices[j]
#                                self.distance[k] = self.distance[j] + 1
#                    except ValueError:
#                        print("Nao")
#                self.color[j] = "P"
#            print("lista:",self.lista)
#            print("Cor:",self.color)
#            print("Anterior",self.anterior)
#            print("Distancia",self.distance)


def bfs(grafo, entra, sai, parent):
    visited = [False] * len(grafo)
    fila = []
    fila.append(entra)
    visited[entra] = True
    while fila:
        u = fila.pop(0)
        print(u)
        print(fila)
        for v, capacidade in enumerate(grafo[u]):
            if not visited[v] and capacidade > 0:
                #print(visited[v])
                #print(parent[v])
                fila.append(v)
                visited[v] = True
                parent[v] = u
    return visited[sai]

def ff(grafo, entra, sai):
    parent = [-1] * len(grafo)
    fluxo_maximo = 0
    while bfs(grafo, entra, sai, parent):
        fluxo_caminho = float('inf')
        v = sai
        #print(fluxocanminho)
        while v != entra:
            u = parent[v]
            fluxo_caminho = min(fluxo_caminho, grafo[u][v])
            v = u
        fluxo_maximo += fluxo_caminho
        v = sai
        while v != entra:
            print(parent[v])
            u = parent[v]
            grafo[u][v] -= fluxo_caminho
            grafo[v][u] += fluxo_caminho
            v = u
    return fluxo_maximo

grafo = [[0, 14, 13, 0, 0, 0],[0, 0, 12, 17, 0, 0],
        [0, 4, 0, 0, 14, 0],[0, 0, 9, 0, 0, 6],
        [0, 5, 0, 7, 0, 4],[0, 19, 0, 0, 7, 0]]
entra = 0
sai = 5 
fluxo_maximo = ff(grafo, entra, sai)
print("fluxo máximo:", fluxo_maximo)

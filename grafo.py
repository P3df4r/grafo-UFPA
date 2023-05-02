class grafo: 
    def __init__ (self):
        self.list_vertices = []
        self.list_arestas = []

    def new_vertice(self, a1):
        count = 0
        for i in range(len(self.list_vertices)):
            if a1 == self.list_vertices[i]:
                count += 1
        if count == 1:
            print("O vértice {vertice} já existe".format(vertice=a1))
        else:
            self.list_vertices.append(a1)
            print("Vertice adicionado")

    def new_aresta(self, a1, a2):
        count = 0
        for i in range(len(self.list_vertices)):
            if a1 == self.list_vertices[i]:
                count += 1
        for i in range(len(self.list_vertices)):
            if a2 == self.list_vertices[i]:
                count +=1
        if count == 2:
            self.list_arestas.append((a1, a2))

    def print_vertice_completo(self):
        return print(self.list_vertices)

    def print_arestas_completo(self):
        return print(self.list_arestas)

    def print_vertice(self):
        return print(len(self.list_vertices))

    def print_arestas(self):
        return print(len(self.list_arestas))

    def view_matriz_direcionada(self):
        line = ""
        count = 0
        for i in range(len(self.list_vertices)):
            for j in range(len(self.list_vertices)):
                try:
                    self.list_arestas.index((self.list_vertices[i], self.list_vertices[j]))
                    line += '1\t'
                except ValueError:
                    line += '0\t'
            print(line)
            line = ''

    def view_matriz(self):
        line = ""
        count = 0
        for i in range(len(self.list_vertices)):
            for j in range(len(self.list_vertices)):
                try:
                    self.list_arestas.index((self.list_vertices[i], self.list_vertices[j])) or self.list_arestas.index((self.list_vertices[i], self.list_vertices[j]))
                    line += '1\t'
                except ValueError:
                    line += '0\t'
            print(line)
            line = ''


if __name__ == "__main__":
    #entradas de teste
    graph = grafo()
    graph.new_vertice(1)
    graph.new_vertice(2)
    graph.new_vertice(3)
    graph.new_aresta(1, 2)
    graph.new_aresta(1, 3)
    graph.new_aresta(3, 1)
    graph.new_aresta(3, 3)
    graph.print_vertice()
    graph.print_arestas()
    graph.view_matriz()

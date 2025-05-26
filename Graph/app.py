class Graph:
    def __init__(self):
        self.adj_list = {}
    
    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex] )

    def add_vertex(self, v1):
        if v1 not in self.adj_list:
            self.adj_list[v1] = []
            return True
        return False


graph = Graph()
graph.add_vertex('A')
graph.print_graph()
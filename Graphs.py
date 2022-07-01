# Graphs:

class graph:
    
    def __init__(self):
        self.adj_list={}
    
    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])
    
    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex]=[]
            return True
        return False

    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False        

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                return True
        return False

    def remove_vertex(self, v):
        if v in self.adj_list.keys():
            for x in self.adj_list[v]:
                self.adj_list[x].remove(v)
            del self.adj_list[v]
            return True
        return False

graph1=graph()

graph1.add_vertex('A')
graph1.add_vertex('B')
graph1.add_vertex('C')

graph1.add_edge('A','B')
graph1.add_edge('B','C')
graph1.add_edge('C','A')

graph1.remove_edge('B','C')
graph1.remove_edge('C','B')

graph1.remove_vertex('C')

graph1.print_graph()
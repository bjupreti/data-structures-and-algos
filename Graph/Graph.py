class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print("Graph_dict", self.graph_dict)
        
    def find_all_paths(self, start, end):
        pass
        
    def find_shortest_path(self, start, end):
        pass
    

if __name__ == "__main__":
    routes = [
        ("Kathmandu", "Paris"),
        ("Kathmandu", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto")
    ]
    
    route_graph = Graph(routes)
    
    ktm_ktm_route = route_graph.find_all_paths("Kathmandu", "Kathmandu")
    toronto_ktm_route = route_graph.find_all_paths("Toronto", "Kathmandu")
    print(f"Paths between {'Kathmandu'} and {'Kathmandu'}:", ktm_ktm_route)
    print(f"Paths between {'Toronto'} and {'Kathmandu'}:", toronto_ktm_route)
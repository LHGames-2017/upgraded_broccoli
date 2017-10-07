import networkx as nx

class Search():
    def __init__(self, graph, player):
        self.graph = graph
        self.player = player
        self.interest_points = dict()

    # Return all nodes from start to end
    def astar(self, start, end):
        return nx.astar_path(self.graph, start, end)
    
    # 
    def breadth_search(self):
        return nx.algorithms.coloring.strategy_connected_sequential(self.graph, "", traversal='bfs')



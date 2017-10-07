import networkx as nx
import structs

class Search():
    def __init__(self, graph, the_map, player):
        self.graph = graph
        self.the_map = the_map
        self.player = player
        # update home ressources quand marche sur maison
        self.home_ressources = player.Score - player.CarriedRessources
        self.total_ressources = self.home_ressources + player.CarriedRessources
        # list of objectives [ (prix, UpgradeType) ]
        self.upgrade_queue = [
                (15000, "structs.UpgradeType.CarryingCapacity")

                ]

    # Return all nodes from start to end
    def astar(self, start, end):
        return nx.astar_path(self.graph, start, end)

    # return shortest path to home
    def go_home(self):
        home = self.player.HouseLocation.to_tuple()
        pos = self.player.Position.to_tuple()
        return self.astar(self.graph, pos, home)

    # action to do every beginning
    def indispendable_checks(self):
        # TODO make sure score keep track money at home TODO
        # Am I home?
        if self.player.Position == self.player.HouseLocation:
            price, upgrade_type = self.upgrade_queue.pop(0)
            if self.total_ressources >= price:
                return [structs.create_action("UpgradeAction", upgrade_type)] #upgrade type marche TODO
            else:
                return self.find_mine()

        # find if capacity is full
        if self.player.CarriedRessources == self.player.CarryingCapacity:
            return self.transform_path(self.go_home(), "MoveAction")
        else:
            return self.find_mine()

        return self.find_mine()
            
    # find best_decision
    def find_best_decision(self):
        self.indispendable_checks()

    # find closets mining ressources
    # TODO garder mine trouvee en memoire et pas toujours rappeler
    def find_mine(self):
        return self.transform_path(self.bfs(structs.TileContent.Resource), "CollectAction")

    # breadth first search
    def bfs(self, tile_type):
        player_pos = self.player.Position.to_tuple()
        top_corner = (self.the_map[0][0].x, self.the_map[0][0].y)
        #print(tuple(x-y for x, y in zip(player_pos, top_corner)))
        bfs_gen = nx.bfs_edges(self.graph, tuple(x-y for x, y in zip(player_pos, top_corner)))
        for node in bfs_gen:
            #print(node[1][1],node[1][0])
            #print( self.the_map[node[1][1]][node[1][0]].content)
            if self.the_map[node[1][1]][node[1][0]].content == tile_type:
                return self.astar( tuple(x-y for x, y in zip(player_pos, top_corner)), node[1])
            # self.graph.remove_node()
                # print(self.astar(self.player.Position.to_tuple, node))
                # print([tuple(x+y for x,y in zip(n, top_corner)) for n in self.astar(self.player.Position.to_tuple, node)])
                # return [tuple(x+y for x,y in zip(n, top_corner)) for n in self.astar(self.player.Position.to_tuple, node)]
    

    # transform a path, to last Point, the rest
    def transform_path(self, path, action, item=""):
        movepath = [structs.Point(i,j) for (i,j) in path]
        print(movepath)
        # gerer le cas si path de 1 point seulement
        actionpath = []
        while len(movepath) > 1:
            actionpath.append(structs.create_action("MoveAction", movepath.pop(0)))
        
        if (action == "PurchaseAction" or action == "UpgradeAction" or action == "HealAction"):
            actionpath.append(structs.create_action(action, item))
        else:
            actionpath.append(structs.create_action(action, movepath.pop(0)))

        return actionpath

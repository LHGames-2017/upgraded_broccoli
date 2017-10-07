import networkx as nx
import structs

class Search():
    def __init__(self, graph, the_map, player):
        self.graph = graph
        self.the_map = the_map
        self.player = player
        # update home ressources quand marche sur maison
        self.home_ressources = 0
        self.total_ressources = 0

        self.home_interests_points = {}
        self.interest_points = {}
        # list of objectives [ (condition, action) ]
        self.upgrade_queue = [
                ("self.total_ressources == 15000", "self.go_upgrade('structs.UpgradeType.CarryingCapacity')"), # update carrying capacity
                ("self.total_ressources == 15000", "self.go_upgrade()")
                    

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
        # ajuster ressources si maison
        if self.player.Position == self.player.HouseLocation:
            self.home_ressources += self.player.CarriedRessources
            self.total_ressources = self.home_ressources

        # find if capacity is full
        if self.player.CarriedRessources == self.player.CarryingCapacity:
            self.go_home()

        # find if ready for upgrade (execute first objective priority list)
        if eval(self.upgrade_queue[0][0]):
            action = self.upgrade_queue[0][1]
            self.upgrade_queue.pop(0)
            eval(action)
    

    # find closets mining ressources
    def find_mine(self):
        a = "player.collect("
        return self.transform_path(self.bfs(structs.TileContent.Resource))

    # go to upgrade
    def go_upgrade(self, upgrade_type):
        action = "player.upgrade(" + upgrade_type
        return self.transform_path(self.go_home(), action)


    # breadth first search
    def bfs(self, tile_type):
        bfs_gen = nx.bfs_edges(self.graph, self.pos)
        for node in bfs_gen:
            if self.the_map[node[1]][node[0]].content == tile_type:
                return self.astar(self.player.Position.to_tuple,node)

    # transform a path, to last Point, the rest
    def transform_path(self, path, action):
        movepath = [structs.Point(i,j) for (i,j) in path]
        movepath, lastpoint = movepath[:-1], movepath[-1]
        lastpoint = lastpoint.to_tuple()
        newaction = action + "Point(" + str(lastpoint[0]) + "," str(lastpoint[1]) + ")"
        # reste a faire des move pour tous les points dans movepath, et on eval newaction
        return (movepath, newaction)



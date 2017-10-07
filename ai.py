from flask import Flask, request
from structs import Player, PlayerInfo, Tile, TileContent, Point
import json
from Queue import Queue
# from search import Search
# import numpy as np
import networkx as nx

app = Flask(__name__)


def print_map(m):
    # for i in range(len(m)):
        # print([(tile.x, tile.y) for tile in m[i]])
    for i in range(len(m)):
        print([tile.content.name[0] for tile in m[i]])

def manhattan_dist(start, end):
    sx, sy = start
    ex, ey = end
    return abs(ex - sx) + abs(ey - sy)


def bfs(m, g, start, gohome):
    frontier = Queue()
    frontier.put(start)
    visited = {}
    visited[start] = True

    while not frontier.empty():
        current = frontier.get()
        for n in g.neighbors(current):
            if n not in visited:
                if gohome and m[n[1]][n[0]].content == TileContent.House:
                    return n
                elif not gohome and m[n[1]][n[0]].content == TileContent.Resource:
                    return n
                frontier.put(n)
                visited[n] = True


def do_something(p, m, g):
    #print(p.__dict__)
    #print_map(m)
    # print(g.nodes())

    player_pos = (p.Position.to_tuple()[0] - m[0][0].x, p.Position.to_tuple()[1] - m[0][0].y)
    dest_pos = bfs(m, g, player_pos, p.CarriedRessources == p.CarryingCapacity)
    next_pos = nx.astar_path(g, player_pos, dest_pos)[1]

    # print(player_pos)
    # print(dest_pos)
    # print(next_pos)
    if next_pos == dest_pos:
        if (p.CarriedRessources < p.CarryingCapacity):
            return p.collect(Point(next_pos[0] + m[0][0].x, next_pos[1] + m[0][0].y))
    return p.move(Point(next_pos[0] + m[0][0].x, next_pos[1] + m[0][0].y))


def create_graph(tiles):
    graph = nx.grid_graph([20, 20])

    for i in range(20):
        for j in range(20):
            if tiles[i][j].content == TileContent.Lava:
                graph.remove_node((j, i))
            elif tiles[i][j].content == TileContent.Wall:
                graph.remove_node((j, i))
            # elif tiles[i][j].content == TileContent.Player:
                # graph.remove_node((j, i))

    return graph


def deserialize_map(serialized_map):
    """
    Fonction utilitaire pour comprendre la map
    """
    serialized_map = serialized_map[1:]
    rows = serialized_map.split('[')
    column = rows[0].split('{')
    deserialized_map = [[Tile() for x in range(20)] for y in range(20)]
    for i in range(len(rows) - 1):
        column = rows[i + 1].split('{')

        for j in range(len(column) - 1):
            infos = column[j + 1].split(',')
            end_index = infos[2].find('}')
            x = int(infos[1])
            y = int(infos[2][:end_index])
            content = int(infos[0])
            deserialized_map[j][i] = Tile(x, y, content)

    return deserialized_map


def bot():
    """
    Main de votre bot.
    """
    map_json = request.form["map"]

    # Player info

    encoded_map = map_json.encode()
    map_json = json.loads(encoded_map.decode('utf-8'))
    p = map_json["Player"]
    pos = p["Position"]
    x = pos["X"]
    y = pos["Y"]
    house = p["HouseLocation"]
    player = Player(p["Health"], p["MaxHealth"], Point(x,y),
                    Point(house["X"], house["Y"]), p["Score"],
                    p["CarriedResources"], p["CarryingCapacity"])

    # print(player.__dict__)
    # print("MY POSITION", player.Position)
    # print(player.__dict__)

    # Map
    serialized_map = map_json["CustomSerializedMap"]
    deserialized_map = deserialize_map(serialized_map)
    graph = create_graph(deserialized_map)

    # print(deserialized_map)
    # print(player.__dict__)
    # print(player.Position)
    # print_map(deserialized_map)
    # print(graph.nodes())

    otherPlayers = []

    for player_dict in map_json["OtherPlayers"]:
        for player_name in player_dict.keys():
            player_info = player_dict[player_name]
            p_pos = player_info["Position"]
            # print("\n\n\n", p_pos)
            player_info = PlayerInfo(player_info["Health"],
                                     player_info["MaxHealth"],
                                     Point(p_pos["X"], p_pos["Y"]))

            otherPlayers.append({player_name: player_info })

    return do_something(player, deserialized_map, graph)
    # s = Search(graph, deserialized_map, player)
    # print(s.find_best_decision())
    ### BOT EXECUTION
    # cherche prochaine action si path est vide
    #    if len(path) == 0 and len(lastaction) == 0:
    #        s = Search(graph, deserialized_map, player)
    #        path, action = s.find_best_decision()

    #        if len(path) == 0:
    #            return eval(lastaction)

    # move to tile adjacent to last action
    #target = path.pop(0)
    #return player.move(target)



@app.route("/", methods=["POST"])
def reponse():
    """
    Point d'entree appelle par le GameServer
    """
    return bot()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
    path = []
    lastaction = []

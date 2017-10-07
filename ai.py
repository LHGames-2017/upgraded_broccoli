from flask import Flask, request
from structs import Player, PlayerInfo, Tile, TileContent, Point
import json
# import Search
# import numpy as np
import networkx as nx

app = Flask(__name__)


def print_map(m):
    # for i in range(len(m)):
        # print([(tile.x, tile.y) for tile in m[i]])
    for i in range(len(m)):
        print([tile.content.name[0] for tile in m[i]])


def create_graph(tiles):
    graph = nx.grid_graph([20, 20])

    for i in range(20):
        for j in range(20):
            if tiles[i][j].content == TileContent.Lava:
                graph.remove_node((j, i))
            elif tiles[i][j].content == TileContent.Wall:
                graph.remove_node((j, i))
            elif tiles[i][j].content == TileContent.Player:
                graph.remove_node((j, i))

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

    print(player.__dict__)
    print("MY POSITION", player.Position)
    # print(player.__dict__)

    # Map
    serialized_map = map_json["CustomSerializedMap"]
    deserialized_map = deserialize_map(serialized_map)
    graph = create_graph(deserialized_map)

    # print(deserialized_map)
    # print(player.__dict__)
    # print(player.Position)
    print_map(deserialized_map)
    # print(graph.nodes())

    otherPlayers = []

    for player_dict in map_json["OtherPlayers"]:
        for player_name in player_dict.keys():
            player_info = player_dict[player_name]
            p_pos = player_info["Position"]
            print("\n\n\n", p_pos)
            player_info = PlayerInfo(player_info["Health"],
                                     player_info["MaxHealth"],
                                     Point(p_pos["X"], p_pos["Y"]))

            otherPlayers.append({player_name: player_info })
    print(pos)

    # return decision
    s = Search(graph, deserialized_map, player)
    return s.find_best_decision()


@app.route("/", methods=["POST"])
def reponse():
    """
    Point d'entree appelle par le GameServer
    """
    return bot()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

import math
import json

class ActionTypes:
    DefaultAction, MoveAction, AttackAction, CollectAction, UpgradeAction, StealAction, PurchaseAction = range(7)


class UpgradeType:
    CarryingCapacity, AttackPower, Defence, MaximumHealth, CollectingSpeed = range(5)


class TileType:
    Tile, Wall, House, Lava, Resource, Shop = range(6)


class TileContent:
    Empty, Resource, House, Player, Wall, Lava, Shop = range(7)


class Point:

    # Constructor
    def __init__(self, X=0, Y=0):
        self.X = X
        self.Y = Y

    # Overloaded operators
    def __add__(self, point):
        return Point(self.X + point.X, self.Y + point.Y)

    def __sub__(self, point):
        return Point(self.X - point.X, self.Y - point.Y)

    def __str__(self):
        return "{{{0}, {1}}}".format(self.X, self.Y)

    # Distance between two Points
    def Distance(self, p1, p2):
        delta_x = p1.X - p2.X
        delta_y = p1.Y - p2.Y
        return math.sqrt(math.pow(delta_x, 2) + math.pow(delta_y, 2))


class GameInfo:

    def __init__(self, json_dict):
        self.__dict__ = json_dict
        self.HouseLocation = Point(json_dict["HouseLocation"])
        self.Map = None
        self.Players = dict()


class Tile:

    def __init__(self, content=None, x=0, y=0):
        self.Content = content
        self.X = x
        self.Y = y


def create_action(action_type, target):
    actionContent = ActionContent(action_type, target.__dict__)
    return json.dumps(actionContent.__dict__)


class Player:

    def __init__(self, health, maxHealth, position, houseLocation, score, carriedRessources,
                 carryingCapacity=1000):
        self.Health = health
        self.MaxHealth = maxHealth
        self.Position = position
        self.HouseLocation = houseLocation
        self.Score = score
        self.CarriedRessources = carriedRessources
        self.CarryingCapacity = carryingCapacity

        def move(target):
            return create_action("MoveAction", target)

        def attack(target):
            return create_action("AttackAction", target)

        def collect(target):
            return create_action("CollectAction", target)

        def steal(target):
            return create_action("StealAction", target)

        def heal():
            return create_action("HealAction", "")

        def purchase(item):
            return create_action("PurchaseAction", item)

class PlayerInfo:

    def __init__(self, health, maxHealth, position):
        self.Health = health
        self.MaxHealth = maxHealth
        self.Position = position

class ActionContent:

    def __init__(self, action_name, content):
        self.ActionName = action_name
        self.Content = {}

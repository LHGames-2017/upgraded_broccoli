from enum import Enum


class TileContent(Enum):
    Empty = 0
    Resource = 1
    House = 2
    Player = 3
    Wall = 4
    Lava = 5
    Shop = 6


class Tile:
    def __init__(self, x=0, y=0, content=4):
        self.x = x
        self.y = y
        self.content = TileContent(content)


import math
import json
test = False

class ActionTypes:
    DefaultAction, MoveAction, AttackAction, CollectAction, UpgradeAction, StealAction, PurchaseAction = range(7)


class UpgradeType:
    CarryingCapacity, AttackPower, Defence, MaximumHealth, CollectingSpeed = range(5)


# class TileType:
    # Tile, Wall, House, Lava, Resource, Shop = range(6)


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
    
    def to_tuple(self):
        return (self.X, self.Y)

    def equals(self, p1):
        return self.X == p1.X and self.Y == p1.Y

    def __str__(self):
        return "{{{0}, {1}}}".format(self.X, self.Y)

    # Distance between two Points
    def Distance(self, p1, p2):
        return abs(p1.X-p2.X) + abs(p1.Y-p2.Y)

class GameInfo:

    def __init__(self, json_dict):
        self.__dict__ = json_dict
        self.HouseLocation = Point(json_dict["HouseLocation"])
        self.Map = None
        self.Players = dict()


# class Tile:
    # def __init__(self, content=None, x=0, y=0):
        # self.Content = content
        # self.X = x
        # self.Y = y


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

    def move(self, target):
        return create_action("MoveAction", target)

    def attack(self, target):
        return create_action("AttackAction", target)

    def collect(self, target):
        return create_action("CollectAction", target)

    def steal(self, target):
        return create_action("StealAction", target)

    def heal(self):
        return create_action("HealAction", "")

    def purchase(self, item):
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

if test:
    point = Point(2,3)
    print(point.to_tuple())
    point2 = Point(2,3)
    point3 = Point(4,5)
    print(point.equals(point2))
    print(point.equals(point3))


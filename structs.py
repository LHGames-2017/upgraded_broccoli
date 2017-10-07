import json
from enum import Enum


class TileContent(Enum):
    Empty = 0
    Wall = 1
    House = 2
    Lava = 3
    Resource = 4
    Shop = 5
    Player = 6


class ActionTypes(Enum):
    DefaultAction = 0
    MoveAction = 1
    AttackAction = 2
    CollectAction = 3
    UpgradeAction = 4
    StealAction = 5
    PurchaseAction = 6
    HealAction = 7


class UpgradeType(Enum):
    CarryingCapacity = 0
    AttackPower = 1
    Defence = 2
    MaximumHealth = 3
    CollectingSpeed = 4


class PurchasableItem(Enum):
    MicrosoftSword = 0
    UbisoftShield = 1
    DevolutionsBackpack = 2
    DevolutionsPickaxe = 3
    HealthPotion = 4


class Tile:

    def __init__(self, x=0, y=0, content=4):
        self.x = x
        self.y = y
        self.content = TileContent(content)


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

    def move(self, diff):
        target = self.Position + diff
        print(self.Position, diff, target, type(target))
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

    def upgrade(self, upgrade_type, item):
        return create_action("UpgradeAction", upgrade_type, item)

class PlayerInfo:

    def __init__(self, health, maxHealth, position):
        self.Health = health
        self.MaxHealth = maxHealth
        self.Position = position

class ActionContent:

    def __init__(self, action_name, content):
        self.ActionName = action_name
        self.Content = {}

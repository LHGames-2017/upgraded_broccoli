# LHGames
## Goal of the game
Score as many points as possible. To earn points, you must gather resources and defeat your opponents.

# Resources
## Minerals
Minerals give you points when they are deposited in your house. They are also the currency of the game. Using your minerals to buy upgrades, potions and items will not decrease your score.
To collect minerals, you need to mine them from resource tiles, steal them from other players or kill other players to earn what they were carrying.

To steal minerals, you need to be adjacent to another player's house.
When you kill a player, you are awarded the resources they were carrying. If you do not have enough room to carry them, they will drop on the ground, where everyone can collect them.
A player can only carry a certain amount of minerals before they need to be deposited into their base. This capacity can be increased by purchasin upgrades and items.

## Health
Run out of health and you are dead. 
When you die, the minerals you were carrying are awarded to the player who killed you.
To regain health, you can buy potions from the stores. You can carry as many potions as you want. Each potion you drink regenerates 5HP.

## Items
Players can acquire items through the Shop.
To buy an Item, the player must be next to the shop.
All items (except potions) cost 40 000 resources.

There are different types of items:
- Attack items: These items will give you more Attack power, which means more damage output.
    - Microsoft Sword (+2 attack)
- Defence items: These items will give you more Defence, which means you take less damage when someone attacks you.
    - Ubisoft Shield (+2 defence)
- Carrying capacity items: There items increase you capacity to carry minerals (think of it as a backpack).
    - Devolutions Backpack (+2 000 carrying capacity)
- Collecting speed items: There items make you collect minerals faster.
    - Devolutions Pickaxe (+75% base mining amount)
- Health potions: 
    - They regenerate 5HP when they are used, they cost 5 000 minerals.

# Combat
Players can execute melee attacks.
An attack deals damage based on the characters's attack, his items and the other character's defence and his items.
Killing an enemy grants a number of points that depends on each's player position on the leaderboard. 

Damage is calculated with this formula:
Floor(3 + attacker's power + offensive items - 2 * (defender's defence + defensive items)^0.6 )

| Attack | Defence | Damage | Damage with Sword | Damage with shield | Damage with sword & shield |
|--------|---------|--------|-------------------|--------------------|----------------------------|
| 1      | 1       | 2      | 4                 | 0                  | 2                          |
| 1      | 3       | 0      | 2                 | 0                  | 0                          |
| 1      | 5       | 0      | 0                 | 0                  | 0                          |
| 3      | 1       | 4      | 6                 | 2                  | 4                          |
| 3      | 3       | 2      | 4                 | 0                  | 2                          |
| 3      | 5       | 0      | 2                 | 0                  | 1                          |
| 3      | 7       | 0      | 1                 | 0                  | 0                          |
| 3      | 9       | 0      | 0                 | 0                  | 0                          |
| 5      | 1       | 6      | 8                 | 4                  | 6                          |
| 5      | 3       | 4      | 6                 | 2                  | 4                          |
| 5      | 5       | 2      | 4                 | 1                  | 3                          |
| 5      | 7       | 1      | 3                 | 0                  | 2                          |
| 5      | 9       | 0      | 2                 | 0                  | 1                          |
| 5      | 11      | 0      | 1                 | 0                  | 0                          |
| 7      | 1       | 8      | 10                | 6                  | 8                          |
| 7      | 3       | 6      | 8                 | 4                  | 6                          |
| 7      | 5       | 4      | 6                 | 3                  | 5                          |
| 7      | 7       | 3      | 5                 | 2                  | 4                          |
| 7      | 9       | 2      | 4                 | 1                  | 3                          |
| 7      | 11      | 1      | 3                 | 0                  | 2                          |
| 9      | 1       | 10     | 12                | 8                  | 10                         |
| 9      | 3       | 8      | 10                | 6                  | 8                          |
| 9      | 5       | 6      | 8                 | 5                  | 7                          |
| 9      | 7       | 5      | 7                 | 4                  | 6                          |
| 9      | 9       | 4      | 6                 | 3                  | 5                          |
| 9      | 11      | 3      | 5                 | 2                  | 4                          |
| 11     | 1       | 12     | 14                | 10                 | 12                         |
| 11     | 3       | 10     | 12                | 8                  | 10                         |
| 11     | 5       | 8      | 10                | 7                  | 9                          |
| 11     | 7       | 7      | 9                 | 6                  | 8                          |
| 11     | 9       | 6      | 8                 | 5                  | 7                          |
| 11     | 11      | 5      | 7                 | 4                  | 6                          |

# Actions
Actions are executed in the order in which they are received. If 3 players are asked to send us their desired answer and they answer in the order 2, 3, 1 then player 2 gets to go first, followed by player 3 and then player 1 would go last.

## Move actions
When a move action is attempted, the destination tile must be within reachable distance (1 square, no diagonal movement) and it must be empty.
If another player is standing on that tile, the action will fail.
Players cannot step on blocked tiles.
A player can walk in lava but will die.

## Attack actions
To be able to attack a target, it must be within striking distance. If the target dies, the player responsible for the last hit is awarded the kill.
For example, player 1 and player 2 are attacking player 3 who has 10hp. Player 1 strikes player 3 for 8 damage and then player 2 strikes for 5 damage. Player 2 is awarded the kill because he is the one who dealt the killing blow.   

## Collect actions
To collect resources, a player must adjacent to the resource.
The amount of resources collected each turn is determined by a player's upgrades collecting speed upgrades, his items and the density of the resource patch.
A player cannot carry more than his Carrying capacity allows. When his inventory is full, he needs to visit his home to deposit his resources. Resources are automatically deposited when a player steps on his house tile.

## Heal actions
To heal himself, a player must have health potions on him.
If you do not have any potions, the action will fail.

## Upgrade actions
To purchase an upgrade, the player must be in his house.
Resources that you are carrying are used first, then the ones stored in your house. If you do not have enough resources, the upgrade will fail. All upgrades have 5 levels that can be purchased.

### Upgrade levels
|   	    | Health  | Attack 	| Defence 	| Collecting speed 	| Carrying capacity 	|
|---------- |-------- |--------	|---------- |------------------	|-------------------	|
| Level 0 	| 5       | 1      	| 1       	| 1                	| 1000              	|
| Level 1 	| 8       | 3      	| 3       	| 1.25             	| 1500              	|
| Level 2 	| 10      | 5      	| 5       	| 1.5              	| 2500              	|
| Level 3 	| 15      | 7      	| 7       	| 2                	| 5000              	|
| Level 4 	| 20      | 9     	| 9      	| 2.5              	| 10000              	|
| Level 5 	| 30      | 11     	| 11      	| 3.5              	| 25000              	|

### Upgrade prices
|   	    | Price for AttackPower, Defence, CollectingSpeed, CarryingCapacity | Price for MaxHealth |
|---------- |------------------------------------------------------------------ | ------------------- |
| Level 0   | 0                                                                 | 0                   |
| Level 1 	| 15000                                                             | 10000               |
| Level 2 	| 50000                                                             | 20000               |
| Level 3 	| 100000                                                            | 30000               |
| Level 4 	| 250000                                                            | 50000               |
| Level 5 	| 500000                                                            | 100000              |

## Stealing actions
To steal from an other player, you must be on a tile adjacent to their house. Stealing quantity scales with collecting speed.

## Purchase actions
To purchase an item, you must be next to a shop and have enough minerals to buy it. Minerals that you are carrying are used first.

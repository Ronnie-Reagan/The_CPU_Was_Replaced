# This file gives Python type definitions to TFWR builtins to allow editing code with Python editors.
# Note that the games language is not Python and these definitions are only an approximation.
# Contributed by @Noon, @KlingonDragon and @dieckie on the TFWR Discord server.

from typing import Any, Optional, Iterable


# -------------------------------------------------------------------------------
class Item:
    """A member of the Items Class"""


class Items:
    Carrot: Item
    """Obtained by harvesting carrots."""

    Fertilizer: Item
    """Call `use_item(Items.Fertilizer)` to instantly grow the plant under the drone by 2s."""

    Gold: Item
    """Found in treasure chests in mazes."""

    Hay: Item
    """Obtained by cutting grass."""

    Power: Item
    """Obtained by harvesting sunflowers. The drone automatically uses this to move twice as fast."""

    Pumpkin: Item
    """Obtained when harvesting pumpkins."""



    Water: Item
    """Used to water the ground by calling `use_item(Items.Water)`."""

    Weird_Substance: Item
    """Call `use_item(Items.Weird_Substance)` on a bush to grow a maze."""

    Wood: Item
    """Obtained from bushes and trees."""

    Cactus: Item
    """Obtained when harvesting sorted cacti."""

    Bone: Item
    """The bones of an ancient creature."""


# -------------------------------------------------------------------------------
class Hat:
    """A member of the Hats class"""

class Hats:
    Straw_Hat: Hat
    """The default hat."""

    Dinosaur_Hat: Hat
    """Equip it to start the dinosaur game."""

# -------------------------------------------------------------------------------
class Leaderboard:
    """A member of the Leaderboards class"""

class Leaderboards:
    Fastest_Reset: Leaderboard
    """Fully automate the entire game."""

    Maze: Leaderboard
    """Farm 300000 gold."""

    Dinosaur: Leaderboard
    """Farm 98000 bones."""

    Cactus: Leaderboard
    """Farm 100000 cacti."""

    Wood: Leaderboard
    """Farm 100000 wood"""

    Carrots: Leaderboard
    """Farm 100000 carrots"""

    Pumpkins: Leaderboard
    """Farm 100000 pumpkins"""

    Hay: Leaderboard
    """Farm 100000 hay"""

    Polyculture: Leaderboard
    """Farm 100000 hay, wood and carrots"""
    
    Sunflowers: Leaderboard
    """Farm 100000 sunflowers"""

# -------------------------------------------------------------------------------
class Entity:
    """A member of the Entities Class"""

class Entities:
    Apple: Entity
    """Dinosaurs love them apparently."""
    
    Grass: Entity
    """
    Grows automatically. Harvest it to obtain `Items.Hay`.

    Average seconds to grow: 0.5
    Grows on: grassland or soil
    """

    Bush: Entity
    """
    A small bush that drops `Items.Wood`.

    Average seconds to grow: 4
    Grows on: grassland or soil
    """

    Tree: Entity
    """
    Trees drop more wood than bushes. They take longer to grow if other trees grow next to them.

    Average seconds to grow: 7
    Grows on: grassland or soil
    """

    Carrot: Entity
    """
    Carrots!

    Average seconds to grow: 6
    Grows on: soil
    """

    Pumpkin: Entity
    """
    Pumpkins grow together when they are next to other fully grown pumpkins. About 1 in 5 pumpkins dies when it grows up.
     When you harvest a pumpkin you get `Items.Pumpkin` equal to the number of pumpkins in the mega pumpkin cubed.

    Average seconds to grow: 2
    Grows on: soil
    """

    Sunflower: Entity
    """
    Sunflowers collect the power from the sun. Harvesting them will give you `Items.Power` equal to the number of sunflowers in the farm.
     If you harvest a sunflower that doesn't have the maximum number of petals all the sunflowers will die.

    Average seconds to grow: 5
    Grows on: soil
    """

    Cactus: Entity
    """
    Cacti come in 10 different sizes. When harvested, all cacti on the field will be harvested. Only those that are in sorted order will drop `Items.Cactus`.

    Average seconds to grow: 1
    Grows on: soil
    """

    Hedge: Entity
    """Part of the maze. Grow a maze by fertilizing a fully grown bush."""

    Treasure: Entity
    """A treasure that contains gold equal to the side length of the maze in which it is hidden. It can be harvested like a plant."""

    Dinosaur: Entity
    """
    A majestic dinosaur. It moves around randomly but won't move for a while after being measured. Harvesting it harvests all adjacent dinosaurs of the same type and makes them drop `Items.Bones`.

    Average seconds to grow: 0.2
    Grows on: grassland or soil
    """


# -------------------------------------------------------------------------------
class Ground:
    """A member of the Grounds Class"""


class Grounds:
    Grassland: Ground
    """The default ground. Grass will automatically grow on it."""

    Soil: Ground
    """Calling `till()` turns the ground into this. Calling `till()` again changes it back to grassland."""


# -------------------------------------------------------------------------------
class Unlock:
    """A member of the Unlocks Class"""


class Unlocks:
    Trees: Unlock
    """
    Unlock: Unlocks trees.
    Upgrade: Increases the yield of bushes and trees.
    """

    Speed: Unlock
    """Increases the speed of the drone."""

    Plant: Unlock
    """Unlocks planting."""

    Loops: Unlock
    """Unlocks a simple while loop."""

    Senses: Unlock
    """The drone can see what's under it and where it is."""

    Expand: Unlock
    """
    Unlock: Expands the farm land and unlocks movement.
    Upgrade: Expands the farm. This also clears the farm.
    """

    Operators: Unlock
    """Arithmetic, comparison and logic operators."""

    Pumpkins: Unlock
    """
    Unlock: Pumpkins!
    Upgrade: Increases the yield and cost of pumpkins.
    """

    Variables: Unlock
    """Assign values to variables."""

    Functions: Unlock
    """Define your own functions."""

    Watering: Unlock
    """Water the plants to make them grow faster."""

    Carrots: Unlock
    """
    Unlock: Till the soil and plant carrots.
    Upgrade: Increases the yield and cost of carrots.
    """

    Lists: Unlock
    """Use lists to store lots of values."""

    Costs: Unlock
    """Allows access to the cost of things."""

    Fertilizer: Unlock
    """Reduces the remaining growing time of the plant under the drone by 2 seconds."""

    Mazes: Unlock
    """
    Unlock: A maze with a treasure in the middle.
    Upgrade: Increases the gold in treasure chests.
    """

    Debug: Unlock
    """Tools to help with debugging programs."""

    Debug_2: Unlock
    """Functions to temporarily slow down the execution and make the grid smaller."""

    Timing: Unlock
    """Functions to help measure performance."""

    Grass: Unlock
    """Increases the yield of grass."""

    Multi_Trade: Unlock
    """Trade multiple items at once."""

    Auto_Unlock: Unlock
    """Automatically unlock things."""

    Polyculture: Unlock
    """Use companion planting to increase the yield."""

    Sunflowers: Unlock
    """
    Unlock: Sunflowers and Power.
    Upgrade: Increases the power gained from sunflowers.
    """

    Leaderboard: Unlock
    """Join the leaderboard for the fastest reset time."""

    Dictionaries: Unlock
    """Get access to dictionaries and sets."""

    Utilities: Unlock
    """Unlocks the `min()`, `max()` and `abs()` functions."""

    Cactus: Unlock
    """
    Unlock: Cactus!
    Upgrade: Increases the yield and cost of cactus.
    """

    Dinosaurs: Unlock
    """
    Unlock: Majestic ancient creatures.
    Upgrade: Increases the yield and cost of dinosaurs.
    """


# -------------------------------------------------------------------------------
class Direction:
    """
    A direction, e.g. North.
    """


North = Direction()
"""
The direction north, i.e. up.
"""

East = Direction()
"""
The direction east, i.e. right.
"""
South = Direction()
"""
The direction south, i.e. down.
"""
West = Direction()
"""
The direction west, i.e. left.
"""


# -------------------------------------------------------------------------------
def harvest() -> bool:
    """
    Harvests the entity under the drone.
    If you harvest an entity that can't be harvested, it will be destroyed.

    returns `True` if an entity was removed, `False` otherwise.

    takes `200` ticks to execute if an entity was removed, `1` tick otherwise.

    example usage:
    ```
    harvest()
    ```
    """
    ...


# -------------------------------------------------------------------------------
def can_harvest() -> bool:
    """
    Used to find out if plants are fully grown.

    returns `True` if there is an entity under the drone that is ready to be harvested, `False` otherwise.

    takes `1` tick to execute.

    example usage:
    ```
    if can_harvest():
        harvest()
    ```
    """
    ...


# -------------------------------------------------------------------------------
def plant(entity: Entity) -> bool:
    """
    Spends the cost of the specified `entity` and plants it under the drone.
    It fails if you can't afford the plant, the ground type is wrong or there's already a plant there.

    returns `True` if it succeeded, `False` otherwise.

    takes `200` ticks to execute if it succeeded, `1` tick otherwise.

    example usage:
    ```
    plant(Entities.Bush)
    ```
    """
    ...


# -------------------------------------------------------------------------------
def move(direction: Direction) -> bool:
    """
    Moves the drone into the specified `direction` by one tile.
    If the drone moves over the edge of the farm it wraps back to the other side of the farm.

    - `East `  =  right
    - `West `  =  left
    - `North`  =  up
    - `South`  =  down

    returns `True` if the drone has moved, `False` otherwise.

    takes `200` ticks to execute if the drone has moved, `1` tick otherwise.

    example usage:
    ```
    move(North)
    ```
    """
    ...


# -------------------------------------------------------------------------------
def swap(direction: Direction) -> bool:
    """
    Swaps the entity under the drone with the entity next to the drone in the specified `direction`.
    - Doesn't work on all entities.
    - Also works if one (or both) of the entities are `None`.

    returns `True` if it succeeded, `False` otherwise.

    takes `200` ticks to execute on success, `1` tick otherwise.

    example usage:
    ```
    swap(North)
    ```
    """
    ...


# -------------------------------------------------------------------------------
def till() -> None:
    """
    Tills the ground under the drone into soil. If it's already soil it will change the ground back to grassland.

    returns `None`

    takes `200` ticks to execute.

    example usage:
    ```
    till()
    ```
    """
    ...


# -------------------------------------------------------------------------------
def get_pos_x() -> int:
    """
    Gets the current x position of the drone.
    The x position starts at `0` in the `West` and increases in the `East` direction.

    returns a number representing the current x coordinate of the drone.

    takes `1` tick to execute.

    example usage:
    ```
    x, y = get_pos_x(), get_pos_y()
    ```
    """
    ...


# -------------------------------------------------------------------------------
def get_pos_y() -> int:
    """
    Gets the current y position of the drone.
    The y position starts at `0` in the `South` and increases in the `North` direction.

    returns a number representing the current y coordinate of the drone.

    takes `1` tick to execute.

    example usage:
    ```
    x, y = get_pos_x(), get_pos_y()
    ```
    """
    ...


# -------------------------------------------------------------------------------
def get_world_size() -> int:
    """
    Get the current size of the farm.

    returns the side length of the grid in the north to south direction.

    takes `1` tick to execute.

    example usage:
    ```
    for i in range(get_world_size()):
        move(North)
    ```
    """
    ...


# -------------------------------------------------------------------------------
def get_entity_type() -> Entity | None:
    """
    Find out what kind of entity is under the drone.

    returns `None` if the tile is empty, otherwise returns the type of the entity under the drone.

    takes `1` tick to execute.

    example usage:
    ```
    if get_entity_type() == Entities.Grass:
        harvest()
    ```
    """
    ...


# -------------------------------------------------------------------------------
def get_ground_type() -> Ground:
    """
    Find out what kind of ground is under the drone.

    returns the type of the ground under the drone.

    takes `1` tick to execute.

    example usage:
    ```
    if get_ground_type() != Grounds.Soil:
        till()
    ```
    """
    ...


# -------------------------------------------------------------------------------
def get_time() -> float:
    """
    Get the current game time.

    returns the time in seconds since the start of the game.

    takes `1` tick to execute.

    example usage:
    ```
    start = get_time()

    do_something()

    time_passed = get_time() - start
    ```
    """
    ...


# -------------------------------------------------------------------------------
def get_tick_count() -> float:
    """
    Used to measure the number of ticks performed.

    returns the number of ticks performed since the start of execution.

    takes `0` tick to execute.

    example usage:
    ```
    do_something()

    print(get_tick_count())
    ```
    """
    ...


# -------------------------------------------------------------------------------
def trade(item: Item, n: Optional[float] = None) -> bool:
    """
    Tries to buy the specified `item`.
     If the `item` cannot be bought or you don't have the required resources it simply does nothing.

    overloads:
    `trade(item)`: Buy the `item` once.
    `trade(item, n)`: If `Unlocks.Multi_Trade` is unlocked, this will buy the `item` `n` times immediately. If you can't afford all `n` items, it won't buy any at all. If `Unlocks.Multi_Trade` is not unlocked, it throws an error.

    returns `True` if it was able to buy the item(s), `False` otherwise.

    takes `200` ticks to execute if it succeeded, `1` tick otherwise.

    example usage:
    ```
    if num_unlocked(Unlocks.Multi_Trade) > 0:
        trade(Items.Carrot_Seed, 10)
    else:
        for i in range(10):
            trade(Items.Carrot_Seed)
    ```
    """
    ...


# -------------------------------------------------------------------------------
def use_item(item: Item, n: int = 1) -> bool:
    """
    Attempts to use the specified `item` `n` times. Can only be used with some items including `Items.Water`, `Items.Fertilizer` and `Items.Egg`.

    returns `True` if an item was used, `False` otherwise.

    takes `200` ticks to execute if it succeeded, `1` tick otherwise.

    example usage:
    ```
    use_item(Items.Fertilizer)
    ```
    """
    ...


# -------------------------------------------------------------------------------
def get_water() -> float:
    """
    Get the current water level under the drone.

    returns the water level under the drone as a number between `0` and `1`.

    takes `1` tick to execute.

    example usage:
    ```
    if get_water() < 0.5:
        use_item(Items.Water)
    ```
    """
    ...


# -------------------------------------------------------------------------------
def do_a_flip() -> None:
    """
    Makes the drone do a flip! This action is not affected by speed upgrades.

    returns `None`

    takes 1s to execute.

    example usage:
    ```
    while True:
        do_a_flip()
    ```
    """
    ...


# -------------------------------------------------------------------------------
def print(*something: Any) -> None:
    """
    Prints `something` into the air above the drone using smoke. This action is not affected by speed upgrades.
    Multiple values can be printed at once.

    returns `None`

    takes 1s to execute.

    example usage:
    ```
    print('ground:', get_ground_type())
    ```
    """
    ...


# -------------------------------------------------------------------------------
def set_execution_speed(speed: float) -> None:
    """
    Limits the speed at which the program is executed to better see what's happening.

    - A `speed` of `1` is the speed the drone has without any speed upgrades.
    - A `speed` of `10` makes the code execute `10` times faster and corresponds to the speed of the drone after `9` speed upgrades.
    - A `speed` of `0.5` makes the code execute at half of the speed without speed upgrades. This can be useful to see what the code is doing.

    If `speed` is faster than the execution can currently go it will just go at max speed.

    If `speed` is `0` or negative, the speed is changed back to max speed.
     The effect will also stop when the execution stops.

    returns `None`

    takes `200` ticks to execute.

    example usage:
    ```
    set_execution_speed(1)
    ```
    """
    ...


# -------------------------------------------------------------------------------
def set_world_size(size: float) -> None:
    """
    Limits the size of the farm to better see what's happening.
    Also clears the farm and resets the drone position.
    - Sets the farm to a `size` x `size` grid.
    - The smallest `size` possible is `3`.
    - A `size` smaller than `3` will change the grid back to its full size.
    - The effect will also stop when the execution stops.

    returns `None`

    takes `200` ticks to execute.

    example usage:
    ```
    set_world_size(5)
    ```
    """
    ...


# -------------------------------------------------------------------------------
def num_items(item: Item) -> float:
    """
    Find out how much of `item` you currently have.

    returns the number of `item` currently in your inventory.

    takes `1` tick to execute.

    example usage:
    ```
    if num_items(Items.Fertilizer) == 0:
        trade(Items.Fertilizer)
    ```
    """
    ...


# -------------------------------------------------------------------------------
def get_cost(thing: Entity | Item | Unlock) -> dict[Item, float] | None:
    """
    Gets the cost of a `thing`

    If `thing` is an item: get the cost of buying it when using `trade(item)`.
    If `thing` is an entity: get the cost of planting it.
    If `thing` is an unlock: get the cost of unlocking it.

    - returns a dictionary with items as keys and numbers as values. Each item is mapped to how much of it is needed.
    - returns `{}` when used on an upgradeable unlock that is already at the max level.

    takes `1` tick to execute.

    example usage:
    ```
    cost = get_cost(Unlocks.Carrots)
    for item in cost:
        if num_items(item) < cost[item]:
            print('not enough items to unlock carrots')
    ```
    """
    ...


# -------------------------------------------------------------------------------
def clear() -> None:
    """
    Removes everything from the farm, moves the drone back to position `(0,0)` and changes the hat back to the default.

    returns `None`

    takes `200` ticks to execute.

    example usage:
    ```
    clear()
    ```
    """
    ...


# -------------------------------------------------------------------------------
def get_companion() -> tuple[Entity, tuple[int, int]] | None:
    """
    Get the companion preference of the plant under the drone.

    returns a list of the form `(companion_type, (companion_x_position, companion_y_position))`

    takes `1` tick to execute.

    example usage:
    ```
    companion = get_companion()
    if companion != None:
        print(companion)
    ```
    """
    ...


# -------------------------------------------------------------------------------
def unlock(unlock: Unlock) -> bool:
    """
    Has exactly the same effect as clicking the button corresponding to `unlock` in the research tree.

    returns `True` if the unlock was successful, `False` otherwise.

    takes `200` ticks to execute if it succeeded, `1` tick otherwise.

    example usage:
    ```
    unlock(Unlocks.Carrots)
    ```
    """
    ...


# -------------------------------------------------------------------------------
def num_unlocked(thing: Unlock | Entity | Ground | Item) -> int:
    """
    Used to check if an unlock, entity, ground or item is already unlocked.

    returns `1` plus the number of times `thing` has been upgraded if `thing` is upgradable. Otherwise returns `1` if `thing` is unlocked, `0` otherwise.

    takes `1` tick to execute.

    example usage:
    ```
    if num_unlocked(Unlocks.Multi_Trade) > 0:
        trade(Items.Carrot_Seed, 10)
    else:
        for i in range(10):
            trade(Items.Carrot_Seed)
    ```
    """
    ...


# -------------------------------------------------------------------------------
def measure(direction: Optional[Direction] = None) -> float | tuple[int, int] | None:
    """
    Can measure some values on some entities. The effect of this depends on the entity.

    overloads:
    `measure()`: measures the entity under the drone.
    `measure(direction)`: measures the neighboring entity in the `direction` of the drone.

    Sunflower: returns the number of petals.
    Treasure: returns the next position.
    Cactus: returns the size.
    Dinosaur: returns the number corresponding to the type.
    All other entities: returns `None`.

    takes `1` tick to execute.

    example usage:
    ```
    num_petals = measure()
    ```
    """
    ...


# -------------------------------------------------------------------------------
def leaderboard_run(leaderboard: Leaderboard, file_name: str, speedup: float) -> None:
    """
    Starts a timed run for the `leaderboard` using the specified `file_name` as a starting point.
    `speedup` sets the starting speedup.

    returns `None`

    takes `200` ticks to execute.

    example usage:
    ```
    leaderboard_run(Leaderboards.Fastest_Reset, "full_run", 256)
    ```
    """
    ...


# -------------------------------------------------------------------------------
def simulate(filename: str, sim_unlocks: dict[Unlocks, float] | Iterable[Unlocks], sim_items: dict[Items, float], sim_globals: dict[str, Any], seed: float, speedup: float) -> None:
    """
    Starts a simulation for the leaderboard using the specified `file_name` as a starting point.

    `sim_unlocks`: A sequence containing the starting unlocks.

    `sim_items`: A dict mapping items to amounts. The simulation starts with these items.

    `sim_globals`: A dict mapping variable names to values. The simulation starts with these variables in the global scope.

    `seed`: The random seed of the simulation. Must be a positive integer.

    `speedup`: The starting speedup.

    returns the time it took to run the simulation.

    takes `200` ticks to execute.

    example usage:

    ```
    filename = "f1"
    sim_unlocks = Unlocks
    sim_items = {Items.Carrot : 10000, Items.Hay : 50}
    sim_globals = {"a" : 13}
    seed = 0
    speedup = 64
    run_time = simulate(filename, sim_unlocks, sim_items, sim_globals, seed, speedup)
    ```
    """
    ...


# -------------------------------------------------------------------------------
def quick_print(*something: Any) -> None:
    """
    Prints a value just like `print()` but it doesn't stop to write it into the air so it can only be found on the output page.

    returns `None`

    takes `0` ticks to execute.

    example usage:
    ```
    quick_print('hi mom')
    ```
    """
    ...


# -------------------------------------------------------------------------------
def random() -> float:
    """
    Samples a random number between 0 (inclusive) and 1 (exclusive).

    returns the random number.

    takes `1` ticks to execute.

    example usage:
    ```
    def random_elem(list):
        index = random() * len(list) // 1
        return list[index]
    ```
    """
    ...


# -------------------------------------------------------------------------------
def change_hat(hat: Hat) -> None:
    """
    Changes the hat of the drone to the specified `hat`.

    returns `None`

    takes `200` ticks to execute.

    example usage:
    ```
    change_hat(Hats.Dinosaur_Hat)
    ```
    ...
    """
    ...

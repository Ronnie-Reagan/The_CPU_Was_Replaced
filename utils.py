# Utility helpers for navigating the farm grid


stringDirections = {
    "north": [North],
    "south": [South],
    "east": [East],
    "west": [West],
}


def go(dir: str) -> None:
    # Move one tile in the given cardinal direction
    # The input is normalised to lowercase and ignored if invalid

    if not dir:
        return

    key = dir.lower()
    if key in stringDirections:
        move(stringDirections[key])


def goto(spot) -> None:
    # Move the drone to the provided (x, y) coordinate

    target_x, target_y = spot

    while target_x != get_pos_x():
        direction = "east" if target_x > get_pos_x() else "west"
        go(direction)

    while target_y != get_pos_y():
        direction = "north" if target_y > get_pos_y() else "south"
        go(direction)


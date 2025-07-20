stringDirections = {
    "north":[North],
    "south":[South],
    "east":[East],
    "west":[West]
}

def go(String: dir):
    # must be revised to be non dependant on capitalization (auto lowercase all)
    # no use of str.
    if dir:
        move(stringDirections[dir])

def goto(spot):
    x, y = spot
    while x != get_pos_x():
        dir =  x < get_pos_x() and "east" or "west"
        go(dir)
    while y != get_pos_y():
        dir =  y < get_pos_y() and "north" or "south"
        go(dir)
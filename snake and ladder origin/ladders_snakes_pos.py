ladders = {
    2: 32,
    11: 23,
    45: 59,
    53: 86,
    60: 78,
    67: 133,
    83: 180,
    97: 130,
    113: 127,
    118: 121,
    139: 169,
    155: 190,
    171: 203,
    175: 199
}

snakes = {
    202: 142,
    197: 177,
    192: 157,
    179: 161,
    178: 76,
    127: 94,
    121: 90,
    61: 28,
    56: 15,
    51: 19,
    38: 3
}

def get_position_coordinates(position):
    tile_width = (1280 - 200) / 17
    tile_height = (720 - 145) / 12
    row = (position - 1) // 17
    column = (position - 1) % 17

    if row % 2 == 1:
        column = 16 - column

    x = 100 + column * tile_width
    y = 720 - 56 - (row + 1) * tile_height
    return int(x), int(y)
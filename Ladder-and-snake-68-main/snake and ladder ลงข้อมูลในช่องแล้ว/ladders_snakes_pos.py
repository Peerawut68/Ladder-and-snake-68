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

checkpoints = {68, 87, 179}
respawn_points = {25, 70, 137, 200}
bombs = {9, 28, 164, 182, 194}
cages = {57, 64, 110, 191}
presents = {7, 17, 20, 38, 43, 69, 74, 
    82, 94, 101, 107, 124, 133, 
    144, 153, 157, 167, 173, 189,
    196, 197, 201}

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
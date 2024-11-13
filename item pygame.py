gift_tiles = [7, 17, 20, 38, 43, 74, 82, 94, 101, 107, 124, 133, 144, 153, 157, 167, 174, 189, 196, 197, 201]


def apply_random_item(player):
    global opponent_frozen_turns, player_has_shield, opponent_has_shield, player_pos, opponent_pos
    items = ["FREEZE", "SHIELD", "JUMP", "KNOCKBACK"]
    item = random.choice(items)
    
    if item == "FREEZE" and player == "player":
        opponent_frozen_turns = 1
    elif item == "SHIELD":
        if player == "player":
            player_has_shield = True
        else:
            opponent_has_shield = True
    elif item == "JUMP" and player == "player":
        player_pos = min(player_pos + 3, BOARD_WIDTH * BOARD_HEIGHT)
    elif item == "KNOCKBACK" and player == "player":
        opponent_pos = max(opponent_pos - 3, 1)


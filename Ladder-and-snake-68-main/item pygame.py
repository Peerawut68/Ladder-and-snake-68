def gift_effect(player):
    global opponent_frozen_turns, player_has_shield, opponent_has_shield, player_pos, opponent_pos
    
    #สุ่มitem
    gift = random.choice(["freeze", "shield", "jump", "knockback"])
    
    if gift == "freeze":
        if player == "player":
            if not opponent_has_shield:
                opponent_frozen_turns += 1
            else:
                opponent_has_shield = False
        else:
            if not player_has_shield:
                opponent_frozen_turns += 1
            else:
                player_has_shield = False

    elif gift == "shield":
        if player == "player":
            player_has_shield = True
        else:
            opponent_has_shield = True

    elif gift == "jump":
        if player == "player":
            player_pos = min(player_pos + 3, BOARD_WIDTH * BOARD_HEIGHT)
        else:
            opponent_pos = min(opponent_pos + 3, BOARD_WIDTH * BOARD_HEIGHT)

    elif gift == "knockback":
        if player == "player":
            if not opponent_has_shield:
                opponent_pos = max(opponent_pos - 3, 1)
            else:
                opponent_has_shield = False
        else:
            if not player_has_shield:
                player_pos = max(player_pos - 3, 1)
            else:
                player_has_shield = False


def apply_tile_effects(player):
    global player_pos, opponent_pos, player_has_shield, opponent_has_shield

    pos = player_pos if player == "player" else opponent_pos
    has_shield = player_has_shield if player == "player" else opponent_has_shield

    if pos in bomb_tiles:
        if has_shield:
            if player == "player":
                player_has_shield = False
            else:
                opponent_has_shield = False
        else:
            pos = max(pos - 3, 1)

    elif pos in return_tiles:
        if has_shield:
            if player == "player":
                player_has_shield = False
            else:
                opponent_has_shield = False
        else:
            for checkpoint in reversed(sorted(checkpoint_tiles)):
                if pos > checkpoint:
                    pos = checkpoint
                    break

    elif pos in cage_tiles:
        if has_shield:
            if player == "player":
                player_has_shield = False
            else:
                opponent_has_shield = False
        else:
            if player == "player":
                player_frozen_turns += 1
            else:
                opponent_frozen_turns += 1

    if player == "player":
        player_pos = pos
    else:
        opponent_pos = pos

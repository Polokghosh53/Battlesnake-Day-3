def get_next(currentHead, nextMove):
    """
    return the coordinate of the head if our snake goes that way
    """
    futureHead = currentHead.copy()
    if nextMove == 'left':
        futureHead['x'] = currentHead['x'] - 1
    if nextMove == 'right':
        futureHead['x'] = currentHead['x'] + 1
    if nextMove == 'up':
        futureHead['y'] = currentHead['y'] + 1
    if nextMove == 'down':
        futureHead['y'] = currentHead['y'] - 1
    return futureHead


def get_safe_moves(possible_moves, body, board):
    safe_moves = []

    for guess in possible_moves:
        guess_coord = get_next(body[0], guess)
        if avoid_walls(guess_coord, board["width"], board["height"]) and avoid_snakes(guess_coord, board["snakes"]):
            safe_moves.append(guess)
        elif len(body) > 1 and guess_coord == body[-1] and guess_coord not in body[:-1]:
            safe_moves.append(guess)
    return safe_moves


def avoid_walls(future_head, board_width, board_height):
    result = True

    x = int(future_head["x"])
    y = int(future_head["y"])

    if x < 0 or y < 0 or x >= board_width or y >= board_height:
        result = False

    return result


def avoid_snakes(future_head, snake_bodies):
    for snake in snake_bodies:
        if future_head in snake["body"][:-1]:
            return False
    return True

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

def get_all_moves(coord):
    # return a list of all coordinates reachable from this point
    return [{'x' : coord['x'] + 1, 'y':coord['y']}, {'x' : coord['x'] - 1, 'y':coord['y']}, {'x' : coord['x'], 'y':coord['y'] + 1}, {'x' : coord['x'], 'y':coord['y'] - 1}]

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

def avoid_consumption(future_head, snake_bodies, my_snake):
    if len(snake_bodies) < 2:
        return True

    my_length = my_snake['length']
    for snake in snake_bodies:
        if snake == my_snake:
            continue
        if future_head in get_all_moves(snake['head']) and future_head not in snake['body'][1:-1] and my_length <= snake['length']:
            return False
    return True

def avoid_hazards(future_head, hazards):
    return future_head not in hazards

def avoid_snakes(future_head, snake_bodies):
    for snake in snake_bodies:
        if future_head in snake["body"][:-1]:
            return False
    return True


def get_minimum_moves(start_coord, targets):
    moves = []
    for coord in targets:
        moves.append(abs(coord['x'] - start_coord['x']) + abs(coord['y'] - start_coord['y']))
    return moves

def at_wall(coord, board):
    return coord['x'] <= 0 or coord['y'] <= 0 or coord['x'] >= board['width'] - 1 or coord['y'] >= board['height'] - 1

def get_future_head_positions(body, turns, board):
    turn = 0
    explores = {}
    explores[0] = [body[0]]
    while turn < turns:
        turn += 1
        explores[turn] = []
        for explore in explores[turn-1]:
            next_path = get_safe_moves(['left', 'right', 'up', 'down'], [explore], board)
            for path in next_path:
                explores[turn].append(get_next(explore, path))

    return explores[turns]




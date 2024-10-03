from classes.sprites import Player, Collectible, Enemy
from classes.map import Map
import os


def validate_entities(map_data, game):
    player_count, exit_count = 0, 0
    player = None

    for y in range(len(map_data)):
        for x in range(len(map_data[y])):
            entity = map_data[y][x]
            match entity:
                case 'P':
                    if player_count < 1:
                        player = Player(x, y, 100, game)
                        map_data[y] = map_data[y][:x] + '0' + map_data[y][x+1:]
                        player_count += 1
                    else:
                        break
                case 'C':
                    Collectible(x, y, 0)
                case 'X':
                    Enemy(x, y, 0, 1)
                case 'E':
                    if exit_count < 1:
                        exit_count += 1
                    else:
                        break
    print("Enemy Count:", Enemy.get_total_count())
    print("Collectible Count:", Collectible.get_total_count())
    return player


def check_path_dfs(map_data, x, y, map_instance, visited):
    if map_data[y][x] == 'E':
        return True

    visited.add((x, y))

    # Check left
    if x > 0 and map_data[y][x - 1] != '1' and (x - 1, y) not in visited:
        if check_path_dfs(map_data, x - 1, y, map_instance, visited):
            return True
    # Check right
    if x < map_instance.w - 1 and map_data[y][x + 1] != '1' and (x + 1, y) not in visited:
        if check_path_dfs(map_data, x + 1, y, map_instance, visited):
            return True
    # Check up
    if y > 0 and map_data[y - 1][x] != '1' and (x, y - 1) not in visited:
        if check_path_dfs(map_data, x, y - 1, map_instance, visited):
            return True
    # Check down
    if y < map_instance.h - 1 and map_data[y + 1][x] != '1' and (x, y + 1) not in visited:
        if check_path_dfs(map_data, x, y + 1, map_instance, visited):
            return True
    return False


def check_map(map_data):
    map_instance = None

    if not map_data:
        return map_instance
    row_length = len(map_data[0])
    for row in map_data:
        if len(row) != row_length:
            break
    for x in range(row_length):
        if map_data[0][x] != '1' or map_data[-1][x] != '1':
            break
    for y in range(len(map_data)):
        if map_data[y][0] != '1' or map_data[y][-1] != '1':
            break

    map_instance = Map(row_length, len(map_data), map_data)
    print("Map dimensions:", map_instance.get_dimensions())
    return map_instance


def validate(game):
    try:
        base_path = os.path.dirname(os.path.dirname(__file__))
        map_path = os.path.join(base_path, 'maps', 'test.txt')

        with open(map_path, 'r') as file:
            map_data = [line.strip() for line in file]

    except FileNotFoundError:
        print("Map file not found.")
        return None, None

    map_instance = check_map(map_data)
    if map_instance is None:
        print("Map is invalid")
        return None, None

    player = validate_entities(map_data, game)
    if player is None:
        print("Invalid entity count")
        return None, None

    if check_path_dfs(map_data, player.x, player.y, map_instance, visited=set()) is True:
        return player
    print("Invalid player path to exit")
    return None, None

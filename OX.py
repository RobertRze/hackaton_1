matrix = [['-', '1', '|', '2', '|' ,'3'],
['A', '.', '|', '.', '|', '.'],
['B', '.', '|', '.', '|', '.'],
['C', '.', '|', '.', '|', '.']]
def print_matrix():
    for row in matrix:
        print(row)


def set_matrix(mark, x, y):
    x = 2 * x - 1
    result = ''
    while result != '.':
        result = get_xy_matrix(x, y)
        print(get_xy_matrix(x,y))
        if result == '.':
            matrix[y][x] = mark
            return matrix
        else:
            return None

def get_xy_matrix(x, y):
    return matrix[y][x]

def set_player():
    players = {'0': '', 'X': ''}
    for key in players.keys():
        player = input(f'Podaj nick dla {key}: ')
        players[key]=player
    return(players)

def get_player(key):
    return players_dict[key]

players_dict = {}
players_dict = set_player()

print_matrix()
game_over = False
while game_over is False:
    move = []
    for key in players_dict:
        move = input(f"{key} podaj współrzędne (xy): ")
        if set_matrix(key, int(move[0]), int(move[1])) is None:

        print_matrix()
def create_game() -> dict:
    return {
        'board': [
            ['_', '_', '_'],
            ['_', '_', '_'],
            ['_', '_', '_'],
        ],
        'turn': 'X',
        'counter': 1
    }


def input_square(game, x_or_o):
    while True:
        user_input = input(f"Enter location for {x_or_o} (row,col): ")

        try:
            row, col = map(int, user_input.split(','))
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid input. Please enter numbers between 0 and 2 for both row and column.")
                continue

            if game['board'][row][col] == '_':
                return row, col
            else:
                print("The cell is already taken, try again.")

        except ValueError:
            print("Invalid input format. Please enter in the format row,col (e.g. 1,2).")


def update_board(game, row, col, player):
    game['board'][row][col] = player


def draw_board(game):
    print("  0 1 2")
    for i, row in enumerate(game['board']):
        print(i, ' '.join((row)))


def check_win(game, player):
    for row in game['board']:
        if row[0] == row[1] == row[2] == player:
            return True
    for col in range(3):
        if game['board'][0][col] == game['board'][1][col] == game['board'][2][col] == player:
            return True
    if game['board'][0][0] == game['board'][1][1] == game['board'][2][2] == player:
        return True
    if game['board'][0][2] == game['board'][1][1] == game['board'][2][0] == player:
        return True

    return False


def check_tie(game):
    return all(cell != "_" for row in game['board'] for cell in row)


def play_x_o():
    my_game = create_game()
    while True:
        draw_board(my_game)
        current_player = my_game['turn']
        print(f"it's {current_player}'s turn.")
        row, col = input_square(my_game, current_player)
        update_board(my_game, row, col, current_player)
        if check_win(my_game, current_player):
            draw_board(my_game)
            print(f"{current_player} wins!")
            break
        if check_tie(my_game):
            draw_board(my_game)
            print("It's a tie!")
        my_game['turn'] = 'O' if current_player == 'X' else 'X'
        my_game['counter'] += 1


if __name__ == "__main__":
    play_x_o()

"""
All what I was able to do in 30 min interview + 15 afterwards bugfixing
"""

players = {1: "X", 2: "O", 0: "  "}


def check_is_win(board_matrix, player, x, y):
    result = False

    # horizontal
    for i in range(3):
        if board_matrix[x][i] != player:
            break
    else:
        return True

    # vertical
    for i in range(3):
        if board_matrix[i][y] != player:
            break
    else:
        return True

    # check diagonal
    if x == y:
        for i in range(3):
            if board_matrix[i][i] != player:
                break
        else:
            return True
        for i in range(3):
            if board_matrix[2 - i][i] != player:
                break
        else:
            return True

    return result


def print_board(board_matrix):
    for i in range(3):
        print(" | ".join([players[board_matrix[i][j]] for j in range(3)]))
        print("-----------")


if __name__ == "__main__":
    # 1 -> X
    # 2 -> O
    board_matrix = [[0] * 3 for _ in range(3)]
    print("Tic Tac Toe Game Started")
    current_player = 1
    while True:
        print_board(board_matrix)
        print(f"Player {current_player} (put X Y of cell): ")
        is_valid = False
        try:
            x, y = (map(int, input().split()))
            # validate range
            is_valid = 0 <= x < 3 and 0 <= y < 3
            # validate is cell empty
            is_valid = is_valid and board_matrix[x][y] == 0
        except Exception:
            print("Exception happen please try again")

        if not is_valid:
            print(f"Entered values are not valid please try again")
        else:
            board_matrix[x][y] = current_player
            # check is player win
            is_win = check_is_win(board_matrix, current_player, x, y)
            if is_win:
                print(f"Player {current_player} is winner!!!")
                print("Game over.")
                break
            else:
                can_continue = False
                for i in range(3):
                    if 0 in board_matrix[i]:
                        can_continue = True
                        break

                if can_continue:
                    current_player = 1 if current_player == 2 else 2
                else:
                    print("The board is full - no available turns left.")
                    print("Game over.")






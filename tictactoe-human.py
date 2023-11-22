BOARD_EMPTY = 0
BOARD_PLAYER_X = 1
BOARD_PLAYER_O = -1

import time
from collections import Counter

state = [0, 0, 0, 0, 0, 0, 0, 0, 0]

def print_board(s, index=0):
    if s == BOARD_PLAYER_X:
        return 'X'
    if s == BOARD_PLAYER_O:
        return 'O'
    return str(index)

def display_board(board):
    print(" " + print_board(board[0], 0) + "  | " + print_board(board[1], 1) + "  | " + print_board(board[2], 2) + "  ")
    print("----|----|----")
    print(" " + print_board(board[3], 3) + "  | " + print_board(board[4], 4) + "  | " + print_board(board[5], 5) + "  ")
    print("----|----|---")
    print(" " + print_board(board[6], 6) + "  | " + print_board(board[7], 7) + "  | " + print_board(board[8], 8) + "  ")

def player(s):
    counter = Counter(s)
    x_places = counter[1]
    o_places = counter[-1]

    if x_places + o_places == 9:
        return None
    elif x_places > o_places:
        return BOARD_PLAYER_O
    else:
        return BOARD_PLAYER_X

def actions(s):
    play = player(s)
    actions_list = [(play, i) for i in range(len(s)) if s[i] == BOARD_EMPTY]
    return actions_list

def result(s, a):
    (play, index) = a
    s_copy = s.copy()
    s_copy[index] = play
    return s_copy

def terminal(s):
  for i in range(3):
    # Checking if a row is filled and equal.
    if s[3 * i] == s[3 * i + 1] == s[3 * i + 2] != BOARD_EMPTY:
      return s[3 * i]
    # Checking if a column is filled and equal.
    if s[i] == s[i + 3] == s[i + 6] != BOARD_EMPTY:
      return s[i]

  if s[0] == s[4] == s[8] != BOARD_EMPTY:
    return s[0]
  if s[2] == s[4] == s[6] != BOARD_EMPTY:
    return s[2]

  # Checking if the game has no more moves available
  if player(s) is None:
    return 0
    
  # Return None if none of the previous conditions satisfy.
  return None

def play_tic_tac_toe():
    s = [BOARD_EMPTY for _ in range(9)]
    print('|------- WELCOME TO TIC TAC TOE -----------|')
    display_board(s)
    print('Player 1 is X and Player 2 is O')

    while terminal(s) is None:
        play = player(s)
        num = 1 if play == BOARD_PLAYER_X else 2
        print(f"\n\nIt is Player {num} turn", end='\n\n')
        index = int(input(f"Player {num}, enter the index (0-8): "))

        if not s[index] == BOARD_EMPTY:
            print('That coordinate is already taken. Please try again.')
            continue

        s = result(s, (play, index))
        display_board(s)
        time.sleep(1)

    winner = terminal(s)
    if winner == BOARD_PLAYER_X:
        print("Player X has won!")
    elif winner == BOARD_PLAYER_O:
        print("Player O has won!")
    else:
        print("It's a tie.")

if __name__ == '__main__':
    play_tic_tac_toe()
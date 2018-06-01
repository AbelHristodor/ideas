import time
player1 = 0
player2 = 0
answer = input("Ciao, vuoi giocare a Tris? Si/No ")
if answer == 'Si':
    player1 = input("Giocatore 1, vuoi essere X oppure 0? ")
    if player1 == 'X':
        player2 = '0'
    else:
        player2 = 'X'
else:
    print("Vabbè giocheremo un'altra volta.")


def display_board(board2):
    print('  ' + board2[1] + '  |  ' + board2[2] + '  |  ' + board2[3] + '  ')
    print("-----!-----!-----")
    print('  ' + board2[4] + '  |  ' + board2[5] + '  |  ' + board2[6] + '  ')
    print("-----!-----!-----")
    print('  ' + board2[7] + '  |  ' + board2[8] + '  |  ' + board2[9] + '  ')


def player_choice(board, sign, n_player):
    pos = int(input(f"Giocatore{n_player}, scegli un numero: "))
    print("\n")
    board[pos] = sign
    return display_board(board)


def instructions():
    print("\n\n")
    print("Allora il gioco funzionerà cosi:")
    print("Ogni casella corrisponderà al numero del numpad al contrario da 1(alto-sinistra) a 9 (basso-destra)")
    print("Il numero scelto corrisponde a tale casella.")


def switcher(board, player_n1):
    sign = player_n1
    if board[1] == sign and board[2] == sign and board[3] == sign:
        if player_n1 == 'X':
            print(f"\nIl giocatore" + str(1) + " ha vinto!")
        else:
            print(f"\nIl giocatore" + str(2) + " ha vinto!")
    elif board[4] == 'X' and board[5] == 'X' and board[6] == sign:
        if player_n1 == 'X':
            print(f"\nIl giocatore" + str(1) + " ha vinto!")
        else:
            print(f"\nIl giocatore" + str(2) + " ha vinto!")
    elif board[7] == 'X' and board[8] == 'X' and board[9] == sign:
        if player_n1 == 'X':
            print(f"\nIl giocatore" + str(1) + " ha vinto!")
        else:
            print(f"\nIl giocatore" + str(2) + " ha vinto!")
    elif board[1] == sign and board[5] == sign and board[9] == sign:
        if player_n1 == 'X':
            print(f"\nIl giocatore" + str(1) + " ha vinto!")
        else:
            print(f"\nIl giocatore" + str(2) + " ha vinto!")
    elif board[3] == sign and board[5] == sign and board[7] == sign:
        if player_n1 == 'X':
            print(f"\nIl giocatore" + str(1) + " ha vinto!")
        else:
            print(f"\nIl giocatore" + str(2) + " ha vinto!")
    elif board[1] == sign and board[4] == sign and board[7] == sign:
        if player_n1 == 'X':
            print(f"\nIl giocatore" + str(1) + " ha vinto!")
        else:
            print(f"\nIl giocatore" + str(2) + " ha vinto!")
    elif board[2] == sign and board[5] == sign and board[8] == sign:
        if player_n1 == 'X':
            print(f"\nIl giocatore" + str(1) + "ha vinto!")
        else:
            print(f"\nIl giocatore" + str(2) + " ha vinto!")
    elif board[3] == sign and board[6] == sign and board[9] == sign:
        if player_n1 == 'X':
            print(f"\nIl giocatore" + str(1) + " ha vinto!")
        else:
            print(f"\nIl giocatore" + str(2) + " ha vinto!")
    else: return "\n"


instructions()
while True:
    board_test = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    time.sleep(5)
    print("\n" * 100)
    print("Iniziamo\n")
    while answer == 'Si':
        display_board(board_test)
        print("\n")
        player_choice(board_test, player1, 1)
        if switcher(board_test, player1) != "\n":
            break
        time.sleep(2)
        print("\n" * 100)
        display_board(board_test)
        print("\n")
        player_choice(board_test, player2, 2)
        if switcher(board_test, player1) != "\n":
            break
        time.sleep(2)
        print("\n" * 100)
    answer = input("Vuoi giocare di nuovo?  Si/No")
    if answer == 'No':
        break
    else:
        continue

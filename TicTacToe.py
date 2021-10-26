
# main method
def mainMethod():

    print("Welcome to TicTacToe!\n")

    # Python does not have built-in support for Arrays, use List instead.
    # PlayingField is an array with length of 10: 9 available spots.
    playingField = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    count = 0
    player1 = "null"
    player2 = "null"
    winner = False
    playerTurn = 1

    # Setup player1 (validate user input)
    while True:
        player1 = input("Please enter a symbol to use: X or O:\n")
        if player1 not in ('X', 'O'):
            print("Not a valid selection, try again.")
            continue
        else:
            # set player2 to the other available symbol
            # both players are set, break out of the loop
            if player1 == 'X':
                player2 = 'O'
            else:
                player2 = 'X'
            break

    # Display the initial playing field (Make into seperate method)
    print("--------------------")
    print("\nObserve the playing field!\nplayer1: " +
          player1 + "\nplayer2: " + player2)
    showPlayingField(playingField, count)

    # officially start the game (continue game until there is a winner or a draw)
    while winner == False:
        # Who's turn is it?
        if (playerTurn % 2) == 0:
            playerSymbol = player2
        else:
            playerSymbol = player1
        playerMove = input(
            "\n\nPick a number on the field to place your symbol player: " + playerSymbol + "\n")

        # replace number in list with players' symbol
        if playingField.__contains__(playerMove):
            playingField = [position.replace(playerMove, playerSymbol)
                            for position in playingField]

        # print new field after players' move, increment playerTurn
        showPlayingField(playingField, count)
        playerTurn += 1

        # check if there is a winner (conditionals)
        # if we get 3 identical symbols in a row, end the game and declare the winner
        # if we've run out of numbers to pick from, it is a draw

        # 8 ways to win
        # vertical
        if (playingField[0] == playerSymbol) and (playingField[3] == playerSymbol) and (playingField[6] == playerSymbol):
            print("\n\nThe winner is player: " + playerSymbol)
            break
        elif (playingField[1] == playerSymbol) and (playingField[4] == playerSymbol) and (playingField[7] == playerSymbol):
            print("\n\nThe winner is player: " + playerSymbol)
            break
        elif (playingField[2] == playerSymbol) and (playingField[5] == playerSymbol) and (playingField[8] == playerSymbol):
            print("\n\nThe winner is player: " + playerSymbol)
            break

        # lateral
        if (playingField[0] == playerSymbol) and (playingField[1] == playerSymbol) and (playingField[2] == playerSymbol):
            print("\n\nThe winner is player: " + playerSymbol)
            break
        elif (playingField[3] == playerSymbol) and (playingField[4] == playerSymbol) and (playingField[5] == playerSymbol):
            print("\n\nThe winner is player: " + playerSymbol)
            break
        elif (playingField[6] == playerSymbol) and (playingField[7] == playerSymbol) and (playingField[8] == playerSymbol):
            print("\n\nThe winner is player: " + playerSymbol)
            break

        # criss-cross
        if (playingField[0] == playerSymbol) and (playingField[4] == playerSymbol) and (playingField[8] == playerSymbol):
            print("\n\nThe winner is player: " + playerSymbol)
            break
        elif (playingField[2] == playerSymbol) and (playingField[4] == playerSymbol) and (playingField[6] == playerSymbol):
            print("\n\nThe winner is player: " + playerSymbol)
            break

# end of mainMethod


# function for displaying playing field
def showPlayingField(field, count):
    for symbol in field:

        if count % 3 == 0:
            print("\n")

        count += 1
        print(symbol, end=" ")


# run mainMethod() when program is executed
if __name__ == "__main__":
    mainMethod()

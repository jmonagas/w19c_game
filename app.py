import gameboard
import player

print("-----------------------------")
print("Welcome to the Maze Game!")
print("-----------------------------")

print("Instructions: ")
print("-----------------------------")
print(" To move UP, type: ' u '")
print(" To move DOWN, type: ' d '")
print(" To move LEFT, type: ' l '")
print(" To move RIGHT, type: ' r '")
print("-----------------------------")

print("To Win, You Need To Move the ' X ' Out of the Maze...")
print("-----------------------------")

# TODO
# Create a new GameBoard called board
board = gameboard.GameBoard()

# Create a new Player called player starting at position 3, 4
player = player.Player(3, 4)

while True:
    board.printBoard(player.rowPosition, player.columnPosition)
    selection = input("Now, Make a Move: ")
    # TODO
    # Move the player through the board
    if selection == "u":
        if board.checkMove(player.rowPosition - 1, player.columnPosition):
            player.moveUp()
    elif selection == "d":
        if board.checkMove(player.rowPosition + 1, player.columnPosition):
            player.moveDown()
    elif selection == "l":
        if board.checkMove(player.rowPosition, player.columnPosition - 1):
            player.moveLeft()
    elif selection == "r":
        if board.checkMove(player.rowPosition, player.columnPosition + 1):
            player.moveRight()
        # Check if the player has won, if so print a message and break the loop!
    if board.checkWin(player.rowPosition, player.columnPosition):
        print("Congratulations, You Win!")
        break

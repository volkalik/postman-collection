def display_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])


# test_board = ['#','X','O','X','O','X','O','X','O','X']
test_board = [' ']*10

display_board(test_board)
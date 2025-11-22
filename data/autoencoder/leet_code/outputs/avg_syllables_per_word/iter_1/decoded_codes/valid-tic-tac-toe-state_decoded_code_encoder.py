def valid_tic_tac_toe(board):
    countX = sum(row.count('X') for row in board)
    countO = sum(row.count('O') for row in board)
    if countX < countO or countX > countO + 1:
        return False

    def check_win(p):
        return (
            any(row == p*3 for row in board) or
            any(all(board[r][c] == p for r in range(3)) for c in range(3)) or
            (board[0][0] == board[1][1] == board[2][2] == p) or
            (board[0][2] == board[1][1] == board[2][0] == p)
        )

    winX = check_win('X')
    winO = check_win('O')
    if winX and winO:
        return False
    if winX and countX == countO:
        return False
    if winO and countX != countO:
        return False
    return True
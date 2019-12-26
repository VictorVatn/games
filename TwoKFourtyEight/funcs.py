def down(board):
    for i in range(4):
        for k in range(3):
            for j in range(3):
                if board[j][i] != 0 and board[j + 1][i] == 0:
                    board[j + 1][i] = board[j][i]
                    board[j][i] = 0
    for i in range(4):
        if board[3][i] == board[2][i]:
            board[3][i] *= 2
            board[2][i] = board[1][i]
            board[1][i] = board[0][i]
            board[0][i] = 0
            if board[1][i] == board[2][i]:
                board[2][i] *= 2
                board[1][i] = 0
        elif board[1][i] == board[2][i]:
            board[2][i] *= 2
            board[1][i] = board[0][i]
            board[0][i] = 0
        elif board[0][i] == board[1][i]:
            board[1][i] *= 2
            board[0][i] = 0
    return board


def right(board):
    for i in range(4):
        for k in range(3):
            for j in range(3):
                if board[i][j] != 0 and board[i][j + 1] == 0:
                    board[i][j + 1] = board[i][j]
                    board[i][j] = 0
    for i in range(4):
        if board[i][3] == board[i][2]:
            board[i][3] *= 2
            board[i][2] = board[i][1]
            board[i][1] = board[i][0]
            board[i][0] = 0
            if board[i][1] == board[i][2]:
                board[i][2] *= 2
                board[i][1] = 0
        elif board[i][1] == board[i][2]:
            board[i][2] *= 2
            board[i][1] = board[i][0]
            board[i][0] = 0
        elif board[i][0] == board[i][1]:
            board[i][1] *= 2
            board[i][0] = 0
    return board


def up(board):
    board = board[::-1][:]
    down(board)
    board = board[::-1][:]
    return board


def left(board):
    board[0] = board[0][::-1]
    board[1] = board[1][::-1]
    board[2] = board[2][::-1]
    board[3] = board[3][::-1]
    right(board)
    board[0] = board[0][::-1]
    board[1] = board[1][::-1]
    board[2] = board[2][::-1]
    board[3] = board[3][::-1]
    return board


def game_over(board):
    a = 0
    for k in range(4):
        test_board = []
        for i in range(4):
            test_board.append(board[i])
        if k == 0:
            if down(test_board) == board:
                a += 1
        if k == 1:
            if up(test_board) == board:
                a += 1
        if k == 0:
            if right(test_board) == board:
                a += 1
        if k == 0:
            if left(test_board) == board:
                a += 1
    if a == 4:
        return True
    else:
        return False
def valid_solution(board):
    for i in board:
        x = set(i)
        if (0 in x) or len(x) != 9:
            return False

    trans = [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]
    for j in trans:
        x = set(j)
        if len(x) != 9:
            return False

    n1, n2, n3 = [], [], []

    for j in range(0, 7, 3):
        for i in range(3):
            n1 += board[j + i][:3]
            n2 += board[j + i][3:6]
            n3 += board[j + i][6:]

        for x in n1, n2, n3:
            z = set(x)
            if (0 in z) or len(z) != 9:
                return False
        n1, n2, n3 = [], [], []
    return True

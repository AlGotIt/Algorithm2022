def solution(n):
    board = [[0] * n for _ in range(n)]
    answer = []
    x, y, num = -1, 0, 1

    for i in range(n):
        for _ in range(i, n):

            if i % 3 == 0:
                x += 1

            elif i % 3 == 1:
                y += 1

            elif i % 3 == 2:
                x -= 1
                y -= 1

            board[x][y] = num
            num += 1

    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:
                answer.append(board[i][j])
                
    return answer

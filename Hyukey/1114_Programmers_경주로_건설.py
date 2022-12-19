# python 3.10

import sys

def solution(board):
    """
    Args:
        board : 도면의 상태(0은 비어 있음, 1은 벽)을 나타내는 2차원 배열
    Returns:
        경주로를 건설하는데 필요한 최소 비용
    """
    global answer
    answer = sys.maxsize
    dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]  # 4가지 방향

    board_size = len(board)

    visited = [[False] * len(row) for row in board] # 방문 여부
    min_prices = [[sys.maxsize] * len(row) for row in board] # 각 블럭마다의 최소 건설 비용
    visited[0][0] = True

    # 백트래킹
    def dfs(cur_y, cur_x, price, dir):
        global answer

        # 가지치기
        if price > min_prices[cur_y][cur_x]: # 기존 블럭에 있던 비용보다 큰 경우 return 
            return
        else:
            min_prices[cur_y][cur_x] = price # 기존 블럭 비용 갱신

        # 목적지인가
        if cur_y == board_size - 1 and cur_x == board_size - 1:
            answer = min(answer, price)
            return
        
        # 연결된 곳 순회
        for i in range(4):
            ty = cur_y + dy[i]
            tx = cur_x + dx[i]
            # 갈 수 있는가
            if 0 <= ty < board_size and 0 <= tx < board_size and board[ty][tx] == 0 and not visited[ty][tx]:
                # 체크인
                visited[ty][tx] = True
                # 간다
                if dir == i or dir == -1:
                    dfs(ty, tx, price+100, i)
                else:
                    dfs(ty, tx, price+600, i)
                # 체크아웃
                visited[ty][tx] = False

    dfs(0, 0, 0, -1)

    return answer

board = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
print(solution(board))
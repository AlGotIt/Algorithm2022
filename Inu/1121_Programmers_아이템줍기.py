# python 3.8

def solution(rectangle, characterX, characterY, itemX, itemY) -> int:
    """
    겹쳐있는 사각형들의 테두리를 따라 움직일 때 목표 지점까지의 최단거리를 탐색

    Args:
        rectangle (list): 사각형의 x min, y min, x max, y max
        characterX (int): 현재 위치의 x 좌표
        characterY (int): 현재 위치의 y 좌표
        itemX (int): 목표 위치의 x 좌표
        itemY (int): 목표 위치의 y 좌표

    Returns:
        answer (int): 최단거리
    """
    # 사각형이 그려진 보드
    ground = [[-1 for j in range(102)] for i in range(102)]
    # 방문한 노드까지의 거리 저장
    visited = [[1 for j in range(102)] for i in range(102)]
    
    # 테두리가 한 칸 간격으로 있을 때 의도한 최단거리를 계산하지 못할 수 있으므로 
    # 좌표를 두 배로 늘려서 점간 간격을 넓힘
    for xmin, ymin, xmax, ymax in rectangle:
        for i in range(2 * xmin, 2 * xmax + 1):
            for j in range(2 * ymin, 2 * ymax + 1):
                # 사각형 내부에 포함되는 경우 0
                if xmin * 2 < i < xmax * 2 and ymin * 2 < j < ymax * 2:
                    ground[i][j] = 0
                # 테두리 1
                elif ground[i][j] != 0:
                    ground[i][j] = 1

    answer = 0
    # bfs를 진행할 방향
    direction_x = [-1, 0, 1, 0] # left, up, right, down
    direction_y = [0, 1, 0, -1]

    # 올바른 답을 만날 때까지 캐릭터 위치를 저장할 Q
    q = []
    q.append([characterX * 2, characterY * 2])
    while q:
        x, y = q.pop(0)
        # 정답인 경우
        if x == itemX * 2 and y == itemY * 2:
            answer = visited[x][y] // 2
            break
        # 네 방향으로 탐색
        for dir in range(4):
            # 좌표 이동
            new_x = x + direction_x[dir]
            new_y = y + direction_y[dir]
            # 테두리이고 방문하지 않은 경우
            if ground[new_x][new_y] == 1 and visited[new_x][new_y] == 1:
                q.append([new_x, new_y])
                # 거리 업데이트
                visited[new_x][new_y] = visited[x][y] + 1
    return answer

S = solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8)
print(S)
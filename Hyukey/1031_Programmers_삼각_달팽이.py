# 움직이는 방향 정의
dy, dx = [0, 1, -1], [1, 0, -1]

def solution(n):
    answer = []

    # 2차원 배열로 선언
    snail = [[0] * (i+1) for i in range(n)]

    # 현재 이동해야할 거리 
    move_cnt = n
    # 현재 위치
    cur_y, cur_x = 0, -1
    # 현재 이동 방향
    cur_d = 0
    # 현재 숫자
    cur_num = 1

    # 이동해야할 거리가 0 초과인 경우 반복
    while move_cnt > 0:
        # 이동
        for _ in range(move_cnt):
            cur_y += dy[cur_d]
            cur_x += dx[cur_d]
            snail[cur_x][cur_y] = cur_num
            cur_num += 1

        # 이동 거리 감소
        move_cnt -= 1
        # 이동 방향 변화
        if cur_d < 2:
            cur_d +=1
        else:
            cur_d = 0

    # 1차원 배열로 입력
    for i in range(n):
        for item in snail[i]:
            answer.append(item)

    return answer

n = 6
print(solution(n))
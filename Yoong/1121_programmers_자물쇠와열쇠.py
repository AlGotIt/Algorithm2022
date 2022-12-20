# https://school.programmers.co.kr/learn/courses/30/lessons/60059

def rotate(array, d):
    n = len(array)  # 배열의 길이
    result = [[0] * n for _ in range(n)]

    if d % 4 == 1: # 90도
        for r in range(n):
            for c in range(n):
                result[c][n - r - 1] = array[r][c]
    elif d % 4 == 2: # 180도
        for r in range(n):
            for c in range(n):
                result[n - r - 1][n - c - 1] = array[r][c]
    elif d % 4 == 3: # 270도
        for r in range(n):
            for c in range(n):
                result[n - c - 1][r] = array[r][c]
    else: # 360도
        for r in range(n):
            for c in range(n):
                result[r][c] = array[r][c]
    return result

# 자물쇠 NxN 부분이 모두 1인지 확인 (1 이면 열쇠로 자물쇠를 열 수 있음 )
def final_check(new_lock):
    n = len(new_lock)
    for r in range(n, n * 2):
        for c in range(n, n * 2):
            if new_lock[r][c] != 1:
                return False
    return True

def solution(key, lock):
    len_key = len(key) # m
    len_lock = len(lock) # n

    # 기존 자물쇠보다 3배 큰 자물쇠
    newLock = [[0] * (len_lock * 3) for _ in range(len_lock * 3)]
    # 새로운 자물쇠의 가장 중앙 부분에 기존 자물쇠 넣기
    for r in range(len_lock):
        for c in range(len_lock):
            newLock[len_lock+r][len_lock+c] = lock[r][c]
    
    # 열쇠로 자물쇠 돌아다니면서 확인
    for r in range(1, len_lock*2):
        for c in range(1, len_lock*2):
            # 열쇠 0, 90, 180, 270 만큼 회전시키면서 확인
            for d in range(4):
                rotate_key = rotate(key, d) # 열쇠를 d만큼 회전시킨 리스트
                for x in range(len_key):
                    for y in range(len_key):
                        newLock[r + x][c + y] += rotate_key[x][y]
                
                if final_check(newLock): # 자물쇠와 열쇠가 맞으면
                    return True # 정답
                # 자물쇠와 열쇠가 안맞으면 이동한 만큼 다시 제자리로
                for x in range(len_key):
                    for y in range(len_key):
                        newLock[r + x][c + y] -= rotate_key[x][y]
    return False
    
key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]             
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))
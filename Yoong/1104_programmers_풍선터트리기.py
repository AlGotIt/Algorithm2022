# https://school.programmers.co.kr/learn/courses/30/lessons/68646

# 해당 풍선이 자신기준 왼쪽풍선들의 최솟값과 오른쪽풍선들의 최솟값 보다 크지 않으면(작으면) 살아남을 수 있음. -> 크면 살아남을 수 없음.
# 작은거 한번만 터트릴 수 있기 때문임
# mL mR B 세개만 남아있는 상황에서 mL과 mR중 큰거 터트리고 
# 남은 한개의 풍선과 B 자신의 풍선을 터트려야하는 상황일 때 자신보다 작은 남은 한개의 풍선을 터트림. (작은 풍선 터트릴 수 있는 단 한번의 기회를 이때 쓰는거임.)

def solution(a):
    result = [False for _ in a]         # 터트린 풍선 체크 배열
    mL, mR = float("inf"), float("inf") # mL : 자신 기준 왼쪽 풍선들 중 최솟값, mR : 자신 기준 오른쪽 풍선들 중 최솟값
    for i in range(len(a)):
        if a[i] < mL:                   # 자신 기준 왼쪽 풍선들에서 최솟값찾기
            # print('a[i] = ',a[i])
            mL = a[i]
            result[i] = True
        if a[-1-i] < mR:                # 자신 기준 오른쪽 풍선들에서 최솟값찾기
            # print('a[-1-i] = ',a[-1-i])
            mR = a[-1-i]
            result[-1-i] = True
    # print(result)
    return sum(result)

# a = [-16,27,65,-2,58,-92,-71,-68,-61,-33]
# print(solution(a))
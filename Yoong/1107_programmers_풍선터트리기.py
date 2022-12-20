# https://school.programmers.co.kr/learn/courses/30/lessons/68646

# 해당 풍선이 자신기준 왼쪽풍선들의 최솟값과 오른쪽풍선들의 최솟값 보다 크지 않으면(작으면) 살아남을 수 있음. -> 크면 살아남을 수 없음.
# 작은거 한번만 터트릴 수 있기 때문임

# mL B mR
# 10 5 9 가능 (B이 양쪽보다 작을때)
# 10 9 5 가능 (B가 둘중 하나보다 작을때)
# 5 10 9 불가능 (B가 양쪽보다 클때)

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
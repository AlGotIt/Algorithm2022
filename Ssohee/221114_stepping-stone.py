# https://school.programmers.co.kr/learn/courses/30/lessons/64062
# 프로그래머스 Lv3. 징검다리 건너기

import sys

def solution(stones, k):
    answer = 0  # 리턴
    n = len(stones)
    while(1):
        answer += 1
        for i in range(n):
            if stones[i] != 0:  # 이 디딤돌을 건널 수 있으면 !
                stones[i] -= 1  # 건너고 -1
            else:   # stones[i] == 0 건널 수 없으면
                continue
        zero = 0 # 건널 수 없는 디딤돌의 개수
        for i in stones:
            if i == 0:  #건널 수 없는 디딤돌이 있다면
                zero += 1
                if zero == k:   # 최대로 지나갈 수 있는 K
                    return answer

stones = sys.stdin.readlines()
k = input()
print(solution)
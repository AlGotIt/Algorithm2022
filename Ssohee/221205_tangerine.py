# https://school.programmers.co.kr/learn/courses/30/lessons/138476
# 프로그래머스 Lv2. 귤 고르기

def solution(k, tangerine):
    answer = 0
    t = {}
    for i in tangerine: # 튜플 만들기
        if t.get(i) : 
            t[i] += 1
        else : 
            t[i]=1
    t = sorted(t.items(), key = lambda item : item[1], reverse = True)  # value 값 내림차순 정렬
    s = 0
    for i in range(len(t)):
        s += t[i][1]    # 귤 개수가 많은 것부터 담기
        if s >= k:  # k만큼 채워졌을 때
            return len(t[:i+1]) # 담겨진 종류의 개수를 리턴

k, t = 2, [1, 1, 1, 1, 2, 2, 2, 3]
print(solution(k, t))

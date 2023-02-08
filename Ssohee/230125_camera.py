# https://school.programmers.co.kr/learn/courses/30/lessons/42884
# 프로그래머스 Lv3. 단속카메라

def solution(routes):
    answer = 0
    flag = -30001
    routes.sort(key=lambda x : x[1])  

    for route in routes:
        if flag < route[0]:
            answer +=1
            flag = route[1]
    return answer
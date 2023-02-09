# https://school.programmers.co.kr/learn/courses/30/lessons/42884
# 프로그래머스 Lv3. 단속카메라

def solution(routes):
    answer = 0
    flag = -30001 
    routes.sort(key=lambda x : x[1]) # 진출시점 기준으로 오름차순 정렬
    for route in routes:
        if flag < route[0]: #새로운 자동차의 진입 시점보다 카메라가 앞에 있다면
            answer +=1  #새로 카메라를 달아줌
            flag = route[1] #그 자동차의 나가는 시점에 flag를 달아준다
    return answer
    
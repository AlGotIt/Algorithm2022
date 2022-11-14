# https://school.programmers.co.kr/learn/courses/30/lessons/42884

def solution(routes):
    B = sorted(routes, key = lambda x: x[1], reverse=False) # 나간 지점을 기준으로 오름차순으로 정렬

    k = 0
    cnt = 1                                                 # 처음 나간 차량의 나간 지점에 하나 설치 먼저함.
    for i in range(1,len(B)):                               # 두번째 차량부터 마지막 번째 차량까지 반복문 실행
        if B[i][0] > B[k][1]:                               # 다음 차량이 들어온 지점과 카메라가 설치되어 있는 지점을 비교
            cnt += 1                                        # 카메라가 설치된 지점보다 다음 차량의 들어온 시간이 늦으면 카메라 설치
            k = i                                           # 카메라 지점을 다음 차량의 나간 지점으로 업데이트함.
    # return B, cnt
    return cnt


routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
# routes = [[7,7],[3,4],[0,10],[2,5],[3,5]]
print(solution(routes))
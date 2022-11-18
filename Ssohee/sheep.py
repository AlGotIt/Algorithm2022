# https://school.programmers.co.kr/learn/courses/30/lessons/92343
# 프로그래머스 Lv3. 양과 늑대
import sys

def solution(s, w):  #sheep, wolf
    global result
    if s > w:   # 양의 수가 늑대의 수보다 많으면
        li.append(s)
    else:   # 더이상 내려갈 노드가 없으면 리턴!
        return
    for p, c in edges:
        if visited[p] == 1 and visited[c] == 0: #부모는 방문인데 자식은 방문이 아닐 때
            visited[c] = 1 # 자식노드 방문
            if info[c] == 0:    # 자식노드가 양이면
                solution(s+1, w)
            else:   # 자식노드가 늑대면
                solution(s, w+1)
            visited[c] = 0

info = sys.stdin.readlines()
edges = sys.stdin.readlines()
result = 0
visited = [[0] * len(info)]   # 방문 했는지 안했는지 확인을 위함
visited[0] = 1  # 루트 노드 방문
li = [] #양을 수집한 횟수를 저장하는 리스트
solution(1, 0)   #항상 루트는 양이기 때문에 s=1로 시작
print(max(li))  #가장 많은 횟수의 양을 출력 횟수의 양을 출력

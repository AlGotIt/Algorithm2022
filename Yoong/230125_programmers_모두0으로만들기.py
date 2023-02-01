# https://school.programmers.co.kr/learn/courses/30/lessons/76503

'''
가중치의 총합이 0일 경우에 모든 가중치를 0으로 만드는 것이 가능하지만
총합이 0이 아닐경우에는 모든 가중치를 0으로 만드는 것이 불가능.
'''
'''
파이썬의 기본 재귀 깊이 제한은 1000으로 굉장히 적다.
그러므로 파이썬으로 알고리즘 문제를 풀 때 재귀를 사용한다면 
반드시 sys.setrecursionlimit() 함수를 통해서 재귀 깊이를 크게 잡아야한다.
'''
import sys
sys.setrecursionlimit(300000) # 재귀 -> 런타임 에러 방지

answer = 0
def solution(a, edges):
    if sum(a) != 0:
        return -1

    graph = [[] for _ in range(len(a))]
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    print("graph: ", graph)
    # 재귀함수를 통한 dfs 구현
    def dfs(curr, parent):
        global answer
        # 루트노드에서 리프노드 까지 dfs를 호출하여 리프노드부터 값 계산
        for next in graph[curr]:
            if next != parent:
                dfs(next, curr)
        a[parent] += a[curr] # 가중치를 받은 만큼 +
        # a[curr] -= a[curr] # 가중치를 준 만큼 -
        answer += abs(a[curr]) # 절댓값 가중치 값을 더해 나감
    dfs(0,0)
    return answer

# a = [0,1,0]
# edges = [[0,1],[1,2]]
a = [-5,0,2,1,2]
edges = [[0,1],[3,4],[2,3],[0,3]]
print(solution(a, edges))



# python 3.9

import heapq

def solution(n, s, a, b, fares) -> int:
    """


    Args:
        n (int): node 개수
        s (int): 시작 노드
        a (int): a의 목적지
        b (int): b의 목적지
        fares (list): 노드 간의 요금

    Returns:
        int: 최소 금액
    """

    # dijkstra algorithm
    def dijkstra(start):
        res = [float('INF') for _ in range(n+1)]
        res[start] = 0
        q = []
        heapq.heappush(q, (res[start], start))

        while q:
            cur, cost = heapq.heappop(q)
            for u, w in graph[cost]:
                if res[u] > cur + w:
                    res[u] = cur + w
                    heapq.heappush(q, ([res[u], u]))
        return res
    
    answer = 200000001

    # 그래프 생성
    graph = [[] for _ in range(n+1)]
    for f, t, p in fares:               # fares = [[3, 4, 23]], etc.            
        graph[f].append((t, p))
        graph[t].append((f, p))
    
    payment = [[]]

    # 최단거리 갱신, 각 노드에 대해 전부 실행
    for i in range(1, n+1): 
        payment.append(dijkstra(i))

    # 최소 비용 검색
    for node in range(1, n+1):
        answer = min(answer, payment[s][node] + payment[node][a] + payment[node][b])
    print(answer)
    return answer


n = 6	
s = 4	
a = 6	
b = 2	
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

solution(n, s, a, b, fares)
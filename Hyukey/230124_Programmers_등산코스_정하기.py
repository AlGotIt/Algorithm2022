# python 3.10
from collections import defaultdict
import heapq

def solution(n, paths, gates, summits):
    """
    Args:
        n : XX산의 지점 수
        paths : 각 등산로의 정보를 담은 2차원 정수 배열
        gates : 출입구들의 번호가 담긴 정수 배열
        summits : 산봉우리들의 번호가 담긴 정수 배열

    Returns:
        intensity가 최소가 되는 등산코스에 포함된 산봉우리 번호와 intensity의 최솟값을 차례대로 담긴 정수 배열
    """
    summits = set(summits) ## 중요!! 해시 테이블로 탐색 시간 감소
    answer = []
    adj = defaultdict(list)

    # 인접리스트로 그래프 구축
    for start, end, weight in paths:
        adj[start].append((end, weight))
        adj[end].append((start, weight))

    # 모든 지점으로 가는 최소 intensity
    dp = [10000001] * (n+1)
        
    def dijkstra(start):
        dp[start] = 0
        hq = [(0, start)]

        while hq:
            # 큐에서 꺼낸다
            intens, cur = heapq.heappop(hq) # 현 위치까지 오는 최소 intensity, 현재 위치

            # intensity가 기존보다 클 경우 패스
            if intens > dp[cur]:
                continue

            # 연결된 곳 순회
            for t, w in adj[cur]:
                nextIntens = max(intens, w)
                # 갈 수 있는가
                if dp[t] > nextIntens:
                    dp[t] = nextIntens
                    # 산봉우리가 아닌 경우에 이동
                    if t not in summits:
                        # 큐에 넣는다
                        heapq.heappush(hq, (dp[t], t))
    
    for gate in gates:
        dijkstra(gate)

    answer = [0, 10000001]
    for summit in sorted(summits): ## 번호가 낮은 순서대로 먼저 체크
        if dp[summit] < answer[1]:
            answer = [summit, dp[summit]]

    return answer

n = 7
paths = [[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]]
gates = [1, 2]
summits = [5]

print(solution(n, paths, gates, summits))
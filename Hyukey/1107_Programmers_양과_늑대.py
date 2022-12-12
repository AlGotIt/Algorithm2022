# python 3.10

def solution(info, edges):
    """
    Args:
        info : 각 노드에 있는 양 또는 늑대에 대한 정보가 담긴 배열
        edges : 2진 트리의 각 노드들의 연결 관계를 담은 2차원 배열

    Returns:
        문제에 제시된 조건에 따라 각 노드를 방문하면서 모을 수 있는 양
    """

    # 전역적으로 활용할 수 있는 변수로 선언
    global answer

    answer = 1

    # 인접 리스트로 구현
    adj = [[] for _ in range(len(info))]

    for x, y in edges:
        adj[x].append(y)

    # 백트래킹
    def dfs(index, nextIdxs, sheep, wolf):
        global answer

        # 1. 체크인
        if info[index] == 0:
            sheep += 1 # 양 추가
        else:
            wolf += 1 # 늑대 추가

        answer = max(answer, sheep)

        # 2. 목적지인가
        if sheep <= wolf:
            return

        # 3. 연결된 곳 순회
        for idx in nextIdxs:
            newNext = nextIdxs[:] # 다시 갈 수 있는 다음 인덱스 주소들 복사
            newNext.remove(idx) # 현재 인덱스 제외
            newNext.extend(adj[idx]) # 현재에서 추가로 갈 수 있는 인덱스 주소들 복사
            # 4. 간다
            dfs(idx, newNext, sheep, wolf)

    dfs(0, adj[0], 0, 0)

    return answer

info = [0,1,0,1,1,0,1,0,0,1,0]
edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]
print(solution(info, edges))
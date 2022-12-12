import Foundation

var answer = 1
var adj = [[Int]]()

func dfs(index: Int, nextIdxs: [Int], sheep: Int, wolf: Int, info: [Int]) {
    // 함수 내에서만 활용 될 임시 변수
    var tmpSheep = sheep
    var tmpWolf = wolf
    
    // 1. 체크인
    if info[index] == 0 {
        tmpSheep += 1
    } else {
        tmpWolf += 1
    }
    
    answer = max(answer, tmpSheep)
    
    // 2. 목적지인가
    if tmpSheep <= tmpWolf {
        return
    }
    
    // 3. 연결된 곳 순회
    for idx in nextIdxs {
        var newNext = nextIdxs // 다시 갈 수 있는 다음 인덱스 주소들 복사
        newNext = newNext.filter { $0 != idx } // 현재 제외
        newNext.append(contentsOf: adj[idx]) // 현재에서 추가로 갈 수 있는 인덱스 주소들 복사
        // 4. 간다
        dfs(index: idx, nextIdxs: newNext, sheep: tmpSheep, wolf: tmpWolf, info: info)
    }
}

func solution(_ info:[Int], _ edges:[[Int]]) -> Int {
    /*
     Args:
        info : 각 노드에 있는 양 또는 늑대에 대한 정보가 담긴 배열
        edges : 2진 트리의 각 노드들의 연결 관계를 담은 2차원 배열
     
     Returns:
        문제에 제시된 조건에 따라 각 노드를 방문하면서 모을 수 있는 양
    */
    
    // 인접 리스트로 구현
    adj = Array(repeating: [], count: info.count)
    for edge in edges {
        adj[edge[0]].append(edge[1])
    }
    
    // 백트래킹
    dfs(index: 0, nextIdxs: adj[0], sheep: 0, wolf: 0, info: info)
    
    return answer
}

let info = [0,1,0,1,1,0,1,0,0,1,0]
let edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]
print(solution(info, edges))
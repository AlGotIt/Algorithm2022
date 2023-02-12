# python 3.10
from collections import deque

def solution(begin, target, words):
    """
    Args:
        begin : 단어
        target : 단어 
        words : 단어의 집합
    Returns:
        몇 단계의 과정을 거쳐 begin을 target으로 변환할 수 있는지 최솟값
    """
    answer = 0

    if target not in words: # 타겟이 words에 없는 경우 실패 
        return 0

    def diff(str1, str2): # 차이나는 개수를 반환하는 함수
        cnt = 0
        for i in range(len(str1)):
            if str1[i]!=str2[i]:
                cnt+=1
        return cnt

    q = deque()
    q.append((begin, 0))
    visit = [False] * (len(words))

    while q:
        # 큐에서 꺼낸다
        cur, cnt = q.popleft()

        # 목적지인가
        if cur == target:
            answer = cnt

        # 연결된 곳 순회
        for i, w in enumerate(words):
            # 갈 수 있는가
            if diff(cur, w)==1 and not visit[i]:
                visit[i] = True
                # 큐에 넣는다
                q.append((w, cnt+1))

    return answer
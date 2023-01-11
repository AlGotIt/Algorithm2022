# python 3.10

import operator

def solution(orders, course):
    """
    Args:
        orders : 각 손님들이 주문한 단품메뉴들이 문자열 형식으로 담긴 배열
        course : "스카피"가 추가하고 싶어하는 코스요리를 구성하는 단품메뉴들의 갯수가 담긴 배열
    Returns:
        "스카피"가 새로 추가하게 될 코스요리의 메뉴 구성을 담은 문자열 형태의 배열
    """
    answer = []
    cand = {} # 만들 수 있는 코스 후보 딕셔너리

    def dfs(word, idx, cnt, des, ans):
        # 목적지인가
        if(cnt == des): # 후보 코스 추가
            if(ans in cand):
                cand[ans] += 1
            else:
                cand[ans] = 1
            return

        # 연결된 곳 순회
        for i in range(idx, len(word)):
            # 갈 수 있는가    
            # 간다
            dfs(word, i+1, cnt+1, des, ans+word[i])

    for word in orders:
        word = sorted(word)
        for c in course:
            dfs(word, 0, 0, c, "")

    cand = sorted(cand.items(), key=operator.itemgetter(1), reverse=True) # value 기준으로 내림차순 정렬

    for c in course:
        maxNum = 2 # 최소 2번 이상 주문한 건
        maxList = []
        for k, v in cand:
            if len(k)==c:
                if v == maxNum:
                    maxList.append(k)
                elif v > maxNum:
                    maxNum = v
                    maxList.clear()
                    maxList.append(k)
        answer += maxList

    answer = sorted(answer)
    return answer
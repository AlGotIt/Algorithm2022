from itertools import combinations
from collections import Counter

def solution(orders:list, course:list) -> list:
    """
    Return available course compositions

    Args:
        orders (list): single menu order list
        course (list): menu number list in each course

    Returns:
        list: available course compositions
    """
    rough = []                                              # temporary list
    for c in course:                                        # course menu number list
        o_list = []
        for o in orders:                                    # ordered menu = o
            o_l = list(combinations(o, c))                  # menu로 가능한 조합 전체
            o_list += [tuple(sorted(ol)) for ol in o_l]     # 조합을 오름차순으로 정렬하여 o_list에 append
        if len(o_list) != 0:                                # 조합이 불가능하지 않으면
            o_D = Counter(o_list)               
            l = [key                                        # 각 조합의 개수를 샌 뒤 max값과 같고 2보다 큰 key만 l에 append
                 for m in [max(o_D.values())] 
                 for key,val in o_D.items()                 
                 if val == m and val >= 2]
            rough += l                                      # rough에 l 추가
    answer = []
    for r in rough:                                         # rough에 담긴 튜플을 string으로 변환해 answer에 넣고 정렬
        temp = ''
        for t in r:
            temp += t
        answer.append(temp)
    answer = sorted(answer)
    return answer

order = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2, 3, 4]
# order = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
# course = [2,3,5]
# order = ["XYZ", "XWY", "WXA"]
# course = [2, 3, 4]
print(solution(order, course))
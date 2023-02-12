# python 3.10

def solution(scores):
    """
    Args:
        scores : 각 사원의 근무 태도 점수와 동료 평가 점수 목록
    Returns:
        완호의 석차
    """
    re_arr = []
    for idx, score in enumerate(scores):
        re_arr.append((idx, score[0], score[1])) # 인덱스, 근무태도, 동료평가

    re_arr.sort(key=lambda x: (x[1], -x[2]), reverse=True) # 근무 태도는 내림차순, 동료 평가는 오름차순

    rank = []
    _, cur_att, cur_eval = re_arr[0] # 비교할 점수 저장
    for idx, att, eval in re_arr:
        if cur_att > att and cur_eval > eval: # 두 점수가 모두 작은 경우
            if idx == 0: # 완호일 경우
                return -1
        else:
            rank.append((idx, att+eval))
            cur_att = att
            cur_eval = eval

    rank.sort(key=lambda x:x[1], reverse=True) # 합산으로 정렬

    for num, (idx, _) in enumerate(rank):
        if idx == 0:
            return num+1
    return -1


scores = [[2,2],[1,4],[3,2],[3,2],[2,1]]
print(solution(scores))
# python 3.10

def solution(msg):
    """
    Args:
        msg : 입력으로 영문 대문자로만 이뤄진 문자열
    Returns:
        주어진 문자열을 압축한 후의 사전 색인 번호가 담긴 배열
    """
    dic = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    answer = []

    idx = 0
    while idx < len(msg):
        w = msg[idx] # 현재 글자
        while idx+1 < len(msg) and w+msg[idx+1] in dic: # 다음 글자를 더했을때 사전에 있을 경우 글자 증가
            idx+=1
            w += msg[idx]
        answer.append(dic.index(w)+1)
        idx+=1
        if idx < len(msg):
            c = msg[idx] # 다음 글자
            dic.append(w+c) # 다음 글자와 합친 글자를 사전에 추가

    return answer

msg = "TOBEORNOTTOBEORTOBEORNOT"
print(solution(msg))
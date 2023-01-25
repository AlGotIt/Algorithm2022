# python 3.9

def solution(msg) -> list:
    """
    문자열 압축
    A~Z 사이의 문자가 사전 등록되어있고, 문자열을 앞에서부터 검토하며 사전에 있는 가장 긴 문자열의 색인번호를
    출력하고, 다음 문자까지를 사전에 새로 등록한다.

    Args:
        msg (string): 입력 문자열

    Returns:
        answer(list): 색인번호 리스트
    """
    answer = []                     # 색인 번호 리스트 
    dic = dict()
    index = 1
    for c in range(65, 91):         # A~Z 사전 생성
        dic[chr(c)] = index
        index += 1
    
    s, e = 0, 1                     # 문자열 내 인덱스 start / end
    
    while e < len(msg) + 1:
        word = msg[s:e]
        if word in dic:             # 현재 문자열 슬라이스가 사전에 있는 경우 다음 문자 검사
            e += 1
        else:                       # 현재 문자열 슬라이스가 사전에 없는 경우 
            answer.append(dic[word[:-1]])   # 앞 문자까지의 색인번호를 answer에 추가
            dic[word] = index               # 사전에 새 문자열 추가
            index += 1
            s = e - 1
    answer.append(dic[word])                # 마지막 문자열의 색인번호를 answer에 추가
    return answer
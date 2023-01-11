# python 3.10

from collections import Counter

def solution(topping):
    """
    Args:
        topping : 롤케이크에 올려진 토핑들의 번호를 저장한 정수 배열
    Returns:
        롤케이크를 공평하게 자르는 방법의 수
    """
    answer = 0

    dic = Counter(topping) # 모든 토핑의 카운트를 기록
    bro = set() # 동생이 가져간 토핑의 종류

    for top in topping:
        bro.add(top) # 동생에게 토핑 하나를 줌
        dic[top] -= 1

        if dic[top] == 0: # 철수의 토핑 종류 하나가 사라지면 제거
            del dic[top]
        if len(bro) == len(dic): # 토핑 종류 개수가 같아졌을 때
            answer += 1
        if len(bro) > len(dic): # 토핑 종류가 동생이 더 많아진 경우
            break

    return answer

topping = [1, 2, 3, 1, 4]
print(solution(topping))
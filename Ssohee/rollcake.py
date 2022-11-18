# 프로그래머스 롤케이크 자르기
# https://school.programmers.co.kr/learn/courses/30/lessons/132265

from collections import Counter
import sys

def solution(topping):
    result = 0
    topping_dic = Counter(topping)  #토핑 종류별로 몇개씩 있는지 먼저 센다
    li = set()
    for i in topping:
        topping_dic[i] -= 1
        li.add(i)
        if topping_dic[i] == 0:
            topping_dic.pop(i)
        if len(li) == len(topping_dic): # 동일한 개수의 토핑을 가질 때 +1
            result += 1
        if len(li) > len(topping_dic):
            break
            # topping_dic에서 삭제된 값이 li에 추가되기 때문에 항상 topping_dic의 개수가 li의 개수 보다 많다.
            # 즉, li의 개수가 더 많을 때 탈출!
    return result

topping = sys.stdin.readlines()
#topping = list(map(int, input().split()))
solution(topping)

# 타임에러
# def solution(topping):
#     result = 0
#     for i in range(1, len(topping)):
#         a, b = topping[:i], topping[i:]
#         if len(set(a)) == len(set(b)):
#             result += 1
#     return result

#프로그래머스 

# def solution(topping):
#     result = 0
#     for i in range(1, len(topping)):
#         a, b = topping[:i], topping[i:]
#         if len(set(a)) == len(set(b)):
#             result += 1
#     return result

from collections import Counter

def solution(topping):
    result = 0
    topping_dic = Counter(topping)
    li = set()
    for i in topping:
        topping_dic[i] -= 1
        li.add(i)
        if topping_dic[i] == 0:
            topping_dic.pop(i)
        if len(li) == len(topping_dic):
            result += 1
    return result

topping = list(map(int, input().split()))
solution(topping)

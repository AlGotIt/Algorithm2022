# https://school.programmers.co.kr/learn/courses/30/lessons/42577
# 프로그래머스 Lv2. 전화번호 목록

def solution(phone_book):
    answer = True
    phone_book.sort()   #정렬하면 각 자리의 수가 적은 것 순으로 
    for i in range(len(phone_book)-2):
        if phone_book[i] in phone_book[i+1]:    #앞의 수가 바로 뒤에 포함되어 있으면!
            answer = False
            break
    return answer

phone_book = ["123","456","789"]
print(solution(phone_book))


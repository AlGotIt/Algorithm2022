# https://school.programmers.co.kr/learn/courses/30/lessons/42577
# 프로그래머스 Lv2. 전화번호 목록

def solution(phone_book):
    phone_book.sort() #정렬하면 각 자리의 수가 적은 것 순으로 
    for i in range(len(phone_book)-1):
        #if phone[i+1].startswith(phone[i]):    # yes
        n = len(phone_book[i])
        if phone_book[i+1][:n] == phone_book[i]:#앞의 수가 바로 뒤에 포함되어 있으면!
            return False
    return True

phone_book = ["123","456","789"]
print(solution(phone_book))

######### 오류코드 ############
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i] in phone_book[i+1]: # 접두어가 아닌 중간에 존재하거나~~ 등의 예외가 포함되었을 때 오류가 발생!
            return False
    return True
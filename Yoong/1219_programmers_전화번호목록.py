# https://school.programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i + 1][:len(phone_book[i])] == phone_book[i]:
            return False
    return True

phone_book = ["119", "97674223", "21195524421"]
# ['119', '1195524421', '97674223']
print(solution(phone_book))

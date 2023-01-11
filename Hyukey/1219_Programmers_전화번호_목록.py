# python 3.10

def solution(phone_book):
    """
    Args:
        phone_book : 전화번호부에 적힌 전화번호를 담은 배열 
    Returns:
        어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true
    """
    answer = True

    phone_book.sort() # 정렬을 통해 앞 문자열이 같은것끼리 묶을 수 있음

    for i in range(len(phone_book)-1):
        if phone_book[i+1][:len(phone_book[i])] == phone_book[i]: # 다음 인덱스의 앞 문자열이 현재 인덱스의 문자열과 같으면 False
            return False

    return answer
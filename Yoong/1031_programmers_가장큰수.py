def solution(numbers):
    numbers = list(map(str, numbers)) # map을 사용해서 str로 변환 후 list로 변경
    numbers.sort(key=lambda x: x * 3, reverse=True) # key 조건에 맞게 sort // x*3 : 인자 각각의 문자열을 세번씩 반복 (numbers의 원소는 1000이하의 숫자임. 3자리수로 통일 후 비교위함.)
    return str(int(''.join(numbers))) # 모든 값이 0일때 '000'으로 처리하기 위함.

num_list = list(input().split()) # int형 list 입력받기
print(solution(num_list))


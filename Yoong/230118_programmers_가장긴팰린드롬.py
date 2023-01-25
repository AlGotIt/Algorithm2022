# https://school.programmers.co.kr/learn/courses/30/lessons/12904
'''
 0부터 N - 1 까지 의 문자열 이 가장 긴 문자열이다.
 즉, 0부터 N-1, N-2, N-3, ... , 0 까지,
 1부터 N-1, N-2, ... , 1 까지,
 N부터 N까지 이런 식으로 반복하며,

 각각의 문자열이 펠린드롬인지 확인
'''

def solution(s):
    answer = 0
    for i in range(len(s)): # 문자열 시작 인덱스
        for j in range(len(s), i, -1): # 문자열 끝 인덱스
            new = s[i:j] # i부터 j까지 새로운 문자열 생성 후 저장
            if new == new[::-1]: # 문자열을 뒤집었을때도 같으면
                answer = max(answer, len(new)) # 팰린드롬
    return answer

s = "abcdcba"
# s = "abacde"
print(solution(s))

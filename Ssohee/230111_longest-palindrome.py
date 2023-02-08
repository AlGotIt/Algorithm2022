# https://school.programmers.co.kr/learn/courses/30/lessons/12904
# 프로그래머스 Lv3. 가장 긴 팰린드롬

def is_palindrome(s, left, right):
    while((left >= 0) and (right < len(s))):
        if s[left] != s[right]:
            break
        left -=1
        right +=1
    return right -left -1

def solution(s):
    answer = 0
    for i in range(len(s)):
        odd = is_palindrome(s, i, i)    #ABABA
        even = is_palindrome(s, i-1, i) #ABBA
        answer = max(answer, max(odd, even))
    return answer

s = 'abcdcba'
print(solution(s))
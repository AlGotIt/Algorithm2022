# https://school.programmers.co.kr/learn/courses/30/lessons/43163
# 프로그래머스 Lv3. 단어 변환

from collections import deque

def is_word(a, b): # 한개의 알파벳만 다른지 체크하는 함수
    result = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            result +=1
    if result == 1:
        return True
    return False


def solution(begin, target, words):
    if target not in words:
        return 0
    
    queue = deque()
    queue.append([begin, []])   # queue변수에 다녀온 경로를 저장해줌
    while queue:
        start, box = queue.popleft()
        for word in words:
            if is_word(word, start) and word not in box:
                if word == target:  # 제일 먼저 target을 만난다면, 그것이 반드시 최소임
                    return len(box) + 1 # begin의 단어까지 +1 
                tmp = box[0:] 
                tmp.append(word)
                queue.append([word, tmp])
    return 0

words = ["hot", "dot", "dog", "lot", "log", "cog"]
begin = "hit"
target = "cog"	

print(solution(begin, target, words))
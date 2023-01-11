# https://school.programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    answer = [] # Stack
    for num in number:
        # k > 0이고 스택이 비어 있지 않고 스택 마지막 값 < num 이면
        while k > 0 and answer and answer[-1] < num:
            answer.pop() # 스택 마지막 값 pop
            k -= 1 # k 1 감소
        answer.append(num) # 스택에 num을 push

    # 처음부터 끝까지 다 돌았어도 k > 0 이상이면 스택에서 남은 k개 삭제 후 join해서 결과 값 반환 (number = 100000000, k = 3)
    return ''.join(answer[:len(answer)-k])

number = '4177252841'
k = 4
print(solution(number, k))
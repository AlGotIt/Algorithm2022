from collections import deque

def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    limit = (len(queue1)) * 4
    total1 = sum(queue1)
    total2 = sum(queue2)
    total = total1 + total2
    
    if total % 2 != 0:
        return -1
    
    while True:
        if total1 > total2:
            tmp = queue1.popleft()
            queue2.append(tmp)
            total1 -= tmp
            total2 += tmp
            answer += 1
        elif total1 < total2:
            tmp = queue2.popleft()
            queue1.append(tmp)
            total1 += tmp
            total2 -= tmp
            answer += 1
        else:
            break
        if answer == limit:
            answer = -1
            break
    return answer
# python 3.8

def solution(queue1:list, queue2:list) -> int:
    """
    Return minimum number of moving to make sum of both queue same

    Args:
        queue1 (list): queue1, length of queue1 is same with queue2
        queue2 (list): queue2, length of queue2 is same with queue1

    Returns:
        int: minimum number of moving. 
             if no answer, return -1
    """
    Q = queue1 + queue2                 # combine queues
    q1_sum = sum(queue1)                    
    q2_sum = sum(queue2)

    if(q1_sum + q2_sum) % 2 != 0:       # if sum of queue is odd-number, there is no answer
        return -1 

    q1_s = 0                            # queue1[0]
    q2_s = len(queue1)                  # queue2[0]
    
    answer = 0
    while True:
        if answer > len(Q) * 1.5:       # if loop for len(queue1) * 3, It considered every case. No answer
            return -1
        if q1_sum > q2_sum:             # sum of queue1 > queue2 = queue1.pop -> queue2
            q1_sum -= Q[q1_s]
            q2_sum += Q[q1_s]
            q1_s = (q1_s + 1) % len(Q)  # update index
            answer += 1
        elif q1_sum < q2_sum:           # sum of queue2 > queue1 = queue2.pop -> queue1
            q1_sum += Q[q2_s]
            q2_sum -= Q[q2_s]
            q2_s = (q2_s + 1) % len(Q)  # update index
            answer += 1
        else:
            break
    return answer


queue1 = list(map(int, input().split()))
queue2 = list(map(int, input().split()))

print(solution(queue1, queue2))


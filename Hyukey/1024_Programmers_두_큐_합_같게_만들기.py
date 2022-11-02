def solution(queue1, queue2):
    pointer1 = 0
    pointer2 = len(queue1)

    total_array = queue1 + queue2

    # 1. 반으로 안나눠지는 경우 에러 
    if sum(total_array) % 2 != 0:
        return -1

    target_sum = sum(total_array) // 2

    present_sum = sum(queue1)

    answer = 0

    # 2. 하나만 맞추면 나머지도 맞춰짐
    # 2-1. 부족하면 추가 넘치면 제거
    while present_sum != target_sum:
        # 포인터가 겹칠 경우 에러
        if pointer1 == pointer2:
            return -1
        # 최대 이동 구간이 넘을 경우 에러
        if answer > len(total_array) * 2:
            return -1

        if present_sum < target_sum:
            present_sum += total_array[pointer2]
            pointer2 += 1
            answer += 1
        else:
            present_sum -= total_array[pointer1]
            pointer1 += 1
            answer += 1

        if pointer1 == len(total_array):
            pointer1 = 0
        if pointer2 == len(total_array):
            pointer2 = 0

    return answer


queue1 = [30, 2, 5, 3, 6]
queue2 = [2, 1, 3, 4, 6]

print(solution(queue1, queue2))
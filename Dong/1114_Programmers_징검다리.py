def solution(stones, k):
    answer = 0
    left, right = 1, max(stones) #최소 1회는 건넘
    #ct는 stones의 원소에 mid를 제거했을 때 0이 나오는 횟수
    while left <= right:
        count = 0
        mid = (left+right) // 2
        for stone in stones:
            if(stone-mid)<=0:
                count += 1
            else:
                count = 0 #0이 연속적으로 나오지 않을 때 초기화
            if count >= k:
                break
        if count < k:
            left = mid + 1
        else:
            answer = mid
            right = mid - 1
    return answer
        
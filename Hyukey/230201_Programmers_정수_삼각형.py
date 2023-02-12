# python 3.10

def solution(triangle):
    """
    Args:
        triangle : 삼각형의 정보가 담긴 배열
    Returns:
        거쳐간 숫자의 최댓값
    """
    answer = 0

    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == len(triangle[i]) - 1:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

    for num in triangle[-1]:
        answer = max(answer, num)

    return answer

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))
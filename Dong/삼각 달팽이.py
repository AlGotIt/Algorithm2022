def solution(n):
    answer = []
    array = [[0] * n for _ in range(n)]
    x,y = 0,-1
    num = 1
    for i in range(n):
        for _ in range(i,n):
            if i % 3 == 0:
                y += 1
            elif i % 3 == 1:
                x += 1
            elif i % 3 == 2:
                x -= 1
                y -= 1
            array[y][x] = num
            num += 1
    
    for i in array:
        for j in i:
            if j != 0:
                answer.append(j)
    return answer
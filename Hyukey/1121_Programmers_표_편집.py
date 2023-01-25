# python 3.10

def solution(n, k, cmd):
    """
    Args:
        n : 처음 표의 행 개수를 나타내는 정수
        k : 처음에 선택된 행의 위치를 나타내는 정수
        cmd : 수행한 명령어들이 담긴 문자열 배열

    Returns:
        모든 명령어를 수행한 후 표의 상태와 처음 주어진 표의 상태를 비교하여 삭제되지 않은 행은 O, 삭제된 행은 X로 표시한 문자열 형태
    """
    answer = ['O'] * n
    table = [[i-1, i+1] for i in range(n)]
    table[0] = [None, 1]
    table[n-1] = [n-2, None] 
    history = []

    for command in cmd:
        if command[0] == 'D':
            for _ in range(int(command[2:])):
                k = table[k][1]
        elif command[0] == 'U':
            for _ in range(int(command[2:])):
                k = table[k][0]
        elif command[0] == 'C':
            answer[k] = 'X'
            up, down = table[k]
            history.append((k, up, down))

            # 아래로 갈 수 없는 경우
            if down == None:
                k = table[k][0] 
            else:
                k = table[k][1]

            # 링크드 리스트 연결
            if up == None:
                table[down][0] = None
            elif down == None:
                table[up][1] = None
            else:
                table[up][1] = down
                table[down][0] = up
        else:
            tmp, up, down = history.pop()
            answer[tmp] = 'O'
            
            # 링크드 리스트 연결
            if up == None:
                table[down][0] = tmp
            elif down == None:
                table[up][1] = tmp
            else:
                table[down][0] = tmp
                table[up][1] = tmp

    return ''.join(answer)


n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]

print(solution(n, k, cmd))
# python 3.10

from functools import cmp_to_key

def solution(numbers):
    """
    Args:
        numbers : 0 또는 양의 정수
    Returns:
        정수를 이어 붙여 만들 수 있는 가장 큰 수
    """
    answer = ''

    def comp(a, b):
        t1 = int(a+b)
        t2 = int(b+a)
        return (t1 > t2) - (t1 < t2) # 양수면 두번째 인자가 앞에 정렬, 음수면 첫번째 인자가 앞에 정렬, 0이면 변화 없음

    numbers = sorted(list(map(str, numbers)), key=cmp_to_key(comp), reverse=True) # 큰 수를 만들어야하기 때문에 reverse

    answer = str(int(''.join(numbers)))

    return answer
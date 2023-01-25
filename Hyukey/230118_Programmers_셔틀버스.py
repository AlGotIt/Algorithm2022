# python 3.10
from collections import deque

def solution(n, t, m, timetable):
    """
    Args:
        n : 셔틀 운행 횟수
        t : 셔틀 운행 간격
        m : 한 셔틀에 탈 수 있는 최대 크루 수
        timetable : 크루가 대기열에 도착하는 시각을 모은 배열

    Returns:
        콘이 무사히 셔틀을 타고 사무실로 갈 수 있는 제일 늦은 도착 시각
    """
    answer = ''

    timetable = deque(sorted(timetable)) # 태울 승객을 도착순서대로 FIFO로 정렬
    cur_min = 540
    cur_pass = 0

    while n>0:
        if timetable: # 태울 승객 목록이 있는 경우
            hour, min = tuple(map(int, timetable[0].split(":"))) # 시간 추출
            total_min = (hour*60 + min)
            if total_min <= cur_min: # 맨 앞에 온 사람이 현재 시간보다 빠르거나 같은 경우
                if n == 1 and cur_pass == m-1: # 그 차가 마지막이고 마지막 자리일 경우 그 사람보다 정답은 1분 빠르게 와야 함
                    answer_min = total_min-1
                    answer = min_to_string(answer_min)
                    break
                timetable.popleft() # 그렇지 않은 경우 차에 탑승
                cur_pass += 1
                if cur_pass == m: # 탑승 정원이 꽉찬 경우 다음 차로 넘어감
                    cur_min += t
                    cur_pass = 0
                    n -= 1
            else: # 맨 앞에 온 사람이 현재 시간보다 늦을 경우
                if n==1: # 그 차가 마지막인 경우 그 시간이 정답
                    answer = min_to_string(cur_min)
                    break
                cur_min += t #그렇지 않은 경우 다음 차로 넘어감
                cur_pass = 0
                n -= 1
        else: # 태울 승객이 더 이상 없는 경우 마지막 버스 시간이 정답
            if n==1:
                answer = min_to_string(cur_min)
                break
            else:
                n-=1

    return answer

def min_to_string(total_min):
    hour_str = str(total_min//60)
    min_str = str(total_min%60)
    if len(hour_str)<2: 
        hour_str = "0"+hour_str
    if len(min_str)<2:
        min_str = "0"+min_str
    return hour_str + ":" + min_str

n = 10
t = 60
m = 45
timetable = ["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]
print(solution(n, t, m, timetable))
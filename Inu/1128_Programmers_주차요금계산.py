from collections import defaultdict

def solution(fees:list, records:list) -> list:
    answer = []                                             # 요금 저장
    parking_lot = {}                                        # 차량번호/입차시간 기록
    time_dict = defaultdict(int)                            # 주차시간 기록
    
    for record in records:                                  # 입출차 기록
        time, num, status = record.split(' ')               # 차례로 시간 / 차량번호 / 입출차
        if status == 'IN':                                  # 입차인 경우
            parking_lot[num] = time                         # 차량 입차 시간 저장
        else:
            h1, m1 = map(int, parking_lot[num].split(':'))  # 출차인 경우 시간차 계산
            h2, m2 = map(int, time.split(':'))
            times = ((h2 - h1) * 60) + m2 - m1
            time_dict[num] += times                         # 시간 저장
            del parking_lot[num]
            
    for num, time in parking_lot.items():                   # 차량번호 / 입차 시간
        h1, m1 = map(int, parking_lot[num].split(':'))      # 시간 추출
        time_dict[num] += ((23 - h1) * 60) + 59 - m1    
    
    for num, time in sorted(time_dict.items()):             # 차량번호 / 입차시간
        answer.append(fees[1])                              # 기본요금 추가
        if time > fees[0]:                                  # 기본시간 이상 주차한 경우
            time -= fees[0]                                 # 시간 - 기본시간
            overtime = time // fees[2]                      # 추가시간 / 단위시간
            if time % fees[2]:                              # 추가시간이 나누어 떨어지는 경우
                overtime += 1
            answer[-1] += (overtime * fees[3])              # 추가시간 * 시간당 요금
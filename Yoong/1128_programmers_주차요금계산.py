# https://school.programmers.co.kr/learn/courses/30/lessons/92341
import math

# 시간을 분단위로 환산
def timeToMinutes(time):
    h, m = map(int, time.split(':'))
    return h*60 + m

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", 
                "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

memo = dict()                                                   # records를 dictionary로 저장(차량 번호 조회시 한번에 그 차량의 입/출차 내역을 조회할 수 있도록)
bt, bf, ut, uf = fees                                           # 기본 시간, 기본 요금, 단위 시간, 단위 요금

answer = []

for record in records:                                          # 차량 번호를 key, 그 차량의 입출차 시각 및 내역 values
    time, carNum, history = record.split()                      # 시각 차량번호 내역 순
    # 차량 입출차 시각을 분단위로 환산 후 memo에 저장
    if carNum in memo:
        memo[carNum].append([timeToMinutes(time), history])
    else:
        memo[carNum] = [[timeToMinutes(time), history]]
# print(sorted(memo.items()))
'''
[
    ('0000', [[360, 'IN'], [394, 'OUT'], [1139, 'IN']]), 
    ('0148', [[479, 'IN'], [1149, 'OUT']]), 
    ('5961', [[334, 'IN'], [479, 'OUT'], [1379, 'IN'], [1380, 'OUT']])
]
'''

# memo = list(memo.items())
# memo.sort(key=lambda x : x[0])

for record in sorted(memo.items()):                             # key 기준으로 오름차순 정렬
    sumTime = 0                                                 # 시간 계산 편리를 위한 변수
    for checkIn in record[1]:
        if checkIn[1] == "IN":
            sumTime -= checkIn[0]
        else: # checkIn[1] == "OUT"
            sumTime += checkIn[0]
    
    if record[1][-1][1] == "IN":                                # 출차된 내역이 없는 경우
        sumTime += timeToMinutes("23:59")                       # 23:59에 출차된 것으로 간주
    
    # 요금 계산
    if sumTime <= bt:                                           # 기본시간 이하
        answer.append(bf)                                       # 기본요금
    else:                                                       # 기본시간 초과
        answer.append(bf + math.ceil((sumTime - bt) / ut) * uf) # 기본 요금 + 초과한 시간에 대해 단위 시간 마다 단위 요금 청구

print(answer)

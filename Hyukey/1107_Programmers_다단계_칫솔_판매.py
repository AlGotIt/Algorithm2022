# python 3.10

def solution(enroll, referral, seller, amount):
    """
    Args:
        enroll : 각 판매원의 이름을 담은 배열
        referral : 각 판매원을 다단계 조직에 참여시킨 다른 판매원의 이름을 담은 배열
        seller : 판매량 집계 데이터의 판매원 이름을 나열한 배열
        amount : 판매량 집계 데이터의 판매 수량을 나열한 배열

    Returns:
        각 판매원이 득한 이익금을 나열한 배열
    """
    answer = []

    dic = dict()

    for en, re in zip(enroll, referral):
        dic[en] = [re, 0]
        
    for se, am in zip(seller, amount):
        val = am * 100
        nextSeller = se
        while nextSeller != "-" and val != 0:
            pay = val // 10
            dic[nextSeller][1] += val - pay
            val = pay
            nextSeller = dic[nextSeller][0]

    for di in dic.values():
        answer.append(di[1])

    return answer

enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["sam", "emily", "jaimie", "edward"]
amount = [2, 3, 5, 4]

print(solution(enroll, referral, seller, amount))
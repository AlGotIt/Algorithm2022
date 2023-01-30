# https://school.programmers.co.kr/learn/courses/30/lessons/42579

def solution(genres, plays):
    dic1 = {}
    dic2 = {}
    answer = []
    for index, (genre, play) in enumerate(zip(genres, plays)):
        # 장르를 Key로 가지는 (고유번호,재생횟수) 딕셔너리
        if genre in dic1:
            dic1[genre].append((index,play))
        else:
            dic1[genre] = [(index,play)]

        # 장르를 Key로 가지는 총 재생 수 딕셔너리
        if genre in dic2:
            dic2[genre] += play
        else:
            dic2[genre] = play

    genre_rank = sorted(dic2.items(), key = lambda x:x[1], reverse = True)                  # dic2의 키와 값들의 쌍을 첫번재 인자(총 재생수 기준)로 내림차순 정렬 -> 속한 노래가 많이 재생된 장르 순서
    for (genre,value) in genre_rank:                                                        # 많이 재생된 장르중에서도
        for (index, play) in sorted(dic1[genre], key = lambda x:x[1],reverse = True)[:2]:   # 같은 장르 내에서 많이 재생된 노래의 고유번호 2가지
            answer.append((index))
    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

'''
dic1 -> {'classic': [(0, 500), (2, 150), (3, 800)], 'pop': [(1, 600), (4, 2500)]}
dic2 -> {'classic': 1450, 'pop': 3100}
'''

print(solution(genres,plays))



### defaultdict 방법 생각해보기
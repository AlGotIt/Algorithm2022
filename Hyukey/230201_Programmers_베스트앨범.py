# python 3.10

import operator

def solution(genres, plays):
    """
    Args:
        genres : 노래의 장르를 나타내는 문자열 배열
        plays : 노래별 재생 횟수
    Returns:
        베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 담은 리스트
    """
    answer = []
    pg = [] # (재생횟수, 장르, 인덱스)로 저장한 리스트
    gen = {} # 장르 재생횟수

    for i, g in enumerate(genres):
        if g not in gen:
            gen[g] = plays[i]
        else:
            gen[g] += plays[i]
        pg.append([plays[i], g, i])

    sgen = sorted(gen.items(), key=operator.itemgetter(1), reverse=True) # 재생횟수 많은 순서대로 정렬
    spg = sorted(pg, key=lambda x : (x[0], -x[2]), reverse=True) # 재생횟수 많은 순, 인덱스(고유번호) 낮은 순서대로 정렬

    for g in sgen:
        cnt = 2 # 장르별로 최대 두개
        for p in spg:
            if p[1]==g[0]: # 해당 장르에서 추가
                answer.append(p[2])
                cnt -= 1
            if cnt == 0:
                break

    return answer
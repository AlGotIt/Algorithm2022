def solution(genres, plays):
    answer = []
    gen_dict = dict()                   # 재생된 수, 고유번호
    gen_sum = dict()                    # 장르별 총 재생 수

    for i in range(len(genres)):
        gen_dict[genres[i]] = gen_dict.get(genres[i], []) + [(plays[i], i)]
        gen_sum[genres[i]] = gen_sum.get(genres[i], 0) + plays[i]
    
    # 장르 재생 수 정렬
    gen_sum = sorted(gen_sum.items(), key = lambda x:x[1], reverse=True)

    # 재생 수는 내림차순, 고유번호는 오름차순 정렬
    for key in gen_dict.keys():
        gen_dict[key].sort(key = lambda x:(-x[0], x[1]))
    
    for gen in gen_sum:
        if len(gen_dict[gen[0]]) > 1:               # 장르 개수가 2개 이상
            for i in range(2):                      # 재생 수가 가장 높은 두 곡만 수록
                cnt, idx = gen_dict[gen[0]][i]
                answer.append(idx)
        else:                                       # 장르 개수가 한 개
            cnt, idx = gen_dict[gen[0]][0]
            answer.append(idx)
    
    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

print(solution(genres, plays))
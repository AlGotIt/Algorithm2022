# https://school.programmers.co.kr/learn/courses/30/lessons/138476
from collections import Counter
'''
collections.Counter(a) : a에서 요소들의 개수를 세어, 딕셔너리 형태로 반환합니다.  {문자 : 개수} 형태
collections.Counter(a).most_common() : a의 요소를 세어, 개수가 많은 순으로 정렬된 배열을 리턴
'''
tangerine = [1, 3, 2, 5, 4, 5, 2, 3] # 귤의 크기를 담은 배열
k = 4 # 한 상자에 담으려는 귤의 개수
'''
귤 k개를 고를 때 크기가 서로 다른 종류의 수의 최솟값을 return 해야함
즉 같은 종류의 귤의 수가 많은 것을 골라서 k를 채워함.
6 = 2 2 1 1 (X)
6 = 2 2 2 (O)
'''

#counter = sorted(Counter(tangerine).items(),reverse = True, key = lambda x : x[1]) # Counter 사용해서 귤 크기별 귤의 개수 저장 후 귤의 개수 기준으로 내림차순 정렬
counter = Counter(tangerine).most_common()                                          # 개수가 많은 순으로 정렬된 배열을 리턴
# print(counter) 
ans = 0                                                                             # 크기가 서로 다른 귤의 종류의 수 저장하는 변수

for key , value in counter:
    if k <= 0:                                                                      # k 개를 다 고르면
        break                                                                       # 종료
    k -= value                                                                      # 귤의 수 차감
    ans += 1                                                                        # 귤의 종류의 수 1 증가

print(ans)


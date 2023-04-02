def solution(book_time):
    new_book_time = []  # 분 단위로 변형
    for start, end in book_time:
        s = int(start.split(':')[0]) * 60 + int(start.split(':')[1])
        e = int(end.split(':')[0]) * 60 + int(end.split(':')[1])
        new_book_time.append([s, e])
        
    rooms = [0 for _ in range(24*60 + 10)]
    for start, end in new_book_time: 
        rooms[start] += 1
        rooms[end+10] -= 1
    
    for i in range(1, len(rooms)):
        rooms[i] += rooms[i - 1]
    answer = max(rooms)
    return answer
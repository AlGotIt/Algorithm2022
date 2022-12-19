def solution(queue1, queue2):
    if len(queue1+queue2)%2==1:
        return -1
    else:
        list1=[]
        list2=[]
        for i in sorted(queue1+queue2,reverse=True):
            if sum(list1)>=sum(list2):
                list2.append(i)
            else:
                list1.append(i)
        if sum(list1)!=sum(list2):
            return -1
    answer = 0
    while sum(queue1)!=sum(queue2):
        if sum(queue1)<sum(queue2):
            queue1.append(queue2.pop(0))
            answer+=1
        else:
            queue2.append(queue1.pop(0))
            answer+=1
            
    return answer

 
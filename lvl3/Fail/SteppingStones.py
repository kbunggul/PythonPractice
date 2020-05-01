maxValue = 0
minValue = 0
def solution(stones,k):
    global maxValue
    global minValue
    maxValue = max(stones)
    minValue = min(stones)
    mid = maxValue + minValue // 2


def steppingStones(stones,mid,k):
    cnt = 0
    for stone in stones:
        if stone <= mid:
            cnt += 1
        else:
            cnt = 0
        if k >= cnt:
            
    
    
    
##    answer = float('inf')
##    tmp = []
##    for idx, stone in enumerate(stones):
##        tmp += [stone]
##        if idx < k-1:
##            continue
##        value = max(tmp)
##        answer = (value < answer) and value or answer
##        tmp.pop(0)
##
##    return answer
        
##    
##    for i in range(k,leng):
##        tmp += [stones[i]]
##        value = max(tmp)
##        answer = (value < answer) and value or answer
##        tmp.pop(0)
##    return answer

##    answer = float('inf')
##    leng = len(stones)
##    tmp = stones[:k-1]
##    stones = stones[k-1:]
##    
##    for i in range(k,leng):
##        tmp += [stones.pop(0)]
####        tmp = stones[i-k:i]
##        print(tmp)
##        value = max(tmp)
##        answer = (value < answer) and value or answer
##        tmp.pop(0)
##    
##    return answer
##
##
####    answer = 0
##    distance = [1 for i in range(len(stones)+1)]
##    runFlag = True
##    
##
##    while runFlag:
##        tmp = min(stones)
##        answer = tmp
##        indexSet = []
##        for idx, stone in enumerate(stones):
##            if stone == tmp:
##                indexSet = [idx] + indexSet
##        for index in indexSet:
##            stones.pop(index)
##            distance[index] += distance.pop(index +1)
##            if distance[index] > k:
##                runFlag = False
##    
##    return answer

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1],3))

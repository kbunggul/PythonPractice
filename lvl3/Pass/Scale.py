def solution(weight):
    maxValue = max(weight)
    sumValue = sum(weight)
    weightSet = set(weight)
    
    if 1 not in weight:
        return 1
    
    value = 1
    sumValue = weight.count(1)
    
    while True:
        tmp = [i for i in weight if i <= sumValue+1]
        if sum(tmp)+1 != sumValue:
            value = max(tmp)
            sumValue = sum(tmp) + 1
        else:
            return sum(tmp) +1
            
        

def solution(weight):
    weight.sort()
    ans = 1
    for e in weight:
        if ans < e:
            break
        ans += e

    return ans

def makeSumList(sumList, i, count):
    tmp = []

    for j in range(1, count+1):
        value = i * j

        if value not in sumList and value not in tmp:
            tmp += [value]        

        for x in sumList:
            if x+value not in sumList and x+value not in tmp:
                tmp += [x+value]
        
    sumList+= tmp

    
print(solution2([3,5,1,1,3,5,4]))

    
##    for i in range(1,maxValue):
##        if i in weight:
##            makeSumList(sumList, i,weight.count(i))
##            
##            continue
##        if i not in sumList:
##            return i
##            
##    return sum(weight) + 1

    

##    if 1 not in weight:
##        return 1
##
##    for i in weightSet:
##        count = weight.count(i)
##        for j in range(1,count+1):
##            tmp += [i * j]
##    weight += tmp
##    weightSet = set(weight)
##    weight = None
##    
##    tmp = 1
##    
##    while True:
##        maxValue= max([i for i in weightSet if i < tmp*2+1])
##        if tmp == maxValue:
##            return tmp*2
##        tmp = maxValue



##    maxValue = max(weight)
##    sumValue = sum(weight)
##    weightSet = set(weight)
##    sumList = []
##    
##    for i in range(1,maxValue):
##        if i in weight:
##            makeSumList(sumList, i,weight.count(i))
##            tmp = [x for x in weight if x>maxValue and x<2*maxValue+1]
##            for j in tmp:
##                makeSumList(sumList,j,weight.count(j))
##            i = i*2            
##            continue
##        if i not in sumList:
##            return i
##            
##    return sum(weight) + 1
##
##    for i in range(1,maxValue):
##        if i in weight:
##            makeSumList(sumList, i,weight.count(i))
##            tmp = [x for x in weight if x>maxValue and x<2*maxValue+1]
##            for j in tmp:
##                makeSumList(sumList,j,weight.count(j))
##            i = i*2            
##            continue
##        if i not in sumList:
##            return i
##            
##    return sum(weight) + 1

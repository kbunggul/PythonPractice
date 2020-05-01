
import time as tim
##def solution(n, times):
##    
##    minValue = min(times)
##    totalTime = minValue * n
##    halfTime = totalTime//2 + totalTime%2
##    count = checkCount(totalTime,times)
##    leftList = []
##    leng = len(times)
##    cutValue = float('inf')
##
##    while  count != n:
##        if halfTime < minValue/2:
##            totalTime += minValue
##            break
##        totalTime += count>n and -1*halfTime or halfTime
##        halfTime = halfTime//2 + 1
##        count = checkCount(totalTime,times)
##
##        
##    count = checkCount(totalTime,times)
##    
##    for time in times:
##        leftList += [totalTime % time]
##    
##    while count!= n:
##        count += 1
##        minIndex = leftList.index(min(leftList))
##        leftList[minIndex] += times[minIndex]
##        
##                
##    totalTime -= min(leftList)
##        
##
##    return totalTime
##    
##    

##from math import gcd
##
##def solution(n, times):
##    answer = 0
##    totalTime = 0
##    minValue = min(times)
##    leng = len(times)
##
##    lcm = getLcm(times)
##    lcmCount = getLcmCount(times,lcm)
##    
##    while n >= lcmCount:
##        n -= lcmCount
##        totalTime += lcm
##    
##    timeList = [0 for i in range(leng)]    
##    print(lcm,lcmCount,timeList,n)
##
##    while answer< n:
##        print(timeList)
##        totalTime += minValue
##        for i in range(leng):
##            timeList[i] += minValue
##            if timeList[i] >= times[i]:
##                answer += 1
##                timeList[i] -= times[i]
##
##    while answer != n:
##        answer -= 1
##        timeList.remove(min(timeList))
##
##    totalTime -= min(timeList)
##    
##    
##    return totalTime
##
##def getLcm(times):
##    times = times[:]
##    def lcm(x,y):
##        return x*y//gcd(x,y)
##
##    while True:
##        times.append(lcm(times.pop(),times.pop()))
##        if len(times) == 1:
##            return times[0]
##        
##def getLcmCount(times,lcm):
##    count = 0
##    for time in times:
##        count += lcm/time
##    return int(count)


##
##def solution(n, times):
##    
##    minValue = min(times)
##    totalTime = minValue * n
##    halfTime = totalTime//2 + totalTime%2
##    count = checkCount(totalTime,times)
##    leng = len(times)
##    leftList = []
##    cutValue = float('inf')
##    while  count != n :
##        if halfTime < minValue/2:
##            break
##        totalTime += count>n and -1*halfTime or halfTime
##        halfTime = halfTime//2 + halfTime%2        
##        count = checkCount(totalTime,times)
##
##    totalTime += minValue    
##    count = checkCount(totalTime,times)
##    
##    for time in times:
##        leftList += [totalTime % time]
##
##    while count != n:
##        cutValue = min(leftList)
##        cutIndex = leftList.index(cutValue)
##        leftList[cutIndex] += times[cutIndex]
##        count -= 1
##                
##    totalTime -= min(leftList)
##        
##
##    return totalTime
##    
##    
def solution(n, times):
    
    totalTime = min(times) * n
    halfTime = totalTime//2 + totalTime%2
    count = 0
    for time in times:
        count += totalTime//time
    cutValue = float('inf')

    while  count != n:
        totalTime += count>n and -1*halfTime or halfTime
        halfTime = halfTime//2 + 1
        count=0
        for time in times:
            count += totalTime//time

    for time in times:
        tmp = totalTime % time
        if  tmp < cutValue:
            cutValue = tmp

##    totalTime -= cutValue
        
    return totalTime
    
    
def checkCount(totalTime,times):
    count=0
    for time in times:
        count += totalTime//time
    return count
    
print(solution(500000,[7,8,9,10,23,4,5,4,34,123,345,457,23,345687,2345,234,45,7345]))


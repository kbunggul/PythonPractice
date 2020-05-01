
leastValue = float('inf')

def solution(n,weak,dist):
    weak.sort()
    dist.sort(reverse = True)
    leng = len(dist)

    for i in range(leng):
        if (remodelling(n, weak, dist[:i+1])):
            return (i + 1)
    return -1


def remodelling(n, weaks,dists):
    
    for weak in weaks:
        tmpWeaks = weaks[:]
        tmpWeaks.remove(weak)
        
        for dist in dists:
            tmpDist = dists[:]
            tmpDist.remove(dist)
            
            if weak+dist > n:
                tmpWeaks = [i for i in tmpWeaks if i < weak and i >  weak + dist - n]
            else:
                tmpWeaks = [i for i in tmpWeaks if i > weak+dist or i < weak]
                
            if len(tmpWeaks) == 0:
                return True

            if remodelling(n,tmpWeaks,tmpDist):
                return True
            
    return False
            
        
        
        


##        
##
##def remodelling(n, weaks, distSet, count):
##    global leastValue
##    leng = len(weaks)
##
##    if count > leastValue:
##        return leastValue
##    
##    if leng == 0:
##        if count < leastValue:
##            leastValue = count
##            return leastValue
##    
##    if len(distSet) == 0:
##        return float('inf')
##    
##    for dist in distSet:
##        
##        tmpDistSet = distSet[:]
##        tmpDistSet.remove(dist)
##        
##        for weak in weaks:
##            tmpWeaks = weaks[:]
##            tmpWeaks.remove(weak)
##            
##            if weak+dist > n:
##                tmpWeaks = [i for i in tmpWeaks if i < weak and i >  weak + dist - n]
##            else:
##                tmpWeaks = [i for i in tmpWeaks if i > weak+dist or i < weak]
##                
##            returnValue = remodelling(n,tmpWeaks,tmpDistSet,count+1)
##            
##            if returnValue < leastValue:
##                leastValue = returnValue
##    return leastValue


print(solution(12,[1, 5, 6, 10],[1, 2, 3, 4]))
print(solution(50,[1, 5, 10, 16, 22, 25] ,[3, 4, 6]))
print(solution(50,[1] ,[6]))




##def solution(n,weak,dist):
##    weak.sort()
##    answer = remodelling(n, weak, dist, 0)
##    if answer == float('inf'):
##        answer = -1
##    return answer
##        
##
##def remodelling(n, weaks, distSet, count):
##    leastValue = float('inf')
##    leng = len(weaks)
##    
##    if leng == 0:
##        return count
##    
##    if len(distSet) == 0:
##        return float('inf')
##    
##    for dist in distSet:
##        
##        tmpDistSet = distSet[:]
##        tmpDistSet.remove(dist)
##        
##        for weak in weaks:
##            tmpWeaks = weaks[:]
##            tmpWeaks.remove(weak)
##            
##            if weak+dist > n:
##                tmpWeaks = [i for i in tmpWeaks if i < weak and i >  weak + dist - n]
##            else:
##                tmpWeaks = [i for i in tmpWeaks if i > weak+dist or i < weak]
##                
##            returnValue = remodelling(n,tmpWeaks,tmpDistSet,count+1)
##            
##            if returnValue == float('inf'):
##                pass
##            elif returnValue < leastValue:
##                leastValue = returnValue                
##
##    return leastValue


def solution(n, edge):
    answer = 0
    clearSet = {1}
    waitSet = {1}
    
    
    while len(clearSet) != n:
        tmpEdge = []
        tmpSet = []
        for tmp in edge:
            if tmp[0] in waitSet or tmp[1] in waitSet:
                tmpSet+= [tmp]
            else:
                tmpEdge += [tmp]
        edge = tmpEdge
##        tmpSet = [i for i in edge if i[0] in waitSet or i[1] in waitSet]
##        edge = [tmp for tmp in edge if tmp not in tmpSet]
        if len(tmpSet) == 0:
            return n-len(clearSet)

##        tmpWait = set()
##        for tmp in tmpSet:
##            tmpWait = tmpWait | set(tmp)
##        waitSet = tmpWait.difference(waitSet)
            
        waitSet = ({tmp[0] for tmp in tmpSet} | {tmp[1] for tmp in tmpSet}).difference(waitSet)
        clearSet = clearSet | waitSet

            
    if len(clearSet) == n:
        return len(waitSet)
    else:
        return n - len(clearSet)

print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
print(solution(8,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2],[8, 7]]))



##
##def solution(n, edge):
##    answer = 0
##    nodeSet = [i for i in range(1,n+1)]    
##    clearSet = [1]
##    waitSet = [1]
##    
##    
##    while len(waitSet) != 0 and len(edge) != 0:        
##        waitSet = set([i[1] for i in edge if i[0] in waitSet] + [i[0] for i in edge if i[1] in waitSet])     
##        clearSet += waitSet        
##        for wait in waitSet:
##            edge = [i for i in edge if i[0] not in clearSet or i[1] not in clearSet]
##            
##            
##    if len(clearSet) == n:
##        return len(waitSet)
##    else:
##        return n - len(clearSet)

def solution(n):
    answer = 0
    for i in range(n):
        answer += NQueen(n,1,[i],[i+0],[abs(i-0)])    
    return answer

def NQueen(n, count,xSet,sumSet,diffSet):
    if count == n:
        return 1
    returnValue = 0
    for i in range(n):
        if i not in xSet and i+count not in sumSet and i-count not in diffSet:            
            returnValue += NQueen(n,count+1,xSet + [i], sumSet + [i+count], diffSet + [i-count])
    return returnValue

##print(solution(1))
##print(solution(2))
##print(solution(3))
print(solution(4))
##print(solution(5))
##print(solution(6))
##print(solution(7))
##print(solution(8))
##print(solution(9))
##print(solution(10))
##print(solution(11))
##print(solution(12))

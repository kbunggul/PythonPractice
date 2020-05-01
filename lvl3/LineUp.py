def solution(n,k):
    answer = []
    k -= 1
    factorioList= []
    getFactorio(n - 1,factorioList)
    factorioList.sort(reverse = True)
    line = [i+1 for i in range(n)]

    for i in range(n-1):        
        share = k // factorioList[i]
        k -= factorioList[i] * share
        answer += [line.pop(share)]
    answer += line
        
        
    return answer


def getFactorio(n,factorioList):
    if n > 1:
        factorioList += [n * getFactorio(n-1,factorioList)]
        return factorioList[-1]
    else:
        factorioList += [1]
        return 1


print(solution(3,0))

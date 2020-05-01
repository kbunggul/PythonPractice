def solution(n, works):
    answer = 0
    downValue = works[0]
    index = 0    
    leng = len(works)
    rest = 0
    
    if sum(works) < n:
        return 0
    
    works.sort(reverse = True)
    
    for idx, work in enumerate(works):
        if idx == leng-1:
            break
        tmp = work - works[idx + 1]
        
        if (idx+1) * tmp < n:
            downValue = works[idx + 1]
            n -= (idx+1) * tmp
            index = idx + 1
            
        else:
            works = works[idx + 1:]
            share = n // (idx +1)
            rest = n % (idx + 1)
            downValue -= share
            break

    if index + 1 == leng:
        share = n // (index +1)
        rest = n % (index + 1)
        downValue -= share
        works = []
        

    for work in works:
        answer += work ** 2

    for i in range(index+1):
        if rest > 0:
            answer += (downValue -1) **2
            rest -= 1
        else:
            answer += downValue ** 2
    

    return answer


##print(solution(4,[3,3,4]))
##print(solution(1,[2,1,2]))
##print(solution(20,[10,9,8,7,6,5,4,3,2,1]))
##print(solution(3,[1,1]))
print(solution(2,[5,1]))
print(solution(3,[3,3,3]))

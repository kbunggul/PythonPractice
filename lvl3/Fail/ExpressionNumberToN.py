def solution(N, number):
    answer = 0
    count = [[int(str(N)*i)] for i in range(1,9)]

    for idx, num in enumerate(count):
        count[idx + 1] += num + num
        count[idx + 1] += num - num
        count[idx + 1] += num * num
        count[idx + 1] += num / num
        


    return answer
##    leng = len(str(number))
##    
##    if leng > 9:
##        return -1
##    
##    if N == 1:
##        count = 0 
##        for num in str(number):
##            count += int(num)
##        count = (count > 8) and -1 or count
##        return count
##    
##    answer = expressionNumberToN(N, number, 0)
##    
##    if answer == float('inf'):
##        return -1
##    
##    return answer 
##
##def expressionNumberToN(N, number, count):
##    tmpNumber = number
##    print(N, number, count)
##    
##    returnValue = float('inf')
##    if count > 8 :
##        return float('inf')
##    
##    if number < N:
##        count += tmpNumber * 2
##        if count > 8:
##            return float('inf')
##        else:
##            return count
##
##    for i in range(2,len(str(tmpNumber))+1):        
##        nS = int(str(N) * i)
##        if nS < tmpNumber:
##            value = expressionNumberToN(N, tmpNumber - nS, count + i)
##            returnValue = value < returnValue and value or returnValue
##            
##        oneS = int('1' * i)
##        if oneS < tmpNumber:
##            value = expressionNumberToN(N, tmpNumber - oneS, count + i + 1)
##            returnValue = value < returnValue and value or returnValue
##
##    for i in range(1, 9-count):
##        if N ** i < tmpNumber:
##            value = expressionNumberToN(N, tmpNumber - N**i, count + i)
##            returnValue = value < returnValue and value or returnValue
##    
##            
##
##    return returnValue
##        
            

    

##print(solution(5,3))
##print(solution(6,5))
print(solution(5,12))
##print(solution(1,123))
##print(solution(1,1235))

##def solution(N, number):
##    answer = 0
##    
##    oneFill = ""
##    
##    for i in range(leng):
##        oneFill += '1'
##        
##    for i in range(0,leng-1):
##        lengt = len(oneFill)
##        
##        tmp = int(oneFill) * N
##        while number >= tmp:
##            number -= tmp
##            answer += lengt
##            
##        tmp = int(oneFill)        
##        while number >= tmp and tmp > N**(lengt+1):
##            number -= tmp
##            answer += lengt + 1
##            if N == 1:
##                answer -= 1        
##            
##        oneFill = oneFill[1:]
##    print(number)
##
##    if N == 1:
##        answer += number
##        return answer
##    
##    print(number)
##    while number > N:
##        tmp = N
##        count = 1
##        while number > tmp*N:
##            tmp *= N
##            count += 1
##        number -= tmp
##        answer += count
##            
##    answer += 2 * number
##    if answer >=8:
##        return -1
##    return answer
##

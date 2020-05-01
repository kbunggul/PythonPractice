def solution(N, number):
    answer = 0
    
    leng = len(str(number))
    oneFill = ""
    
    for i in range(leng):
        oneFill += '1'
        
    for i in range(0,leng-1):
        lengt = len(oneFill)
        
        tmp = int(oneFill) * N
        while number >= tmp:
            number -= tmp
            answer += lengt
            
        tmp = int(oneFill)        
        while number >= tmp and tmp > N**(lengt+1):
            number -= tmp
            answer += lengt + 1
            if N == 1:
                answer -= 1        
            
        oneFill = oneFill[1:]
    print(number)

    if N == 1:
        answer += number
        return answer
    
    print(number)
    while number > N:
        tmp = N
        count = 1
        while number > tmp*N:
            tmp *= N
            count += 1
        number -= tmp
        answer += count
            
    answer += 2 * number
    if answer >=8:
        return -1
    return answer


print(solution(5,12))

def solution(n):
    answer = n
    nM2 = 1
    nM1 = 2

    for i in range(3,1+n):
        answer = nM2 +nM1
        nM2= nM1
        nM1 = answer
        
    answer%=1000000007
    
    return answer

print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))
print(solution(5))
print(solution(6))
print(solution(7))

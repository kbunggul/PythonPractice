def solution(n):
    answer = [1,2]
    if n == 1:
        return answer[0]
        
    for i in range(2,n):
        answer += [(answer[i-2]+ answer[i-1])% 1234567]
    return answer[-1]

print(solution(3))
print(solution(2))

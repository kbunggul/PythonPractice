def solution(budgets, M):    
    answer = 0
    sumCount = 0
    
    if sum(budgets)< M:
        return max(budgets)
    budgets.sort()
    leng = len(budgets)

    
    for i in range(leng):
        if sumCount + (leng-i) * budgets[i] > M:
            answer = budgets[i-1]
            M -= sumCount + (leng-i) * budgets[i-1]
            budgets =budgets[i:]
            break
        sumCount += budgets[i]

    answer += M // len(budgets)
    M = M % len(budgets)

    while budgets[0]< answer:
        M += answer - budgets.pop(0)
        answer += M // len(budgets)
        M = M % len(budgets)

    return answer


print(solution([120,110,140,150],485))

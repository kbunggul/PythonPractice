def solution(n):
    answer = []
    hanoi(n, 1, 2, 3, answer)
    
    return answer



def hanoi(n, start, tmp, end, answer):
    if n == 1:
        answer += [[start,end]]
        return

    hanoi(n-1, start,end, tmp, answer)
    answer += [[start,end]]
    hanoi(n-1, tmp, start, end, answer)
        

print(solution(2))

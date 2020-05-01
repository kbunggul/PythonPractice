def solution(n,s):
    if s < n:
        return [-1]
    answer = []

    share = s // n
    rest = s % n

    for i in range(n):
        if rest > 0:
            answer += [share + 1]
            rest -= 1
        else:
            answer += [share]

    answer.sort()

    
    return answer

print(solution(2,9))

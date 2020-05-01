def solution(A,B):
    answer = 0
    A.sort()
    B.sort()
    a = A.pop()
    b = B.pop()
    leng = len(A)
    for i in range(leng):
        if a >= b:
            a = A.pop()
            B.pop(0)
        else:
            b = B.pop()
            a = A.pop()
            answer += 1       
    if b > a:
        answer += 1
    return answer

print(solution([5,1,3,7],[2,2,6,8]))

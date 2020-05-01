def solution(n):
    answer = [0]
    faces = [0,1]
    
    tmp = []

    for i in range(0,n-1):            
        for j in range(0,len(answer)):
            if j % 2 == 0:
                if answer[j] == 0:
                    tmp += [0,0,1]
                else:
                    tmp += [0,1,1]
            else:
                tmp += [answer[j]]
        answer = tmp
        tmp = []
            
    print(answer)
    return answer


if solution(1) == [0]:
    print("true")
if solution(2) == [0,0,1]:
    print("true")
if solution(3) == [0,0,1,0,0,1,1]:
    print("true")

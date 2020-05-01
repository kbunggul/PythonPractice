def solution(operations):
    answer = []
    integerList = []
    leng = 0

    for operation in operations:
        operate, num = operation.split(' ')
        if operate == 'I':
            leng += 1
            integerList += [int(num)]
        else:
            if num == '-1':
                if leng == 0:
                    pass
                else:
                    leng -= 1
                    integerList.remove(min(integerList))
            else:
                if leng == 0:
                    pass
                else:
                    leng -= 1
                    integerList.remove(max(integerList))

    if leng == 0:
        return [0,0]
    else:
        return [max(integerList),min(integerList)]
    return answer


print(solution(["I 16","D 1"]))
print(solution(["I 7","I 5","I -5","D -1"]))

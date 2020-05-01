def solution(n,money):
    money.sort(reverse =True)    
    return change(n,money)


def change(n,money):
    returnValue = 0
    money = money[:]
    tmp = money.pop(0)
    
    if len(money) == 0:
        if n % tmp != 0:
            return 0
        else:
            return 1
        
    if tmp > n:        
        return change(n,money) % 1000000007
    else:
        while n >= tmp:
            returnValue += change(n,money)
            n -= tmp
            
        if n == 0:
            returnValue += 1
        else:
            returnValue += change(n,money)
    return returnValue % 1000000007
    

print(solution(19,[1,2,5]))
##print(solution(18,[1,2,5]))
##print(solution(17,[1,2,5]))
##print(solution(16,[1,2,5]))
##print(solution(15,[1,2,5]))
print(solution(14,[1,2,5]))
##print(solution(13,[1,2,5]))
##print(solution(12,[1,2,5]))
##print(solution(11,[1,2,5]))
##print(solution(10,[1,2,5]))
print(solution(9,[1,2,5]))
##print(solution(8,[1,2,5]))
##print(solution(7,[1,2,5]))
##print(solution(6,[1,2,5]))
##print(solution(5,[1,2,5]))
print(solution(4,[1,2,5]))
##print(solution(3,[1,2,5]))
##print(solution(2,[1,2,5]))
##print(solution(1,[1,2,5]))


def solution(N):  
    def tileDeco(n):
        if n == 1 or n == 2:
            return [1,1]
        value = tileDeco(n-1)
        return  value[0] + value[1], value[0]
    
    return (4*tileDeco(N)[0] + 2* tileDeco(N)[1])



print(solution(5))

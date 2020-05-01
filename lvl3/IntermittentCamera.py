def solution(routes):
    answer = 0
    routes = sorted(routes,key = lambda route : route[0])
    leng = len(routes)
    endRoute = float('-inf')
    
    for route in routes:
        if route[0] > endRoute:
            answer += 1
            endRoute = route[1]
            
        if endRoute > route[1]:
            endRoute = route[1]
        
        
    return answer


print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))

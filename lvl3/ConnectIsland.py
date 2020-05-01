def solution(n, costs):
    answer = 0
    connectSet = [[i] for i in range(n)]
    costs = sorted(costs,key=lambda costs: costs[2])
    
    for cost in costs:
        if cost[0] not in connectSet[cost[1]]:         
            for connect in connectSet[cost[1]]:
                connectSet[connect] += connectSet[cost[0]]
            for connect in connectSet[cost[0]]:
                connectSet[connect] = connectSet[cost[1]][:]
            answer += cost[2]
##            
##    while len(connectSet[0]) != n:
##        for cost in costs:
##            if cost[0] not in connectSet[cost[0]] and cost[1] in connectSet[cost[0]] or cost[0] in connectSet[cost[0]] and cost[1] not in connectSet[cost[0]]:  
##                for connect in connectSet[cost[1]]:
##                    connectSet[connect] += connectSet[cost[0]]
##                for connect in connectSet[cost[0]]:
##                    connectSet[connect] = connectSet[cost[1]]
##                answer += cost[2]

    
    return answer

print(solution(5,[[0,1,1],[0,2,2],[1,2,5],[1,3,3],[2,3,8],[3,4,1]] ))
print(solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))

def solution(n,results):
    answer = 0
    players = []
    players = [[set(),set()] for i in range(0,n)]

    for result in results:
        result = [result[0]-1,result[1] -1]
        
        for player in players[result[0]][0]:
            players[player][1].add(result[1])
            players[player][1] = players[player][1] | players[result[1]][1]
                
            players[result[1]][0].add(player)
            players[result[1]][0] = players[result[1]][0] | players[player][0]
                
        for player in players[result[1]][1]:
            players[player][0].add(result[0])
            players[player][0] = players[player][0] | players[result[0]][0]
            
            players[result[0]][1].add(player)
            players[result[0]][1] = players[result[0]][1]| players[player][1]
  
        players[result[0]][1].add(result[1])
        players[result[0]][1] =  players[result[0]][1] | players[result[1]][1]
        
        players[result[1]][0].add(result[0])
        players[result[1]][0] = players[result[1]][0] | players[result[0]][0]
        
    
    for player in players:
        if len(player[0]) +len(player[1]) == n -1:
            answer += 1
            
    return answer

    
    answer = 0

##print(solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
print(solution(8, [[1, 2], [2, 3], [3, 4], [5, 6], [6, 7], [7, 8],[4,5]]))




def solution(m,n,puddles):
    tile = [[0 for i in range(m)] for j in range(n)]

    for puddle in puddles:
        tile[puddle[1]-1][puddle[0]-1] = -1
        
    tile[0][0] = 1
    for i in range(1,m):
        tile[0][i] = (tile[0][i] != -1 and tile[0][i-1] or -1)
    for i in range(1,n):
        tile[i][0] = (tile[i][0] != -1 and tile[i-1][0] or -1)

    for i in range(1, n):
        for j in range(1, m):
            if tile[i][j] != -1:                
                tile[i][j] = ((tile[i-1][j] != -1 and tile[i-1][j] or 0) + (tile[i][j-1] != -1 and tile[i][j-1] or 0)) % 1000000007

    return tile[n-1][m-1]

print(solution(4,3,[[2,2]]))

##def solution(m,n,puddles):
##    schoolRoad = SchoolRoad(m,n,puddles)
##    answer = schoolRoad.run(0,0)
##    print(schoolRoad.tile)
##    return answer
##    
##class SchoolRoad():
##    def __init__(self,m,n,puddles):
##        self.m = m - 1
##        self.n = n - 1
##        self.tile = [[0 for i in range(m)] for j in range(n)]
##        for puddle in puddles:
##            self.tile[puddle[1]-1][puddle[0]-1] = -1
##            
##    def run (self,x,y):
##        value = 0
##        
##        if self.tile[y][x] == -1:
##            return 0
##        if x == self.m or y == self.n:
##            return 1
##        if self.tile[y][x] != 0:
##            return self.tile[y][x]
##        
##        if x != self.m:
##            value += self.run(x+1,y)
##            
##        if y != self.n:
##            value += self.run(x,y+1)
##
##        self.tile[y][x] = value
##        
##            
##        return value

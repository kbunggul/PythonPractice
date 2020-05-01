def solution(triangle):
    leng = len(triangle)-1
    for i in range(leng):
        height = leng - i
        lengt = len(triangle[height]) - 1 
        for j in range(lengt):
            if triangle[height][j] > triangle[height][j+1]:
                triangle[height-1][j] += triangle[height][j]
            else:               
                triangle[height-1][j] += triangle[height][j+1]
    return triangle[0][0]
            
        
    
    
##class Triangle:    
##    def __init__(self,triangle):
##        self.triangle = triangle
##        self.leng = len(triangle)
##        
##    def run(self,width,height):
##        sumValue = 0
##        if height == self.leng - 1:
##            return self.triangle[height][width]           
##        tmp = self.run(width,height+1)
##        if tmp > sumValue:
##            sumValue = tmp
##        tmp = self.run(width+1,height+1)
##        if tmp > sumValue:
##            sumValue = tmp
##            
##        return sumValue + self.triangle[height][width]
##    def run(self, height):
        

        
    
    
print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))

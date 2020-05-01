def solution(N,roads,K):
    roads = [i for i in roads if i[2] <= K]
    
    lengthList = [float('inf')]*(N+1)
    lengthList[1] = 0
    values = [1]
    clearRoads = [1]
    while len(clearRoads) != N:
        lengths = [i for i in roads if i[0] in clearRoads or i[1] in clearRoads]
        minValue = float('inf')
        minLand = 0
        for length in lengths:
            print(length,lengthList[length[0]])
            if length[0] in clearRoads:
                if (length[2] + lengthList[length[0]]) < minValue:
                    minValue = length[2] + lengthList[length[0]]
                    minLand = length[1]
            
            if length[1] in clearRoads:
                if (length[2] + lengthList[length[1]]) < minValue:
                    minValue = length[2] + lengthList[length[1]]
                    minLand = length[0]
                    
        clearRoads += [minLand]
        lengthList[minLand] = minValue            
            
        roads = [i for i in roads if i[0] not in clearRoads or i[1] not in clearRoads]
        
    return len([i for i in lengthList if i<=K])     
    

        
##    while len(values) != 0:
##        value = values.pop(0)
##        tmpRoads = [i for i in roads if i[0] == value or i[1] == value]
##        print(roads,lengthList,tmpRoads)
##        for road in tmpRoads:
##            roads.remove(road)
##            road.remove(value)
##            if road[0] not in values:
##                values += [road[0]]
##            lengthList[road[0]] = lengthList[road[0]] > (road[1]+lengthList[value]) and (road[1]+lengthList[value]) or lengthList[road[0]]
##    return len([i for i in lengthList if i<=K])

print(solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2],[4,5,0]],3))

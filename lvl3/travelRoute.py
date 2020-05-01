import copy
def solution(tickets):
    hashTable = []
    answer = []
    leng = len(tickets)
    for ticket in tickets:
        for place in ticket:
            if place not in hashTable:
                hashTable += [place]
                
    hashTable = sorted(hashTable,key = lambda hashTable:hashTable[0])
    
    radexTable = [[] for i in hashTable]

    for ticket in tickets:
        radexTable[hashTable.index(ticket[0])] += [hashTable.index(ticket[1])]
    

    routes = travelRoute(radexTable, hashTable.index('ICN'),0, leng)

    for route in routes:
        answer += [hashTable[route]]
    
    return answer

def travelRoute(radexTable, index, count, leng):
    minValue = float('inf')
    returnValue = []
    
    if count == leng:
        return [index]
    
    if len(radexTable[index]) == 0:
        return []
    
    for route in radexTable[index]:        
        tmpTable = copy.deepcopy(radexTable[:])
        tmpTable[index].remove(route)
        end = travelRoute(tmpTable, route, count +1, leng)

        if len(end) != 0:
            if minValue > route:
                returnValue = end
                minValue = route
    if len(returnValue) == 0:
        return [] 
    return [index] + returnValue
            
        
    

print(solution([["ICN", "COO"], ["ICN", "BOO"], ["COO", "ICN"], ["BOO", "DOO"]]))
print(solution([['ICN','BOO' ], [ 'ICN', 'COO' ], [ 'COO', 'DOO' ], ['DOO', 'COO'], [ 'BOO', 'DOO'] ,['DOO', 'BOO'], ['BOO', 'ICN' ], ['COO', 'BOO']]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))

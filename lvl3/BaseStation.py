def solution(n,stations, w):
    answer = 0
    stations.sort()
    arrival = 0
    
    for station in stations:
        if station - w > arrival:
            answer += (station - w -arrival) // (2 * w + 1) 
            if (station - w -arrival) % (2 * w + 1) !=0:
                answer += 1
            arrival = station + w
    if arrival < n:
        answer += (station - w -arrival) // (2 * w + 1) 
        if (station - w -arrival) % (2 * w + 1) !=0:
            answer += 1
        arrival = station + w
        
    
    return answer

print(solution(11,[4,11],1))

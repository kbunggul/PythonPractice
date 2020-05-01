def solution(n,stations, w):
    answer = 0
    arrival = 1
    covered = 2 * w + 1
    
    for station in stations:
        if (station - w) > arrival:
            answer += (station - w - arrival) // covered
            if (station - w - arrival) % covered != 0:
                answer += 1
        arrival = station + w +1
    arrival -= 1
    if arrival <= n:
        answer += (n - arrival) // covered 
        if (n-arrival) % covered != 0:
            answer += 1
        
    return answer

print(solution(5,[5],1))
print(solution(6,[6],1))
print(solution(5,[1],1))
print(solution(6,[1],1))
print(solution(14,[4, 14],1))
print(solution(16,[9],2))
print(solution(17,[9],2))
print(solution(9,[2, 7],2))

from datetime import datetime, timedelta
from dateutil.parser import parse

def solution(lines):
    answer = 0
    
    countSet = []
    startSet = []
    endSet = []
    
    for line in lines:
        runTime = line.split(' ')[-1]
        line = line.replace(runTime,'')
        parsedData = parse(line)
        countSet += [1]
        endSet += [parsedData]
        startSet += [parsedData - timedelta(seconds = float(runTime.replace('s','')))]

    print(startSet)
    print(endSet)
        
    endLeng = len(endSet)
    startLeng = len(startSet)
    for i in range(endLeng):
        for j in range(i+1, startLeng):
            if endSet[i] > startSet[j]:
                countSet[i] += 1
                countSet[j] += 1       
                
    answer = max(countSet)
    return answer


print(solution(	["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]))

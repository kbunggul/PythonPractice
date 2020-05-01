def solution(genres,plays):
    answer = []
    nameList = []
    indexList = []
    playsList = []
    sumList = []

    for idx, genre in enumerate(genres):
        if genre not in nameList:
            nameList += [genre]
            indexList += [[idx]]
            playsList += [[plays[genres.index(genre)]]]
        else:
            index = nameList.index(genre)
            indexList[index] += [idx]
            playsList[index] += [plays[idx]]
    for playCount in playsList:
        sumList += [sum(playCount)]
        
    while len(sumList) != 0:
        idx = sumList.index(max(sumList))
        sumList.pop(idx)
        subPlaysList = playsList.pop(idx)
        subIndexList = indexList.pop(idx)
        if len(subIndexList) > 1:            
            maxIdx = subPlaysList.index(max(subPlaysList))
            subPlaysList.pop(maxIdx)
            answer += [subIndexList.pop(maxIdx)]
        
        maxIdx = subPlaysList.index(max(subPlaysList))
        subPlaysList.pop(maxIdx)
        answer += [subIndexList[maxIdx]]        
  
    return answer

##print(solution(["classic","pop","classic","classic","pop"],[500,600,150,800,2500]))
##print(solution(["a", "b", "a", "b", "c"],[100, 200, 300, 400, 500]))
##print(solution(["a"],[1]))
print(solution(["a", "a", "a"],[1, 1, 1]))
##print(solution(["a", "b", "c", "b", "c", "d"],[1000, 1, 2, 3, 4, 5]))

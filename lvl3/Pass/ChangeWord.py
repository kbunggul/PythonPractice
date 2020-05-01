def solution(begin, target, words):
    answer = 0
    
    if target not in words:
        return 0
    
    answer = search1Differ(begin, words, target, 0)
    if answer == float("inf"):
        return 0
    return answer

def search1Differ(currentWord, tmpWordSet, target, count):

    leastCount = float("inf")

    searchWordSet = []
    leng = len(currentWord)
    
    if target == currentWord:
        return count
    
    for word in tmpWordSet:
        searchCount = 0
        for i in range(leng):
            if word[i] != currentWord[i]:
                searchCount += 1
                if searchCount > 1:
                    break
        if searchCount == 1:
            searchWordSet += [word]
            
    tmpWordSet = list(set(tmpWordSet).difference(searchWordSet))

    for searchWord in searchWordSet:
        returnValue = search1Differ(searchWord, tmpWordSet, target, count+1)
        if returnValue < leastCount :
            leastCount = returnValue
        
    return leastCount

    
print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))

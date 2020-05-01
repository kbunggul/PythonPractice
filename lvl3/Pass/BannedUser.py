def solution(user_id,banned_id):
    
    multiAllValue = 1
    lenSet = []
    nameSet = []
    banUserList = []
    
    for user in user_id:
        leng = len(user)
        if leng not in lenSet:            
            lenSet += [leng]
            nameSet += [[user]]
        else:
            nameSet[lenSet.index(leng)] += [user]

    for index, banned in enumerate(banned_id):
        leng = len(banned)
        lengIndex = lenSet.index(leng)
        userSet = nameSet[lengIndex]
        tmp = []
        for user in userSet:
            checkFlag = True
            for idx, char in enumerate(banned):
                if char != '*':
                    if char != user[idx]:
                        checkFlag = False
                        break
            if checkFlag:
                tmp += [user]
        banUserList += [tmp]

        
    answer = getNumberOfCases(len(banUserList),banUserList, [],[])
    
    
    return int(answer)


def getNumberOfCases(leng, banUserList, selectUser, completeSet):
    answer = 0
    for banUser in banUserList[0]:
        if banUser not in selectUser:
            tmpList = selectUser[:]
            tmpList += [banUser]
            if len(tmpList) == leng:
                tmpList.sort()
                if tmpList not in completeSet:
                    answer += 1
                    completeSet += [tmpList]
            else:
                answer += getNumberOfCases(leng, banUserList[1:], tmpList, completeSet)
    return answer

##
##print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "abc1**"]))
##print(solution(["frodo","fradi"],["fr*d*"]))
##print(solution(["frodo","fradi"],["fr*d*","frod*"]))
##print(solution(["abcde","abcdf","abcdg","abcdh","abcae"],["abc**","abcd*"]))
##print(solution(["abcde","abcdf","abcdg","abcdh","abcae"],["abc**","abcd*","ab**e"]))
print(solution(["a","b","c"],["*","*","*"]))


#2,3,4,5,6,11 중복 3개 이상


##    for banUser in banUserList:
##        multiAllValue *= len(banUser)
##    
##    answer = multiAllValue
##
##    for idx,banUser in enumerate(banUserList):
##        for banId in banUser:
##            tmp = multiAllValue / len(banUser)
##            for i in range(idx+1,len(banUserList)):     
##                    if banId in banUserList[i]:
##                        tmp /= len(banUserList[i])
##                        answer -= tmp
##    return int(answer)

import copy

def solution(key, lock):
    answer = False
    lenKey = len(key)
    lenLock = len(lock)    
    countLock = 0
    
    keyVectorSet = [[],[],[],[]]
    lockVectorSet = []

    #초기 Key 위치 저장
    for i in range(lenKey):
        for j in range(lenKey):
            if key[i][j] == 1:
                keyVectorSet[0] += [[i,j]]

    #초기 Lock 위치 저장
    for i in range(lenLock):
        for j in range(lenLock):
            if lock[i][j] == 0:
                lockVectorSet += [[i,j]]

    #각 Key값을 기준으로 한번씩 실행
    for base in range(len(keyVectorSet[0])):
        tmpKeyVectorSet = copy.deepcopy(keyVectorSet[:])
        
        #0,0으로 baseKey 위치 초기화
        for i in range(0,len(keyVectorSet[0])):
            tmpKeyVectorSet[0][i][0] -= tmpKeyVectorSet[0][base][0]
            tmpKeyVectorSet[0][i][1] -= tmpKeyVectorSet[0][base][1]
            
        #중심점이 될 Key값 제거
        tmpKeyVectorSet[0].pop(base)
        
        #90,180,270도 회전한 Key값 추가
        for keyVector in tmpKeyVectorSet[0]:
            tmpKeyVectorSet[1] += [[keyVector[0]*-1,keyVector[1]*-1]]
            tmpKeyVectorSet[2] += [[keyVector[1]*-1,keyVector[0]]]
            tmpKeyVectorSet[3] += [[keyVector[1],keyVector[0]*-1]]
        
        for lockVector in lockVectorSet:
            tmpSet = copy.deepcopy(tmpKeyVectorSet[:])
            tmpLockSet = copy.deepcopy(lockVectorSet[:]
            tmpLockSet.remove(lockVector)
            
            for keyVector in tmpSet:      
                removeSet = []      
                for key in keyVector:
                    key[0] += lockVector[0]
                    key[1] += lockVector[1]
                    if key[0] >= lenLock or key[1]>= lenLock or key[0] < 0 or key[1]< 0:
                        removeSet += [key]
                for remove in removeSet:
                    keyVector.remove(remove)

                    
            if tmpLockSet in tmpSet:
                return True   

        
    return answer


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))

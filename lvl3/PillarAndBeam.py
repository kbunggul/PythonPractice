def solution(n, buildFrame):
    answer= []
    
    pillarAble = [[i,0] for i in range(0,n+1)]
    beamAble = []

    pillarList = []
    beamList = []

    for build in buildFrame:
        if build[2] == 0:
            
            if [build[0],build[1]] in pillarAble:                
                if [build[0]-1,build[1]] in beamAble and [build[0]+1,build[1]] in beamAble:
                    beamAble.remove([build[0]-1,build[1]])
                    beamAble.remove([build[0]+1,build[1]])
                elif build[1] != 0:
                    continue
                
                pillarAble += [[build[0],build[1]+1]]
                pillarAble.remove([build[0],build[1]])
                beamAble += [[build[0]-1,build[1]+1]]
                beamAble += [[build[0]+1,build[1]+1]]
                pillarList += [[build[0],build[1]]]
                
        if build[2] == 1:
            
            if [build[0],build[1]] in beamAble:
                beamAble.remove([build[0],build[1]])
                if [build[0]+1,build[1]-1] in pillarList:
                    pillarAble.remove(build[0]+1,build[1])

                if [build[0]+2,build[1]] in beamList:
                    if [build[0]+1,build[1]] not in beamList:
                        beamAble += [build[0]+1,build[1]]
                    
                
                if [build[0] + 1 ,build[1]] not in beamAble:
                    beamAble += [build[0] + 1 ,build[1]]
                if [build[0] ,build[1]] not in beamAble:
                    beamAble += [build[0],build[1]]
                    
            

    for pillar in pillarList:
        answer += [[pillar[0],pillar[1],0]]
    for beam in beamList:
        answer += [[beam[0],beam[1],1]]
    return answer


print(solution(5,[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))

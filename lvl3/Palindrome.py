def solution(s):
    leng = len(s)

    if leng == 0 or leng == 1:
        return leng
    
    sameIndexs = []
    betweenIndexs = []

    if s[0] == s[1]:
        sameIndexs += [0]
    for i in range(1, leng-1):
        if s[i] == s[i + 1]:
            sameIndexs += [i]
        if s[i - 1] == s[i + 1]:
            betweenIndexs += [i]

    if len(sameIndexs) == 0 and len(betweenIndexs) == 0:
        return 1
    
    i = 1

    while True:
        i += 1
        tmp = []
        
        for sameIndex in sameIndexs:
            if sameIndex < i-1 or sameIndex + i >= leng:
                tmp += [sameIndex]                
            elif s[sameIndex - i + 1] != s[sameIndex + i]:
                tmp += [sameIndex]
        sameIndexs = [j for j in sameIndexs if j not in tmp]
                    
        if len(sameIndexs) == 0 and len(betweenIndexs) == 0:
            return (i-1)*2

        tmp = []
        for betweenIndex in betweenIndexs:
            if betweenIndex < i or betweenIndex + i >= leng:
                tmp += [betweenIndex]
            elif s[betweenIndex -i] != s[betweenIndex +i]:
                tmp += [betweenIndex]
                    
        betweenIndexs = [j for j in betweenIndexs if j not in tmp]       
                
        if len(sameIndexs) == 0 and len(betweenIndexs) == 0:
            return (i-1)*2 + 1


print(solution("cccaacdcaaccc"))
print(solution("asdfddccaabbaaccddfdsa"))
	
print(solution("asasa"))

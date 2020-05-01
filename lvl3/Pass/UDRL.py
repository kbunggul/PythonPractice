import pprint
def solution(dirs):
    answer = 0
    #Up Left Down Right
    xy = [[[0,0,0,0] for i in range(11)]for i in range(11)]
    axisX = 5
    axisY = 5
    
    for direction in dirs:
        if direction == 'U':
            if axisY < 10:
                xy[axisY][axisX][0] = 1
                axisY += 1
                xy[axisY][axisX][2] = 1
        elif direction == 'D':
            if axisY > 0:
                xy[axisY][axisX][2] = 1
                axisY -= 1
                xy[axisY][axisX][0] = 1
        elif direction == 'L':
            if axisX > 0:
                xy[axisY][axisX][1] = 1
                axisX -= 1
                xy[axisY][axisX][3] = 1
        elif direction == 'R':
            if axisX < 10:
                xy[axisY][axisX][3] = 1
                axisX += 1
                xy[axisY][axisX][1] = 1
    for xySet in xy:
        for xyValue in xySet:
            answer += sum(xyValue)
        
    return answer//2

print(solution("LULLLLLLU"))

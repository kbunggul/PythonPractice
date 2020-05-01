def solution(jobs):
    answer = 0
    leng = len(jobs)
    waitSet = []
    timeSum = 0
    totalTime = 0
    jobs = sorted(jobs, key = lambda job: job[0])

    while len(waitSet) != 0 or len(jobs) != 0:        
        waitSet += [job for job in jobs if job[0] <= totalTime]
        jobs = [job for job in jobs if job[0] > totalTime]
        
      
        if len(waitSet) == 0 and len(jobs) != 0:
            totalTime = jobs[0][0]
            continue

        waitSet = sorted(waitSet, key = lambda wait: (wait[1],wait[0]))

        runJob = waitSet.pop(0)
        totalTime += runJob[1]
        timeSum += totalTime - runJob[0]
        print(timeSum,totalTime)

    answer = int(timeSum/ leng)
    return answer

print(solution([[0, 3], [4, 9], [15, 6]]))
print(solution([[0, 9], [0, 4], [0, 5], [0, 7], [0, 3]]))
print(solution([[1, 9], [1, 4], [1, 5], [1, 7], [1, 3]]))
print(solution([[0, 3], [1, 9], [500, 6]]))
print(solution([[0,3],[0,1],[4,7]]))

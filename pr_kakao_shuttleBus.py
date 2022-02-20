from collections import deque
def convert_time(t):
    tmp = ''
    if int(t/60) <10:
        tmp += '0' + str(int(t/60)) + ':'
    else:
        tmp += str(int(t/60)) + ':'
    t %= 60
    if t < 10:
        tmp += '0' + str(t)
    else:
        tmp += str(t)
    return tmp
    

def solution(n, t, m, timetable):
    q = []
    for i in range(len(timetable)):
        q.append(int(timetable[i].split(':')[0]) * 60 + int(timetable[i].split(':')[1]))
    q = deque(sorted(q))
    
    time = 9*60
    last_crew = 0
    for i in range(n):
        cnt = 0
        
        while len(q) > 0:
            if cnt >= m or q[0] > time:
                break
            if q[0] <= time:
                cnt += 1
                last_crew = q[0]
                q.popleft()
        
        if i == n-1:
            if cnt == m:
                return convert_time(last_crew - 1)
            else :
                return convert_time(time)
        
        time += t
    
    # answer = ''
    # return answer
    
print(solution(2,10,2,["09:10", "09:09", "08:00"]))